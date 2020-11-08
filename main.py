import omdb
import tastedive

def get_sorted_recommendations(*movie_title_list):
    related_movies = tastedive.get_related_movies(*movie_title_list)
    #in case i need to add rotten tomatoes rating for more visualization (uncomment 2 next lines and comment line 3)
    #related_movies = list(map(lambda movie_title: (omdb.get_movie_rating(omdb.get_movie_data(movie_title)), movie_title), related_movies))
    #related_movies = sorted(related_movies, key=lambda movie: (movie[0], movie[1]), reverse=True)
    related_movies = sorted(related_movies, key=lambda movie_title: (omdb.get_movie_rating(omdb.get_movie_data(movie_title)), movie_title), reverse=True)
    return related_movies

print(get_sorted_recommendations('Ready Player One'))