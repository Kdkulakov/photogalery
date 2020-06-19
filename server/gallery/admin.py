from django.contrib import admin
from .models import ImageModel


@admin.register(ImageModel)
class ImageAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'manufacturer',
        'camera_model',
        'file_url',
        'file_size',
        'object_created',
        'photo_created',
    ]
