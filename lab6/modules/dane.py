import csv


class Movie:
    def __init__(self, id: int, title: str, genres: str):
        self.id = id
        self.title = title
        self.genres = genres

    def __str__(self):
        return f'Film {self.title}'


class Ratings:
    def __init__(self, userId: int, movieId: int, rating: int, timestamp: int):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


class Links:
    def __init__(self, movieId: int, imdbId: int, tmdbId: int):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


class Tags:
    def __init__(self, userId: int, movieId: int, tag: str, timestamp: int):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp


def what_class(x: str, a):
    if "links" in x:
        return Links(*a)
    elif ("movie" in x):
        return Movie(*a)
    elif ("tag" in x):
        return Tags(*a)
    elif ('rating' in x):
        return Ratings(*a)


def data_new(x: str):
    with open(x, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader.__next__()
        return [what_class(x, row).__dict__ for row in csv_reader]


# data_new('movies.csv')
# print(data_new('links.csv'))
