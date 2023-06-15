from django.db import models
import hashlib
from keys import PRIVATE_KEY, PUBLIC_KEY


class Characters(models.Model):
    name = models.CharField(max_length=100)
    picture = models.URLField()
    char_id = models.IntegerField()
    description = models.CharField(max_length=500)
    ts = models.DateTimeField(auto_now_add=True)
    hash = hashlib.md5(ts + PRIVATE_KEY + PUBLIC_KEY)

    def __str__(self):
        return self.name
