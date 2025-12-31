from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "facebook/nllb-200-distilled-600M"

LANG_MAP = {
    "en": "eng_Latn",
    "ta": "tam_Taml",
    "hi": "hin_Deva",
    "te": "tel_Telu",
    "fr": "fra_Latn",
    "es": "spa_Latn",
    "de": "deu_Latn",
    "it": "ita_Latn",
    "ru": "rus_Cyrl",
    "ja": "jpn_Jpan",
    "ko": "kor_Hang"
}

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def translate(text, source_lang, target_lang):
    if source_lang == target_lang or not text.strip():
        return text

    if source_lang not in LANG_MAP or target_lang not in LANG_MAP:
        return "[Translation not supported]"

    src = LANG_MAP[source_lang]
    tgt = LANG_MAP[target_lang]

    tokenizer.src_lang = src
    inputs = tokenizer(text, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids(tgt),
        max_length=128
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
