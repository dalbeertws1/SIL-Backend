import json
from .models import Room, Player
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async
from asgiref.sync import async_to_sync
import random
from channels.layers import get_channel_layer
from sylApp.main import thullu , user_card_return
import json


def cardDistribute(player):

   totalCards = []
   givenCardUnicode = ["♣","♦","♥","♠"]
   turn = 0

   for i in range(len(givenCardUnicode)):
       for j in range(2,15):
        value = str(j)+givenCardUnicode[i]
        totalCards.append(value)
           

   allPlayers = []
   totalNumberOfCard = 52
   for j in range(player):

       singlePlayer = {"command":"your_cards" , "cards":[],"first_turn":""}
       for k in range(totalNumberOfCard//player):
           givenvalue = random.choice(totalCards)
           if givenvalue=="14♠":
              print(j,"gddddddddddddddddddddddddddddddddddddddddddddddddddd")
              turn  = j
              singlePlayer["first_turn"]=j
           L = len(givenvalue)
           singlePlayer["cards"].append({'number':givenvalue[:-1], 'symbol':givenvalue[L-1]})
           totalCards.remove(givenvalue)
       allPlayers.append(singlePlayer)

   for i in range(totalNumberOfCard%player):
       givenvalue = random.choice(totalCards)
       L = len(givenvalue)
       allPlayers[i+1]["cards"].append({'number':givenvalue[:-1], 'symbol':givenvalue[L-1]})
       totalCards.remove(givenvalue)

   for b in range(player):
        allPlayers[b]["first_turn"]=turn
   return allPlayers
























class SYLConsumer(AsyncWebsocketConsumer):

    messages = []
    room = {}
    all_players_cards = {}

    def join_chat(self,username):
        key = self.room_id
        print(key,"--------------------dgdgdggddg------------------",self.room)
        value = []
        if key in self.room.keys():
            self.room[key].append(username)
            re = self.room
            print( self.room,"dsdsdsdsd")
        else:
            value.append(username)
            self.room[key]=value
            re = self.room
            print( self.room,"dsdsdsdsd")
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
        room = room[0].created_by.id
        return room

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
        if (len(self.room[self.room_id]))<9:
            return await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                    'type': 'chat_message',  
                    "message":{
                                "command": "new_player",
                                "user": [{
                                "id": self.user_id,
                                "username":username,
                                # "all_user":self.room[self.room_id],
                                "status": "Playing",
                             }
                            ]
                        }
                    }
                    )
        else:
              return await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                    'type': 'chat_message',  
                    "message":{
                                "command": "new_player",
                                "user": [{
                                "id": self.user_id,
                                "username":username,
                                # "all_user":self.room[self.room_id],
                                "status": "Watching",
                             }
                            ]
                        }
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
        text_data_json = text_data
        username = self.scope['url_route']['kwargs']['user_id']
        message = json.loads(text_data_json)
        if message["command"]== "distribute":
            room = await self.get_roomname(self.room_id)
            print(room,"roomroomroomroomroomroomroomroomroom")
            if room == message["user_id"]:
                user_ids = self.room[key]
                print(user_ids,"1111111111111111")
                cards = cardDistribute(len(user_ids))
                print(cards,"cardscardscardscardscardscardscardscardscards")
                for i in range(len(user_ids)):
                    if len(self.all_players_cards) <1:
                        self.all_players_cards[key]={user_ids[i]:cards[i]['cards']}
                    else:
                          self.all_players_cards[key][user_ids[i]]=cards[i]['cards']
                    card=cards[i]
                    ele=card['first_turn']
                    card['first_turn']=user_ids[int(ele)]
                    self.user_group_name = '_%s' % user_ids[i]
                    await self.channel_layer.group_send(
                    self.user_group_name,
                    {
                    'type': 'chat_message',
                    "id":  user_ids[i],
                    "username": user_ids[i],
                    "profile_pic": "url",
                    "status": "playing",
                    "message": card
                    }
                    )
            else:
                 print(username,"username")
                 await self.channel_layer.group_send(
                    self.user_group_name,
                    {
                    'type': 'chat_message',
                    "message": "User is  not a room owner"
                    }
                    )
        elif message["command"] == "my_play":
            reply = user_card_return(message["card"] , self.all_players_cards, message["user_data"]["user_id"] , message["user_data"]["room_id"],user_ids)
            print(reply,"replyreplyreplyreplyreplyreplyreplyreply")
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                'type': 'chat_message',
                "message": reply
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
