from django.db import models


class ImageModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='название фото')
    manufacturer = models.CharField(max_length=50, verbose_name='производитель')
    camera_model = models.CharField(max_length=50, verbose_name='модель камеры')
    file_url = models.ImageField(upload_to='media/images/%y/%m/%d/')
    file_size = models.CharField(max_length=50, verbose_name='размер файла')
    object_created = models.DateTimeField(auto_now_add=True, verbose_name='дата загрузки')
    photo_created = models.CharField(max_length=50, verbose_name='дата создания')

    def __str__(self):
        return self.title or ""

    class Meta:
        ordering = ['-object_created']
        verbose_name = "Фото"
        verbose_name_plural = "Фотки"