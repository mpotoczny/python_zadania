import random
def mess_word(word):
    if len(word) <= 2: return word
    return word[0] + "".join(sorted(word[1:-1], key=lambda x: random.random())) + word[-1]

def jumble(string):
    my_text = string
    punctuation = ".,;!?():*«'»… "

    # indexes of punctuations in string
    positions = [pos for pos, char in enumerate(my_text) if char in punctuation]
    # punctuations of these indexes
    puncts = [punct for punct in my_text if punct in punctuation]

    # replace each punctuation with space
    for char in my_text:
        if char in punctuation:
            my_text = my_text.replace(char, " ")

    # into a list
    words_list = my_text.split(" ")

    # jumbling words
    messed_words_list = list()
    for word in words_list:
        new_word = mess_word(word)
        messed_words_list.append(new_word)
    
    # again string - joined by space
    messed_string_with_spaces = " ".join(messed_words_list)
    # ang again list to easier replacement than using string
    list_of_characters = list(messed_string_with_spaces)

    # replacement space with original punctuation
    i = 0
    j = 0
    while i < len(list_of_characters):
        if i in positions:
            list_of_characters[i] = puncts[j]
            j = j + 1
        i += 1

    # the last transformation from list to string
    messed_text = "".join(list_of_characters)
    return messed_text

a = jumble("According! to a researcher at Cambridge University, it doesn't matter in what order the letters in a word are, the only important thing is that the first and last letter be at the right place. The rest can be a total mess and you can still read it without problem. This is because the human mind does not read every letter by itself but the word as a whole.")
print(a)