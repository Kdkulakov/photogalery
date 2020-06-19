from django.views.generic import (ListView, CreateView, DeleteView)
from .models import ImageModel


class ImagesList(ListView):
    """
    Контроллер вывода списка изображений
    """
    model = ImageModel
    template_name = 'gallery/list.html'
    context_object_name = 'images'
    # paginate_by = "1"