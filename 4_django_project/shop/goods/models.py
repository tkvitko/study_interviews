from django.db import models


class Good(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления')
    price = models.FloatField(verbose_name='Цена')
    unit = models.CharField(max_length=64, verbose_name='Единица измерения')
    vendor = models.CharField(max_length=64, verbose_name='Поставщик')
