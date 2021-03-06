from django.db import models

# Create your models here.

class DownloadItem(models.Model):
    file = models.FileField()

    class Meta:
        verbose_name = 'Dowload Item'
        verbose_name_plural = 'Download Items'

    def __str__(self):
        return self.file.name

    def get_size(self):
        size = self.file.size / 1000000
        return size
