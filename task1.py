import requests

url = "https://superheroapi.com/api/" + '2619421814940190'

method_stats = '/powerstats'  # id + / + powerstats
method_find_by_name = '/search/'

heroes = ['Hulk', 'Captain America', 'Thanos']

# --- start 1 task


def get_id(hero):
    return requests.get(url + method_find_by_name + hero)


def get_stats(hero_id):
    return requests.get(url + '/' + hero_id + method_stats)


def get_max_int_hero(heroes):
    result = dict()
    for hero in heroes:
        id_info = get_id(hero)
        if id_info.status_code == 200:
            current_id = id_info.json()['results'][0]['id']
            stats = get_stats(current_id)
            current_int = int(stats.json()['intelligence'])
            result[hero] = current_int
        else:
            print('ERROR: ' + str(id_info))

    return max(result, key=result.get)


print(get_max_int_hero(heroes))