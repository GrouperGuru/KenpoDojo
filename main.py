#!/usr/bin/env python3

import speech_recognition as speech
from gtts import gTTS
import os as player

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

tasks = []

def main():
    while True:
        orders = listening()
        trigger = "assistant"

        if orders and trigger in orders:
            if "add a task" in orders:
                response("What task would you like to add?")
                task = listening()
                tasks.append(task)
                response("Adding " + task + " to your list of tasks")
            elif "list tasks" in orders:
                response("Your tasks are:")
                for task in tasks:
                    response(task)
            elif "exit" in orders:
                response("See you soon!")
                break

if __name__ == "__main__":
    response("Hello, I'm your Dojo assistant. To interact simply say, Assistant.")
    main()