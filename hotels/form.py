from django import forms
from .models import Hotel, Review, Room, Booking

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', MultipleFileInput)
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class Hotelform(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('name', 'address', 'star', 'num_rooms', 'description', 'services')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment')

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('room_type', 'capacity', 'price_per_night', 'description')

class BookingFrom(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('check_in', 'check_out', 'guests')
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }
