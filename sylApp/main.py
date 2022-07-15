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


def thullu(allSortedCard):

    for i in range(len(allSortedCard)):
       print(allSortedCard[i])

    running = True

    card = []
    allplayers = allSortedCard
    loopInc = 0
    while running ==  True:

        for i in range(len(allplayers)):
            if i==0:
                card = []
            # if len(card)>1:
                # restriction(allplayers[i], card[len(card)-1])
            givencard=str(input(f"Player{i+1}:enter the card you want to display: "))
            card.append(givencard)
            allplayers[i].remove(givencard)
            if loopInc != 0:
                if i >= 1:
                    c = card[i-1]
                    if givencard[len(givencard)-1] != c[len(c)-1] :
                        if len(card)==2:
                            allplayers[0].extend(card)
                            break
                        else:
                            for j in range(len(card)):
                                a=card[j]
                                if  int(temp1) < int(a[slice(-1)]):
                                    print(temp1)
                                    temp1 = a[slice(-1)]
                                    temp = j
                            allplayers[temp].extend(card)
                            break
        loopInc += 1
        print(allplayers)
        print(card)
        if len(allplayers)<1:
            running = False



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


main()