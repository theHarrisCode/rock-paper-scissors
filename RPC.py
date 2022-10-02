import random

def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors ")
    computer = random.choice(['r','p','s'])

    def computer_answer():
        if(computer == 'r'):
            print('The computer selected rock.')
        if(computer == 's'):
            print('The computer selected scissors.')
        if(computer == 'p'):
            print("The computer selected paper")

    if user == computer:
        computer_answer()
        return 'It\'s a tie'

    #r > s, s > p, p > r
    if is_win(user, computer):
        computer_answer()
        return 'You Won!'

    computer_answer()
    return 'You Lost!'


def is_win(player, opponent):
    # return true if player wins
    #r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())