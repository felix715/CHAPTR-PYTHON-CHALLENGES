import random
import math

def play():
    user= input("what is your choice? 'r' for rock or 'p' for paper? or 's' for scissors? \n")
    user= user.lower()

    computer = random.choice(['r','p','s'])

    if user == computer:
        # return "You and the Computer have chosen {}.It's a tie.".format(computer)
        return (0,user,computer)
    if is_win(user,computer):
        # return "You have chosen {} and the computer has chosen {}. You Won!!".format(user,computer)
        return (1,user,computer)
    # return "You have chosen {} and the computer has chosen {}. You Lost!!".format(user, computer)
    return (-1, user, computer)
def is_win(player,opponent):
    # returns true if the player beats the opponent
    # winning conditions r>s,s>pp>r
    if (player=='r' and opponent=='s')or (player== 's'and opponent=='p')or (player=='p' and opponent=='r'):
        return True
    return False
def play_best_of(n):
#     play against the computer untill someone wins best of n games
# to win you must win ceil(n/2)games
    player_wins=0
    computer_wins=0
    wins_necessary=math.ceil(n/2)
    while player_wins<wins_necessary and computer_wins<wins_necessary:
        result,user,computer=play()
        if result==0:
            print("I's a Tie.You and the Computer have chosen {}.\n".format(computer))
        elif result==1:
            player_wins+=1
            print("You have chosen {} and the computer has chosen {}. You Won!\n.".format(user,computer))
        else:
            computer_wins+=1
            print("You have chosen {} and the computer has chosen {}. You Lost!\n".format(user, computer))
        print()
    if player_wins>computer:
        print("You have won the best of {} games!What a champ:D".format(n))
    else:
        print("Unfortunately the computer has won the best of {}games.Better try again later")
if __name__=='__main__':
     play_best_of(3)

