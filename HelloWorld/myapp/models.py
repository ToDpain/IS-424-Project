from django.db import models

class Car(models.Model):
    year = models.IntegerField()
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.model
