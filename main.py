# Her şeyi elimden geldiğince açıklamaya çalıştım senin için.
# Komut satırından dosya yolu almak için kullanılıyor(Bu yazdığım API sayesinde oluyor).
import sys
import os  # Dosya işlemleri için gerekli modül.
import spacy  # Metin işleme için spaCy kütüphanesi.
# Kendi özel isim tanımlamalarımız için kullanıyoruz.
from spacy.pipeline import EntityRuler

# Önceden eğitilmiş İngilizce dil modeli yükleniyor.
nlp = spacy.load("en_core_web_md")

# "entity_ruler" adlı bileşeni, "ner" (adlandırılmış varlık tanıma) bileşeninden önce ekliyoruz.
# Bu sayede kendi eklediğimiz kurallar, modelin öğrendiği bilgilerden önce uygulanır.
ruler = nlp.add_pipe("entity_ruler", before="ner")

# Özel olarak tespit edilmesini istediğimiz kişi ve organizasyon isimlerini tanımlıyoruz.
patterns = [
    # "Google" kelimesi ORGANIZATION (şirket) olarak tanımlanıyor.
    {"label": "ORG", "pattern": "Google"},
    # "Elon Musk" bir kişi ismi olarak tanımlanıyor.
    {"label": "PERSON", "pattern": "Elon Musk"},
    {"label": "ORG", "pattern": "Tesla"},  # "Tesla" şirket olarak algılanıyor.
    # "Kocaeli Üniversitesi" de bir organizasyon olarak işaretleniyor.
    {"label": "ORG", "pattern": "Kocaeli Üniversitesi"},
]

# Belirlenen özel isimler entity_ruler'a ekleniyor.
ruler.add_patterns(patterns)

# Komut satırından dosya yolunu alıyoruz.
# Kullanıcı, kodu çalıştırırken bir dosya yolu vermeli.
file_path = sys.argv[1]

# Belirtilen dosyayı okuyup içeriğini değişkene alıyoruz. Bu dosya yolu benim yazdığım API den geliyor, kafan karışmasın.
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# spaCy modeli ile metni işliyoruz.
doc = nlp(text)

# Yeni anonimleştirilmiş metin değişkeni oluşturuyoruz.
anonymized_text = text

# Algılanan isimleri ve organizasyonları [REDACTED] ile değiştiriyoruz.
for ent in doc.ents:
    # Sadece kişi ve organizasyon isimlerini değiştiriyoruz.
    if ent.label_ in ['PERSON', 'ORG']:
        anonymized_text = anonymized_text.replace(ent.text, "[REDACTED]")

# Dosyanın bulunduğu dizini ve orijinal adını alıyoruz.
directory, original_filename = os.path.split(file_path)

# Yeni dosya adını oluşturuyoruz.
new_filename = f"tamamlandi-{original_filename}"

# Yeni dosyanın tam yolunu oluşturuyoruz.
new_file_path = os.path.join(directory, new_filename)

# Yeni anonimleştirilmiş metni yeni dosyaya kaydediyoruz.
with open(new_file_path, "w", encoding='utf-8') as file:
    file.write(anonymized_text)

# Kullanıcıya işlemin tamamlandığını bildiriyoruz.
print(f"İşlem tamamlandı! Yeni dosya kaydedildi: {new_file_path}")
# Umarım işinize yarar efenim.
# İyi çalışmalar.
