import re

def laugh_score(laugh):
    score = 0
    search_laugh  = re.search(r'[hH][aA][hHaA]*', laugh)
    if search_laugh:
        score = len(search_laugh.group())
        return score
    else:
        return 0 
user_input = input("Enter a laugh: ")
print(laugh_score(user_input))
print(f'The laugh score for "{user_input}" is: {laugh_score(user_input)}')
assert laugh_score('abcdefg') == 0
assert laugh_score('h') == 0
assert laugh_score('ha') == 2
assert laugh_score('HA') == 2
assert laugh_score('hahaha') == 6
assert laugh_score('ha ha ha') == 2
assert laugh_score('haaaaa') == 6
assert laugh_score('ahaha') == 4
assert laugh_score('Harry said Hahaha') == 2