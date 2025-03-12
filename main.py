import spacy

# İngilizce modelini yükle
nlp = spacy.load("en_core_web_sm")

# Uzun bir metin örneği
text = """
Google LLC is an American multinational technology company specializing in Internet-related services and products.
It was founded by Larry Page and Sergey Brin in September 1998 while they were Ph.D. students at Stanford University in California.
The company's headquarters are located in Mountain View, California, also known as the "Googleplex".
Alphabet Inc., Google's parent company, was created in 2015 to restructure Google by moving some of its subsidiaries into a new holding company.
One of Google's most famous products is its search engine, which is used by millions of people worldwide.
Google also owns YouTube, Android, and other services like Google Drive and Gmail, which are essential parts of people's daily digital experience.
Elon Musk, the CEO of Tesla, has also expressed interest in the development of artificial intelligence technologies to compete with companies like Google.
The United States and the European Union have been involved in regulating tech giants like Google, questioning their dominance and data privacy practices.
"""

# Metni işleyin
doc = nlp(text)

# Anonimleştirilecek varlıkları tespit et
anonymized_text = text
for ent in doc.ents:
    if ent.label_ in ['PERSON', 'ORG', 'GPE']:
        anonymized_text = anonymized_text.replace(ent.text, "[REDACTED]")

# Anonimleştirilmiş metni dosyaya yazma
with open("anonimized_article.txt", "w") as file:
    file.write(anonymized_text)

print("Anonimleştirilmiş metin 'anonimized_article.txt' dosyasına kaydedildi.")
