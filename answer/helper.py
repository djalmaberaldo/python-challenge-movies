from movie import Movie

def print_movies(movies: list[Movie]) -> None:
    for movie in movies:
        print(
            f"{movie.id:>2} | "
            f"{movie.movie_title:<30} | "
            f"Rating: {movie.rating} | "
            f"Certified Fresh: {movie.certified_fresh}"
        )