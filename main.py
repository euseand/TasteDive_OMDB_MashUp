import omdb
import tastedive


movie_titles_list = []
while(True):
    title = input('Enter movie title (leave blank to stop): ')
    if title != '':
        movie_titles_list.append(title)
    else:
        break

related_movies = tastedive.get_related_movies(movie_titles_list)
#in case i need to add rotten tomatoes rating for more visualization (uncomment 2 next lines and comment line 3)
related_movies = list(map(lambda movie_title: (omdb.get_movie_rating(omdb.get_movie_data(movie_title)), movie_title), related_movies))
related_movies = sorted(related_movies, key=lambda movie: (movie[0], movie[1]), reverse=True)
#related_movies = sorted(related_movies, key=lambda movie_title: (omdb.get_movie_rating(omdb.get_movie_data(movie_title)), movie_title), reverse=True)
print(related_movies)