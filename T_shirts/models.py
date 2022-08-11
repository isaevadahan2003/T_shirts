from django.db import models

class T_shirts(models.Model):
    name = models.CharField("название", max_length=20)

    def __str__(self):
        return self.name
