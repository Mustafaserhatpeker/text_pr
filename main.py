import spacy
import pdfplumber
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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

# Yeni bir PDF dosyasına anonimleştirilmiş metni yazmak için reportlab kullanacağız
def save_text_as_pdf(text, output_pdf_path):
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    width, height = letter
    y_position = height - 40  # Başlangıç y konumu (üstten)

    for line in text.split('\n'):
        c.drawString(40, y_position, line)
        y_position -= 12  # Satır aralığı

        if y_position < 40:  # Sayfa sonuna gelindiğinde yeni sayfa ekle
            c.showPage()
            y_position = height - 40

    c.save()

# Yeni anonimleştirilmiş PDF dosyasını kaydet
output_pdf_path = "anonymized_document.pdf"
save_text_as_pdf(anonymized_text, output_pdf_path)

print(f"Dosya kaydedildi: {output_pdf_path}")
