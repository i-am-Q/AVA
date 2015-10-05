

# pre_selection compares what the user said against a list of trigger words
def pre_selection(user_text, compare):
    print user_text
    print compare
    try:
        my_command = [user_text.find(word) != -1 for word in compare]
        com_interpreted = [i for i, x in enumerate(my_command) if x]
        return com_interpreted
    except AttributeError, e:
        print e
