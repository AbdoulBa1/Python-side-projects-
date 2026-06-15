import re
def get_hash_tags(sentence):
    list_of_hastags =[]
    hash_tags = re.findall(r'#\w+', sentence)
    for tag in hash_tags:
        list_of_hastags.append(tag)
    return list_of_hastags
user_input =input("Enter a sentence: ")
print(get_hash_tags(user_input))
