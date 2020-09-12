def num_key_strokes(text):

    # # SPOSÓB NR 1
    # presses_sum = 0
    # for character in text:
    #     # lower case
    #     if 97 <= ord(character) < 123:
    #         presses_sum += 1
    #     # numbers
    #     elif 48 <= ord(character) < 58:
    #         presses_sum += 1
    #     # one-pressed characters: ` -=[];'\,./
    #     elif character in " `-=[];'\,./":
    #         presses_sum += 1
    #     # tab and enter
    #     elif ord(character) == 9 or ord(character) == 11:
    #         presses_sum += 1
    #
    #     # upper case
    #     elif 65 <= ord(character) < 91:
    #         presses_sum += 2
    #     # characters with SHIFT
    #     elif character in '"~!@#$%^&*()_+{}:|<>?':
    #         presses_sum += 2
    #
    # return presses_sum

    # # SPOSÓB NR 2
    # return sum([1 if i in "abcdefghijklmnopqrestuvwxyz1234567890-=`];[',.\/ " else 2 for i in text])

    # SPOSÓB NR 3
    symbol = '~!@#$%^&*()_+{}:"|<>?' # znaki z shiftem
    count = 0
    for letter in text:
        if letter.isupper() or letter in symbol:
            count += 1
        count += 1
    return count


test_one = "Hello, world!"
test_two = "0297350298-02-30856-174346"
test_three = "This is a long SEnteNce.1"

print(num_key_strokes(test_one))
print(num_key_strokes(test_two))
print(num_key_strokes(test_three))