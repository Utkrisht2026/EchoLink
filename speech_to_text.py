import whisper

model = whisper.load_model("medium")

def speech_to_text():
    result = model.transcribe("../input/input.wav")  # AUTO detect
    return result["text"], result["language"]

if __name__ == "__main__":
    text, lang = speech_to_text()
    print(text, lang)
