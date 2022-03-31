from django.db import models
from shop.choises import GenderChoise


class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name='Названия типа одежды')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип одежды'
        verbose_name_plural = 'Типы одежды'


class Year(models.Model):
    year = models.CharField(max_length=10)


class Product(models.Model):
    image = models.ImageField(upload_to='images', verbose_name="Изображение")
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    available = models.BooleanField(default=True, verbose_name="актуальность")
    content = models.TextField(verbose_name='Содержание')
    stock = models.PositiveIntegerField(verbose_name="Количество товара")
    gender = models.CharField(max_length=10,choices=GenderChoise.choices)
    year = models.ForeignKey(
        Year,
        on_delete=models.CASCADE,
        related_name='products'
        )
    type = models.ForeignKey(
        "Type",
        on_delete=models.CASCADE, 
        verbose_name='Тип одежды', 
        null=True,
        blank=True
        )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT, 
        related_name='posts', 
        verbose_name='Категория'
        )

    def __str__(self):
        return self.title

    class Meta:
        unique_together = [['category', 'slug']]
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
