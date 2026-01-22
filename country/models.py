from django.db import models

class Country(models.Model):

    name = models.CharField(max_length=200)

    capital = models.CharField(max_length=200)

    region = models.CharField(max_length=200)

    subregion = models.CharField(max_length=200)

    population = models.PositiveIntegerField()

    area = models.FloatField()

    currency = models.CharField(max_length=200)

    language = models.CharField(max_length=200)

    is_independent = models.BooleanField(default="True")


