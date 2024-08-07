from django.db import models
import uuid

class Dog(models.Model):
    id = models.IntegerField(primary_key=True,  editable=True)
    name = models.CharField(max_length=100, default='name')
    breed = models.CharField(max_length=100, default='Unknown')
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name
