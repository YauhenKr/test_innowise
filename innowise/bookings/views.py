from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

from bookings.models import Booking, BookingUser
from workspaces.models import Room


class BookingAPIView(APIView):
    class InputSerializer(serializers.Serializer):
        room = serializers.IntegerField()
        date_in = serializers.DateField(format='iso-8601')
        date_out = serializers.DateField(format='iso-8601')
        user = serializers.IntegerField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        room = get_object_or_404(Room, pk=data.get('room'))
        user = get_user_model().objects.get(id=data.get('user'))
        requested_date_in = data['date_in']
        requested_date_out = data['date_out']
        room_bookings = Booking.objects.filter(
            room_id=room,
            date_in__lte=requested_date_in,
            date_out__gte=requested_date_out
        )
        if room_bookings.count() != 0:
            return Response({'message': 'room is already reserved!'}, status=status.HTTP_400_BAD_REQUEST,)
        booking = Booking.objects.create(
            date_in=data.get('date_in'),
            date_out=data.get('date_out'),
            booked_by=user,
            room=room
        )
        return Response({'booking_id': booking.id}, status=status.HTTP_201_CREATED)




