import speech_recognition as sr

def transcribe_online(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        print("[Online] Listening to audio...")
        audio = recognizer.record(source)

    try:
        print("[Online] Recognizing using Google API...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "[Online] Could not understand audio"
    except sr.RequestError as e:
        return f"[Online] API error: {e}"
