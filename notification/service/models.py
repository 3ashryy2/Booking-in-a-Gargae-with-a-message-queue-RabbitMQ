from django.db import models

class Device(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    registration_token = models.CharField(max_length=255, unique=True)

class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subscribers = models.ManyToManyField(Device)
