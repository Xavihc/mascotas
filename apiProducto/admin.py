from django.contrib import admin
from .models import Producto, UserProfile, ProfileFeedItem
# Register your models here.

admin.site.register(Producto)
admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)