def analyze_countries(df, top_n=10):
    """
    We will analyze the top n (default is 10) countries producing
    content on Netflix.
    """

    countries = df["country"]
    top_countries = countries.value_counts().head(top_n)

    print(f"\nTop {top_n} Countries:")

    for i, (country, count) in enumerate(top_countries.items(), 1):
        print(f"  {i}. {country}: {count}")

    return top_countries


def analyze_genres(df, top_n=15):
    """
    We will analyze the top n (default is 15) genres on Netflix.
    """

    genres = df["listed_in"].str.split(", ").explode()
    top_genres = genres.value_counts().head(top_n)

    print(f"\nTop {top_n} Genres:")

    for i, (genre, count) in enumerate(top_genres.items(), 1):
        print(f"  {i}. {genre}: {count}")

    return top_genres


def analyze_ratings(df):
    """
    We will analyze the distribution of content ratings on Netflix.
    """

    ratings = df["rating"].value_counts()

    print("\nContent Ratings Distribution:")

    for rating, count in ratings.items():
        print(f"  {rating}: {count}")

    return ratings
