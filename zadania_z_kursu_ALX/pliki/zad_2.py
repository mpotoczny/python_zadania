"""
Napisz program wczytujący plik z logami aktywności użytkowników w systemie.
Na podstawie wczytanych danych wyświetl informację o sumarycznym
czasie przebywania każdego użytkownika w systemie.
Przykład użycia:
$ python read_logs.py logs.txt
Czas przebywania w systemie:
- user-1: 92 s
- user-2: 51 s
- user-3: 20 s
"""

import sys

try:
    file_name = sys.argv[1]

    total_time = {}
    last_login = {}

    with open(file_name) as file:
        for line in file:
            # user-10;LOGIN;114
            user, action, time = line.split(';')
            time = int(time)

            if action == 'LOGIN':
                last_login[user] = time

            elif action == 'LOGOUT':
                if user in total_time:
                    total_time[user] += time - last_login[user]
                else:
                    total_time[user] = time - last_login[user]

        for user, time in total_time.items():
            print(f'{user}: {time}')




except IndexError:
    print('usage: python zad_2.py logs.txt')
    exit(1)
except FileNotFoundError:
    print(f'File {file_name} not found!')
    exit(1)