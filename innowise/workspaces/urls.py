from django.urls import path

from .views import *

urlpatterns = [
    path('', RoomsView.as_view(), name='list-of-rooms'),
    path('empty_room/', EmptyRoomView.as_view(), name='list-of-empty-rooms'),
]