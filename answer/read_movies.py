
import csv
from movie import Movie

def parse_bool(value: str) -> bool:
    return value.strip().lower() == "true"

def read_movies_from_csv(path: str) -> list[Movie]:
    movies = []

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            movie = Movie(
                id=int(row["id"]),
                movie_title=row["movie_title"],
                rating=float(row["rating"]),
                certified_fresh=parse_bool(row["certified_fresh"]),
            )
            movies.append(movie)

    return movies
