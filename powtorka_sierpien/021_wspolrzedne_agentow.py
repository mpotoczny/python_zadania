def create_map(n):
    map = []
    for x in range(n):
        for y in range(n):
            map.append((x,y))
    return map

def locate_agents(map, agents):
    map_with_agents = ["AGENT" if place in agents else place for place in map]
    return map_with_agents

def advice(agents: list, n: int) -> list:

    map = create_map(n)
    # map_with_agents = locate_agents(map, agents)
    # print(map_with_agents)

    print(f' mapa {map}')
    print(f' agenci {agents}')
    print()


    # big_dict = dict()
    # for place in map:
    #     big_dict[place] = 0
    # print(big_dict)

    from collections import defaultdict

    list_of_all_dicts = []
    for agent in agents:
        s1 = defaultdict(int)  # wartość domyślna = 0
        for place in map:
            if place == agent:
                s1[place] = 0
            else:
                distance = abs(agent[0] - place[0]) + abs(agent[1] - place[1])
                s1[place] = distance

        list_of_all_dicts.append(s1)

        print(f'agent {agent}: slownik: {s1}')
        print()

    print(list_of_all_dicts)
    print()

    from functools import reduce
    all_keys = reduce((lambda x,y : x | y),[d.keys() for d in list_of_all_dicts])
    result_dict = { k : min(d.get(k,0) for d in list_of_all_dicts) for k in all_keys }

    print(result_dict)

    # safe_places = []
    # maxiu = max(result_dict.values())
    # print(maxiu)
    # for k,v in result_dict.items():
    #     if v == maxiu:
    #         safe_places.append(k)

    safe_places = [ k for k,v in result_dict.items() if v == max(result_dict.values()) ]
    print(safe_places)

    return safe_places



# advice([(5,1)],6)
advice([(0,0), (1, 5), (5,1) ], 6)