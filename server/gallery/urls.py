from django.urls import path
from .views import gallery_list, image_delete

app_name = 'gallery'

urlpatterns = [
    path('', gallery_list, name='images'),
    path('delete/<pk>', image_delete, name='delete'),
]
