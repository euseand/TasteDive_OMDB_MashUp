import requests

OMDB_KEY = '40d7ac1c'

def get_movie_data(movie_title):
    url = "http://www.omdbapi.com/?"
    keys_d = {}
    keys_d['apikey'] = OMDB_KEY
    keys_d['t'] = movie_title
    try:
        response = requests.get(url, params=keys_d)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ('Http Error: ', errh)
    except requests.exceptions.ConnectionError as errc:
        print ('Error Connecting: ', errc)
    except requests.exceptions.Timeout as errt:
        print ('Timeout Error: ', errt)
    except requests.exceptions.RequestException as err:
        print ('Oops: Something Else', err)
    return response.json()

def get_movie_rating(result_dict):
    try:
        for rating in result_dict['Ratings']:
            if rating['Source'] == 'Rotten Tomatoes':
                return rating['Value'][:-1]
    except KeyError as err:
        print('Error: ', err)
    return 0