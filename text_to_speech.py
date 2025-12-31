from gtts import gTTS
import os

def speak(text, lang):
    tts = gTTS(text=text, lang=lang)
    tts.save("../output/output.mp3")
    os.system("start ../output/output.mp3")  # Windows

if __name__ == "__main__":
    speak("This is a test", "en")
