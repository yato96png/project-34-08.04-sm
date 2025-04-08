import pandas as pd
from collections import defaultdict

def load_movies(path='movies.csv'):
    return pd.read_csv(path)

def get_user_ratings(movies):
    print("\nОцените следующие фильмы (от 1 до 5, или 0 если не смотрели):")
    user_ratings = []
    for _, row in movies.sample(5).iterrows():
        try:
            rating = int(input(f"{row['title']} ({row['genres']}): "))
            if rating >= 1 and rating <= 5:
                user_ratings.append((row['movie_id'], rating))
        except:
            pass
    return user_ratings

def get_genre_preferences(user_ratings, movies):
    genre_scores = defaultdict(int)
    for movie_id, rating in user_ratings:
        genres = movies[movies.movie_id == movie_id].iloc[0]['genres'].split('|')
        for genre in genres:
            genre_scores[genre] += rating
    return sorted(genre_scores.items(), key=lambda x: x[1], reverse=True)

def recommend_movies(user_ratings, movies, top_n=5):
    rated_ids = {movie_id for movie_id, _ in user_ratings}
    preferences = get_genre_preferences(user_ratings, movies)

    recommended = []
    for genre, _ in preferences:
        candidates = movies[~movies.movie_id.isin(rated_ids)]
        candidates = candidates[candidates['genres'].str.contains(genre)]
        for _, row in candidates.iterrows():
            if row['movie_id'] not in [m[0] for m in recommended]:
                recommended.append((row['title'], row['genres']))
            if len(recommended) >= top_n:
                return recommended
    return recommended
