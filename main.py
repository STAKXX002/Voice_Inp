from speech_recognition_module import check_ambient_noise, record_speech
from transcribe_module import transcribe_audio
from tts_module import text_to_speech

if __name__ == "__main__":
    recognizer = check_ambient_noise()  
    audio = record_speech(recognizer)  
    transcribed_text = transcribe_audio(audio)  

    chatbot_response = f"{transcribed_text}"
    
    print("Chatbot Response:", chatbot_response)
    text_to_speech(chatbot_response)
