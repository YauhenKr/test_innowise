from django.db import models
from django.contrib.auth import get_user_model
from common.models.mixin import Creatable


class Booking(Creatable):
    booked_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        'workspaces.Room',
        on_delete=models.CASCADE
    )
    date_in = models.DateField()
    date_out = models.DateField()


class BookingUser(Creatable):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    booking = models.ForeignKey(
        'Booking',
        on_delete=models.CASCADE
    )
