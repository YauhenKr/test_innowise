from rest_framework.serializers import ModelSerializer

from workspaces.models import Room, Workspace


class WorkspaceSerializer(ModelSerializer):
    class Meta:
        model = Workspace
        fields = [
            'address'
        ]


class RoomSerializer(ModelSerializer):
    workspace = WorkspaceSerializer()

    class Meta:
        model = Room
        fields = [
            'number_of_room',
            'amount_of_rooms',
            'workspace'
        ]
