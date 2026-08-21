import spacy

nlp = spacy.load("en_core_web_sm")

text = "Elon Musk founded SpaceX in California in 2002."

doc = nlp(text)

print("=" * 60)
print("        NAMED ENTITY RECOGNITION")
print("=" * 60)

print("\nInput Text:")
print(text)

print("\nNamed Entities:\n")

for entity in doc.ents:
    print("{:<20}{}".format(entity.text, entity.label_))

print("\nNER Completed Successfully.")
print("=" * 60)