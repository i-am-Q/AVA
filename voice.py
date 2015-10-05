try:
    # will run if on OSX
    from AppKit import NSSpeechSynthesizer
    ve = NSSpeechSynthesizer.alloc().init()
    ve.setVoice_('com.apple.speech.synthesis.voice.kate.premium')
    os_version = 1
except Exception, e:
    # run if on linux
    print e
    from os import system
    os_version = 2

import time
import subprocess


def talking(text):
    # talking creates the estimated time to speak and then creates speech
    talk_time = len(text) / 9
    # runs if OSX
    if os_version == 1:
        while ve.isSpeaking:
            ve.startSpeakingString_(text)
            time.sleep(talk_time)
            break
    # runs if Linux
    elif os_version == 2:
        system('pico2wave -w /tmp/ttspeech.wav \"a ' + text + '\"')
        speak = subprocess.call(['aplay', '/tmp/ttspeech.wav'])


def play_audio(play_track):
    try:
        subprocess.call(["afplay", play_track])
    except OSError, e:
        subprocess.call(['aplay', play_track])
