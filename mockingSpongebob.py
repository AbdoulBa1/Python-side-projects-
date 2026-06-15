def spongebob(text):
    lower_next = True
    result = ""
    for i in range(len(text)):
        if text[i].isalpha():
            if lower_next:
                result += text[i].lower()
                lower_next = False
            else:
                result += text[i].upper()
                lower_next = True
        else:
            result += text[i]
    return result
user_input = input("Enter a sentence: ")
output = spongebob(user_input)
print(output)

