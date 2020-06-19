from django.urls import path
from .views import ImagesList


urlpatterns = [
    path('', ImagesList.as_view(), name='images'),
]
