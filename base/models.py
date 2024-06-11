from django.db import models


class File(models.Model):
    title = models.CharField(max_length=100)
    xml = models.FileField(upload_to='files/xml/')

    def __str__(self):
        return self.title
