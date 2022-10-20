from django.db import models


class Workspace(models.Model):
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.address}'


class Room(models.Model):
    number_of_room = models.IntegerField()
    amount_of_rooms = models.IntegerField()
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'


