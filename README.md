Leer en español mas abajo
# Learning NLP

This project is suitable for beginners who want to take their first steps into NLP.

### What is NLP?
It is a branch of AI that refers to the interactions between computers and human language. It refers to the ability of program computers to understand spoken and written human language.
NLP has become increasingly important in recent years as the amount of natural language data available has grown exponentially. Due to the increasing recognition of NLP, learning about this topic has become essential.

### What is included in the notebook?
- Basic example showing how to use NLP in different languages
- How to select slices of text
- Example showing how to extract percentages in a text
- Examples of extraction of brand names
- Examples of prediction and extraction of name entities (Amazon, Sony)
- Example of how to find words and phrases in text using the Matcher

### How to use it?

You can open the notebook (the .ipynb file) directly on your Google Colab account.
Also, if you are a Jupyter and Python user, you can download the notebook and run it directly on your computer.

# spaCy Matcher Patterns

The `Matcher` in spaCy allows for robust and efficient matching of words, phrases, and patterns in text. This document covers commonly used token attributes to define patterns.

## 1. Text and Lexical Attributes

- **TEXT**: Exact token text.
  * Example: `{'TEXT': 'iPhone'}` matches tokens with the exact text "iPhone".
- **LOWER**: Lowercase form of the token text.
  * Example: `{'LOWER': 'iphone'}` matches "iPhone", "iphone", "IPHONE", etc.
- **LENGTH**: Length of the token text.
  * Example: `{'LENGTH': 5}` matches tokens with 5 characters.
- **IS_ALPHA**, **IS_ASCII**, **IS_DIGIT**:
  * Check if the token is alphabetic, ASCII, or a digit.
- **IS_LOWER**, **IS_UPPER**, **IS_TITLE**: 
  * Check the token's casing. 
- **IS_PUNCT**, **IS_SPACE**, **IS_STOP**: 
  * Check if the token is punctuation, whitespace, or a stop word.

## 2. Grammatical Attributes

- **POS**: Coarse-grained part-of-speech tag.
  * Example: `{'POS': 'NOUN'}` matches any noun.
- **TAG**: Fine-grained part-of-speech tag specific to the language model.
- **DEP**: Dependency label.
- **LEMMA**: Base form of the word.
  * Example: `{'LEMMA': 'run'}` matches "run", "runs", "running", etc.

## 3. Boolean Value Attributes

Check attributes that return boolean values:
- **IS_DIGIT**, **IS_ALPHA**, **IS_ASCII**, etc.

## 4. Operators

- **OP**: Set regex-like operators:
  * `'!'`: Match exactly one time (default).
  * `'?'`: Match 0 or 1 times.
  * `'+'`: Match 1 or more times.
  * `'*'`: Match 0 or more times.

## 5. Shape

- **SHAPE**: Word shape of the token.
  * Example: `{'SHAPE': 'Xxxx.'}` matches capitalized words followed by a period.

## 6. Lookahead and Lookbehind

Use the `?` notation for positive and negative lookahead assertions.

---

## Pattern Examples

- Match the word "iPhone" in any case:
  ```python
  [{'LOWER': 'iphone'}]
