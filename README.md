# python-challenge-movies
Python Challenge

![Alt text](/Home-assignment.png "Home assignment") 


## Purpose

This script reads movie data from a CSV file, converts each record into a structured object, filters only **Certified Fresh** movies, and displays the **Top 10 highest-rated** entries.

The solution prioritizes:
- Readability
- Simple data structures
- Pure Python (no external libraries)

## Data Representation

Each movie is represented as a **Movie object** with clearly defined attributes:

- `id`
- `rating`
- `movie_title`
- `certified_fresh`

This structure improves clarity compared to using lists or dictionaries and allows direct access to fields such as `movie.rating`.

---

## Processing Flow

1. Read the CSV file
2. Convert each row into a Movie object
3. Filter movies marked as **Certified Fresh**
4. Sort by rating in descending order
5. Select the top 10 results
6. Display the results in a formatted table


### Run scripts
```bash
python answer/highest_ratings.py
```

### Expected Output

## Top 10 Certified Fresh Movies

| Rank | ID | Movie Title                  | Rating | Certified Fresh |
|-----:|---:|------------------------------|-------:|-----------------|
| 1    | 17 | The Shawshank Redemption     | 9.6    | ✅ True |
| 2    | 4  | The Godfather                | 9.5    | ✅ True |
| 3    | 10 | Pulp Fiction                 | 9.3    | ✅ True |
| 4    | 13 | The Matrix                   | 9.2    | ✅ True |
| 5    | 8  | The Dark Knight              | 9.1    | ✅ True |
| 6    | 1  | Interstellar                 | 9.0    | ✅ True |
| 7    | 6  | Inception                    | 8.9    | ✅ True |
| 8    | 15 | Forrest Gump                 | 8.8    | ✅ True |
| 9    | 11 | Gladiator                    | 8.7    | ✅ True |
| 10   | 19 | Avengers Endgame             | 8.6    | ✅ True |
