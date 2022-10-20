from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

from users.models import User
from bookings.models import Booking, BookingUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username'
        ]


class UserBookingsSerializer(ModelSerializer):
    booked_by = UserSerializer()

    class Meta:
        model = Booking
        fields = [
            'booked_by',
            'date_in',
            'date_out',
            'room'
        ]

