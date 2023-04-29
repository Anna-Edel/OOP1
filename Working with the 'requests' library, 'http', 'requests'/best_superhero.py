import requests


def most_intelligence_hero(self):
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url)
    resp = response.json()
    count_intel = 0
    for hero in resp:
        if hero['name'] in heroes_list:
            hero_intel = hero['powerstats']['intelligence']
            if hero_intel > count_intel:
                count_intel = hero_intel
                intelligence_dict = hero['name']
    print(intelligence_dict)


heroes_list = ['Hulk', 'Captain America', 'Thanos']

if __name__ == '__main__':
    most_intelligence_hero(heroes_list)
