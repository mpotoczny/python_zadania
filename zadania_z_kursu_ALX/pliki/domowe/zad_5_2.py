import sys
import collections
import time

try:
    file_name = sys.argv[1]
    print(file_name, '\n')

    with open(file_name, encoding='utf-8') as file:
        epos_text = file.read()

        word = 'Tadeusz'
        word_counter = 0

        word_counter = epos_text.count(word)
        print(f'Word \'{word}\' is used {word_counter} times in the text.\n')

        # # SPOSÓB 2
        # file.seek(0)
        # word_counter = 0
        # while True:
        #     el = file.readline()
        #     if word in el:
        #         word_counter += 1
        #     elif not el:
        #         break
        # print(word_counter)

        # # SPOSÓB 3
        # file.seek(0)
        # word_counter = 0
        # data = file.readlines()
        # for el in data:
        #     if word in el:
        #         word_counter += 1
        # print(word_counter)

    #zadanie -> słownik z częstością występowania wyrazów

        words_frequency = {}

        epos_text_copy = epos_text
        characters = '.,;!?():*«»…'
        for char in epos_text_copy:
            if char in characters:
                epos_text_copy = epos_text_copy.replace(char, " ")

        # print(epos_text_copy)
        # print('%'*30)

        for word in epos_text_copy.split():
            word = word.lower()
            if word not in words_frequency:
                words_frequency[word] = 1
            else:
                words_frequency[word] += 1

        # # SPOSÓB 2
        # words_frequency = collections.defaultdict(int)
        # file.seek(0)
        # while True:
        #     el = file.readline()
        #     if not el:
        #         break
        #
        #     words = el.split()
        #     for word in words:
        #         words_frequency[word] += 1
        # print(words_frequency)

        for word in sorted(words_frequency, key=words_frequency.get, reverse=True):
            print(f'{word} -> {words_frequency[word]}')

        # for word, frequency in words_frequency.items():
        #     print(f'{word} -> {frequency}')

        #SUMA SŁÓW



        #SUMA ZNAKÓW









except IndexError:
    print('To run program use command: python zad_5_2.py pan-tadeusz.txt')
    exit(1)

except FileNotFoundError:
    print(f'File {file_name} not found!')
    exit(1)
