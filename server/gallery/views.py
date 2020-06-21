from .models import ImageModel
from .forms import ImageModelForm
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect
import magic
import hashlib
from functools import partial
from django.forms import ValidationError


def get_mimetype(fobject):
    mime = magic.Magic(mime=True)
    mimetype = mime.from_buffer(fobject.read(1024))
    fobject.seek(0)
    return mimetype


def valid_image_mimetype(fobject):
    mimetype = get_mimetype(fobject)
    if mimetype:
        return mimetype.startswith('image')
    else:
        return False


def hash_file(file, block_size=65536):
    '''
    функция создания hash из файла
    '''
    hasher = hashlib.md5()
    for buf in iter(partial(file.read, block_size), b''):
        hasher.update(buf)

    return hasher.hexdigest()


def gallery_list(request):
    '''
    Контероллер вывода списка изображений и формы загрузки
    '''
    context = {}
    context['form'] = ImageModelForm(request.POST, request.FILES)

    if request.method == 'GET':
        context['images'] = ImageModel.objects.all()
        return render(request, 'gallery/list.html', context)

    if request.method == 'POST':
        form = context['form']
        if form.is_valid():
            # сохраняем файл предварително в базу, дабы получить данные из exif
            image_instance = form.save()

            hash_file_in_form = hash_file(image_instance.file_url)
            if ImageModel.objects.filter(hash_of_file=hash_file_in_form):
                print('EST V BAZE')
                image_instance.delete()
            else:
                try:
                    image_instance.manufacturer = image_instance.exif['Make']['val']
                except Exception:
                    pass
                try:
                    image_instance.camera_model = image_instance.exif['Model']['val']
                except Exception:
                    pass
                try:
                    image_instance.photo_created = image_instance.exif['CreateDate']['val']
                except Exception:
                    pass
                image_instance.file_size = image_instance.filesize

                image_instance.hash_of_file = hash_file_in_form
                image_instance.save()

            return HttpResponseRedirect(reverse_lazy('gallery:images'))
        else:
            print('Form not valide')
            context['images'] = ImageModel.objects.all()
            return render(request, 'gallery/list.html', context)


def image_delete(request, pk):
    ImageModel.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse_lazy('gallery:images'))