from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.room_number

class Receptionist(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guest_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Booking for {self.guest_name} - Room {self.room.room_number}"