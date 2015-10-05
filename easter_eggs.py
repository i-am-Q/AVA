"""
this section is to contain irrelivent projects that are defined as easter eggs
"""
from voice import talking
from comprehension import pre_selection


def decide(i_said):
    key = ['who', 'are', 'made', 'you']
    i_mean = pre_selection(i_said, key)
    if i_mean == [0, 1, 3]:
        identity()
    elif i_mean == [0, 2, 3]:
        maker()
    else:
        print 'no eggs here'


# gives explanation of what AVA is
def identity():
    who_am_i = 'I am the automated virtual assistant better known as ava. I was created to make your life easier'
    talking(who_am_i)


def maker():
    your_maker = 'I was created august 24th by the all knowing Quincy'
    talking(your_maker)

