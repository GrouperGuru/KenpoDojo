#!/usr/bin/env python3

import speech_recognition as speech
from gtts import gTTS
import os as player
import random
import time

def listening():
    # obtain audio from the microphone
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
        return None
    except speech.RequestError:
        print("Unable to connect to speech engine services. Please check your connection or API details.")
        return None

def response(response_text):
    print(response_text)
    tts = gTTS(text=response_text, lang='en')
    tts.save("response.mp3")
    player.system('afplay response.mp3')

techniques = "techniques.txt"

def main():
    while True:
        orders = listening()
        trigger = "dojo"

        if orders and trigger in orders:
            if "start training" in orders:
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
                response("See you soon!")
                break

if __name__ == "__main__":
    response("Hello, I'm your Dojo assistant. To interact simply say, Dojo.")
    main()