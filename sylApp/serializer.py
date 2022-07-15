from dataclasses import field
from rest_framework import serializers
from .models import Player, Room


class CreateRoomSerializer(serializers.Serializer):
    room_name = serializers.CharField(max_length=200)
    room_password = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=50)
    photo = serializers.ImageField()

    
    def create(self, validated_data):
        roomName=validated_data['room_name']
        roomPassword=validated_data['room_password']
        user = Player.objects.create(username=validated_data['username'], photo=validated_data['photo'])
        room = Room.objects.create(room_name=roomName, room_password=roomPassword, created_by=user)
        room.player.add(user)

        return validated_data


class JoinRoomSerializer(serializers.Serializer):

    room_name = serializers.CharField(max_length=200)
    room_password = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=50)
    photo = serializers.ImageField()

    
    def create(self, validated_data):
        roomName=validated_data['room_name']
        roomPassword=validated_data['room_password']
        player = Player.objects.create(username=validated_data['username'], photo=validated_data['photo'])
        room = Room.objects.get(room_name=roomName, room_password=roomPassword)
        
        room.player.add(player)
        return validated_data



