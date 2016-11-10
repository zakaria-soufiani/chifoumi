
import random
 

#Variable defining#
count = 0
match = 0
pointsh = 0
pointsc = 0
callfire = 0
comp_guess_og = ['rock', 'paper', 'scissors']
game = 1
friends_counter = 0
#Function defining#
def tryagain():
    if friends_counter == 0:
        lines()
        print "Try rock || paper || scissors || Joey's secret move"
        lines()
       
    elif friends_counter == 1:
        lines()
        print "COME ON ! You don't know what Joey's secret move is ?"
        lines()
        print "Try rock || paper || scissors || Joey's secret move"
        lines()
       
    elif friends_counter == 2:
        lines()
        print "Have you ever watched friends ? EVER ?"
        lines()
        print "Try rock || paper || scissors || Joey's secret move"
        lines()
       
    elif friends_counter >= 3:
        lines()
        print "The secret move is fire. Such a dissapointment"
        lines()
        print "Try rock || paper || scissors || Joey's secret move"
        lines()


def showmethebooty():
    i = 0
    while i <= 5:
        print u'(\u0361\u00b0\u035c\u0296\u0361\u00b0)',u'(\u0361\u00b0\u035c\u0296\u0361\u00b0)',u'(\u0361\u00b0\u035c\u0296\u0361\u00b0)', u'(\u0361\u00b0\u035c\u0296\u0361\u00b0)',u'(\u0361\u00b0\u035c\u0296\u0361\u00b0)', u'(\u0361\u00b0\u035c\u0296\u0361\u00b0)'
        i += 1

def lines():
    print '-------------------------------------------------------------------------------------------'

def endofgame():
    global pointsc, pointsh, callfire
    if(pointsc > pointsh) and callfire == 0:
        print ''
        print "AND the Computer wins the game"
    elif callfire == 1 :
        pointsh = 100000000000000000000
        print ''
        lines()
        print "Fire called, player WINS the game and decimates the computer. Take that technology !"
        lines()
        showmethebooty()
    elif (pointsc < pointsh) and callfire == 0:
        print ''
        print "AND YOU win the game"
        lines()
                
def score():
    print "====||| SCORE BOARD |||===="
    print "Computer : ", pointsc
    print "Player : ", pointsh
    print ''
def compwin():  
    print ''
    print "your guess was ", guess, "and the computer guess was ", comp_guess
    lines()
    print "Computer wins this round!"
    lines()
def pointscomp():
    global pointsc 
    pointsc+= 1    
    
def pointshum():
    global pointsh 
    pointsh+= 1

def matchinc():
    global match 
    match += 1    

def comploose():
    print ''
    print "your guess was ", guess, "and the computer guess was ", comp_guess
    lines()
    print "You win this round !"
    lines()

def tie():
    print ''
    print "your guess was ", guess, "and the computer guess was ", comp_guess
    lines()
    print "It's a tie"
    lines()

def game(guess):
   
    global callfire
    if guess == 'rock':
        if comp_guess == 'paper':
            compwin()
            pointscomp()
            matchinc() 
            
        elif comp_guess == 'scissors':
            comploose()
            pointshum()
            matchinc()
           
        elif comp_guess == guess:
            tie()
           
    elif guess == 'paper':
        if comp_guess == 'scissors':
            compwin()   
            pointscomp()
            matchinc()
           
        elif comp_guess == 'rock':
            comploose()
            pointshum()
            matchinc()
           
        elif comp_guess == guess:
            tie()
           
    elif guess == 'scissors':
        if comp_guess == 'paper':
            comploose()
            pointshum()
            matchinc()
           
        elif  comp_guess == 'rock':
            compwin()
            pointscomp()
            matchinc()
           
        elif  comp_guess == guess:
            tie()
    elif guess == 'fire':
        callfire = 1
        endofgame()

while True:

    while (pointsh < 2 and pointsc < 2 and callfire == 0):    
        guess = raw_input ("Enter rock OR paper OR scissors (you can use Joey's secret move) =>> ")
        if (guess == 'rock' or guess == 'paper' or guess == 'scissors' or guess == 'fire'):
            comp_guess = comp_guess_og[random.randrange(0,2)]           
            game(guess)
            print ''
            score()
        elif guess == 'score':
            score()
        elif guess == "Joey's secret move":
            lines()
            print "YOu seriously thought this was the secret move ? HA-HA "
            lines()
            tryagain() 
        else:
            lines()
            print 'WRONG INPUT ! TRY AGAIN !'
            lines()
            tryagain()
            friends_counter += 1
            lines()
    if (pointsh == 2 or pointsc == 2) :
        endofgame()
        break
            
    elif (callfire == 1):
        break     
