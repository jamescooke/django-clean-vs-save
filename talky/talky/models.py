from django.db import models


class NewPlayer(models.Model):
    name = models.CharField(max_length=10, blank=False, unique=True)

class Player(models.Model):
    name = models.CharField(max_length=10, blank=False)

class Passport(models.Model):
    passport_number = models.IntegerField(unique=True)
