from django.urls import path
from .views import hotelList, hotelDetails

urlpatterns = [
    path('', hotelList, name='hotel-list'),
    path('<int:hid>', hotelDetails, name='details-page'),
]
