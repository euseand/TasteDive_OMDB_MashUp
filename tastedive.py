import requests

def get_movies_from_tastedive(movie_title):
    url = "https://tastedive.com/api/similar"
    keys_d = {'q':movie_title, 'type':'movie', 'limit':5}
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
    
def extract_movie_titles(result_dict):
    try:
        titles = [movie['Name'] for movie in result_dict['Similar']['Results']]
        return titles
    except KeyError as err:
        print('Error: ', err, ' - tastedive.py - extract_movie_titles')

def get_related_movies(movie_titles_list):
    result = []
    for movie_title in movie_titles_list:
        try:
            result += extract_movie_titles(get_movies_from_tastedive(movie_title))
        except TypeError as err:
            print('Error: ', err, ' - tastedive.py - get_related_movies')
    result = list(set(result))
    if result != []:
        return result
    else:
        return 'No related movies or API limit exceeded'