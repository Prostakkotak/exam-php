from django.db import models
from django.contrib.auth.models import User

class Thing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    wrnt = models.DateField()
    master = models.CharField(max_length=100) # Уникальная подпись создателя, вроде как

class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    repair = models.BooleanField(default=False)
    work = models.BooleanField(default=False)

class Usage(models.Model):
    thing_id = models.ForeignKey(Thing, on_delete=models.CASCADE)
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)