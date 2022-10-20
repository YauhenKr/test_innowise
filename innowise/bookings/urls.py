from django.urls import path

from bookings.views import BookingAPIView


urlpatterns = [
    path('', BookingAPIView.as_view(), name='list-of-bookings')
    ]
