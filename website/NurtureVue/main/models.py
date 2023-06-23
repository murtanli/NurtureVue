from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse




class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    number_phone = models.CharField(max_length=30)
    city = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('account', kwargs={'account_id': self.pk})

class greenhouse(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    imei = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=92, decimal_places=90)
    longitude = models.DecimalField(max_digits=92, decimal_places=90)

class reports(models.Model):
    datetime = models.DateTimeField()
    description = models.TextField(blank=True)
    rate_plants = models.CharField(max_length=10)
    harvest = models.IntegerField()

class registry(models.Model):
    greenhouse = models.ForeignKey(greenhouse, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    humidity = models.IntegerField()
    water = models.IntegerField()
    temperature = models.IntegerField()
    energy = models.IntegerField()
    soil_moisture = models.IntegerField()
    brightness_of_lights = models.IntegerField()
    heating = models.IntegerField()
    ventilation = models.IntegerField()
    window1 = models.IntegerField()
    window2 = models.IntegerField()
    pump1 = models.IntegerField()
    pump2 = models.IntegerField()
    error = models.IntegerField()
    report = models.ForeignKey(reports,  on_delete=models.SET_NULL, null=True)