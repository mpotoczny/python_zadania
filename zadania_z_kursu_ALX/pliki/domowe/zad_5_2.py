import sys
import collections
import time

try:
    file_name = sys.argv[1]
    print(file_name, '\n')

    with open(file_name, encoding='utf-8') as file:
        epos_text = file.read()

        print('-'*60, end='\n')

        word = 'Tadeusz'
        word_counter = 0

        word_counter = epos_text.count(word)
        print(f'Word \'{word}\' is used {word_counter} times in the text.\n')
        print('-'*60, end='\n')

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

        characters = '.,;!?():*«»…' # znaki w tekście przeszkadzające w policzeniu wyrazów
        epos_text_copy = epos_text # kopia, aby nie modyfikować tesktu pierwotnego
        for char in epos_text_copy:
            if char in characters: # dla każdego znaku w tekście, jeśli jest w zm. 'characters' to zamienić na spację
                epos_text_copy = epos_text_copy.replace(char, " ")

        # print(epos_text_copy)
        # print('%'*30)

        # print(epos_text_copy.split())
        for word in epos_text_copy.split(): # metoda split tworzy z całego tesktu książki listę z wyrazami oddzielonymi spacją
            word = word.lower()
            if word not in words_frequency:
                words_frequency[word] = 1
            else:
                words_frequency[word] += 1

        # # SPOSÓB 2 (bez zamiany na spacje)
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

        # metoda sorted nie zmienia oryginalnego słownika
        for word in sorted(words_frequency, key=words_frequency.get, reverse=True):
            print(f'{word} -> {words_frequency[word]}')

        print('-'*60, end='\n')

        # for word, frequency in words_frequency.items():
        #     print(f'{word} -> {frequency}')

        #SUMA SŁÓW
        sum_of_words1 = sum(words_frequency.values())
        print('Sum of words: =', sum_of_words1)

        # # SPOSÓB 2 i 3
        # sum_of_words2 = 0
        # sum_of_words3 = 0
        # for word, frequency in words_frequency.items():
        #     sum_of_words2 += words_frequency[word]
        #     sum_of_words3 += frequency
        # print(sum_of_words1)
        # print(sum_of_words3)

        print('-'*60, end='\n')

        #SUMA ZNAKÓW
        from collections import Counter
        co = Counter(epos_text) # tworzy słownik ze znakami i ilością ich wystąpień
        sum_of_chars1 = sum(co.values())
        print('Sum of chars: =', sum_of_chars1)

        # # # SPOSÓB 2
        # print( epos_text.count('') )
        #
        # # # SPOSÓB 3
        # sum_of_chars3 = 0
        # for letter in epos_text:
        #     if bool(letter) == True:
        #         sum_of_chars3 += 1
        # print(sum_of_chars3)

        print('-'*60, end='\n')

except IndexError:
    print('To run program use command: python zad_5_2.py pan-tadeusz.txt')
    exit(1)

except FileNotFoundError:
    print(f'File {file_name} not found!')
    exit(1)
