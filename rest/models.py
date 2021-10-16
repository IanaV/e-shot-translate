from django.db import models

# Create your models here.
from django.db import models


class Rest_Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    food = models.CharField('Кухня', max_length=250)
    full_text = models.TextField('Информация о ресторане')
    date = models.DateTimeField('Дата открытия')
    tel =  models.CharField('Tелефон', max_length=250)
    url =  models.CharField('URL ресторана', max_length=250)
    addr =  models.CharField('Адрес', max_length=250)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/rest/{self.id}'

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'