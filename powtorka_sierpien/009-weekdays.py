'''
Deﬁne a function weekdays(weekday) that returns a list of weekdays,
starting with the given weekday. It should work like this:
weekdays('Wednesday')
['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
'''

def weekdays(day:str) -> list:
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # SPOSÓB 1
    # i = days.index(day)
    # list1 = days[i:]
    # list2 = days[:i]
    # # list1.extend(list2)
    # result = list1 + list2

    # SPOSÓB 2
    # result = days[days.index(day):] + days[:days.index(day)]

    # SPOSÓB 3
    # result = list( days[days.index(day): ] + days )[:7]

    # SPOSÓB 4
    index = days.index(day)
    result = (days + days)[index:index+7]

    print(result)
    return result

weekdays('Friday')