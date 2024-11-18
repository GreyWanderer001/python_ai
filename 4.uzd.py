from transformers import pipeline


sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")


teikumi = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]


for teikums in teikumi:
    rezultāts = sentiment_pipeline(teikums)[0]

    stars = int(rezultāts['label'][0])
    if stars >= 4:
        noskanojums = "pozitīvs"
    elif stars == 3:
        noskanojums = "neitrāls"
    else:
        noskanojums = "negatīvs"
    print(f"Teikums: \"{teikums}\" -> Noskaņojums: {noskanojums}")
