from modeltranslation.translator import register, TranslationOptions
from .models import Hotel

@register(Hotel)
class HotelTranslation(TranslationOptions):
    fields = ('name', 'description', 'address', 'country', 'city', 'services')