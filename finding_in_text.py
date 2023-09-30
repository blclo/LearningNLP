import spacy
from spacy.matcher import Matcher

# We will  be using spacy.matcher. One of its utilities is allowing us to create 
# custom token patterns and then search the document for occurences on these patterns
nlp = spacy.load("en_core_web_sm")

# The vocabulary (nlp.vocab) contains all the available tokens and their 
# respective attributes in the loaded language model. 
matcher = Matcher(nlp.vocab)

doc = nlp(
    "After making the iOS update you won't notice a radical system-wide "
    "redesign: nothing like the aesthetic upheaval we got with iOS 7. Most of "
    "iOS 11's furniture remains the same as in iOS 10. But you will discover "
    "some tweaks once you delve a little deeper."
)

pattern = [{"TEXT":"iOS"}, {"IS_DIGIT":True}]
# add the pattern to the matcher, and give it a name, here "IOS_VERSION_PATTERN"
matcher.add("IOS_VERSION_PATTERN", [pattern])
matches = matcher(doc)
print("Total matches found: ", len(matches))

print(matches, "counts 3 tuples, having ", matches[0][0], "as the Match_ID which is basically the ID assigned to the string. \n Start Token Position", matches[0][1], "Finish token position:", matches[0][2])

for match_id, start, end in matches:
    print(doc[start:end].text)