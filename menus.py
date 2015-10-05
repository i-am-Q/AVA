from random import randint

def menu_intro():
    print '-'*85
    print ''
    print 'Hello! My name is AVA (Automated Virtual Assistant). To wake me up, simply say \"AVA\".'
    print ''
    print 'If you would like you can also ask me a question by saying my name then your question'
    print ''
    print '-'*85


def menu_choice():
    print '-'*80
    print ''
    askable = ['How about you ask me for the current wearther in your area?',
               'How about you ask me for the weather forecast in your area?',
               'How about we find out who the first president is?',
               'How about we find out how tall michael jordan is?',
               'Do you need to add anything to your to do list?',
               'I have a funny joke, do you wnat to hear it?',
               'Would you like to play a game of rock paper scissors?',
               'Would you like to play a game of higher or lower?']
    x = randint(0,len(askable)-1)
    print askable[x]
    print ''
    print '-'*80
