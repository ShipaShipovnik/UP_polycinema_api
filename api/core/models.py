from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

from django.db import models


class Position(models.Model):
    slug = models.SlugField()
    name = models.CharField('Название', max_length=30)
    gramm = models.CharField('Граммовка порции', max_length=10)
    sostav = models.TextField('Описание')
    added_at = models.DateField(default=timezone.now)
    price = models.IntegerField('Цена')
    tags = TaggableManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Позиции меню"


class Comment(models.Model) :
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta :
        ordering = ['-created_date']

    def __str__(self) :
        return self.text
