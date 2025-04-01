import speech_recognition as sr


recognizer = sr.Recognizer()


def recognize_speech_from_microphone():
    with sr.Microphone() as source:
        print("Please say something...")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source) 

    try:
        print("Recognizing... Please wait.")
       
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError:
        print("Sorry, I'm unable to connect to the speech service. Please check your internet connection.")


if __name__ == "__main__":
    recognize_speech_from_microphone()
