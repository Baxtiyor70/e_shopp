import uuid

from django.db import models


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True)
    size = models.FloatField(null=True)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name

