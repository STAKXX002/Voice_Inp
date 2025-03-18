import whisper
import os

model = whisper.load_model("base")

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
