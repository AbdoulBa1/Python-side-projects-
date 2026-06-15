import random 
def get_word_hint(secret_word, guess_word):
    secret_word = secret_word.upper()
    guess_word = guess_word.upper()
    hint = ""
    for x in range(len(secret_word)):
        if secret_word[x] == guess_word[x]:
            hint += "O"
        elif guess_word[x] in secret_word:
            hint += "o" 
        else:
            hint += "x" 
    return hint
words_list ='MITTS FLOAT BRICK LIKED DWARF COMMA GNASH ROOMS UNITE BEARS SPOOL ARMOR'.split()
secret_word = random.choice(words_list)
for turn in range(1,7):
     guess_word = input("Enter your guess: ")
     hint = get_word_hint(secret_word, guess_word)
     print(f"Hint: {hint}")
     if hint == "OOOOO":
            print("You've won !")
            break
else: print(f"The secret word was: {secret_word} Better luck next time !")



