from .models import Room, Player
from .serializer import CreateRoomSerializer, JoinRoomSerializer
from rest_framework import viewsets 
from rest_framework.views import APIView
from rest_framework.response import Response



class CreateRoomViewset(APIView):

    def post(self, request):
        print(request.POST)
        room_name = request.data.get('room_name')
        room_password =request.data.get('room_password')
        room = Room.objects.filter(room_name=room_name, room_password=room_password)
        if room:
            serializer = JoinRoomSerializer(data=request.data)
            print(serializer,"serializer")
            serializer.is_valid(raise_exception=True)
            data=serializer.save()
            print(data,"d")
            return Response({"message": "Room Join successfully" , 'data':data}, status=200)
        else:
            serializer = CreateRoomSerializer(data=request.data)
            if serializer.is_valid():
                data=serializer.save()
                print(data,"d")
                return Response({"message": "Room created successfully",'data':data}, status=200)
            
        