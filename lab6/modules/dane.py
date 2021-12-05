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


def data_new(x: str):
    with open(x, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # print(csv_reader.__next__())
        opis = csv_reader.__next__()
        if opis[1] == 'title':
            return [Movie(row[0], row[1], row[2]).__dict__ for row in csv_reader]
            # for row in csv_reader:
            # lista.append(Movie(row[0], row[1], row[2]).__dict__)
        elif (opis[2] == 'rating'):
            return [Ratings(row[0], row[1], row[2], row[3]).__dict__ for row in csv_reader]

        elif (opis[1] == 'imdbId'):
            return [Links(row[0], row[1], row[2]).__dict__ for row in csv_reader]

        elif (opis[2] == 'tag'):
            return [Tags(row[0], row[1], row[2], row[3]).__dict__ for row in csv_reader]


# data_new('movies.csv')
