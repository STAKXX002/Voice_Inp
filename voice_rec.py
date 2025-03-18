import speech_recognition as sr
import whisper
import os

recognizer = sr.Recognizer()
recognizer.pause_threshold = 1.5  

model = whisper.load_model("base") 

print("Speak into the microphone...")

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source) 
    audio = recognizer.listen(source)  

print("Processing audio...")

with open("temp_audio.wav", "wb") as f:
    f.write(audio.get_wav_data())

result = model.transcribe("temp_audio.wav")
print("Transcription: ", result["text"])

os.remove("temp_audio.wav")
