from rest_framework.serializers import ModelSerializer

from bookings.models import Booking, BookingUser


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'room',
            'date_in',
            'date_out'
        ]
