import speech_recognition as sr
from gtts import gTTS  #google text to speech
import os


def listen(): #listen is a function name , when called will excecute the code after :
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source) #used to denoise background voice
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results: {e}"


def speak(text):
    tts = gTTS(text)
    tts.save("output.mp3")
    os.system("output.mp3")


if __name__ == "__main__":
    while True:
        user_input = listen()
        print("You said:", user_input)

        if "hello" in user_input.lower():
            response = "Hello! How can I assist you?"
            speak(response)
        elif "goodbye" in user_input.lower():
            response = "Goodbye! Have a great day."
            speak(response)
        elif "what is my name" in user_input.lower():
            response ="Your name is Sakshi"
            speak(response)
        elif "when is my birthday" in user_input.lower():
            response ="Your birthday is on thirty first of august"
            speak(response)
        elif "what is my branch" in user_input.lower():
            response = "Your branch is Artificial intelligence and machine learning"
            speak(response)
        elif "what is the name of my college" in user_input.lower():
            response = "Manglore institute of technology and engineering"
            speak(response)