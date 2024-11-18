from langdetect import detect


teksti = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day.",
    "Сегодня солнечный день."
]


for teksts in teksti:
    valoda = detect(teksts)
    print(f"Teksts: \"{teksts}\" -> Valoda: {valoda}")
