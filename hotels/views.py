from django.shortcuts import render, redirect
from .models import Hotel, HotelAttachment
from .form import Hotelform
from django.contrib.auth.decorators import login_required

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

@login_required
def addHotel(request):
    if request.method != 'POST':
        form = Hotelform()
    else: 
        form = Hotelform(request.POST)
        att = request.FILES.getlist('images')
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.author = request.user
            hotel.save()
            for img in att:
                HotelAttachment.objects.create(hotel_id = hotel.pk, image=img)
        return redirect(to='details-page', hid=hotel.pk)
    return render(request, 'hotels/new_hotel.html', {'form': form}) 

@login_required
def editHotel(request, hid):
    hotel = Hotel.objects.get(pk=hid)
    hotel_att = HotelAttachment.objects.filter(hotel_id=hid)
    if request.method != 'POST':
        form = Hotelform(instance=hotel)
    else: 
        form = Hotelform(request.POST, instance=hotel)
        if form.is_valid():
            hotel = form.save(commit=False)
            att = request.FILES.getlist('images')
            for img in att:
                HotelAttachment.objects.create(hotel_id = hotel.pk, image=img)
            chosen = request.POST.getlist('attachments')
            for img_id in chosen:
                HotelAttachment.objects.get(pk=int(img_id)).delete()
            hotel.save()
        return redirect(to='details-page', hid=hotel.pk)
    return render(request, 'hotels/edit_hotel.html', {'form': form, 'hotel_att':hotel_att}) 

@login_required
def deleteHotel(request, hid):
    hotel = Hotel.objects.get(pk=hid)
    hotel.delete()
    return redirect(to='hotel-list')
