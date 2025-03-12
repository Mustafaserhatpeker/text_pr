import spacy
import pdfplumber

# spaCy'nin İngilizce modelini yükle
nlp = spacy.load("en_core_web_sm")
pdf_path = "document.pdf"
# PDF'den metin çıkartma fonksiyonu
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text


# PDF'den metni çıkart
text = extract_text_from_pdf(pdf_path)

# Metni spaCy ile işleyin
doc = nlp(text)

# Anonimleştirilmiş metin
anonymized_text = text
for ent in doc.ents:
    if ent.label_ in ['PERSON', 'ORG', 'GPE']:
        anonymized_text = anonymized_text.replace(ent.text, "[REDACTED]")

# Anonimleştirilmiş metni bir dosyaya yazalım
with open("anonymized_article.txt", "w") as file:
    file.write(anonymized_text)

print("Dosya kaydedildi: anonymized_article.txt")