from django.db import models


class Characters(models.Model):
    name = models.CharField(max_length=100)
    picture = models.URLField()
    char_id = models.IntegerField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name} Character ID: {self.char_id}"
