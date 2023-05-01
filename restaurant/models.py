from django.db import models

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()
    #add the following method in Menu class
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
