import datetime
import uuid

from django.db import models
from . import base62_converter

class UploadImage(models.Model):
    title = models.CharField(max_length=200, blank=True)

    image = models.ImageField()

    uploaded_ts = models.DateTimeField(default=datetime.datetime.now)

    @property
    def as_short(self):
        return base62_converter.dehydrate(self.pk)
