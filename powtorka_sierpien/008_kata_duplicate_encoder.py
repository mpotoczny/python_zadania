'''
The goal of this exercise is to convert a string to a new string where each
character in the new string is "(" if that character appears only once
in the original string, or ")" if that character appears more than once
in the original string. Ignore capitalization when determining
if a character is a duplicate.

Test.assert_equals(duplicate_encode("din"),"(((")
Test.assert_equals(duplicate_encode("recede"),"()()()")
Test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
Test.assert_equals(duplicate_encode("(( @"),"))((")
'''

# # SPOSÓB NR 1
# def duplicate_encoder(word):
#     occurences = {}
#
#     for character in word.lower():
#         if character not in occurences:
#             occurences[character] = 0
#         occurences[character] += 1
#     print(occurences)
#
#     txt = ""
#     for character in word.lower():
#         if occurences[character] == 1:
#             txt += '('
#         else:
#             txt += ')'
#
#     print(txt)
#     return txt

# # SPOSÓB NR 2
# def duplicate_encoder(word):
#     expression = "".join( "(" if word.lower().count(c) == 1 else ')' for c in word.lower()  )
#     print(expression)
#     return expression


# SPOSÓB 3 - podobny do 1
from collections import defaultdict
def duplicate_encoder(word):
    occurences = defaultdict(int) # oznacza, że dla nowego klucza wartością domyślną będzie int o wartości 0
    word = word.lower()

    for character in word:
        occurences[character] += 1
    print(occurences)
    # print(type(occurences))

    txt = ""
    for character in word:
        txt = txt + ( ('(') if occurences[character] == 1 else (')') )

    print(txt)
    return txt


duplicate_encoder("(( @")
duplicate_encoder("Success")