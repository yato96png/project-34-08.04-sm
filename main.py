from recommender import load_movies, get_user_ratings, recommend_movies

def main():
    movies = load_movies()
    user_ratings = get_user_ratings(movies)

    if not user_ratings:
        print("Вы не оценили ни одного фильма. Попробуйте снова.")
        return

    recommendations = recommend_movies(user_ratings, movies)

    print("\n🎬 Рекомендуемые фильмы:")
    for title, genres in recommendations:
        print(f"- {title} ({genres})")

if __name__ == "__main__":
    main()
