import random

all_user_play={}

def restriction(l1,last_card):
    newlist=[]
    for i in l1:
        if i[len(i)-1]==last_card[len(last_card)-1]:
            newlist.append(i)
    if len(newlist)==0:
        return l1
    else:
        return newlist 

# def turn(allplayer_card):
#     print(allplayer_card,"8888888888888888888888888888888888888888888888888888888888888888888888")
#     for i in range(len(allplayer_card[1])):
#        for j in range(len(allplayer_card[1])):
#             if allplayer_card[1][j][0]=='14' and allplayer_card[1][j][1]=="♠":
#                 return {'player':j+1}


# user_play , user_cards , user_id , all_user_id
turns = 0
def update_turn(user_id,all_user_play ,key_list,all_user_cards , room_id):
    all_user_play ={31:{'number':'1' , 'symbol':"♠"},32:{'number':'2' , 'symbol':"♠"}, 
    30:{'number': '12', 'symbol': '♥'}}
    all_user_id=[30,31,32]
    user_id = user_id
    turn=0
    global turns
    turns=turns+1
    turn_starting_player = 0
    key_list = [31,32,30] 
    # working on this "function"
    if turns ==1 :
        for i in range(len(key_list)):
           for j in range(0,int(5/52)+1):
                if all_user_cards[room_id][key_list[j]]['number']=='14' and all_user_cards[room_id][key_list[j]]['symbol']=="♠":
                    return {'player':j+1}

    if turns == len(all_user_id):
        for k in range(len(all_user_play)):
                a=all_user_play[key_list[k]]
                if  int(temp1) < int(a['number']):
                    temp1 = a['number']
                    turn_starting_player = key_list[k]

    for i in range(len(all_user_id)):
        if all_user_id[i]==user_id:
            turn_index = i
            if len(all_user_id)==i+1:
                if turns<len(all_user_id):
                    turn = all_user_id[0]
            else:
                if turns<len(all_user_id):
                    turn = all_user_id[i+1]
    print(turn,"turn")



all_user_play = {} 
def user_card_return(user_play , all_user_cards, user_id, room_id,all_user_id):
    user_play=user_play
    all_user_cards =all_user_cards
    room_id = room_id
    user_id = user_id
    all_user_id=all_user_id
    
    global all_user_play
    # temp1 = 0 
    # turn_starting_player=0
    for i in range(len(all_user_cards[room_id][user_id])):
        if all_user_cards[room_id][user_id][i]['number']==user_play['number'] and user_play['symbol']==all_user_cards[room_id][user_id][i]['symbol']:
            all_user_play[user_id]=user_play
            all_user_cards[room_id][user_id].remove(user_play)
            print(all_user_cards)
            return(all_user_cards)
            # user_cards.remove(user_cards[i])
            # if len(all_user_play)>1:
            #     thullu(user_play , all_user_cards,room_id,all_user_id)
            # else:
            #     update_turn(all_user_id,all_user_cards)
            # # print(user_cards)
            # break


def thullu(user_play,all_user_cards,room_id,all_user_id):
    global all_user_play
    all_user_cards = all_user_cards
    all_user_id  = all_user_id
    room_id = room_id
    key_list = []
    temp1 = 0
    turn_starting_player = 0
    for key in all_user_play.keys():
        key_list.append(key)
    last_card = all_user_play[key_list[len(all_user_play)-2]]
    print(last_card)
    if last_card['symbol']!= user_play['symbol']:
        if len(all_user_play)==2:
            for i in range(len(key_list)):
                if all_user_play[key_list[i]] not in  all_user_cards[room_id][key_list[len(all_user_play)-2]]:
                    all_user_cards[room_id][key_list[len(all_user_play)-2]].append(all_user_play[key_list[i]])
            all_user_play = {}

        # check bigger card
        else:
            for k in range(len(all_user_play)):
                a=all_user_play[key_list[k]]
                if  int(temp1) < int(a['number']):
                    temp1 = a['number']
                    turn_starting_player = key_list[k]
            print(turn_starting_player,"sdsdsdsd")
            for d in range(len(key_list)):
                if all_user_play[key_list[d]] not in  all_user_cards[room_id][turn_starting_player]:
                    all_user_cards[room_id][turn_starting_player].append(all_user_play[key_list[d]])
            all_user_play = {}

    # saar
    else:
        update_turn(all_user_id)
    if len(all_user_id)==len(all_user_play):
        turn=update_turn(all_user_play , key_list)
        all_user_play = {}

    # for j in  range(len(all_user_id)):
    #     if user_id == all_user_id[i]:
    #         return all_user_id[d+1]




