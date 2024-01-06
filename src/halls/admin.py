from django.contrib import admin
from .models import Hall, Seat


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    pass


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    pass
