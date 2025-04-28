from django.contrib import admin
from .models import Hotel, HotelAttachment

# Register your models here.

@admin.register(Hotel)
class CustomHotelAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main information', {'fields': ('name', 'address', 'star', 'num_rooms', 'description', 'services')}),
        ('Additional information', {'fields': ('time_stamp', )})
    )
    add_fieldsets = (
        ('Main information', {'fields': ('name', 'address', 'star', 'num_rooms', 'description', 'services')}),
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
        ('images for hotel', {"fields": ('name','image',)}), 
        ('hotel', {"fields": ('hotel',)})
    )
    add_fieldsets = (
        ('images for hotel', {"fields": ('image',)}), 
        ('hotel', {"fields": ('hotel',)})
    )
    list_display = ('name', 'image', 'hotel')
    search_fields = ('hotel__name', )
    ordering = ('hotel', )

    def get_fieldsets(self, request, obj = None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets