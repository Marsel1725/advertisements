from django.contrib import admin
from .models import Advertisement



class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'is_auction', 'created_at']

admin.site.register(Advertisement, AdvertisementAdmin)
