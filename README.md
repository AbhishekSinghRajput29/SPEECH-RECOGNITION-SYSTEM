# SPEECH RECOGNITION SYSTEM

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: ABHISHEK SINGH RAJPUT

*INTERN ID*: CT04DG3397

*DOMAIN*: ARTIFICIAL INTELLIGENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH


#  Speech Recognition System (Online + Offline)

This project is a simple yet effective **Speech-to-Text system** that converts spoken audio into text. It supports both **online** and **offline** modes using two popular speech recognition approaches:

* **Online mode:** Uses the Google Speech Recognition API to transcribe audio with internet access.
* **Offline mode:** Uses a pre-trained **Wav2Vec2** model from Facebook AI to transcribe audio files locally without needing an internet connection.

The project was built with Python and a set of open-source libraries like `speech_recognition`, `transformers`, `torch`, `torchaudio`, and `pydub`. The main aim was to explore and implement speech recognition using both cloud-based APIs and local machine learning models.


##  Project Overview

Speech recognition is one of the core applications of artificial intelligence and natural language processing. With voice assistants like Alexa, Siri, and Google Assistant becoming increasingly common, converting spoken language to text in real-time has become a practical and in-demand technology.

This system was designed to be lightweight and functional. It allows the user to choose whether they want to use an **online transcription service (Google API)** or an **offline model (Wav2Vec2)**. This hybrid approach makes it flexible and suitable for different environments — such as classrooms, research, or areas with no internet access.

The **online mode** is extremely fast and accurate for clear audio. It requires an active internet connection and sends the audio to Google’s servers for processing. On the other hand, the **offline mode** is powered by Facebook’s Wav2Vec2 model, which performs well even without connectivity. This model runs locally using PyTorch and can transcribe speech with reasonable accuracy for clean audio files.


##  Key Features

* **Dual Mode Support:**

  * Choose between Online (Google API) or Offline (Wav2Vec2)
* **Offline transcription** without needing any internet
* **Accurate** results with short, clear audio samples
* **Simple user interface** via terminal input
* Works with `.wav` files (mono, 16kHz recommended)


##  Technologies & Libraries Used

* Python 3.10
* [`speech_recognition`](https://pypi.org/project/SpeechRecognition/) – for Google API
* [`transformers`](https://huggingface.co/transformers/) – for Wav2Vec2 model
* [`torchaudio`](https://pytorch.org/audio/stable/index.html) – for audio loading
* [`torch`](https://pytorch.org/) – model backend
* [`pydub`](https://github.com/jiaaro/pydub) – for audio conversion
* [`ffmpeg`](https://ffmpeg.org/) – required by `pydub` to process audio


##  How It Works

1. Place a valid `.wav` file named `sample.wav` in the project folder. It should be:

   * Mono channel
   * 16 kHz sample rate
   * Short (under 30 seconds is ideal)
2. Run the script:

   ```bash
   python main.py
   ```
3. Choose:

   * `1` for Online (Google API)
   * `2` for Offline (Wav2Vec2)
4. View the transcribed output printed to the terminal.

Note: If you face errors, check your audio file format. Use `pydub` to convert and compress if needed.

## File Structure

```
SPEECH RECOGNITION SYSTEM/
│
├── main.py                         # Main script to run the system
├── sample.wav                      # Input audio file (not included due to size)
├── transcribers/
│   ├── online_google.py            # Online mode transcription using Google API
│   └── offline_wav2vec.py          # Offline mode transcription using Wav2Vec2
├── README.md                       # Project documentation (this file)

```

## Important Notes

* The actual `.wav` file is not included in the repository due to size limits on GitHub.
* You can record or compress your own `.wav` file and name it `sample.wav`.
* Wav2Vec2 works best on clean audio without background noise.

