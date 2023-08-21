from config import tmdb
import requests
import random


def randomFrame():
    baseurl = "https://image.tmdb.org/t/p/original"
    url = 'https://api.themoviedb.org/3/discover/movie?api_key={0}&language=it-IT&sort_by=popularity.desc&page={1}&vote_count.gte=1000'
    res = requests.get(url.format(tmdb, random.randint(1, 150))).json()['results']
    film = random.choice(res)
    r = {'t': [], 'y': 0, 'frame': ''}
    if 'original_title' in film:
        r['t'].append(film['original_title'].lower())
    if 'title' in film:
        r['t'].append(film['title'].lower())
    for t in r['t']:
        if "-" in t:
            if t.split("-", 1)[0].strip() not in r['t']:
                r['t'].append(t.split("-", 1)[0].strip())
    if 'release_date' in film:
        r['y'] = int(film['release_date'].split("-", 1)[0])
    url = 'https://api.themoviedb.org/3/movie/{1}/images?api_key={0}&language=null'
    res = requests.get(url.format(tmdb, film['id'])).json()['backdrops']
    #frame = baseurl + random.choice(res)['file_path']
    r['frame'] = baseurl + random.choice(res)['file_path']
    return r


if __name__ == "__main__":
    print(randomFrame())
