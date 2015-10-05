# ava

"""

ava is a personal assistant that is written in python.

In order to run, the program needs 3 libraries: wikipedia (pip install wikipedia), speech recognition which can be
installed via 'pip install SpeechRecognition' or 'https://pypi.python.org/pypi/SpeechRecognition' (In the folder, run
'python setup.py install`), and you will also need to install pyaudio for microphone access to work. FLAC will also most
likely need to be installed.

You will also need a key from wunderground weather and wolfram alpha. Add these keys as well as the email and password
for a sender and reciever email.

"""

from mainLogic import wake_up
import thread

try:
    thread.start_new_thread(wake_up, ('main thread',))
except Exception, e:
    print(e)
    print 'Error, unable to start thread'

while 1:
   try:
       pass
   except KeyboardInterrupt:
       print 'Now quiting ava. Goodbye'
       break
