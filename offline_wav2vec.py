import torch
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

def transcribe_offline(audio_path):
    print("[Offline] Loading Wav2Vec model...")
    processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

    print("[Offline] Loading audio...")
    waveform, sample_rate = torchaudio.load(audio_path)

    # Convert to mono (take only 1 channel if stereo)
    if waveform.shape[0] > 1:
        waveform = waveform.mean(dim=0, keepdim=True)

    print("[Offline] Resampling audio...")
    if sample_rate != 16000:
        resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
        waveform = resampler(waveform)

    # Make sure the waveform is 1D
    input_values = processor(waveform.squeeze().numpy(), sampling_rate=16000, return_tensors="pt").input_values

    print("[Offline] Transcribing...")
    with torch.no_grad():
        logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])
    return transcription
