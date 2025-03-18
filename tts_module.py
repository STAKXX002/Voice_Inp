import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 160)  
engine.setProperty("voice", engine.getProperty("voices")[2].id)

def text_to_speech(text):
    """Converts chatbot response into speech."""
    engine.say(text)
    engine.runAndWait()
