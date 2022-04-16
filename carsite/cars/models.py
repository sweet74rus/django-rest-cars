from django.db import models

class Cars(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    body_type = models.CharField(max_length=255, verbose_name='Тип кузова')
    engine_type = models.CharField(max_length=255, verbose_name='Тип двигателя')
    color = models.CharField(max_length=255, verbose_name='Цвет кузова')
    price = models.IntegerField(verbose_name='Стоимость')
    description = models.TextField()
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title + self.body_type


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Класс')

    def __str__(self):
        return self.name
