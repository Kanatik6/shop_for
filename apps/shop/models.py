from django.contrib.auth import get_user_model
from django.db import models

from itertools import chain

from apps.accounts.models import Profile
from apps.shop.choises import (
    GenderChoise,
    RaitingChoise,
    year_choise
    )


class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name='Названия типа одежды')
    year_time = models.ForeignKey(
        'YearTime',
        on_delete=models.PROTECT, 
        related_name='types', 
        verbose_name='Категория'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип одежды'
        verbose_name_plural = 'Типы одежды'


class Product(models.Model):
    image = models.ImageField(upload_to='images', verbose_name="Изображение")
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    available = models.BooleanField(default=True, verbose_name="актуальность")
    content = models.TextField(verbose_name='Содержание')
    gender = models.CharField(
        max_length=10,
        choices=GenderChoise.choices
        )
    year = models.CharField(
        max_length=10,
        choices=year_choise
        )
    type = models.ForeignKey(
        "Type",
        on_delete=models.CASCADE, 
        verbose_name='Тип одежды',
        related_name='products',
        null=True,
        blank=True,
        )
    profiles = models.ManyToManyField(Profile, related_name="favorites")

    @property
    def raiting(self):
        raitings = self.raitings.values_list("value")
        if raitings:
            return sum(chain(*raitings)) / len(raitings)
        else:
            return None


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class YearTime(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Raiting(models.Model):
    title = models.CharField(max_length=500)
    value = models.IntegerField(choices=RaitingChoise.choices)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='raitings'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='raitings'
        )
    
    def __str__(self):
        return self.title
