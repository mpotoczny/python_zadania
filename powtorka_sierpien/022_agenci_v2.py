def create_map(n):
    map = []
    for x in range(n):
        for y in range(n):
            map.append((x,y))
    return map

def advice(agents: list, n: int) -> list:
    map = create_map(n)

    list_of_all_dicts = []
    for agent in agents:
        from collections import defaultdict
        s1 = defaultdict(int)  # wartość domyślna = 0
        for place in map:
            if place == agent:
                s1[place] = 0
            else:
                distance = abs(agent[0] - place[0]) + abs(agent[1] - place[1])
                s1[place] = distance

        list_of_all_dicts.append(s1)

    from functools import reduce
    all_keys = reduce((lambda x,y : x | y),[d.keys() for d in list_of_all_dicts])
    result_dict = { k : min(d.get(k,0) for d in list_of_all_dicts) for k in all_keys }

    safe_places = [ k for k,v in result_dict.items() if v == max(result_dict.values()) ]
    print(safe_places)
    return safe_places


# advice([(5,1)],6)
advice([(0,0), (1, 5), (5,1) ], 6)