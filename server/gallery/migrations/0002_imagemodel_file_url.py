# Generated by Django 3.0.7 on 2020-06-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='file_url',
            field=models.ImageField(default=1, upload_to='media/images/%y/%m/%d/'),
            preserve_default=False,
        ),
    ]