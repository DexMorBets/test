from django.db import models

# Create your models here.

class Detail(models.Model):
    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'

    title = models.CharField(verbose_name='Название детали', max_length=200, db_index=True)
    price = models.IntegerField(verbose_name='Закупочная цена')
    count = models.IntegerField(verbose_name='Количество')

    def __str__(self):
		return self.title