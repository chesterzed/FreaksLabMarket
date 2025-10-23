from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", blank=True, null=True, verbose_name='Аватар')
    background_image = models.ImageField(upload_to="users_bg_images", blank=True, null=True, verbose_name='Обложка')
    bio = models.CharField(blank=True, default='', null=True, max_length=1000, verbose_name='Описание пользователя')
    newsletter = models.BooleanField(default=False, verbose_name='Новости')
    notifications = models.BooleanField(default=False, verbose_name='Оповещения')

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

