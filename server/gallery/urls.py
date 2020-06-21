from django.urls import path
from .views import ImagesList, image_delete

app_name = 'gallery'

urlpatterns = [
    path('', ImagesList.as_view(), name='images'),
    path('delete/<pk>', image_delete, name='delete'),
]
