from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, help_text='Имя файла', verbose_name='Имя')
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title