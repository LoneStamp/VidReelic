import speech_recognition as sr

def recognize_speech():
   
    recognizer = sr.Recognizer()

   
    with sr.Microphone() as source:
        print("Please say something...")
      
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")


recognize_speech()
