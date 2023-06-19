from django.db import models
from django.urls import reverse


class users(models.Model):
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=10)

class greenhouse(models.Model):
    imei = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

class Profile(models.Model):
    users = models.ForeignKey(users, on_delete=models.PROTECT)
    greenhouse = models.ForeignKey(greenhouse, on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    number_phone = models.CharField(max_length=30)
    city = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('account', kwargs={'account_id': self.pk})

class reports(models.Model):
    datetime = models.DateTimeField()
    description = models.TextField(blank=True)
    rate_plants = models.CharField(max_length=10)
    harvest = models.IntegerField()

class registry(models.Model):
    greenhouse = models.ForeignKey(greenhouse, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    humidity = models.IntegerField()
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
    report = models.ForeignKey(reports, on_delete=models.CASCADE)