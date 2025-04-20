import sys
import os
import spacy
import fitz  # PyMuPDF
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
file_ext = os.path.splitext(file_path)[1].lower()

if file_ext != ".pdf":
    print("Bu sürüm sadece PDF dosyaları için çalışır.")
    sys.exit(1)

doc = fitz.open(file_path)

# Tüm sayfalardaki metni birleştir
full_text = ""
for page in doc:
    full_text += page.get_text()

# NLP işlemi
spacy_doc = nlp(full_text)
entities_to_redact = [
    ent.text for ent in spacy_doc.ents if ent.label_ in ["PERSON", "ORG"]]

# Anonimleştirme
for page in doc:
    for ent_text in entities_to_redact:
        matches = page.search_for(ent_text)
        for rect in matches:
            # Üzerine kırmızı kutu çiziyoruz ve metni karartıyoruz
            page.draw_rect(rect, color=(1, 0, 0), fill=(
                1, 0, 0))  # RGB(1,0,0) = kırmızı

# Yeni dosyayı kaydet
directory, original_filename = os.path.split(file_path)
base_filename, _ = os.path.splitext(original_filename)
new_filename = f"anonymized-{base_filename}.pdf"
new_file_path = os.path.join(directory, new_filename)

doc.save(new_file_path)
doc.close()

print(f"İşlem tamamlandı! Yeni PDF kaydedildi: {new_file_path}")
