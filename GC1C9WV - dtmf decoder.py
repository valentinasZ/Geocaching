from dtmf import detect
import librosa
def audio_to_floats(path):
    audio_data,sr = librosa.load(path,sr=None, mono=True)
    float_audio = librosa.util.normalize(audio_data)
   #sr is 16000 but you should lower to 15800 because tool cant recognize one digit

    results = detect(float_audio,15800)

    for result in results:
        print(f"{result.start} - {result.end} : {result.tone!s}")
        #N 51° 33.140  W 0° 06.092


audio_file_path = audio_to_floats("decoder2.wav")
print(audio_file_path)
