#!/usr/bin/env python3

import speech_recognition as speech
import pyttsx4 as voice
import os as player
import random
import time

def listening():
    recognition = speech.Recognizer()
    with speech.Microphone() as source:
        print("Say something!")
        recognition.adjust_for_ambient_noise(source)
        audio = recognition.listen(source)
    try:
        command = recognition.recognize_google(audio)
        print("Heard: ", command)
        return command.lower()
    except speech.UnknownValueError:
        print("I couldn't understand that. Please try again.")
        response("I couldn't understand that. Please try again.")
        return None
    except speech.RequestError:
        print("Unable to connect to speech engine services. Please check your connection or API details.")
        response("Unable to connect to speech engine services. Please check your connection or API details.")
        return None

def response(response_text):
    #print(response_text)
    tts = voice.init()
    voices = tts.getProperty('voices')
    tts.setProperty('rate', 130)
    tts.setProperty('volume', 1.0)
    tts.setProperty('voice', voices[108].id)
    tts.say(response_text)
    tts.runAndWait()

techniques = "techniques.txt"

def main():
    while True:
        orders = listening()
        trigger = "dojo"

        if orders and trigger in orders:
            if "help" in orders:
                response("I can perform the following actions: ")
                response("Say 'Dough Jo Start Training' and I will read aloud randomly selected lines from your techniques list.")
                response("Say 'Dough Jo Next' and I will read aloud one random line from your techniques list.")
                response("Say 'Dough Jo Exit' and The training will complete and the application will close.")
            elif "start training" in orders:
                response("Starting training")
                for technique in techniques:
                    lines = open(techniques).read().splitlines()
                    random_line = random.choice(lines)
                    response(random_line)
                    time.sleep(5)
            elif "next" in orders:
                next = True
                for technique in techniques:
                    while next == True:
                        lines = open(techniques).read().splitlines()
                        random_line = random.choice(lines)
                        response(random_line)
                        next = False
            elif "exit" in orders:
                response("I hope you trained well.")
                player.system('afplay "outro.mp3"')
                break

if __name__ == "__main__":
    player.system('afplay "intro.mp3"')
    response("Hello, I'm your Dough Jo assistant.") #Spelling Dojo as Dough Jo due to pronuncation issue.
    response("To interact say the trigger word 'Dough Jo', followed by a command.") #Spelling Dojo as Dough Jo due to pronuncation issue.
    response("For help, say 'Dough Jo' help.") #Spelling Dojo as Dough Jo due to pronuncation issue.
    main()