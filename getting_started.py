import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("In 1990, more than 60% of people in East Asia were in extreme poverty. "
    "Now less than 4% are.")
print(doc.text)

# selecting the 3rd word in the sentence
print(doc[2])

# finding percentages in text
for token in doc:
    if token.like_num:
        if token.nbor().text == "%":
            print(f"Percentage found is {token.text}%")

# finding entities in the text
entities_text = "Apple is looking at buying U.K. startup for $1 billion"
entities_doc = nlp(entities_text)
ents_list = list(entities_doc.ents)
print(ents_list)

# Print entities, labels and positions
for ent in entities_doc.ents:
    print(ent.label_, ent.text)
