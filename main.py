import spacy
import pdfplumber
from fpdf import FPDF

# spaCy'nin İngilizce modelini yükle
nlp = spacy.load("en_core_web_sm")

# PDF'den metin çıkartma fonksiyonu
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# PDF dosyasının yolunu belirt
pdf_path = "document.pdf"

# PDF'den metni çıkart
text = extract_text_from_pdf(pdf_path)

# Metni spaCy ile işleyin
doc = nlp(text)

# Anonimleştirilmiş metin
anonymized_text = text
for ent in doc.ents:
    if ent.label_ in ['PERSON', 'ORG', 'GPE']:
        anonymized_text = anonymized_text.replace(ent.text, "[REDACTED]")

# ASCII uyumluluğu sağlamak için metni temizleyelim (Türkçe karakterler veya özel karakterler varsa)
anonymized_text = anonymized_text.encode('ascii', 'ignore').decode()

# Yeni bir PDF dosyasına yazmak için fpdf kullan
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)  # Varsayılan ASCII uyumlu font
        self.cell(200, 10, 'Anonimleştirilmiş Makale', ln=True, align='C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)  # Varsayılan ASCII uyumlu font
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)  # Varsayılan ASCII uyumlu font
        self.multi_cell(0, 10, body)
        self.ln()

# Anonimleştirilmiş metni yeni PDF'ye yazma
pdf = PDF()
pdf.add_page()

# Metni sayfalara uygun şekilde ekleyelim
pdf.chapter_body(anonymized_text)

# Yeni anonimleştirilmiş PDF dosyasını kaydedelim
output_pdf_path = "anonymized_article.pdf"
pdf.output(output_pdf_path)

print(f"Dosya kaydedildi: {output_pdf_path}")
