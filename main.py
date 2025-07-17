from transcribers.online_google import transcribe_online
from transcribers.offline_wav2vec import transcribe_offline

def main():
    audio_file = "sample.wav"  # Replace with your file

    print("Select Mode:")
    print("1 - Online (Google API)")
    print("2 - Offline (Wav2Vec2)")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        result = transcribe_online(audio_file)
    elif choice == "2":
        result = transcribe_offline(audio_file)
    else:
        print("Invalid choice.")
        return

    print("\n📝 Transcription Result:")
    print(result)

if __name__ == "__main__":
    main()
