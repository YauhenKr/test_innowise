from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response

from bookings.models import Booking, BookingUser
from users.serializers import UserBookingsSerializer


class UserBookingsHistoryAPIView(APIView):
    class QueryParamsSerializer(serializers.Serializer):
        user = serializers.IntegerField()

    def get(self, request):
        serializer = self.QueryParamsSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        requested_user = data['user']
        info_about_users_bookings = Booking.objects.filter(booked_by=requested_user)
        return Response(
            UserBookingsSerializer(
                info_about_users_bookings, many=True).data, status=status.HTTP_200_OK
        )

