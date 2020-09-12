def get_score(arr) -> int:
    result = 0
    level = 0

    rates = {
        0: 0,
        1: 40,
        2: 100,
        3: 300,
        4: 1200
    }

    count_lines = 0
    for lines in arr:
        result = result + rates[lines] * (level + 1)

        count_lines = count_lines + lines
        if count_lines >= (level + 1) * 10:
            level += 1

    return result


x = get_score([1,2,3,4])
print(x)
x = get_score([0, 1, 1, 3, 0, 2, 1, 2])
print(x)
x = get_score([2, 0, 4, 2, 2, 3, 0, 0, 3, 3])
print(x)
x = get_score([0])
print(x)
