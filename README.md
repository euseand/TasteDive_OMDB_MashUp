# TasteDive_OMDB_MashUp
Small project using TasteDive and OMDB API's  
Basically TasteDive module fetches movie info from API and then extracts list of movie titles, related to the input one.  
OMDB module retrieves info about movie from API and then extracts Rotten Tomatoes rating for the input movie title.  
Main module combines both of them and returns list of related movie titles sorted in descending order by Rotten Tomatoes rating (and alphabetically, in case of ties). 