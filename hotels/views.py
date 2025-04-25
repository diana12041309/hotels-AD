from django.shortcuts import render
from .models import Hotel, HotelAttachment

# Create your views here.

def hotelList(request):
    hotels = Hotel.objects.all()
    for hotel in hotels:
        att = HotelAttachment.objects.filter(hotel_id = hotel.pk)
        hotel.images = att
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels})

def hotelDetails(request, hid):
    hotel = Hotel.objects.get(pk = hid)
    att = HotelAttachment.objects.filter(hotel_id = hid)
    return render(request, 'hotels/details_page.html', {'hotel': hotel, 'images': att})
