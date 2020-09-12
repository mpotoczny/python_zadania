'''
Find the longest substring in alphabetical order.
Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt"
Test.assert_equals(longest('asdfbyfgiklag'), 'fgikl')
'''


def longest(s: str):

    # SPOSÓB 1
    if len(s) < 1:
        raise ValueError("Given text is not long enough.")
    s = s.lower()

    string_temp = ""
    result = ""
    lista = []

    for i in range(len(s)):
        if s[i] >= s[i-1] or i == 0:
            string_temp += s[i]
        else:
            string_temp = s[i]

        lista.append(string_temp) # lista żeby widzieć, że mechanizm wydobywa ciągi alfabetyczne

        if len(string_temp) > len(result):
            result = string_temp

    print(lista)
    return result


print( longest("asdfaaaabbbbcttavvfffffdf") )