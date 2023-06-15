from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    details = models.TextField(blank=False, verbose_name='Текст')
    date = models.DateTimeField(default=timezone.now, verbose_name='Время')
    complite = models.BooleanField(default=False, verbose_name='Выполнено')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-date']
