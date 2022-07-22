from dataclasses import field
from rest_framework import serializers
from .models import Player, Room

class CreateRoomSerializer(serializers.Serializer):
    room_name = serializers.CharField(max_length=200)
    room_password = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100)
    photo = serializers.ImageField(required=False)

    class Meta:
        model = Room
        fields = ['id', 'room_name', 'room_password', 'player']
        read_only_fields = ['id','player']
    
    def create(self, validated_data):
        roomName=validated_data['room_name']
        print(roomName,"55555555555555555555555")
        roomPassword=validated_data['room_password']
        user = Player.objects.create(username=validated_data['username'], photo=validated_data['photo'])
        room = Room.objects.create(room_name=roomName, room_password=roomPassword, created_by=user)
        room.player.add(user)

        re = {
            "host":True,
            "room_name": room.room_name,
            "room_id": room.id,
            "user_id": user.id,
            "username": user.username,
            "photo": user.photo.url,
            "status": "playing"
        }

        return re 


class JoinRoomSerializer(serializers.Serializer):

    room_name = serializers.CharField(max_length=200)
    room_password = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=50)
    photo = serializers.ImageField()

    
    def create(self, validated_data):
        roomName=validated_data['room_name']
        print(roomName)
        roomPassword=validated_data['room_password']
        user = Player.objects.create(username=validated_data['username'], photo=validated_data['photo'])
        print(user,"player")
        print(roomPassword,"roomName")
        room = Room.objects.get(room_name=roomName, room_password=roomPassword)
        print(room)
        
        room.player.add(user)
        
        # return validated_data
        re = {
            "host":False,
            "room_name": room.room_name,
            "room_id": room.id,
            "user_id": user.id,
            "username": user.username,
            "photo": user.photo.url,
            "status": "playing"
        }

        return re
    


