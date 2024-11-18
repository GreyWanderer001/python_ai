import spacy

nlp = spacy.load("xx_ent_wiki_sm")


text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."


doc = nlp(text)

person_entities = []
org_entities = []

for ent in doc.ents:
    if ent.label_ == "PER":
        if ent.text.endswith("Universitāte"):
            org_entities.append(ent.text)
        else:
            person_entities.append(ent.text)
    elif ent.label_ == "ORG":
        org_entities.append(ent.text)

print("Personvārdi:")
for person in person_entities:
    print(f"- {person}")

print("\nOrganizācijas:")
for org in org_entities:
    print(f"- {org}")
