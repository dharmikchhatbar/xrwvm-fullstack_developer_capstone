from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100, default="USA")
    established_year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)],
        default=2000
    )

    def __str__(self):
        return f"{self.name} ({self.country})"


# Car Model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dealer_id = models.IntegerField()
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('TRUCK', 'Truck')
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SEDAN')
    year = models.IntegerField(
        default=2023,
        validators=[MaxValueValidator(2023), MinValueValidator(2015)]
    )

    def __str__(self):
        return f"{self.car_make.name} - {self.name} ({self.year})"
