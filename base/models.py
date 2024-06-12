from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


class File(models.Model):
    title = models.CharField(max_length=100)
    xml = models.FileField(upload_to='files/xml/', validators=[FileExtensionValidator(['xml'])])

    def __str__(self):
        return self.title
