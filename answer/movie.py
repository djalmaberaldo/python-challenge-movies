from dataclasses import dataclass 

@dataclass
class Movie:
    id: int
    movie_title: str
    rating: float
    certified_fresh: bool