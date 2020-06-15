import random
import re

money = 100

# Write your game of chance functions here


def coinFlip(bet, userChoice):
    #validating bet and user choice
    if(not isValidBet(bet)):
        return 0
    userChoice = removeSpecialCharacters(userChoice)
    userChoice = userChoice.lower()

    print('playing coin flip')
    print('you bet {bet}$ for {choice}\n'.format(bet=bet, choice=userChoice))
    randNum = random.randint(1, 2)
    coinSide = 'heads' if randNum == 1 else 'tails'
    print('''flipping coin...  coin = {}'''.format(coinSide))
    if(userChoice == coinSide):
        print('you win {}$'.format(bet))
        return bet
    else:
        print('you lose {}$'.format(-bet))
        return -bet


def choHan(bet, userChoice):
    #validating bet and user choice
    if(not isValidBet(bet)):
        return 0
    userChoice = removeSpecialCharacters(userChoice)
    userChoice = userChoice.lower()

    print('playing choHan')
    print('you bet {bet}$ for {choice}'.format(bet=bet, choice=userChoice))
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    modulo = (dice1 + dice2) % 2
    print('''rolling dice... first dice= {} second dice= {}
            \ntotal={}'''.format(dice1, dice2, dice1+dice2))
    if(modulo == 0):
        # even
        if(userChoice == 'even'):
            print('you win {}$'.format(bet))
            return bet
        else:
            print('you lose {}$'.format(-bet))
            return -bet
    else:
        # odd
        if(userChoice == 'odd'):
            print('you win {}$'.format(bet))
            return bet
        else:
            print('you lose {}$'.format(-bet))
            return -bet

def pickACard(bet):
    if(not isValidBet(bet)):
        return 0

    print('playing pick a card')
    print('you bet {}$ for highest card'.format(bet))
    cardValues = [1,2,3,4,5,6,7,8,9,10,11,12,13]    
    deck = cardValues + cardValues + cardValues + cardValues
    randomIndex1 = random.randint(0, len(deck)-1)
    playerCard = deck[randomIndex1]
    del deck[randomIndex1]
    randomIndex2 = random.randint(0, len(deck)-1) 
    computerCard = deck[randomIndex2] 
    del deck[randomIndex2]
    print('''you picked {} your opponent picked {}'''.format(playerCard, computerCard))
    if(playerCard > computerCard):
        print('you win {}$'.format(bet))
        return bet
    elif(playerCard < computerCard):
        print('you lose {}$'.format(-bet))
        return -bet
    else:
        print('the game is tied, you dont win or lose anything')
        return 0

def playRoulette(bet, guess):
    #validating bet and guess
    if(not isValidBet(bet)):
        return 0
    guess = removeSpecialCharacters(guess)

    print('Playing roulette')
    print('you bet {}$ for {}'.format(bet, guess))
    rouletteNums = [0, 2, 14, 35, 23, 4, 16, 33, 21, 6, 18, 31, 19, 8, 12, 29, 25, 10, 27, '00', 1, 13, 36, 24, 3, 15, 34, 22, 5, 17, 32, 20, 7, 11, 30, 26, 9, 28]
    winningNumber = rouletteNums[random.randint(0,len(rouletteNums)-1)]
    print('The winning number is {}'.format(winningNumber))
    modulo = ''
    if(winningNumber !=0 and winningNumber != '00'):
        modulo = winningNumber%2
    if(isinstance(guess, int) or guess == '00'):
        if(guess == winningNumber):
            print('you win {}$'.format(bet*35))
            return bet*35
        else:
            print('you lose {}$'.format(-bet))
            return -bet
    elif(guess.lower() == 'even' and modulo ==0):
        print('you win {}$'.format(bet))
        return bet
    elif(guess.lower() == 'odd' and modulo == 1):
        print('you win {}$'.format(bet))
        return bet
    else:
        print('you lose {}$'.format(-bet))
        return -bet

def printYourBalance():
    print('You have {}$'.format(money))

def isValidBet(bet):
    if(bet <= 0):
        print("you can't bet this amount")
        return False
    elif(bet > money):
        print("sorry you don't have enough money to bet this amount")   
        return False
    else:
        return True 

def removeSpecialCharacters(myString):
    myString = re.sub('[^A-Za-z0-9]+', '', myString)
    return myString

# Call your game of chance functions here
print('WELCOME TO THE CASINO')

gameChoice = 0
while(gameChoice != 5):
    printYourBalance()
    print('''please enter what would you like to play:
1)Coin flip
2)Cho Han
3)Pick a card
4)Roulette
5)To exit''')
    gameChoice = input()
    bet = 0
    try:
        gameChoice = int(gameChoice)
        if(gameChoice >=1 and gameChoice <=4):
            bet = int(input('how much do you want to bet?  '))
    except:
        gameChoice = 100
    if(gameChoice == 1):
        guess = input('please enter heads or tails: ')
        money += coinFlip(bet, guess)
    elif(gameChoice == 2):
        guess = input('please enter odd or even:  ')
        money += choHan(bet, guess)
    elif(gameChoice == 3):
        money+= pickACard(bet)
    elif(gameChoice ==4):
        guess = input('please enter a number from 0-36, 00, odd or even:  ')
        money += playRoulette(bet, guess)
    elif(gameChoice > 5 or gameChoice < 1):
        print('invalid game choice')
    
    input('press anything to continue..\n\n')
        



printYourBalance()
money += coinFlip(1, 'hEads!!!!')
print('\n')

printYourBalance()
money += choHan(4, 'ODD!!!!')
print('\n')
printYourBalance()
money+= pickACard(20)
print('\n')
printYourBalance()
money += playRoulette(1, 'odd')

printYourBalance()
