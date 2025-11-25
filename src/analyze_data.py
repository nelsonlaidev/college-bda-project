def analyze_countries(df, top_n=10):
    """
    We will analyze the top n (default is 10) countries producing
    content on Netflix.
    """

    countries = df["country"]
    country_counts = countries.value_counts().head(top_n)

    print(f"\nTop {top_n} Countries:")

    for i, (country, count) in enumerate(country_counts.items(), 1):
        print(f"  {i}. {country}: {count}")

    return country_counts
