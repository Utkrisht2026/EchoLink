from transformers import MarianMTModel, MarianTokenizer

MODELS = {
    "hi": "Helsinki-NLP/opus-mt-en-hi",
    "ta": "Helsinki-NLP/opus-mt-en-ta",
    "te": "Helsinki-NLP/opus-mt-en-te",
    "fr": "Helsinki-NLP/opus-mt-en-fr",
    "es": "Helsinki-NLP/opus-mt-en-es",
    "de": "Helsinki-NLP/opus-mt-en-de",
    "it": "Helsinki-NLP/opus-mt-en-it",
    "ru": "Helsinki-NLP/opus-mt-en-ru",
    "ja": "Helsinki-NLP/opus-mt-en-ja",
    "ko": "Helsinki-NLP/opus-mt-en-ko"
}

CACHE = {}

def translate(text, target_lang):
    if target_lang not in MODELS:
        return text

    if target_lang not in CACHE:
        tokenizer = MarianTokenizer.from_pretrained(MODELS[target_lang])
        model = MarianMTModel.from_pretrained(MODELS[target_lang])
        CACHE[target_lang] = (tokenizer, model)

    tokenizer, model = CACHE[target_lang]
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    output = model.generate(**inputs)

    return tokenizer.decode(output[0], skip_special_tokens=True)

