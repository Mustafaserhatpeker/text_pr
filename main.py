import sys
import os
import spacy
from spacy.pipeline import EntityRuler


nlp = spacy.load("en_core_web_md")
ruler = nlp.add_pipe("entity_ruler", before="ner")


patterns = [
    {"label": "ORG", "pattern": "Google"},
    {"label": "PERSON", "pattern": "Elon Musk"},
    {"label": "ORG", "pattern": "Tesla"},
    {"label": "ORG", "pattern": "Kocaeli Üniversitesi"},
]


ruler.add_patterns(patterns)


file_path = sys.argv[1]  

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()


doc = nlp(text)


anonymized_text = text
for ent in doc.ents:
    if ent.label_ in ['PERSON', 'ORG', 'GPE']:
        anonymized_text = anonymized_text.replace(ent.text, "[REDACTED]")


directory, original_filename = os.path.split(file_path)
new_filename = f"tamamlandi-{original_filename}"
new_file_path = os.path.join(directory, new_filename)


with open(new_file_path, "w", encoding='utf-8') as file:
    file.write(anonymized_text)

print(f"İşlem tamamlandı! Yeni dosya kaydedildi: {new_file_path}")
