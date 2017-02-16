import urllib.request
import urllib.parse
import json
import time


def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    temp = urllib.request.urlopen(url)
    if temp.getcode() == 429:
        time.sleep(2)
    response = temp.read().decode('utf-8')
    return json.loads(response)


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)

def get_collect(film):
    if film['belongs_to_collection']:
        return film['belongs_to_collection']['name']
    else:
        return None

def func_genres(film):
    if film['genres']:
        return set(j['name'] for j in film['genres'])
    else:
        return set()


def find_director(film):
    if film['credits']:
        for j in film['credits']['crew']:
            if j['job'].lower() == 'director'.lower():
                return j['name']
    else:
        return None


def func_keywords(film):
    if film['keyw']['keywords']:
        return set(j['name'] for j in film['keyw']['keywords'])
    else:
        return set()


