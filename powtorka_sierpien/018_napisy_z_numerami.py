def increment_string(string):
    txt = string
    print(txt)
    modified_string = ""

    indexes = []
    for i in range(len(txt)-1, -1, -1):
        if txt[i].isdigit():
            print(f'txt[{i}] to {txt[i]}')
            indexes.append(i)
        else:
            break

    if indexes != []:
        indexes.reverse()  # obraca listę, MODYFIKUJE ORYGINAŁ
        print(indexes)

        counter = 0
        digit_start = indexes[0]
        digit_end = indexes[-1]
        while counter < indexes[-1]:
            if txt[digit_start] == '0' and digit_start < indexes[-1]:
                counter += 1
                digit_start = indexes[counter]
            else:
                break
        print(f'digit_start {digit_start}')

        digit_txt = txt[digit_start:digit_end+1]
        number = int(digit_txt)
        print(number)
        next_number = number + 1
        next_number_str = str(next_number)
        print(next_number_str)

        print(f'txt[{digit_start}]{txt[digit_start]}')
        if len(next_number_str) > len(digit_txt) and txt[digit_start-1] == '0':
            digit_start = digit_start - 1

        modified_string = txt[0:digit_start] + next_number_str

        print(modified_string)
        return modified_string

    else:
        modified_string = txt + '1'
        print(modified_string)
        return modified_string

y = increment_string("fo086obar00112")
print('-'*50)
y = increment_string("foo")
print('-'*50)
y = increment_string("foo1")
print('-'*50)
y = increment_string("foo00")
print('-'*50)
y = increment_string("foobar99")
print('-'*50)
y = increment_string("foobar099")
print('-'*50)


