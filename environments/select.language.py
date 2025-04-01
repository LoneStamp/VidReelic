from langdetect import detect


def detect_language(text):
    try:
       
        language = detect(text)
        return language
    except Exception as e:
        return f"Error detecting language: {str(e)}"


text = "Bonjour tout le monde"  


language = detect_language(text)
print(f"The detected language is: {language}")
