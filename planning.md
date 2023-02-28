# Features:
## add

add (`movie-name`)

* searches for the movie in imdb
	* shows interactive selection menu
		* presents 5 top results
		* presents option to search deeper
	* on user selection
		* retrieves the following parameters
			* movie name
			* director
			* genres
			* year
			* description
			* imdb id
			* imdb score
			* rotten tomatoes score
				* separate API call to RT
		* saves the movie to the database
	* ask for status
		* watched / not watched
		* write to db
	* return result

## list

list (`watched | unwatched`)

* displays a list of movies and their status


## remove

remove `movie name`

* searches the db for the `movie name`
	* if no exact match
		* show user selection of possible matches
		* wait for user selection
	* on exact match
		* present "are you sure" dialogue
	* on confirmation
		* send command to db to delete line
			* movie db
			* status db
	* return result

## update

update `movie name`

* searches the db for the `movie name`
	* if no exact match
		* show user selection of possible matches
		* wait for user selection
	* present the options
		* watched
		* unwatched
	* if watched selected
		* update the status db
	* if unwatched selected
		* remove from status db
	* return result


# Tech Design:

## Infra
* create db (movies & status tables)
* find a way to read commands from cli
* How the APIs work

OMDB - http://www.omdbapi.com/?i=tt0133093&apikey=80fafa3a
TMDB - https://api.themoviedb.org/3/movie/550?api_key=b5b1baac3d56cc9ee08b4e017486795d


## add

* querying the db for the movie
	* if not exist:
		* search api for the movie name, show the user the results
		* pagination

		* go to the api and fetch:
			* movie name
			* director
			* genres
			* year
			* description
			* imdb id
			* rotten tomatoes id
			* imdb score
			* rotten tomatoes score
		* add a new movie to db

	* ask for watch status?
	* write status in watch_status db table



1. starting the app
2. searching for a movie (search api)
3. choosing movie from list (ui)
4. finding the movie by some ids in apis (get)
5. inserting into the db (add_movie returns our own MySQL id)
6. what is the status of the movie? (ui)
7. insert status with id (from stage 5) into db



## Imagine app interaction and interface (UI)
* cli: `python -m watchlist add the matrix`
* (we take the movie name, we search it using api and return the results)
* terminal: if no movies found, print "no movies found" and quit.
* terminal: print a list(a row each) of the movies results with a header. each row will contain movie's index in list, name, year.
Example: 
	```
		 	Name 					Year
	1 		The Matrix 				1999
	2 		The Matrix Reloaded 	2002
	3 		The Matrix Revolution 	2005
	```

* terminal: print a request to choose one of the options, or `n` for next page (only if there's next page), or `p` for previous page (only if there's previous page)
* (validate choice)
	* terminal: if not valid, print "invalid choice" and reprint the current movie list
* (on valid `n` choice, up the page num by one and fetch new batch of results)
* (on valid `p` choice, down the page num by one and fetch new batch of results)
* (on valid index choice, get by tmdb_id the movie details from the api, create the movie in movie table only if not exist)
* terminal: print a watched status query, options are [yes,no,y,n]
* (validate choice)
	* terminal: if not valid, print "invalid choice" and reprint the watched status query
* (on valid choice, update watch status table with created movie id (id in movies table) and chosen watch status)
* terminal: print the summary of the action and quit

