import speech_recognition as sr

def check_ambient_noise():
    """Calibrates microphone for ambient noise."""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Calibrating for ambient noise... Stay silent for 2 seconds.")
        recognizer.adjust_for_ambient_noise(source, duration=2.0)  
        print(f"Noise threshold set to: {recognizer.energy_threshold}")

    return recognizer

def record_speech(recognizer):
    """Records user speech after calibration."""
    with sr.Microphone() as source:
        print("Now speak into the microphone...")
        audio = recognizer.listen(source)  
        
    print("Processing audio...")
    return audio
