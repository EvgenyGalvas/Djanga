import pickle
import os.path


class Movie:
    def __init__(self, title, janr, derector, long_time, studia, actors):
        self.title = title
        self.janr = janr
        self.derector = derector
        self.long_time = long_time
        self.studia = studia
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.janr})"


class MovieModel:
    def __init__(self):
        self.db_name = 'db.txt'
        self.movies = self.load_data()

    def add_movie(self, dict_movie):
        movie = Movie(*dict_movie.values())
        self.movies[movie.title] = movie

    def get_all_movie(self):
        return self.movies.values()

    def get_single_movie(self, user_title):
        movie = self.movies[user_title]
        dict_movie = {
            "название": movie.title,
            "жанр": movie.janr,
            "режисёр": movie.derector,
            "длительность": movie.long_time,
            "студия": movie.studia,
            "актёры": movie.actors
        }
        return dict_movie

    def remove_movie(self, user_title):
        return self.movies.pop(user_title)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.movies, f)
