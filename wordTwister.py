import re
def twist_words(sentence):
    pattern = re.compile(r'\b(\w*)(\w)\b')
    print(pattern.sub(r'\2\1', 'My name is Abdoul  .'))
    return sentence
