from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.models import BaseModel


class Country(models.Model):
    title = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.title


class Address(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False)
    address = models.CharField(max_length=256, null=False)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f"{self.country.title}, {self.city.title} | {self.address}"


class Hotel(BaseModel):
    title = models.CharField(max_length=128, null=False)
    description = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=False)
    rating = models.FloatField(validators=[MaxValueValidator(5), MinValueValidator(0)])

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'

    def __str__(self):
        return f"{self.title}"


class Room(BaseModel):
    number = models.PositiveIntegerField(null=False)
    title = models.CharField(max_length=128, null=True)
    price = models.FloatField(validators=[MinValueValidator(0)], null=False)
    max_guest_amount = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)], null=False)

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=False, related_name="rooms")

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return f"{self.number} | {self.hotel}"
