import json
from .models import Room, Player
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async

class SYLConsumer(AsyncWebsocketConsumer):

    messages = []
    room = {}
    playerCount = []

    def join_chat(self,username):
        key = self.room_name
        value = []
        if key in self.room.keys():
            self.room[key].append(username)
            re = self.room
        else:
            value.append(username)
            self.room[key]=value
            re = self.room 
        return re

    def leave_chat(self, username):
        key = self.room_name
        
        self.room[key].remove(username)
        re = self.room
        return re

    @database_sync_to_async
    def get_roomname(self, room_id):
        room = Room.objects.filter(id = room_id)
        allPlayer = []
        for i in room[0].player.all():
            allPlayer.append(i.username)
        room = room[0].created_by

        return allPlayer

    @database_sync_to_async
    def get_username(self, user_id):
        user = Player.objects.filter(id = user_id)
        return user[0].username


    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.room_group_name = 'chat_%s' % self.room_id
        username = await self.get_username(self.user_id)

        self.playerCount.append(self.user_id)
        if len(self.playerCount) == 8:
            await self.channel_layer.group_send(
            self.room_group_name,
            {
            "id": self.user_id,
            "username": username,
            "profile_pic": "url",
            "status": "watchig"
            }
            )
            return
        else:
            await self.channel_layer.group_send(
            self.room_group_name,
            {
            "id": self.user_id,
            "username": username,
            "profile_pic": "url",
            "status": "playing"
            }
            )
            return
        self.room_group_name = '_%s' % self.room_id
        print(self.scope)
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        # self.messages.append({"msg": f"{ self.user_id } Join Group", "id": self.user_id, "username": self.user_id})

   

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json,"--------------------------------------")
        username = self.scope['url_route']['kwargs']['user_id']
        message = text_data_json
        print(message,"message")
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': username
                }
                )
        # print(text_data,"-=-----------------------------------------------------",username,"---------------",self.room_id,self.room_group_name)
        # text_data_json = json.loads(text_data)
        # msgtype = text_data_json.get('type')
        # # username = text_data_json.get("username")
        # if msgtype == "user_joined":
            
        #     await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         'type': 'chat_message',
        #         'message': "Join Group",
        #         'total':self.join_chat(username),
        #         'sender': username
        #         }
        #         )
        #     return
        # message = text_data_json['message']

        # if message == "leaved the chat":
        #     await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         'type': 'chat_message',
        #         'message': message,
        #         'total':self.leave_chat(username),
        #         'sender': username
        #         }
        #         )
        #     return
        # image = text_data_json.get('image')
        # self.user_id = self.scope['user'].id

        # Send message to room group
        # self.messages.append({"msg": message, "id": self.user_id, "username": self.scope['user'].username})
        

    # Receive message from room group
    async def chat_message(self, event):
        print(event,"-=-----------------------------------------------------",self.room_id,self.room_group_name)
        # image = event.get('image')
        message = event['message']
        sender = event.get("sender")
        # total = event['total']

        # # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            # 'image': image,
            'sender': sender,
            # 'total':total
        }))
