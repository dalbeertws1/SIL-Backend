import random
def restriction(l1,last_card):
    newlist=[]
    for i in l1:
        if i[len(i)-1]==last_card[len(last_card)-1]:
            newlist.append(i)
    if len(newlist)==0:
        return l1
    else:
        return newlist


def thullu(allplayers):
   card = []
   print(allplayers,"sdsdssdd")
   turn_starting_player = 0
   temp1 = 0 
   for i in range(len(allplayers)):
       for j in range(len(allplayers)):
            if "14♠" in allplayers[j]:
                return {'player':j+1}
       if i==0:
           card = []
       if len(card)>=1:
           restriction(allplayers[i], card[len(card)-1])
       givencard=str(input(f"Player{i+1}:enter the card you want to display: "))
       card.append(givencard)
       allplayers[i].remove(givencard)
       if i >= 1:
           last_card = card[i-1]
           if givencard[len(givencard)-1] != last_card[len(last_card)-1] :
               if len(card)==2:
                   allplayers[0].extend(card)
                   return allplayers ,{'player':turn_starting_player+1}
               else:
                   for j in range(len(card)):
                       a=card[j]
                       if  int(temp1) < int(a[slice(-1)]):
                           temp1 = a[slice(-1)]
                           turn_starting_player = j
                   allplayers[turn_starting_player].extend(card)
               return allplayers ,{'player':turn_starting_player+1}
           else:
                if len(card)==len(allplayers):
                    for j in range(len(card)):
                        a=card[j]
                        if  int(temp1) < int(a[slice(-1)]):
                            temp1 = a[slice(-1)]
                            turn_starting_player = j
                    return {'player':turn_starting_player+1}
        
             

                


   # card = []
   # allplayers = allSortedCard
   # i = 0
   # temp = 0
   # running = True
   # while running ==  True:

   #     for i in range(len(allplayers)):
   #         givencard=str(input("Player:enter the card you want to display: "))
   #         card.append(givencard)
   #         allplayers[i].remove(givencard)
   #         if i >= 1:
   #             c = card[i-1]
   #             if givencard[len(givencard)-1] != c[len©-1] :
   #                 if len(card)==2:
   #                     allplayers[0].extend(card)
   #                     break
   #                 else:
   #                     for j in range(len(card)):
   #                         if j >=1:
   #                             a=card[j]
   #                             b=card[j-1]
   #                             if  int(b[0]) < int(a[0]):
   #                                 temp = j
   #                             else:
   #                                 temp = j-1

   #                 allplayers[temp].extend(card)
   #                 card =[]
   #                 break
   #     print(allplayers)
   #     if len(allplayers)==1:
   #         running = False





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
