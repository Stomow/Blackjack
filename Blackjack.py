#Blackjack

import random

#Define all cards
cards = ["aceD",'twoD','threeD','fourD','fiveD','sixD','sevenD','eightD','nineD','tenD','jackD','queenD','kingD',
        'aceH','twoH','threeH','fourH','fiveH','sixH','sevenH','eightD','nineH','tenH','jackH','queenH','kingH',
        'aceC','twoC','threeC','fourC','fiveC','sixC','sevenC','eightC','nineC','tenC','jackC','queenC','kingC',
        'aceS','twoS','threeS','fourS','fiveS','sixS','sevenS','eightS','nineS','tenS','jackS','queenS','kingS',]

#keeps track of all values of the cards accordingly
#Face cards all hold a value of ten
cardval = [1,2,3,4,5,6,7,8,9,10,10,10,10,
           1,2,3,4,5,6,7,8,9,10,10,10,10,
           1,2,3,4,5,6,7,8,9,10,10,10,10,
           1,2,3,4,5,6,7,8,9,10,10,10,10,]

#Initiate empty arrays for the player and computers hands
playersHand = []
computersHand = []

#This function will pick a card at random from the deck
def pickCard(num):
    chosen = []
    i=0   
    while i < num:
        x = random.randint(0,52)

        chosen.append(cards[x])
        i += 1

    return chosen

#This function cleanly prints out all elements of an array
def readout(hand):
    print(", ".join(hand))
  
     


def sequence(ans):
    if ans == 'end':
            endless == False
    elif ans == 'hit':
        #Player draws 1 card
        readout(playersHand.extend(pickCard(1)))
    elif ans == 'stand':
         print()

    return ans



def playGame(endless):

    #Create a hand for both the computer and player
    computersHand.extend(pickCard(1))
    print('\nComputers hand is:')
    readout(computersHand)
    playersHand.extend(pickCard(2))
    print('Your hand is:')
    readout(playersHand)
    ans = input('Would you like to hit or stand\n')

    if ans != 'end':
        while endless == True:
            sequence(ans)
        

    
    


endless = False
print("Hello, welcome to Blackjack!")
t = input('Would you like to activate endless mode? Y/N \n')
print("You can type end at any given time to stop the program")

while t != 'Y' and t != 'N':
     print("Invalid input!")
     t = input('Would you like to activate endless mode? Y/N \n')

if t == 'Y':
    endless = True
    playGame(endless)
elif t == 'N':
    playGame(endless)

