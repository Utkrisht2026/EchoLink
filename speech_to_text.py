import whisper

model = whisper.load_model("base")

def speech_to_text():
    result = model.transcribe("../input/input.wav", language="en")
    return result["text"]

if __name__ == "__main__":
    print(speech_to_text())
