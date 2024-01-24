from rest_framework import serializers
from .models import Room, Receptionist

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ReceptionistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receptionist
        fields = '__all__'