from django.db import models

# Create your models here.
class booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return(
         f"Booking by {self.name} "
         f"on {self.booking_date}"
        )
    
class menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
     return f'{self.title} : {str(self.price)}'

class MenuItem(models.Model):
     title = models.CharField(max_length=255)
     price = models.DecimalField(max_digits=6, decimal_places=2)
     featured = models.BooleanField(default=False)

     def __str__(self):
        return self.title
