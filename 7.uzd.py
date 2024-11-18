from gensim.models import FastText

vārdi = ["māja", "dzīvoklis", "jūra"]

korpuss = [
    ["māja", "ir", "liela"],
    ["dzīvoklis", "atrodas", "centrā"],
    ["jūra", "ir", "plaša"],
    ["māja", "un", "dzīvoklis", "ir", "dzīvesvietas"],
    ["jūra", "šķīst", "un", "skaista"]
]

modelis = FastText(sentences=korpuss, vector_size=100, window=3, min_count=1, epochs=10)

for vārds in vārdi:
    vektors = modelis.wv[vārds]
    print(f"Vektors vārda '{vārds}':")
    print(vektors[:5], "...") 

līdzības = modelis.wv.most_similar("māja", topn=2)
print("\nSemantiski līdzīgākie vārdi vārdam 'māja':")
for vārds, līdzība in līdzības:
    print(f"{vārds}: {līdzība:.2f}")
