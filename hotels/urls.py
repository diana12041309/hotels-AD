from django.urls import path
from .views import *
from user.views import registration, userLogin, userLogout

urlpatterns = [
    path('', index, name='index'),
    path('hotels/', hotelList, name='hotel-list'),
    path('<int:hid>', hotelDetails, name='details-page'),
    path('add/', addHotel, name='add-hotel'),
    path('<int:hid>/edit/', editHotel, name='edit-hotel'),
    path('<int:hid>/delete/', deleteHotel, name='delete-hotel'),
    path('registration/', registration, name='registr'),
    path('login/', userLogin, name='login'),
    path('logout/', userLogout, name='logout'),
    path('<int:hid>/new-review/', add_review, name='add_review'),
    path('<int:rid>/room-details/', room_details, name='room-details'),
    path('<int:hid>/new-room/', add_room, name='add-room'),
    path('<int:rid>/edit-room/', edit_room, name='edit-room'),
    path('<int:rid>/delete-room/', delete_room, name='delete-room'),
    path('<int:bid>/booking-details/', booking_details, name='booking-details'),
    path('<int:rid>/create-booking/', create_booking, name='create-booking'),
    path('<int:bid>/edit-booking/', edit_booking, name='edit-booking'),
    path('<int:bid>/delete-booking/', delete_booking, name='delete-booking'),
    path('bookings/', booking_list, name='booking-list'),
    path('search/', search_results, name='search-results'),
]
