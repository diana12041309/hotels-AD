from django.db import models
from django.utils import timezone
from user.models import User

# Create your models here.

class Hotel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
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
    #reviews

    def __str__(self):
        return f"{self.name} {'★' * self.star}, {self.num_rooms} rooms"
    
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
    


