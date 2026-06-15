# A pangram is a sentence that uses all 26 letters of the alphabet at least once.
def is_pangram(sentence):
   
     # This list will store every unique letter we find in the sentence
    EACH_LETTER = []
    
    # We look at every single character (char) inside the string 'sentence'
    for letter in sentence:
        
        # We change the letter to uppercase so 'a' and 'A' count as the same thing
        letter = letter.upper()
        
        # .isalpha() checks if the char is a letter (not a space, number, or !)
        # 'not in' checks if we already found this letter before
        if letter not in EACH_LETTER and letter.isalpha():
            
            # If it is a new letter, we add it to our list
            EACH_LETTER.append(letter)
            
    # After checking the whole sentence, we check the size of our list
    if len(EACH_LETTER) == 26:
        print("This sentence is a pangram!")
        # If there are exactly 26 unique letters, it's a pangram
        return True
    else:        
        # If there are fewer than 26, some letters were missing
        print("This sentence is not a pangram.")
        return False
       
is_pangram(input("Enter a sentence: "))