def sortCards(cards):
   sortedCards = []

   for j in range(len(cards)):

       if '♣' ==  cards[j][-1]:

           sortedCards.append(cards[j])

   for j in range(len(cards)):

       if '♥' ==  cards[j][-1]:

           sortedCards.append(cards[j])

   for j in range(len(cards)):

       if '♦' ==  cards[j][-1]:

           sortedCards.append(cards[j])

   for j in range(len(cards)):

       if '♠' ==  cards[j][-1]:

           sortedCards.append(cards[j])

   return sortedCards


def cardDistribute(player):

   totalCards = []
   givenCardUnicode = ["♣","♦","♥","♠"]

   for i in range(len(givenCardUnicode)):
       for j in range(2,15):
           # if j == 11:
           #     value = "J"+givenCardUnicode[i]
           #     totalCards.append(value)
           # elif j == 12:
           #     value = "Q"+givenCardUnicode[i]
           #     totalCards.append(value)
           # elif j == 13:
           #     value = "K"+givenCardUnicode[i]
           #     totalCards.append(value)
           # elif j == 14:
           #     value = "A"+givenCardUnicode[i]
           #     totalCards.append(value)
           # else:
        value = str(j)+givenCardUnicode[i]
        totalCards.append(value)
           

   allPlayers = []
   totalNumberOfCard = 52
   for j in range(player):

       singlePlayer = []
       for k in range(totalNumberOfCard//player):
           givenvalue = random.choice(totalCards)
           singlePlayer.append(givenvalue)
           totalCards.remove(givenvalue)
       allPlayers.append(singlePlayer)

   for i in range(totalNumberOfCard%player):
       givenvalue = random.choice(totalCards)
       allPlayers[i].append(givenvalue)
       totalCards.remove(givenvalue)
   return allPlayers


# main
def main():
   
    player = int(input("Enter numbers: "))
    cards = cardDistribute(player)
    totalPlyerSorted = []
    for i in range(len(cards)):
        sortedValue = sortCards(cards[i])
        totalPlyerSorted.append(sortedValue)
        # print(sortedValue)
    thullu(totalPlyerSorted)

if __name__ == "__main__":
    main()
    # print(cardDistribute(2))
    #






















# def thullu(allplayers):
#    card = []
#    print(allplayers,"sdsdssdd") 
#    turn_starting_player = 0
#    temp1 = 0 
#    for i in range(len(allplayers)):
#        for j in range(len(allplayers)):
#             if "14♠" in allplayers[j]:
#                 return {'player':j+1}
#        if i==0:
#            card = []
#        if len(card)>=1:
#            restriction(allplayers[i], card[len(card)-1])
#        givencard=str(input(f"Player{i+1}:enter the card you want to display: "))
#        card.append(givencard)
#        allplayers[i].remove(givencard)
#        if i >= 1:
#            last_card = card[i-1]
#            if givencard[len(givencard)-1] != last_card[len(last_card)-1] :
#                if len(card)==2:
#                    allplayers[0].extend(card)
#                    return allplayers ,{'player':turn_starting_player+1}
#                else:
#                    for j in range(len(card)):
#                        a=card[j]
#                        if  int(temp1) < int(a[slice(-1)]):
#                            temp1 = a[slice(-1)]
#                            turn_starting_player = j
#                    allplayers[turn_starting_player].extend(card)
#                return allplayers ,{'player':turn_starting_player+1}
#            else:
#                 if len(card)==len(allplayers):
#                     for j in range(len(card)):
#                         a=card[j]
#                         if  int(temp1) < int(a[slice(-1)]):
#                             temp1 = a[slice(-1)]
#                             turn_starting_player = j
#                     return {'player':turn_starting_player+1}
#         # return playerturn
             
