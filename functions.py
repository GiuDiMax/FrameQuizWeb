from config import tmdb, genres
import requests
import random


def randomFrame(d):
    pgmax = int(d)*100
    pgmin = pgmax-99
    baseurl = "https://image.tmdb.org/t/p/original"
    #url = 'https://api.themoviedb.org/3/discover/movie?api_key={0}&language=en-US&sort_by=popularity.desc&page={1}&vote_count.gte=' + str(int(1/int(d)*1000))
    url = 'https://api.themoviedb.org/3/discover/movie?api_key={0}&language=en-US&sort_by=popularity.desc&page={1}&vote_count.gte=250'
    pag = random.randint(pgmin, pgmax)
    #print(url.format(tmdb, pag))
    res = requests.get(url.format(tmdb, pag)).json()['results']
    film = random.choice(res)
    #print(film)
    r = {'id': film['id'], 't': [], 'y': 0, 'frame': '', 'i': '', 'p': int(1000/film['popularity'] * 1250/film['vote_count']) + 1}
    if 'original_title' in film:
        r['t'].append(film['original_title'].lower())
    if 'title' in film:
        r['t'].append(film['title'].lower())
    url = 'https://api.themoviedb.org/3/movie/{1}?api_key={0}&language=it-IT'
    r['t'].append(requests.get(url.format(tmdb, film['id'])).json()['title'])
    for t in r['t']:
        for sign in [' -', ' (', ': ']:
            if sign in t:
                if t.split(sign, 1)[0].strip() not in r['t']:
                    r['t'].append(t.split(sign, 1)[0].strip())
        #for sign in ['.', '?', '!']:
        #    if sign in t:
        #        t.replace(sign, "")
        for sign in [{'n': ' 2', 'l': ' ii'}, {'n': ' 3', 'l': ' iii'}, {'n': ' 4', 'l': ' iv'}]:
            if sign['l'] in t:
                r['t'].append(t.replace(sign['l'], sign['n']))
        for sign in ['the']:
            if sign in t:
                r['t'].append(t.replace("the", "").strip())
    if 'release_date' in film:
        r['y'] = int(film['release_date'].split("-", 1)[0])
    r['i'] = "Decennio: " + str(int(r['y']/10)*10) + " - Genere:"
    #print(film)
    for g in film['genre_ids']:
        gg = list(filter(lambda genres: genres['id'] == g, genres))[0]
        #print(gg['name'])
        r['i'] = r['i'] + " " + gg['name']
    url = 'https://api.themoviedb.org/3/movie/{1}/images?api_key={0}&language=null'
    res = requests.get(url.format(tmdb, film['id'])).json()['backdrops']
    #frame = baseurl + random.choice(res)['file_path']
    r['frame'] = baseurl + random.choice(res)['file_path']
    return r


if __name__ == "__main__":
    print(randomFrame(1))
    print(randomFrame(2))
    print(randomFrame(3))
    print(randomFrame(4))
