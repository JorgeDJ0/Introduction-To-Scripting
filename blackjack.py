"""
Author: Jorge Juarez

This program will simulate playing blackjack!
"""

#Code for classes

import random

class playerStats():    #Stores player's number, balance, how much they bet, and their hand
    def __init__(self, num, balance, betAmount, zeroBets, handIndex):
        self._num = num
        self._balance = balance
        self._betAmount = betAmount
        self._zeroBets = zeroBets   #Keeps track if the player bets 0 3 times in a row
        self._hand = []
        self._handIndex = handIndex #Keeps track of amount of cards in hand
    
    def displayStats (self): #Displays current player stats to the user
        print("Player", self._num)
        for i in range (0,self._handIndex):
            self._hand[i].cardStats()
        print("Total Value:", self.handValue())
        print("Total Bet:", self._betAmount, "USD")
        print("In Bank:", self._balance,"USD")
    
    def setBet (self, bet): #Sets the bet that the player makes
        self._betAmount = bet
        self._balance -= bet
        if bet == 0:
            self._zeroBets += 1
        else:
            self._zeroBets = 0

    def drawCard(self, deck):
        self._hand.append(deck.drawCard())
        self._handIndex += 1

    def handValue(self):
        sum = 0
        for i in range(0, self._handIndex):
            val = self._hand[i].getValue()
            if val == "J" or val == "Q" or val == "K":
                sum += 10
            elif val == "A":
                sum += 11
            else:
                sum += val

        if sum > 21:
            sum = 0
            for i in range(0, self._handIndex):
                val = self._hand[i].getValue()
                if val == "J" or val == "Q" or val == "K":
                    sum += 10
                elif val == "A":
                    sum += 1
                else:
                    sum += val
        return sum

    def blackjack(self):
        self._balance += self._betAmount * 3
        self._betAmount = 0

    def regPayOff(self):
        self._balance += self._betAmount * 2
        self._betAmount = 0

    def restart(self):      #Removes card values from previous game to set up the next
        self._hand = []
        self._handIndex = 0


class dealer():     #Stores the data for the Dealer
    def __init__(self, handIndex):
        self._hand = []
        self._handIndex = handIndex

    def displayDealer(self):
        print("Dealer Card Numbers:")
        for i in range (1,self._handIndex):
            self._hand[i].cardStats()
        print("Total Value:", self.publicValue())

    def drawCard(self, deck):
        self._hand.append(deck.drawCard())
        self._handIndex += 1

    def handValue(self):    #Holds the dealers ACTUAL hand value
        sum = 0
        for i in range(0, self._handIndex):
            val = self._hand[i].getValue()
            if val == "J" or val == "Q" or val == "K":
                sum += 10
            elif val == "A":
                sum += 11
            else:
                sum += val

        if sum > 21:
            sum = 0
            for i in range(0, self._handIndex):
                val = self._hand[i].getValue()
                if val == "J" or val == "Q" or val == "K":
                    sum += 10
                elif val == "A":
                    sum += 1
                else:
                    sum += val
        return sum
    
    def publicValue(self):  #Holds the value the dealer has to the user
        sum = 0
        for i in range(1, self._handIndex):
            val = self._hand[i].getValue()
            if val == "J" or val == "Q" or val == "K":
                sum += 10
            elif val == "A":
                sum += 11
            else:
                sum += val

        if sum > 21:
            sum = 0
            for i in range(1, self._handIndex):
                val = self._hand[i].getValue()
                if val == "J" or val == "Q" or val == "K":
                    sum += 10
                elif val == "A":
                    sum += 1
                else:
                    sum += val
        return sum

    def restart(self):      #Removes card values from previous game to set up the next
        self._hand = []
        self._handIndex = 0


class card():   #Stores the data for each individual card
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value
    
    def cardStats(self):
        if self._suit == "Spades" or self._suit == "Clubs":
            color = "Black"
        else:
            color = "Red"
        print("Color:", color, "Symbol:", self._suit, "Value:", self._value)

    def getSuit(self):
        return self._suit
    def getValue(self):
        return self._value


