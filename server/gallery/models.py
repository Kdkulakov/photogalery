from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from exiffield.fields import ExifField


class ImageModel(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='название фото'
    )
    manufacturer = models.CharField(
        max_length=50,
        verbose_name='производитель'
    )
    camera_model = models.CharField(
        max_length=50,
        verbose_name='модель камеры'
    )
    file_url = models.ImageField(
        upload_to='images/%y/%m/%d/',
        verbose_name='файл'
    )
    hash_of_file = models.CharField(
        max_length=255,
        editable=False,
    )
    exif = ExifField(
        source='file_url',
    )
    thumbnail = ImageSpecField(
        source='file_url',
        processors=[ResizeToFill(100, 100)],
        format='JPEG',
        options={'quality': 60},
    )
    file_size = models.CharField(
        max_length=50,
        verbose_name='размер файла'
    )
    object_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата загрузки'
    )
    photo_created = models.CharField(
        max_length=50,
        verbose_name='дата создания'
    )

    def __str__(self):
        return self.title or ""

    @property
    def filesize(self):
        x = self.file_url.size
        y = 512000
        if x < y:
            value = round(x/1000, 2)
            ext = ' kb'
        elif x < y*1000:
            value = round(x/1000000, 2)
            ext = ' Mb'
        else:
            value = round(x/1000000000, 2)
            ext = ' Gb'
        return str(value)+ext

    class Meta:
        ordering = ['-object_created']
        verbose_name = "Фото"
        verbose_name_plural = "Фотки"

