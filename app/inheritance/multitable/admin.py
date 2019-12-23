from django.contrib import admin
from .models import Place1, Restaurant1


@admin.register(Place1)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Restaurant1)
class RestaurantAdmin(admin.ModelAdmin):
    pass
