from django.contrib import admin
from .models import Hotel, HotelAttachment, Room, Review
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.

@admin.register(Hotel)
class CustomHotelAdmin(TranslationAdmin):
    fieldsets = (
        (_('Main information'), {'fields': ('name_en', 'address_en', 'star_en', 'num_rooms_en', 'country_en', 'city_en')}),
        (_('Main information'), {'fields': ('name_ru', 'address_ru', 'star_ru', 'num_rooms_ru', 'country_ru', 'city_ru')}),
        (_('Main information'), {'fields': ('name_kk', 'address_kk', 'star_kk', 'num_rooms_kk', 'country_kk', 'city_kk')}),
        (_('Additional information'), {'fields': ('description_en', 'services_en', 'time_stamp')}),
        (_('Additional information'), {'fields': ('description_ru', 'services_ru')}),
        (_('Additional information'), {'fields': ('description_kk', 'services_kk')})
    )
    add_fieldsets = (
        (_('Main information'), {'fields': ('name_en', 'address_en', 'star_en', 'num_rooms_en', 'country_en', 'city_en')}),
        (_('Main information'), {'fields': ('name_ru', 'address_ru', 'star_ru', 'num_rooms_ru', 'country_ru', 'city_ru')}),
        (_('Main information'), {'fields': ('name_kk', 'address_kk', 'star_kk', 'num_rooms_kk', 'country_kk', 'city_kk')}),
        (_('Additional information'), {'fields': ('description_en', 'services_en', 'time_stamp')}),
        (_('Additional information'), {'fields': ('description_ru', 'services_ru')}),
        (_('Additional information'), {'fields': ('description_kk', 'services_kk')})
    )
    list_display = ('name', 'address', 'star', 'num_rooms')
    search_fields = ('name', 'address')
    ordering = ('name', )
    def get_fieldsets(self, request, obj = None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets
    
@admin.register(HotelAttachment)
class CustomHotelAttachment(admin.ModelAdmin):
    fieldsets = (
        ('Images for hotel', {'fields': ('name', 'image',)}), 
        ('Hotel', {'fields': ('hotel',)})
    )
    add_fieldsets = (
        ('Images for hotel', {'fields': ('image',)}), 
        ('Hotel', {'fields': ('hotel',)})
    )
    list_display = ('name', 'image', 'hotel')
    search_fields = ('hotel__name', )
    ordering = ('hotel', )

    def get_fieldsets(self, request, obj = None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets
   
@admin.register(Review)
class CustomReview(admin.ModelAdmin):
    fieldsets = (
        ('Author', {'fields': ('author',)}),
        ('Information about review', {'fields': ('hotel', 'rating', 'comment',)}),
        ('Additional information', {'fields': ('time_stamp',)}),
    )
    list_display = ('author', 'hotel', 'rating')
    search_fields = ('author', 'hotel', 'rating')
    ordering = ('hotel', 'rating')

    def get_fieldsets(self, request, obj = None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets

@admin.register(Room)
class CustomRoom(admin.ModelAdmin):
    fieldsets = (
        ('Main information', {'fields': ('hotel', 'room_type', 'capacity')}),
        ('Additional information', {'fields': ('description', 'is_available')})
    )
    list_display = ('hotel', 'room_type')
    search_fields = ('hotel', 'room_type', 'capacity')
    ordering = ('hotel', 'room_type')

    def get_fieldsets(self, request, obj = None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets

