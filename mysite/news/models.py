from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    creared_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    udpated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.FileField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-creared_at']
