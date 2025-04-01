import spacy


nlp = spacy.load("en_core_web_sm")


def extract_topics(text):
    doc = nlp(text)
    topics = set()  

    for ent in doc.ents:
        
        if ent.label_ in ['PERSON', 'ORG', 'GPE']:  
            topics.add(ent.text)
    
    return topics

text = "Albert Einstein was born in Germany. He was a renowned physicist, and he worked in the United States."


topics = extract_topics(text)
print(f"Identified topics: {topics}")
