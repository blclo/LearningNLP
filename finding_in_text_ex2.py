import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)

doc = nlp("i downloaded Fortnite on my laptop and can't open the game at all. Help? "
    "so when I was downloading Minecraft, I got the Windows version where it "
    "is the '.zip' folder and I used the default program to unpack it... do "
    "I also need to download Winzip?")

pattern = [{"LEMMA":"Download"}, {"POS":"PROPN"}]
matcher.add("DOWNLOAD_NOUN_PATTERN", [pattern])

