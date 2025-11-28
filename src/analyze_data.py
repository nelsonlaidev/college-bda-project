def analyze_countries(df, top_n=10):
    """
    Analyze the top n (default is 10) countries producing
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
    Analyze the top n (default is 15) genres on Netflix.
    """

    genres = df["listed_in"].str.split(", ").explode()
    top_genres = genres.value_counts().head(top_n)

    print(f"\nTop {top_n} Genres:")

    for i, (genre, count) in enumerate(top_genres.items(), 1):
        print(f"  {i}. {genre}: {count}")

    return top_genres


def analyze_ratings(df):
    """
    Analyze the distribution of content ratings on Netflix.
    """

    ratings = df["rating"].value_counts()

    print("\nContent Ratings Distribution:")

    for rating, count in ratings.items():
        print(f"  {rating}: {count}")

    return ratings


def analyze_content_type(df):
    """
    Analyze the distribution of content types (Movies vs TV Shows) on Netflix.
    """

    content_type = df["type"].value_counts()

    print("\nContent Type Distribution:")

    for content, count in content_type.items():
        print(f"  {content}: {count}")

    return content_type


def analyze_yearly_trend(df):
    """
    Analyze the yearly trend of content additions on Netflix.
    """
    yearly_data = df.groupby(["year_added", "type"]).size().unstack(fill_value=0)

    print("\nYearly Content Addition Trend:")
    print(yearly_data)

    return yearly_data


def analyze_movie_duration(df):
    """
    Analyze the distribution of movie durations on Netflix.
    """

    movies = df[df["type"] == "Movie"]

    durations = movies["duration"].str.replace(" min", "").astype(int)

    print("\nMovie Duration Analysis:")
    print(f"  Mean: {durations.mean():.2f} minutes")
    print(f"  Median: {durations.median():.2f} minutes")
    print(f"  Min: {durations.min():.2f} minutes")
    print(f"  Max: {durations.max():.2f} minutes")

    return durations
