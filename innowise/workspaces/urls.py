from django.urls import path

from workspaces.views import RoomsAPIView, EmptyRoomAPIView


urlpatterns = [
    path('', RoomsAPIView.as_view(), name='list-of-rooms'),
    path('empty_room/', EmptyRoomAPIView.as_view(), name='list-of-empty-rooms'),
]
