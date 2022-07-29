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

turns = 0
def update_turn(user_id,all_user_play ,key_list,all_user_cards , room_id , all_user_id):
    all_user_play =all_user_play
    all_user_id=all_user_id
    user_id = user_id
    turn=0
    global turns
    turns=turns+1
    turn_starting_player = 0
    key_list = key_list
    temp1 = 0
    # working on this "function"
    if turns ==1 :
        for i in range(len(key_list)):
           for j in range(0,int(5/52)+1):
                if all_user_cards[room_id][key_list[i]]['number']=='14' and all_user_cards[room_id][key_list[i]]['symbol']=="♠":
                    return {'player':j+1}

    if turns == len(all_user_id):
        for k in range(len(all_user_play)):
            a=all_user_play[key_list[k]]
            if  int(temp1) < int(a['number']):
                temp1 = a['number']
                turn_starting_player = key_list[k]
                return({"turn":turn_starting_player , "all_user_cards":all_user_cards,"all_user_play":all_user_play})

    for i in range(len(all_user_id)):
        if all_user_id[i]==user_id:
            if len(all_user_id)==i+1:
                if turns<len(all_user_id):
                    if len(all_user_cards[room_id][all_user_id[0]]) ==0:
                        user_id = all_user_id[i+1]
                        continue
                    else:
                        turn = all_user_id[0]
                        return({"turn":turn,"all_user_cards":all_user_cards , "all_user_play":all_user_play})
            else:
                if turns<len(all_user_id):
                    if len(all_user_cards[room_id][all_user_id[i+1]]) ==0:
                        user_id = all_user_id[i+1]
                        continue
                    else:
                        turn = all_user_id[i+1]
                        return({"turn":turn,"all_user_cards":all_user_cards , "all_user_play":all_user_play})
                    
                    # for j in range(len(all_user_id)):
                    #     if all_user_id[j]==user_id:
                    #         if len(all_user_cards[room_id][all_user_id[j+1]]) !=0:
                    #             if len(all_user_id)!=i+1:
                    #                 turn = all_user_id[j+1]
                    #                 return({"turn":turn,"all_user_cards":all_user_cards})
                    #             else:
                    #                 turn = all_user_id[0]
                    #                 return({"turn":turn,"all_user_cards":all_user_cards})
                       
all_user_play = {} 
def user_card_return(user_play , all_user_cards, user_id, room_id,all_user_id):
    user_play=user_play
    all_user_cards =all_user_cards
    room_id = room_id
    user_id = user_id
    all_user_id=all_user_id
    key_list = []
    global all_user_play
    for key in all_user_play.keys():
        key_list.append(key)
    print(all_user_cards,"+++++++++++++++++++++++++++++++++++++========================",user_play)
    for i in range(len(all_user_cards[room_id][user_id])):
        if all_user_cards[room_id][user_id][i]['number']==user_play['number'] and user_play['symbol']==all_user_cards[room_id][user_id][i]['symbol']:
            all_user_play[user_id]=user_play
            all_user_cards[room_id][user_id].remove(user_play)
            print(all_user_cards)
            if len(all_user_play)>1:
                print("thulluthulluthulluthulluthulluthulluthulluthulluthulluthulluthulluthulluthulluthullu")
                re = thullu(user_play , all_user_cards,room_id,all_user_id,key_list,user_id)
                return re
            else:
                print("update_turnupdate_turnupdate_turnupdate_turnupdate_turnupdate_turnupdate_turnupdate_turnupdate_turnupdate_turnupdate_turn")
                turn=update_turn(user_id,all_user_play ,key_list,all_user_cards , room_id , all_user_id)
                return turn
            break


def thullu(user_play,all_user_cards,room_id,all_user_id, key_list , user_id) :
    global all_user_play
    user_id = user_id
    all_user_cards = all_user_cards
    all_user_id  = all_user_id
    room_id = room_id
    key_list =key_list
    temp1 = 0
    turn_starting_player = 0
    last_card = all_user_play[key_list[len(all_user_play)-2]]
    print(last_card)
    if last_card['symbol']!= user_play['symbol']:
        if len(all_user_play)==2:
            for i in range(len(key_list)):
                if all_user_play[key_list[i]] not in  all_user_cards[room_id][key_list[len(all_user_play)-2]]:
                    all_user_cards[room_id][key_list[len(all_user_play)-2]].append(all_user_play[key_list[i]])
                    all_user_play = {}
                    return {"all_user_cards":all_user_cards, "turn":[key_list[len(all_user_play)-2]] , "all_user_play":all_user_play}

        # check bigger card
        else:
            for k in range(len(all_user_play)):
                a=all_user_play[key_list[k]]
                if  int(temp1) < int(a['number']):
                    temp1 = a['number']
                    turn_starting_player = key_list[k]
            for d in range(len(key_list)):
                if all_user_play[key_list[d]] not in  all_user_cards[room_id][turn_starting_player]:
                    all_user_cards[room_id][turn_starting_player].append(all_user_play[key_list[d]])
                    all_user_play = {}
                    return {"all_user_cards":all_user_cards, "turn":turn_starting_player , "all_user_play":all_user_play}
    # saar
    else:
        next_turn=update_turn(user_id,all_user_play ,key_list,all_user_cards , room_id , all_user_id)
        return next_turn
    if len(all_user_id)==len(all_user_play):
        next_turn=update_turn(user_id,all_user_play ,key_list,all_user_cards , room_id , all_user_id)
        all_user_play = {}
        return next_turn

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






















