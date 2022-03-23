"""
Do this first!

Adds values to the movie_dict for a new movie name.
If movie name is not in movie_dict, add a new entry.

If the movie_name is already in movie_dict, append the
actors to the existing actors. There should be no
repeat actor names.

Args:
  movie_dict: A movie dictionary.
  movie_name: A string representing the unique name of a movie.
  actors: A list of strings representing the actors in that movie.

Returns the movie_dict.
"""
def add_or_update_a_movie(movie_dict, movie_name, actors):
    pass

"""
Removes an actor from movie_name in a movie_dict object.

Args:
  movie_dict: A movie dictionary.
  movie_name: A string representing the unique name of a movie.
  actors: A list of strings representing the actors in that movie.

Returns the movie_dict.
"""
def remove_actor_from_movie(movie_dict, movie_name, actor):
    pass


"""
Given a movie dictionary, returns the movie with the most actors.
In the case of a tie, any single movie is acceptable.

Args:
  movie_dict: A movie dictionary.

Returns a string.
"""
def find_movie_with_most_actors(movie_dict):
    pass


"""
Given two actors, returns an array of movie names in which both
actors appear.

Args:
  actor_1: {str} Name of first actor.
  actor_2: {str} Name of second actor.

Returns an array of strings.
"""
def find_similar_movies(movie_dict, actor1, actor2):
    pass


"""
Given a movie dictionary, returns the actor which has been in
the most movies.

Args:
  movie_dict: A movie dictionary.

Returns a string.
"""
def find_actor_with_most_movies(movie_dict):
    pass


"""
Opens a file named movie_filename. Each line in this
file is formatted as follows:

movie_1,actor_a,actor_b,actor_c,.....
movie_2,actor_d,actor_e,actor_a
movie_3,actor_e,....
...

This function returns a movie dictionary with the
correct mappings from the given file.
"""
def parse_movie_text_file(movie_filename):
    pass


"""
Extra credit!

The six degrees of Kevin Bacon is a game which
attempts to find how many movies apart a given actor
is to Kevin Bacon. If they have been in a movie with
Kevin Bacon, they are one degree from Kevin Bacon. If
the actor has been in a movie with an actor who has
been in a movie with Kevin Bacon, then they are two
degrees away from Kevin Bacon.

https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon

Write a function which when given two actors, returns 
the number of degrees between actor1 and actor2.

Args:
  actor_1: {str} Name of first actor.
  actor_2: {str} Name of second actor.

Returns an integer.
"""
def degrees_between(actor1, actor2):
    pass

