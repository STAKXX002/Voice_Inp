import speech_recognition as sr
import whisper
import pyttsx3
import os

model = whisper.load_model("base")

engine = pyttsx3.init()
engine.setProperty("rate", 160)  
engine.setProperty("voice", engine.getProperty("voices")[2].id)  

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

def transcribe_audio(audio):
    """Transcribes recorded audio using Whisper AI and deletes the temp file after use."""
    audio_path = "temp_audio.wav"
    
    with open(audio_path, "wb") as f:
        f.write(audio.get_wav_data(convert_rate=16000))  

    result = model.transcribe(audio_path)
    text = result["text"]

    os.remove(audio_path)

    print("Transcription:", text)
    return text

def text_to_speech(text):
    """Converts chatbot response into speech."""
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    recognizer = check_ambient_noise()  
    audio = record_speech(recognizer)  
    transcribed_text = transcribe_audio(audio)  

    chatbot_response = f"{transcribed_text}"
    
    print("Chatbot Response:", chatbot_response)
    text_to_speech(chatbot_response)  
