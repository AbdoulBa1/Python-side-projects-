import re
def get_price(sentence):
    price = []
    price = re.findall(r'\$\d+(?:\.\d{2})?', sentence)
    return price
user_input =input("Enter a sentence: ")
print(get_price(user_input))