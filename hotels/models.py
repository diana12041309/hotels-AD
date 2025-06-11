from django.db import models
from django.utils import timezone
from user.models import User

# Create your models here.

class Hotel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    class Star(models.IntegerChoices):
        Tourist_1_star = 1
        Standart_2_star = 2
        Comfort_3_star = 3
        First_Class_4_star = 4
        Luxury_5_star = 5
    star = models.IntegerField(choices = Star, default=0, verbose_name='Category')
    num_rooms = models.IntegerField(verbose_name='number of rooms')
    services = models.TextField()
    time_stamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} {'★' * self.star}, {self.num_rooms} rooms"
    
class Room(models.Model):
    capacity_choices = [
        (1, '1 person'),
        (2, '2 people'),
        (3, '3 people'),
        (4, '4 people'),
    ]
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=255)
    capacity = models.IntegerField(choices=capacity_choices)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    # is_available = models.BooleanField(default=True)

    @property
    def is_available(self):
        active_bookings = self.bookings.filter(check_out__gt=timezone.now())
        return not active_bookings.exists()
    def __str__(self):
        return f'{self.hotel.name} : {self.room_type}'
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} : {self.room.hotel} {self.room} from {self.check_in} to {self.check_out}'



class HotelAttachment(models.Model):
    name = models.CharField(blank=True, null=True)
    image = models.ImageField(upload_to='images')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        image_name = self.image.name.split('.')[0]
        self.name = image_name
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.image}'
    
class Review(models.Model):
    rating_choices = [
        (1, '1.0'), (2, '2.0'), (3, '3.0'), (4, '4.0'),
        (5, '5.0'), (6, '6.0'), (7, '7.0'),
        (8, '8.0'), (9, '9.0'), (10, '10'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=rating_choices)
    comment = models.TextField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    time_stamp = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.author} : {self.hotel.name} {self.time_stamp}'



class RoomAttachment(models.Model):
    name = models.CharField(blank=True, null=True)
    image = models.ImageField(upload_to='images')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        image_name = self.image.name.split('.')[0]
        self.name = image_name
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.image}'
    
