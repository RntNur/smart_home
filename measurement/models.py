from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length = 120, verbose_name = 'Название')
    description = models.TextField(blank = True, null = True, verbose_name = 'Описание')

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='Датчик')
    temperature = models.FloatField(verbose_name = 'Температура')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата измерения')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
