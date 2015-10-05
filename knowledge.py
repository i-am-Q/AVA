from voice import talking
from ears import listening
import urllib
import xml.etree.cElementTree as ET
import time
import re
import wikipedia
import config
import comprehension


def wolfram_alpha(my_question):

    searching = True
    search_item = 0
    some_text = None

    look_for = my_question
    talking('let me think')
    key = config.wolf_key
    my_question = my_question.replace('ava ', '')
    my_question = my_question.replace(' ', '+')
    print my_question
    url = 'http://api.wolframalpha.com/v2/query?appid=' + key + '&input=' + my_question + '&format=plaintext'

    tree = ET.ElementTree(file=urllib.urlopen(url))
    for elem in tree.iterfind('pod[@title="Result"]/subpod/plaintext'):
        some_text = elem.text
    try:
        some_text = some_text.replace('\'', ' feet')
        some_text = some_text.replace('\"', ' inches')
        talking(some_text)
        time.sleep(1)
    except Exception, e:
        print e
        pattern = re.compile('([^\s\w]|_)+')
        b_string = re.sub(pattern, '', look_for)
        phrase = b_string
        print phrase
        pattern = re.compile("\\b(lot|lots|a|an|who|can|you|what|is|info|somethings|whats|have|i|something|to|know|like"
                             "|Id|information|about|tell|me)\\W", re.I)
        phrase_noise_removed = [pattern.sub("", phrase)]
        print phrase_noise_removed[0]
        term_search = wikipedia.search(phrase_noise_removed[0])
        # ToDo: test this portion. It checks to see if what AVA is searching for is the correct thing
        while searching:
            text = 'would you like me to get information on %s' % term_search[search_item]
            talking(text)
            rsp = listening()
            my_rsp = comprehension.pre_selection(rsp, ['yes', 'no'])
            if (my_rsp == [0]) and (search_item <= 2):
                print term_search[search_item]
                the_summary = (wikipedia.summary(term_search[search_item], 2))
                print the_summary
                talking(the_summary)
                searching = False
            elif my_rsp == [1]:
                talking('ok')
                search_item += 1


# This module gets the top storries from CNN
def top_stories():
    url = 'rss.cnn.com/rss/edition.rss'
    tree = ET.ElementTree(file=urllib.urlopen(url))
    root = tree.getroot()

    index1 = 0
    index2 = 0
    index3 = 0
    x = 0

    # ToDo: test this section; determines the necesary length of the array
    for item in root.iterfind('channel/item/title'):
        index1 += 1

    goodtext = [None] * index1
    mytitle = [None] * index1

    # gets the titles of each article
    for item in root.iterfind('channel/item/title'):
        mytitle[index3] = item.text
        index3 += 1

    # gets the description of each article
    for item in root.iterfind('channel/item/description'):
        mytext = item.text
        goodtext[index2] = mytext.split('<br', 1)[0]
        index2 += 1

    # if there is no description then use the article title instead
    for stuff in goodtext:
        if stuff == '':
            talking(mytitle[x])
        else:
            talking(stuff)
        x += 1
