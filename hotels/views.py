from django.shortcuts import render, redirect
from .models import Hotel, HotelAttachment, Review, Room, RoomAttachment, Booking
from .form import Hotelform, ReviewForm, RoomForm, BookingFrom
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Prefetch

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
    rooms = Room.objects.filter(hotel=hotel)
    available_rooms = [room for room in rooms if room.is_available]
    services = hotel.services.split(', ')
    reviews = Review.objects.filter(hotel=hotel)
    return render(request, 'hotels/details_page.html', {
        'hotel': hotel, 
        'images': att, 
        'rooms': available_rooms, 
        'services': services, 
        'reviews': reviews,})

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
            print("FILES:", request.FILES.getlist('images'))
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
                HotelAttachment.objects.filter(pk=int(img_id)).delete()
            hotel.save()
        return redirect(to='details-page', hid=hotel.pk)
    return render(request, 'hotels/edit_hotel.html', {'form': form, 'hotel_att':hotel_att}) 

@login_required
def deleteHotel(request, hid):
    hotel = Hotel.objects.get(pk=hid)
    hotel.delete()
    return redirect(to='hotel-list')

def index(request):
    return render(request, 'hotels/index.html')

@login_required
def add_review(request, hid):
    if request.method != 'POST':
        form = ReviewForm()
    else:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.hotel_id = hid
            review.author = request.user
            review.save()
            return redirect('details-page', hid=hid)
    return render(request, 'hotels/new_review.html', {'form': form})

def room_details(request, rid):
    room = Room.objects.get(pk = rid)
    att = RoomAttachment.objects.filter(room_id = rid)
    return render(request, 'hotels/room_details.html', {'room': room, 'images': att})

@login_required
def add_room(request, hid):
    if request.method != 'POST':
        form = RoomForm()
    else:
        form = RoomForm(request.POST)
        att = request.FILES.getlist('images')
        if form.is_valid():
            room = form.save(commit=False)
            room.author = request.user
            room.hotel_id = hid
            room.save()
            for img in att:
                RoomAttachment.objects.create(room=room, image=img)
            return redirect('details-page', hid=hid)
    return render(request, 'hotels/new_room.html', {'form': form})

@login_required
def edit_room(request, rid):
    room = Room.objects.get(pk=rid)
    hotel = room.hotel
    room_att = RoomAttachment.objects.filter(room_id=rid)
    if request.method != 'POST':
        form = RoomForm(instance=room)
    else:
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            room = form.save(commit=False)
            att = request.FILES.getlist('images')
            for img in att:
                RoomAttachment.objects.create(room_id=room.pk, image=img)
            chosen = request.POST.getlist('attachments')
            for img_id in chosen:
                RoomAttachment.objects.filter(pk=int(img_id)).delete()
            room.save()
        return redirect(to='room-details', rid=room.pk)
    return render(request, 'hotels/edit_room.html', {'form': form, 'room_att':room_att})    

@login_required
def delete_room(request, rid):
    room = Room.objects.get(pk=rid)
    hotel_id = room.hotel.pk
    room.delete()
    return redirect(to='details-page', hid=hotel_id)

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).select_related('room__hotel')
    return render(request, 'hotels/booking_list.html', {'bookings': bookings})

@login_required
def booking_details(request, bid):
    booking = Booking.objects.get(pk=bid)
    return render(request, 'hotels/booking_details.html', {'booking': booking})

@login_required
def create_booking(request, rid):
    room = Room.objects.get(pk=rid)
    if request.method != 'POST':
        form = BookingFrom()
    else:
        form = BookingFrom(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.save()
            return redirect(to='booking-details', bid=booking.pk)
        else:
            print(form.errors)
    return render(request, 'hotels/new_booking.html', {'form': form})

@login_required
def edit_booking(request, bid):
    booking = Booking.objects.get(pk=bid)
    if request.method != 'POST':
        form = BookingFrom(instance=booking)
    else:
        form = BookingFrom(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save()
        return redirect(to='booking-details', bid=booking.pk)
    return render(request, 'hotels/edit_booking.html', {'form': form})

@login_required
def delete_booking(request, bid):
    booking = Booking.objects.get(pk=bid)
    hotel_id = booking.room.hotel.id
    booking.delete()
    return redirect(to='details-page', hid=hotel_id)

def search_results(request):
    query = request.GET.get('q', '')
    checkin = request.GET.get('checkin')
    checkout = request.GET.get('checkout')

    hotels = []
    if query:
        hotels = Hotel.objects.filter(
            Q(name__icontains=query) |
            Q(address__icontains=query) |
            Q(description__icontains=query)
        ).prefetch_related(
            Prefetch('room_set', queryset=Room.objects.order_by('price_per_night')),
            Prefetch('hotelattachment_set')
        )

    # Формируем список отелей с нужными данными
    results = []
    for hotel in hotels:
        room = hotel.room_set.first()
        image = hotel.hotelattachment_set.first()
        results.append({
            'id': hotel.id,
            'name': hotel.name,
            'address': hotel.address,
            'star': hotel.star,
            'room': {
                'price_per_night': room.price_per_night if room else 'N/A'
            },
            'images': [image] if image else [],
        })

    return render(request, 'hotels/search_results.html', {
        'query': query,
        'checkin': checkin,
        'checkout': checkout,
        'results': results,
        'destination': query,
        'results_count': len(results)
    })