import sounddevice as sd
from scipy.io.wavfile import write

def record_audio():
    fs = 16000
    duration = 7

    print("Speak now...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write("../input/input.wav", fs, audio)
    print("Audio recorded successfully")

if __name__ == "__main__":
    record_audio()
