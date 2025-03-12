import spacy
from spacy.pipeline import EntityRuler
# İngilizce modelini yükle
nlp = spacy.load("en_core_web_md")
ruler = nlp.add_pipe("entity_ruler", before="ner")

# Özel varlık desenlerini tanımla
patterns = [
    {"label": "ORG", "pattern": "Google"},
    {"label": "PERSON", "pattern": "Elon Musk"},
    {"label": "ORG", "pattern": "Tesla"},
    {"label": "ORG", "pattern": "Kocaeli Üniversitesi"},
    # Burada daha fazla özel desen ekleyebilirsiniz
]

# Desenleri EntityRuler'a ekle
ruler.add_patterns(patterns)
# Uzun bir metin örneği
text = """
The Evolution of Machine Learning: A Journey Through Time and Innovation Kocaeli Üniversitesi 

Machine Learning (ML) has become one of the most transformative fields in modern technology, revolutionizing industries, scientific research, and daily life. The field's evolution is marked by the contributions of numerous researchers, institutions, and companies that have pushed the boundaries of what machines can learn and do. This article explores the journey of machine learning, highlighting the key figures and organizations that have played pivotal roles in its development.

Early Foundations: The Birth of Artificial Intelligence
The roots of machine learning can be traced back to the mid-20th century, with the foundational work of computer scientists like Alan Turing and John von Neumann. Turing, often referred to as the father of artificial intelligence (AI), proposed the concept of a machine that could simulate human intelligence, which laid the groundwork for future AI research. His work, most famously encapsulated in the Turing Test, became a critical milestone for the development of machine learning algorithms.

In the 1950s and 1960s, researchers at institutions such as MIT (Massachusetts Institute of Technology) and Stanford University began to explore the concept of machine learning in earnest. Arthur Samuel, a researcher at IBM, coined the term "machine learning" in 1959, after developing a program capable of learning to play checkers. This work was a major leap forward in demonstrating that machines could improve performance through experience.

The Rise of Neural Networks and Deep Learning
The 1980s and 1990s witnessed significant breakthroughs in machine learning, particularly with the development of neural networks. Key figures in this era include Geoffrey Hinton, Yann LeCun, and Yoshua Bengio, whose research in deep learning and backpropagation methods revitalized the field. Their work, particularly Hinton’s exploration of the restricted Boltzmann machine and deep belief networks, was crucial in setting the stage for the deep learning revolution that would follow.

The rise of deep learning was further supported by advancements in hardware, particularly NVIDIA's development of GPUs (Graphics Processing Units), which enabled faster processing and the ability to train more complex models. Andrew Ng, another prominent figure in the field, co-founded Google Brain in 2011, a project that combined the power of deep neural networks with large-scale computing resources.

Major Institutions and Companies Driving the Machine Learning Revolution
In the 21st century, the progress of machine learning accelerated exponentially, with major institutions and companies becoming significant players in the field. Universities like Stanford, MIT, and Carnegie Mellon University continued to lead research, while tech giants like Google, Microsoft, Facebook (now Meta), and Amazon invested heavily in developing machine learning technologies.

Google DeepMind, established in 2014, is one of the most well-known organizations to emerge from the rapid expansion of AI research. The company achieved global recognition for developing AlphaGo, a program that defeated world champion Lee Sedol in the complex board game Go, a feat previously thought to be decades away from achievement. DeepMind’s innovations, particularly in reinforcement learning, have had far-reaching implications in fields ranging from healthcare to energy efficiency.

Similarly, Microsoft Research has been at the forefront of machine learning advancements, with notable contributions to natural language processing (NLP), computer vision, and cloud computing. Their work on Azure Machine Learning provides businesses and researchers with robust tools for developing and deploying machine learning models.

Machine Learning in Industry: Real-World Applications
Machine learning's impact extends far beyond academic research. Industries such as healthcare, finance, retail, and transportation have integrated machine learning into their operations, transforming the way they function.

In healthcare, companies like IBM Watson Health and Tempus are using machine learning algorithms to analyze medical data, improving diagnostics, treatment plans, and drug discovery. For example, IBM Watson has been used in oncology to assist doctors in selecting personalized cancer treatments by analyzing vast datasets of medical records.

In the financial sector, Goldman Sachs and JP Morgan Chase have employed machine learning to enhance trading algorithms, detect fraudulent activities, and optimize risk management strategies. Meanwhile, PayPal uses machine learning models to detect and prevent fraud in real-time, ensuring secure transactions for millions of users worldwide.

The transportation industry is also embracing machine learning, with companies like Tesla pioneering autonomous vehicles powered by deep learning models. Tesla’s Autopilot system, for instance, uses neural networks to interpret sensor data and make driving decisions, pushing the boundaries of what is possible with autonomous systems.

Ethical Considerations and the Future of Machine Learning
As machine learning continues to evolve, it raises several important ethical and societal questions. Organizations like OpenAI, founded by notable figures such as Elon Musk, Sam Altman, and Greg Brockman, have been working to ensure that artificial intelligence is developed safely and responsibly. OpenAI’s mission is to ensure that AGI (Artificial General Intelligence) benefits humanity as a whole, a goal that requires careful attention to bias, transparency, and accountability.

Governments and policymakers around the world are also beginning to take notice of machine learning’s potential and risks. The European Union has introduced the AI Act, a regulatory framework aimed at ensuring that AI systems are used in a fair and ethical manner, while the United States is exploring the possibility of developing national policies around AI research and application.

Conclusion: Machine Learning's Bright Future
The field of machine learning has come a long way, from its humble beginnings to the cutting-edge technologies we see today. Thanks to the tireless efforts of countless researchers, institutions, and companies, we are witnessing the dawn of a new era of intelligent systems. As the technology continues to advance, machine learning will undoubtedly shape the future of countless industries and improve the way we live and work.

However, as with any powerful technology, it is crucial that we approach the development of machine learning with caution and responsibility. By working together, researchers, policymakers, and industry leaders can ensure that machine learning remains a force for good in the world, empowering individuals and organizations while minimizing potential risks.
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
