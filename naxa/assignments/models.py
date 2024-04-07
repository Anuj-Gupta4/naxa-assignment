from django.db import models
from datetime import date


# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    birth_date = models.DateField()
    age = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    address_latitude = models.FloatField()
    address_longitude = models.FloatField()
    # location = PointField(null=False, blank=False) # in case for postgis

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.age = self.calculate_age()
        super().save(*args, **kwargs)

    def calculate_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (
            self.birth_date.month,
            self.birth_date.day,
        ):  # if birthday has not occured yet this year
            age -= 1
        return age
