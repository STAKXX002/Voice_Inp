# Voice_Inp
# Voice Recognition & TTS

This project implements a **speech-to-text** and **text-to-speech** chatbot using **Whisper AI**, **SpeechRecognition**, and **pyttsx3**.

## Features
- **Speech Recognition:** Uses Whisper AI for accurate speech transcription.
- **Ambient Noise Adjustment:** Automatically calibrates the microphone.
- **Text-to-Speech (TTS):** Uses `pyttsx3` for voice output.
- **Temporary File Management:** Removes recorded audio file after transcription.

---

## Tech Stack
- Python
- OpenAI Whisper AI
- SpeechRecognition (`speech_recognition`)
- Text-to-Speech (`pyttsx3`)

---

##  Installation
Ensure you're using **Python 3.11** or the latest stable version.

### Install Dependencies  
```bash
pip install git+https://github.com/openai/whisper.git -q
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install SpeechRecognition -q
pip install pipwin
pipwin install pyaudio  # Only for Windows users
pip install numpy more-itertools numba tqdm tiktoken ffmpeg-python


### **Download Whisper Model** (Required for speech recognition)
Whisper model gets downloaded automatically when running the script for the first time.

---

##  Usage
Run the script:
```bash
python script.py
```
### **Workflow:**
1. **Calibrates the microphone for ambient noise** (stay silent for 2 seconds)
2. **Records your speech**
3. **Transcribes it using Whisper AI**
4. **Speaks out the chatbot response using `pyttsx3`**
---

## Customization
- Change the voice in `pyttsx3`:
```python
engine.setProperty("voice", engine.getProperty("voices")[2].id)
```
- Adjust speech rate:
```python
engine.setProperty("rate", 160)  # Modify speed
```

---

## Notes
- Whisper AI requires a **good-quality microphone** for better accuracy.
- The script **deletes** recorded audio after processing.

---



