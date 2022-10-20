from django.contrib import admin
from bookings.models import Booking, BookingUser


admin.site.register(Booking)
admin.site.register(BookingUser)