from transformers import pipeline

rezumesanas_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

raksts = """Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm."""

rezume = rezumesanas_pipeline(raksts, max_length=50, min_length=25, do_sample=False)

print("Rezumēts teksts:")
print(rezume[0]['summary_text'])
