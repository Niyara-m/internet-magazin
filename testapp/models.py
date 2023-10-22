from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Products(models.Model):
    name = models.CharField(verbose_name="Название продукта", max_length=256)
    description = models.TextField(verbose_name="Описание продукта")
    category = models.ForeignKey(verbose_name="Категория продукта", to=Category, on_delete=models.CASCADE)
    price = models.FloatField(verbose_name="Цена продукта")
    amount = models.PositiveSmallIntegerField(verbose_name="Количество товара")
    photo = models.ImageField(verbose_name="Картинка", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'