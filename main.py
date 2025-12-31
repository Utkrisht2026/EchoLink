from record_audio import record_audio
from speech_to_text import speech_to_text
from translate_text import translate
from text_to_speech import speak

LANGUAGES = {
    "0": ("English", "en"),
    "1": ("Hindi", "hi"),
    "2": ("Tamil", "ta"),
    "3": ("Telugu", "te"),
    "4": ("French", "fr"),
    "5": ("Spanish", "es"),
    "6": ("German", "de"),
    "7": ("Italian", "it"),
    "8": ("Russian", "ru"),
    "9": ("Japanese", "ja"),
    "10": ("Korean", "ko")
}

print("\nAvailable Output Languages:")
for key, value in LANGUAGES.items():
    print(f"{key}. {value[0]}")

choice = input("\nEnter language number: ").strip()

if choice not in LANGUAGES:
    print("Invalid selection")
    exit()

language_name, target_lang = LANGUAGES[choice]
print(f"\nSelected Output Language: {language_name}")

# 🎤 Record audio
record_audio()

# 🧠 Speech → Text (AUTO language detection)
text, source_lang = speech_to_text()
print("Recognized Text:", text)
print("Detected Input Language:", source_lang)

# 🌍 Translate only if needed
if source_lang == target_lang:
    translated_text = text
else:
    translated_text = translate(text, source_lang, target_lang)

print("Final Text:", translated_text)

# 🔊 Speak output
speak(translated_text, target_lang)

print("\nEchoLink finished successfully.")
