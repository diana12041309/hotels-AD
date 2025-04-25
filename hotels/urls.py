from django.urls import path
from .views import hotelList, hotelDetails, addHotel, editHotel, deleteHotel

urlpatterns = [
    path('', hotelList, name='hotel-list'),
    path('<int:hid>', hotelDetails, name='details-page'),
    path('add/', addHotel, name='add-hotel'),
    path('<int:hid>/edit/', editHotel, name='edit-hotel'),
    path('<int:hid>/delete/', deleteHotel, name='delete-hotel'),
]
