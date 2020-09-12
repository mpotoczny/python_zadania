import random
def mess_word(word):
    if len(word) <= 2: return word
    return word[0] + "".join(sorted(word[1:-1], key=lambda x: random.random())) + word[-1]


def jumble(string):
    my_text = string
    print(my_text)
    print(f'len - {len(my_text)}')

    punctuation = ".,;!?():*«'»… "
    # pozycje znaków interpunkcyjnych
    positions = [pos for pos, char in enumerate(my_text) if char in punctuation]
    print(f'positions - {positions}')
    # znaki interpunkcyjne
    puncts = [punct for punct in my_text if punct in punctuation]
    print(f'puncts - {puncts}')

    # # słownik nie ma tu zastosowania, bo klucze mają być unikatowe
    # positions_dict = {char: position for position, char in enumerate(my_text) if char in punctuation}
    # print(positions_dict)

    for char in my_text:
        if char in punctuation:
            my_text = my_text.replace(char, " ")

    #
    # # tworzy nową listę z wyrazami dłuższymi niż 2 znaki
    # z = [word for word in words_list if len(word) > 2]
    # print(z)


    # # dzieli po spacji
    words_list = my_text.split(" ")
    print(words_list)

    lista_inna_kol_znakow = list()
    for word in words_list:
        new_word = mess_word(word)
        lista_inna_kol_znakow.append(new_word)
    print(lista_inna_kol_znakow)

    string_polaczone = " ".join(lista_inna_kol_znakow)
    print(f'len - {len(string_polaczone)}')
    print(string_polaczone)

    lista_z_tekstu = list(string_polaczone)
    print( len(lista_z_tekstu) )

    i = 0
    j = 0
    while i < len(lista_z_tekstu):
        print(f'{i}- {lista_z_tekstu[i]}')
        if i in positions:
            lista_z_tekstu[i] = puncts[j]
            j = j + 1
        i += 1
    print(lista_z_tekstu)

    xd = "".join(lista_z_tekstu)
    print(xd)

    return xd
# jumble('Hello?, !World! ;bum; a!')
# jumble("Bez przesady można by rzec, iż od interpunkcji zależy znaczenie tekstu, "
#               "a od znaczenia tekstu zależy życie! Życie? Tak;"
#               " w dosłownym rozumieniu lub – życie "
#               "jako aspekty dnia powszedniego!")
# print(mess_word("According to a researcher at Cambridge Uni"))

jumble("According to a researcher at Cambridge University, it doesn't matter in what order the letters in a word are, the only important thing is that the first and last letter be at the right place. The rest can be a total mess and you can still read it without problem. This is because the human mind does not read every letter by itself but the word as a whole.")