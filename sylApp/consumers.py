import json
from .models import Room, Player
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async
from asgiref.sync import async_to_sync
import random
from channels.layers import get_channel_layer
from sylApp.main import thullu


def cardDistribute(player):

   totalCards = []
   givenCardUnicode = ["♣","♦","♥","♠"]

   for i in range(len(givenCardUnicode)):
       for j in range(2,15):
        value = str(j)+givenCardUnicode[i]
        totalCards.append(value)
           

   allPlayers = []
   totalNumberOfCard = 52
   for j in range(player):

       singlePlayer = {"command":"your_cards" , "cards":[]}
       for k in range(totalNumberOfCard//player):
           givenvalue = random.choice(totalCards)
           L = len(givenvalue)
           singlePlayer["cards"].append({'number':givenvalue[:-1], 'symbol':givenvalue[L-1]})
           totalCards.remove(givenvalue)
       allPlayers.append(singlePlayer)

   for i in range(totalNumberOfCard%player):
       givenvalue = random.choice(totalCards)
       L = len(givenvalue)
       allPlayers[i+1]["cards"].append({'number':givenvalue[:-1], 'symbol':givenvalue[L-1]})
       totalCards.remove(givenvalue)
   return allPlayers
























class SYLConsumer(AsyncWebsocketConsumer):

    messages = []
    room = {}

    def join_chat(self,username):
        key = self.room_id
        print(key,"--------------------------------------")
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
        key = self.room_id
        
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
        # self.room_group_name = 'chat_%s' % self.room_id
        username = await self.get_username(self.user_id)
        self.user_group_name = '_%s' % self.user_id
        self.room_group_name = '_%s' % self.room_id
        print(self.user_id,"fdfd")
        
        # Join user group
        await self.channel_layer.group_add(
            self.user_group_name,
            self.channel_name
        )

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        self.join_chat(self.user_id),
        return await self.channel_layer.group_send(
                self.user_group_name,
                {
                'type': 'chat_message',  
                "message":{
                            "command": "new_player",
                            "user": [{
                            "id": self.user_id,
                            "username":username,
                            # "profile_pic": "url",
                            "status": "watchig",
                         }
                        ]
                    }
                # "message": {self.room_id:self.room[self.room_id],'owner':self.room[self.room_id][0]}
                }
                )
        # self.messages.append({"msg": f"{ self.user_id } Join Group", "id": self.user_id, "username": self.user_id})

        # if len(self.playerCount) == 8:
        #         await self.channel_layer.group_send(
        #         self.room_group_name,
        #         {
        #         "id": self.user_id,
        #         "username": username,
        #         "profile_pic": "url",
        #         "status": "playing"
        #         }
        #         )
        #         return
        # else:
        #     await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #     "id": self.user_id,
        #     "username": username,
        #     "profile_pic": "url",
        #     "status": "watchig"
        #     }
        #     )
        #     return

    # Receive message from WebSocket
    async def receive(self, text_data):
        key = self.room_id
        user_ids = self.room[key]
        cards = cardDistribute(len(user_ids))
        print(text_data,"-----------------------------------------------------")
        text_data_json = text_data
        print(text_data_json,"--------------------------------------")
        username = self.scope['url_route']['kwargs']['user_id']
        print(username,"--------------------------------------")
        message = text_data_json
        print(message,"message")
        if message == "distribute":
            user_ids = self.room[key]
            print("--------------------------------------", len(user_ids))
            cards = cardDistribute(len(user_ids))
            for i in range(len(user_ids)):
                print(cards[i],"222")
                self.user_group_name = '_%s' % user_ids[i]
                await self.channel_layer.group_send(
                self.user_group_name,
                {
                'type': 'chat_message',
                "id":  user_ids[i],
                "username": user_ids[i],
                "profile_pic": "url",
                "status": "playing",
                "message": cards[i]
                }
                )
              
        elif message == "turn":
            turn = thullu(cards)
            print(turn)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                'type': 'chat_message',
                "message": turn
                }
                )

            # await self.channel_layer.group_send(
            # self.room_group_name,
            # {
            #     'type': 'chat_message',
            #     'message': message,
            #     'sender': username
            #     }
            #     )
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
            # 'sender': sender,
            # 'total':total
        }))
