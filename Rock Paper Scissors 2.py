#explore random

# import module with random number code
import random
import time


# initialize game clock
again=True

#initialize score
computer_win=0
player_win=0

# user experience
print('*------------------------------------*')
print('*-----ROCK,--------------------------*')
print('*----------PAPER,--------------------*')
print('*----------------SCISSORS------------*')
print('*------------------------------------*')
print('')
time.sleep(3)
print('   First one to 5 points wins!')
print('')
print('*------------------------------------*')

time.sleep(2.5)

# initialize valid plays
choice = ['Rock','Paper','Scissors']

# start main game loop
while(again==True): 

    # pick number 
    pick=random.randint(0,2)
    
    
    # user experience
    print("* Score - Computer:"+str(computer_win)+" Player:"+str(player_win))
    print('*------------------+--------------------*')
            
    # select number from list of plays
    computer_choice = choice[pick]
    
    # user experience, appear as if computer is thinking
    for loop in range(random.randint(1,5)):
        print("*   Computer cogitating <.    >      *", end = '\r') 
        time.sleep(0.12)
        print("*   Computer cogitating < .   >      *", end = '\r')
        time.sleep(0.12)
        print("*   Computer cogitating <  .  >      *", end = '\r')
        time.sleep(0.12)
        print("*   Computer cogitating <   . >      *", end = '\r')
        time.sleep(0.12)
        print("*   Computer cogitating <    .>      *", end = '\r')
        time.sleep(0.12)
        print("*   Computer cogitating <   . >      *", end = '\r')
        time.sleep(0.12)
        print("*   Computer cogitating <  .  >      *", end = '\r')
        time.sleep(0.12)
        print("*   Computer cogitating < .   >      *", end = '\r')

    print("*   Computer cogitating <  !  >     *", end = '\r')
    time.sleep(0.25)
    print("*                                       *")
    # prompt player for play

    player_choice= input("* Player choice? (Q to Quit):")
    
    
    #user experience
    player_choice=player_choice.title()  #so user does not have to match case

    # confirm valid play
    if player_choice in choice:
        #both plays are the same
        print('* >Computer chose '+computer_choice+'.                 *')

        time.sleep(1)  #user experience

        if computer_choice==player_choice:
            print("* >TIE")
            #next line is an error !  computer should not get points in tie
            computer_win=computer_win+1
        #computer chose rock
        elif computer_choice=="Rock" and player_choice=="Scissors":
            print("* >Computer Wins ~"+computer_choice+' beats '+player_choice+'.')
            computer_win=computer_win+1
        #computer chose scissors
        elif computer_choice=="Scissors" and player_choice=="Paper":
            print("* >Computer Wins ~"+computer_choice+' beats '+player_choice+'.')
            computer_win=computer_win+1
        #computer chose paper
        elif computer_choice=="Paper" and player_choice=="Rock":
            print("* >Computer Wins ~"+computer_choice+' beats '+player_choice+'.')
            computer_win=computer_win+1
        # player won
        else :
        #update player on win/loss
            player_win=player_win+1           
            print("* >Player Wins ~"+player_choice+' beats '+computer_choice+'.')
    elif player_choice == 'Q':
        again=False 
    else: 
        print("* >Invalid choice                      *")

    # user experience
    print('*                                       *')
    time.sleep(2)
    
    # user experience
    print('*---------------------------------------*')



    if max(computer_win,player_win)>4:
        again=False 
        if computer_win>player_win:
            print('!!! Computer Wins  !!!')
        else :
            print('    Player Wins      ')
            

    
    