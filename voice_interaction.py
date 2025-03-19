import speech_recognition as sr
import whisper
import pyttsx3
import os
from faiss_rag import search_rag  # Import FAISS search function

# Load Whisper Model
whisper_model = whisper.load_model("base")

# Text-to-Speech Engine Setup
engine = pyttsx3.init()
engine.setProperty("rate", 160)

def transcribe_audio(audio):
    """Transcribes recorded audio using Whisper AI."""
    audio_path = "temp_audio.wav"
    
    # Save the audio data to a file
    with open(audio_path, "wb") as f:
        f.write(audio.get_wav_data(convert_rate=16000))  

    # Transcribe using Whisper
    result = whisper_model.transcribe(audio_path)
    os.remove(audio_path)  # Delete temp file after use
    return result["text"]

def record_speech():
    """Records user speech."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak.")
        recognizer.adjust_for_ambient_noise(source, duration=2.0)
        audio = recognizer.listen(source)
    return audio

def text_to_speech(text):
    """Converts chatbot response into speech."""
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print("Voice Interaction System Ready! Ask about 'The Gift of the Magi'.")
    
    while True:
        audio = record_speech()
        transcribed_text = transcribe_audio(audio)

        if transcribed_text.lower() in ["exit", "quit", "stop"]:
            print("Exiting...")
            break
        
        print("Transcribed:", transcribed_text)

        # Use FAISS RAG to get a response
        chatbot_response = search_rag(transcribed_text)
        print("RAG Response:", chatbot_response)
        
        text_to_speech(chatbot_response)
