from django.contrib import admin
from .models import Advertisement, Status, AdvertisementType

admin.site.register(Advertisement)
admin.site.register(Status)
admin.site.register(AdvertisementType)
