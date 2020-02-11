from django.db import models
from datetime import datetime


class KeyWord(models.Model):
    id = models.BigAutoField(primary_key=True)
    key_word = models.CharField(max_length=100)

    def __str__(self):
        return self.key_word


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    annotation = models.CharField(max_length=1000)
    text = models.TextField()
    key_words = models.ManyToManyField(KeyWord, blank=True)

    def __str__(self):
        return self.title
