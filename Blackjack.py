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
winner = ''
playersHand = []
computersHand = []

#This function will pick a card at random from the deck
def pickCard(num):
    chosen = []
    i=0   
    while i < num:
        x = random.randint(0,51)

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
        playersHand.extend(pickCard(1))
        print("Your hand is:")
        readout(playersHand)
        print('---------------------------------------------------------')
    
    
    elif ans == 'stand':
        draw = True

        scoreP = getPoints(playersHand)
        if any(s == 21 for s in scoreP):
            draw = False
            roundOver = True
            winner = 'play'
        Pdiff = [abs(21 - scoreP[0]), abs(21 - scoreP[1])]

        while draw == True: 
            computersHand.extend(pickCard(1))
            readout(computersHand)
            
            scoreC = getPoints(computersHand)
            Cdiff = [abs(21 - scoreC[0]), abs(21 - scoreC[1])]
            
            if ((Cdiff[0] and Cdiff[1]) < (Pdiff[0] and Pdiff[1])) and (any(s < 21 for s in scoreC)):
                winner = 'comp'
                roundOver = True
                draw = False
            elif any(x == 0 for x in Cdiff):
                winner = 'comp'
                roundOver = True
                draw = False
            elif ((Pdiff[0] and Pdiff[1]) < (Cdiff[0] and Cdiff[1])) and (any(p <= 21 for p in scoreP)):
                winner = 'comp'
                roundOver = True
                draw = False
            elif any(o > 21 for o in scoreC):
                winner = 'player'
                roundOver = True
                draw = False

            

            





def getPoints(Hand):
    #Extract point values from the card and check if it is less than 21
    i = 1
    vals= [None] * len(Hand)
    aceP = 0


    while i <= len(Hand):
        cardName = Hand[i-1]
        position = cards.index(cardName)
        vals[i-1] = cardval[position]
        i = i + 1
    
    

    points = [0,0]
    points[0] = sum(vals)
    if 1 in vals:
        aceP = points[0] + 10

    points[1] = aceP

    return points



def checkScore(computersHand,playersHand,draw,roundOver):
    #Assign point values for both hands
    cPoints = getPoints(computersHand)
    pPoints = getPoints(playersHand)

    


    #Defined absolute win cases for point values
    if cPoints[0] == 21 or cPoints[1] == 21:
        winner = 'comp'
        roundOver = True
    elif pPoints[0] == 21 or pPoints[1] == 21:
        winner = 'play'
        roundOver = True

    if any(p != 21 for p in pPoints) or any(c != 21 for c in cPoints):
        roundOver = False
        draw = True
        if any(x > 21 for x in pPoints):
            roundOver = True
            draw = False
            winner = 'comp'
        elif any(y > 21 for y in cPoints):
            roundOver = True
            draw = False
            winner = 'play'        


    stat = [roundOver,cPoints,pPoints]
    return stat


     




def playGame():

    #Create a hand for both the computer and player
    computersHand.extend(pickCard(1))
    print('\nThe computers hand is:')
    readout(computersHand)
    playersHand.extend(pickCard(2))
    print('\nYour hand is:')
    readout(playersHand)


    
    
    roundOver = False
    draw = False
    #Checks if the round is over
    t = getPoints(playersHand)
    if():
        roundOver = True
        
    while roundOver == False:
        print('---------------------------------------------------------')
        ans = input('\nWould you like to hit or stand\n')
        sequence(ans)
        #Checks score and will break the loop if the round is over
        
        score = checkScore(computersHand,playersHand,draw,roundOver)
        roundOver = score[0]
    
    if score[1] == 'comp':
        print('Sorry you lose')
        input('hit a button when ready')
    elif score[1] == 'play':
        print('You win!')
        input('hit a button when ready')
        

    
    

roundOver = False
endless = False
print("Hello, welcome to Blackjack!")
t = input('Would you like to activate endless mode? Y/N \n')
print("\nYou can type end at any given time to stop the program")

while t != 'Y' and t != 'N':
     print("Invalid input!")
     t = input('Would you like to activate endless mode? Y/N \n')

if t == 'Y':
    endless = True
    while endless == True:
        playGame()
        print(winner + 'wins!')
        print('---------------------------------------------------------')
        print('NEW ROUND!')
        print('---------------------------------------------------------')
        #Clear both hands
        computersHand = []
        playersHand = []

if t == 'N':
    playGame()

