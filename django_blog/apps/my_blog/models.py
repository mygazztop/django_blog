from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField


class KeyWord(models.Model):
    id = models.BigAutoField(primary_key=True)
    key_word = models.CharField(max_length=100)

    def __str__(self):
        return self.key_word


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    FIO = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    birthday = models.DateField()
    photo = models.ImageField(upload_to='static/img', verbose_name='фото автора', blank=True)
    is_active = models.BooleanField(default=True, blank=True)


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    annotation = models.CharField(max_length=1000)
    text = RichTextUploadingField()
    key_words = models.ManyToManyField(KeyWord, blank=True)
    img = models.ImageField(upload_to='static/img', verbose_name='фото', blank=True)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.title
