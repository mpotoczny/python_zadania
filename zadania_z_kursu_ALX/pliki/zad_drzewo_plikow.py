'''
Napisz program wypisujący zawartość wskazanego katalogu w postaci drzewa katalogów i plików.
Przykład użycia:
$ python tree.py . .
|-- other
| |-- create_emails.py
| \-- create_logs.py
\-- README.md
'''

import sys

try:
    file_name = sys.argv[1]
    print(file_name)

except IndexError:
    print('usage of program: python zad_drzewo_plikow directory')
    exit(1)

except FileNotFoundError:
    print(f'File {file_name} not found!')
    exit(1)