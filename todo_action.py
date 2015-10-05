from voice import talking
from ears import listening
from comprehension import pre_selection
from mail_sender import send_email
import config


def todo(action):
    """
    talking('would you like to add to your to do list or clear it')
    key = ['add','clear','ad']
    i_said = listening()
    a = pre_selection(i_said, key)
    print a"""

# prints todo list
    if action == [11, 12]:
        the_start = True
        while the_start:
            try:
                my_file = open(config.todo_loc, 'r')
            except IOError:
                print 'No ToDo list exists, creating a new file'
                my_file = open(config.todo_loc, 'w')
                my_file.close()
                my_file = open(config.todo_loc, 'r')
            f = my_file.readlines()
            my_file.close()
            talking('what would you like to add to your list')
            while True:
                try:
                    i_said = listening()
                    f.insert(0, i_said + '\n')
                    break
                except TypeError, e:
                    print e
                    print 'nothing was said'
            my_file = open(config.todo_loc, 'w')
            my_file.writelines(f)
            my_file.close()
            talking('your task has been added, would you like to add more')
            try:
                i_said = listening()
                key = ['yes', 'ad', 'add', 'more', 'done', 'no', 'finished']
                find_truth = pre_selection(i_said, key)
                for num in find_truth:
                    print find_truth
                    yes_test = [0, 1, 2, 3]
                    no_test = [4, 5, 6]
                    a = num in yes_test
                    if a:
                        for num2 in find_truth:
                            b = num2 in no_test
                            if b:
                                the_start = False
                            else:
                                print 'adding more'
                    elif not a:
                        for num2 in find_truth:
                            b = num2 in no_test
                            if b:
                                the_start = False
            except TypeError, e:
                the_start = False
                print e
                break
# Clears the todo list
    elif action == [11, 14]:
        try:
            talking('clearing your to do list')
            my_file = open(config.todo_loc, 'r')
            my_file.close()
            f = []
            my_file = open(config.todo_loc, 'w')
            my_file.writelines(f)
            my_file.close()
            talking('your list has been cleared')
        except IOError:
            print 'file not created'
# Reads back the todo list
    elif action == [11, 13]:
        try:
            my_file = open(config.todo_loc, 'r')
        except IOError:
            print 'No ToDo list exists, creating a new file'
            my_file = open(config.todo_loc, 'w')
            my_file.close()
            my_file = open(config.todo_loc, 'r')
        f = my_file.readlines()
        my_file.close()
        y = 0
        f2 = f
        for n in f:
            y += 1
            f2[y - 1] = str(y) + ': ' + f[y - 1] + '\n'
        f_readable = ''.join(f2)
        x = len(f)
        if x == 1:
            text1 = 'you have one item on your list'
            text = text1 + 'and it is:' + f_readable
        elif x > 1:
            text1 = 'you have %s items on your list' % x
            text = text1 + ' and they are:\n' + f_readable
        else:
            text = 'you have zero items on your list'
        talking(text)
        talking('Would you like me to send this to your email?')
        i_said = listening()
        key = ['yes', 'no']
        a = pre_selection(i_said, key)
        if a == [0]:
            talking('preparing your todo list to be sent')
            send_email(text, 'ToDo List')
        elif a == [1]:
            pass
