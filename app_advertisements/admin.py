from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_date', 'updated_date', 'auction', 'image_my']
    list_filter = ['created_at', 'auction']
admin.site.register(Advertisement, AdvertisementAdmin)
