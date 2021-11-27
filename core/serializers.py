from pyexpat import model
from attr import field
from rest_framework import serializers
from .models import House, GovernmentCorp, RenewableEnergy, Room
from authentication.models import Owner


class GovernmentCorpSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernmentCorp
        fields = "__all__"


class RenewableEnergySerializer(serializers.ModelSerializer):
    class Meta:
        model = RenewableEnergy
        fields = "__all__"


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('username', 'date_joined', 'phone_number', 'email')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class HouseSerializer(serializers.ModelSerializer):
    govt_corp = GovernmentCorpSerializer()
    renewable_energy = RenewableEnergySerializer()
    owner = OwnerSerializer()
    rooms = RoomSerializer(source='house.rooms')

    class Meta:
        model = House
        read_only_fields = ('id',)
        fields = (
            'address',
            "no_inhabitants",
            "joined",
            "energy_created_today",
            "total_energy",
            'rooms',
            'govt_corp',
            'renewable_energy',
            'owner'
        )
