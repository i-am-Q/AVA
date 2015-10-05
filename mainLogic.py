# main function, will be used to "wake up" similar to "hey siri"
from voice import talking
from ears import listening
from comprehension import pre_selection
from easter_eggs import decide
import games
import weather
import todo_action
import knowledge
import config
import menus


slct = ['high', 'low', 'quit', 'current', 'weather', 'forecast', 'rock', 'paper', 'scissors', 'outside',
        'joke', 'to do', 'add', 'read', 'clear', 'hi-lo', 'what', 'is', 'who', 'how',
        'when', 'where', 'was', 'are', 'you', 'made']


def wake_up(what_thread):
    print 'thread %s has started' % what_thread
    while True:
        menus.menu_intro()
        i_said = listening()
        key = config.my_name
        i_said = i_said.replace('what\'s','what is')
        find_truth = pre_selection(i_said, key)
        if find_truth == [0]:
            selection(i_said)
        else:
            menus.menu_choice()
            print 'no selection made'


def selection(what_i_said):
    find_truth = pre_selection(what_i_said, slct)
    if not find_truth:
        talking('How can I help you sir')
        menus.menu_choice()
        what_i_said = listening()
        what_i_said = what_i_said.replace('what\'s','what is')
        find_truth = pre_selection(what_i_said, slct)
        print find_truth
    while True:

        if (find_truth == [0, 1]) or (find_truth == [15]):
            games.play_hi_low()
            break
        elif find_truth == [2]:
            break
        elif (find_truth == [3, 4, 16, 17]) or (find_truth == [4, 9, 16, 17]) or (find_truth == [3, 4, 9, 16, 17]) \
                or (find_truth == [3, 4]) or (find_truth == [4, 9]) or (find_truth == [3, 4, 9]):
            weather.current_weather()
            break
        elif (find_truth == [4, 5]) or (find_truth == [5]) or (find_truth == [4, 5, 16, 17]) or \
                (find_truth == [4, 16, 17]):
            weather.forecast()
            break
        elif find_truth == [6, 7, 8]:
            games.RPSGame()
            break
        elif find_truth == [10]:
            games.tell_joke()
            break
        elif (find_truth == [11, 12]) or (find_truth == [11, 13]) or (find_truth == [11, 14]):
            todo_action.todo(find_truth)
            break
        elif (find_truth == [16, 17]) or (find_truth == [17, 18]) or (find_truth == [17, 19]) or \
                (find_truth == [17, 20]) or (find_truth == [17, 21]) or (find_truth == [16, 22]) or \
                (find_truth == [22, 18]) or (find_truth == [22, 19]) or (find_truth == [22, 20]) or \
                (find_truth == [22, 21]):
            knowledge.wolfram_alpha(what_i_said)
            break
        else:
            decide(what_i_said)
            break
