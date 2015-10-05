# listening defines a microphone as a source and then listens for speech above a certain level


import speech_recognition as sr
import time
import subprocess
import voice
import thread
import pyaudio

r = sr.Recognizer()


def listening():
    my_words = ''
    with sr.Microphone() as source:
        print '-'*50
        print ''
        #  time.sleep(5)
        print 'Adjusting for background noise'
        try:
            thread.start_new_thread(voice.play_audio, ('/ava/bingbong.wav',))
        except Exception, e:
            print(e)
        r.adjust_for_ambient_noise(source, duration=1.25)
        print("Initial minimum energy threshold is {}".format(r.energy_threshold))
        if r.energy_threshold < 1000:
            r.energy_threshold = 1000
            print 'Threshold was to low and has been increased'
            print("Current minimum energy threshold is {}".format(r.energy_threshold))
        print 'I am listening'
        audio = r.listen(source, timeout=None)
    try:
        try:
            my_words = r.recognize(audio)
        except AttributeError, e:
            print e
            try:
                my_words = r.recognize_google(audio)
            except Exception:
                print 'I did not understand'
                pass
        my_words = my_words.lower()
        try:
            subprocess.call(["afplay", '/ava/bongbing.wav'])
        except OSError, e:
            subprocess.call(['aplay', '/ava/bongbing.wav'])
        print('You said:' + my_words)
        print ''
        return my_words
    except LookupError:
        print 'I did not understand'