class deck(): #Stores a shoe [4-8 Decks - 52 Cards Each]
    def __init__(self):
        self._deck = []

    def build(self):    #Creates the deck
        shoeSize = random.randint(4, 8) #Gets the amount of decks that will be in shoe between 4 and 8
        for s in (0, shoeSize):
            for i in ["Spades", "Clubs", "Diamonds", "Hearts"]:
                for j in range(1, 14):
                    if j > 10:  #Makes cards like J, Q, and K set to the value of 10
                        if j == 11:
                            self._deck.append(card(i, "J"))
                        elif j == 12:
                            self._deck.append(card(i, "Q"))
                        elif j == 13:
                            self._deck.append(card(i, "K"))
                    elif j == 1:    #Creates an A for each suit
                        self._deck.append(card(i, "A"))
                    else:
                        self._deck.append(card(i, j))

    def drawCard(self):
        return self._deck.pop()

    def shuffle(self):
        for i in range(len(self._deck) -1, 0, -1):
            r = random.randint(0, i)
            self._deck[i], self._deck[r] = self._deck[r], self._deck[i]

    def displayDeck(self):  #Displays entire deck
        for i in range(0, 52):
            self._deck[i].cardStats()


#Code for game


def main():
    #Creates shoe
    mainDeck = deck()
    mainDeck.build()
    mainDeck.shuffle()

    #Sets up players and dealer
    dealer = dealerSetUp(mainDeck)
    playerSize = playerAmount()
    playersList = playerSetUp(playerSize, mainDeck)

    #Game
    makeBet(playersList, 0)
    dealer.displayDealer()
    playersList[0].displayStats()
    for i in range (1, playerSize):
        cpuMakeBet(playersList, i)
        playersList[i].displayStats()
    
    activePlayers = playerSize
    check = 0   #Used to make sure a loop iterates only once
    
    for game in range (0, 10):
        print ("Game", game+1)
        while (activePlayers > 0):
            if dealer.handValue() < 17:
                dealer.drawCard(mainDeck)
            if playersList[0].handValue() < 21:
                hitOrStand = int(input("Would you like to Hit(1) or Stand(0): "))
                if hitOrStand > 0:
                    makeBet(playersList, 0)
                    playersList[0].drawCard(mainDeck)
            elif playersList[0].handValue() >= 21 and check == 0:
                activePlayers -= 1
                check += 1
            for i in range (1, playerSize):
                if playersList[i].handValue() < 21:
                    cpuMakeBet(playersList, i)
                    playersList[i].drawCard(mainDeck)
                else:
                    activePlayers -= 1

            dealer.displayDealer()
            for i in range(0, playerSize):
                playersList[i].displayStats()
        
            for i in range (0, playerSize):
                if playersList[i].handValue() == 21:
                    playersList[i].blackjack()
                    activePlayers -= 1

                elif dealer.handValue() > 21 and playersList[i].handValue() < 21:
                    playersList[i].regPayOff()

                elif playersList[i].handValue() >= dealer.handValue() and playersList[i].handValue() <= 21:
                    playersList[i].regPayOff()

        dealer.restart()
        for i in range(0, playerSize):
            playersList[i].restart()

def playerAmount():     #Gets how many players will be in a game
    players = int(input("Enter the amount of players [up to 6]: "))
    while players < 1 or players > 6:  #Input validation
        players = int(input("Invalid! Enter the amount of players [up to 6]: "))
    return players

def playerSetUp(pSize, deck): #Initializes all players to the default
    playerArray = []
    for i in range (0, pSize):
        player = playerStats(i+1, 5000, 0, 0, 0)
        playerArray.append(player)
        player.drawCard(deck)
        player.drawCard(deck)
    return playerArray

def makeBet(pList, index):  #Sets the bet for each player and checks if it's valid
    betTemp = int(input("Enter the amount you would like to bet [0 or 25-500]: "))
    if betTemp != 0:
        while betTemp < 25 or betTemp > 500:
            betTemp = int(input("Invalid! Enter the amount you would like to bet [0 or 25-500]: "))
    pList[index].setBet(betTemp)

def cpuMakeBet(pList, index):
    hitOrStand = random.randint(1,2)
    if hitOrStand == 1:
        betTemp = random.randint(25,500)
    else:
        betTemp = 0
    pList[index].setBet(betTemp)

def dealerSetUp(deck):
    deal = dealer(0)
    deal.drawCard(deck)
    deal.drawCard(deck)

    return deal

main()  #Runs the entire program