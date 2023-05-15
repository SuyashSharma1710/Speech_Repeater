import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

    while True:
        print("Say something!")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said:", text)

            # Speak the recognized text
            engine.say(text)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Error: {0}".format(e))
