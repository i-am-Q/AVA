from random import randint
from comprehension import pre_selection
from voice import talking
from ears import listening


def play_hi_low():
    play_again = True

    while play_again:
        cont = True
        num_guess = 0
        comp_num = randint(1, 10)
        print comp_num
        talking('I have picked a number between one and ten. Can you guess what it is?')
        while True:
            player_guess = listening()
            # checks for the number 6 (has difficulty understanding difference between 6 and sex)
            if player_guess == 'sex':
                player_guess = '6'
            # checks for the number 4 (has difficulty understanding difference between 4 and thor)
            if player_guess == 'thor':
                player_guess = '4'
            try:
                player_guess = int(player_guess)
            except (ValueError, TypeError), e:
                print e
            if player_guess == comp_num:
                num_guess += 1
                text = 'Congratulations! You won in %i guesses!' % num_guess
                talking(text)
                talking('Do you want to play again. Yes or no?')
                i_said = listening()
                key = ['yes', 'no', 'quit']
                redo = pre_selection(i_said, key)
                while cont:
                    if redo == [0]:
                        cont = False
                        break
                    elif (redo == [1, 2]) or (redo == [1]) or (redo == [2]):  # if anything else is said, assume a quit
                        play_again = False
                        cont = False
                        break
                    else:
                        talking('I am sorry. please say either yes or no')
                        break
                break
            elif player_guess < comp_num:
                talking('Guess higher')
                num_guess += 1
            elif player_guess > comp_num:
                talking('Guess lower')
                num_guess += 1


class RPSGame:
    def __init__(self):
        comp_score = 0
        player_score = 0
        tie_game = 0
        player = 0
        playing = True
        validity = True
        talking('Lets play a game of Rock, Paper, Scissors')
        while playing:
            while validity:
                i_said = listening()
                bro_commands = ['rock', 'paper', 'scissors', 'quit', 'Rock']
                player_hand = pre_selection(i_said, bro_commands)
                if (player_hand == [0]) or (player_hand == [4]):
                    player = 1
                    break
                elif player_hand == [1]:
                    player = 2
                    break
                elif player_hand == [2]:
                    player = 3
                    break
                elif player_hand == [3]:
                    player = 4
                    break
                else:
                    print 'Invalid Choice'
            if player == 4:
                if player_score > comp_score:
                    text = 'final score, player %i, computer %i, Congratulations you win' % (player_score, comp_score)
                elif player_score < comp_score:
                    text = 'final score, player %i, computer %i, Computer wins' % (player_score, comp_score)
                else:
                    text = 'final score, player %i, computer %i, tie game' % (player_score, comp_score)
                talking(text)
                break

            else:
                comp = self.comp_hand()
                result = self.play_hand(comp, player)
                player_choice = self.interpret(player)
                comp_choice = self.interpret(comp)
                print '\nYou played %s and the computer played %s' % (player_choice, comp_choice)
                talking(result)
                print ''
                print '-' * 34
                if result == 'Computer wins!':
                    comp_score += 1
                elif result == 'Player wins!':
                    player_score += 1
                elif result == 'Tie game':
                    tie_game += 1
                print 'Player: %i Computer: %i Tie Games: %i' % (player_score, comp_score, tie_game)
                print '-' * 34
                print ''

    @staticmethod
    def comp_hand():
        comp_val = randint(1, 3)
        return comp_val

    @staticmethod
    def interpret(num):
        if num == 1:
            talking('Rock')
            return 'Rock'
        elif num == 2:
            talking('Paper')
            return 'Paper'
        elif num == 3:
            talking('Scissors')
            return 'Scissors'

    @staticmethod
    def play_hand(comp, player):
        if comp == player:
            return 'Tie game'
        if (comp == 1 and player == 3) or (comp == 2 and player == 1) or (comp == 3 and player == 2):
            return 'Computer wins!'
        else:
            return 'Player wins!'


def tell_joke():
    jokes = ['A ham sandwich walks into a bar and orders a beer. Bartender says, Sorry we do not serve food here.',
             'Why do chicken coops only have two doors? Because if they had four, they would be chicken sedans!',
             'Why did the Clydesdale give the pony a glass of water? Because he was a little horse!',
             'How do you make a Kleenex dance? Put a little boogie in it!',
             'Two peanuts were walking down the street. One was a salted.',
             'How do you make holy water? You boil the hell out of it.',
             'A woman is on trial for beating her husband to death with his guitar collection. Judge says, First '
             'offender? She says, No, first a Gibson! Then a Fender!',
             'I had a dream that I was a muffler last night. I woke up exhausted!',
             'How do you tell the difference between a frog and a horny toad? A frog says, Ribbit, ribbit and a horny '
             'toad says, Rub it, rub it.',
             'A three legged dog walks into a bar and says to the bartender, Im looking for the man who shot my paw.',
             'Whats Forrest Gumps password? 1 forrest 1']
    x = randint(0, len(jokes)-1)
    print len(jokes)
    print 'telling joke number %i' % x
    talking(jokes[x])
