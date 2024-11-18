from transformers import MarianMTModel, MarianTokenizer

model_name = 'Helsinki-NLP/opus-mt-lv-en'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

latv_texts = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

encoded_inputs = tokenizer(latv_texts, return_tensors="pt", padding=True)
translated_tokens = model.generate(**encoded_inputs)
translated_texts = [tokenizer.decode(t, skip_special_tokens=True) for t in translated_tokens]

for lv, en in zip(latv_texts, translated_texts):
    print(f"Latviešu: {lv}")
    print(f"Angļu: {en}\n")
