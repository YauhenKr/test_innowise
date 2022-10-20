from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import serializers

from workspaces.models import Workspace, Room
from workspaces.serializers import RoomSerializer
from bookings.models import Booking


class RoomsAPIView(ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        qs = Room.objects.all()
        return qs


class EmptyRoomAPIView(APIView):
    class QueryParamsSerializer(serializers.Serializer):
        workspace = serializers.IntegerField()
        date = serializers.DateField(format='iso-8601')

    def get(self, request):
        serializer = self.QueryParamsSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        workspace = get_object_or_404(Workspace, pk=data.get('workspace'))
        requested_date = request.query_params['date']
        rooms = Room.objects.filter(workspace=workspace)
        list_of_rooms = []

        for room in rooms:
            room_bookings = Booking.objects.filter(
                room_id=room,
                date_in__lte=requested_date,
                date_out__gte=requested_date
            )
            if room_bookings.count() == 0:
                list_of_rooms.append(room.id)

        return Response(RoomSerializer(Room.objects.filter(id__in=list_of_rooms), many=True).data)

