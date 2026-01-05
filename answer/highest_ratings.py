from typing import List
from read_movies import read_movies_from_csv
from movie import Movie
from helper import print_movies

def top_n_certified_fresh(movies: List[Movie],n: int = 10) -> List[Movie]:
    certified_fresh_movies = [
        movie for movie in movies if movie.certified_fresh
    ]

    return sorted(
        certified_fresh_movies,
        key=lambda m: m.rating,
        reverse=True
    )[:n]


if __name__ == "__main__":
    movies = read_movies_from_csv("movies.csv")

    top_10_certified = top_n_certified_fresh(movies)

    print("Top 10 Certified Fresh Movies:\n")
    print_movies(top_10_certified)
