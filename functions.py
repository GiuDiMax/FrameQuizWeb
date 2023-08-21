from config import tmdb, genres
import requests
import random


def randomFrame(d):
    pgmax = int(d)*100
    pgmin = pgmax-99
    baseurl = "https://image.tmdb.org/t/p/original"
    url = 'https://api.themoviedb.org/3/discover/movie?api_key={0}&language=it-IT&sort_by=popularity.desc&page={1}&vote_count.gte=' + str(int(1/int(d)*1000))
    pag = random.randint(pgmin, pgmax)
    res = requests.get(url.format(tmdb, pag)).json()['results']
    film = random.choice(res)
    #print(film)
    r = {'id': film['id'], 't': [], 'y': 0, 'frame': '', 'i': '', 'p': int(pgmax*10/pag)*int(d)}
    if 'original_title' in film:
        r['t'].append(film['original_title'].lower())
    if 'title' in film:
        r['t'].append(film['title'].lower())
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