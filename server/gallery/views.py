from django.views.generic import ListView
from .models import ImageModel
from .forms import ImageModelForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404, HttpResponseRedirect
import magic
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


class ImagesList(ListView):
    """
    Контроллер вывода списка изображений
    """
    model = ImageModel
    template_name = 'gallery/list.html'
    context_object_name = 'images'
    success_url = reverse_lazy('gallery:images')
    # paginate_by = "1"

    def get_context_data(self, **kwargs):
        context = super(ImagesList, self).get_context_data(**kwargs)
        context['form'] = ImageModelForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ImageModelForm(request.POST, request.FILES)

        if form.is_valid():
            image_instance = form.save()

            print(form)
            print(image_instance)
            print(request.POST)

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
            image_instance.save()

            return HttpResponseRedirect(reverse_lazy('gallery:images'))
        else:
            print('Form not valide')
            form = ImageModelForm()

        return HttpResponseRedirect(reverse_lazy('gallery:images'))


def image_delete(request, pk):
    ImageModel.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse_lazy('gallery:images'))