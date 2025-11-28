import matplotlib.pyplot as plt
from analyze_data import analyze_countries, analyze_genres


def plot_top_countries(df, top_n=10):
    """
    Plot top countries producing content
    See: analyze_countries in analyze_data.py
    """

    _, ax = plt.subplots(figsize=(12, 8))

    # Get top countries data
    top_countries = analyze_countries(df, top_n)

    # Horizontal bar plot
    ax.barh(range(len(top_countries)), top_countries.values)

    # Main title
    ax.set_title(f"Top {top_n} Countries Producing Netflix Content")

    # Y axis
    ax.set_yticks(range(len(top_countries)))
    ax.set_yticklabels(top_countries.index)
    ax.invert_yaxis()
    ax.set_ylabel("Country")

    # X axis
    ax.set_xlabel("Number of Titles")

    # Accessibility
    ax.grid(axis="x", alpha=0.3, linestyle="--")

    # Add value labels
    for i, val in enumerate(top_countries.values):
        # Add some padding between the bar and the text (20 units)
        ax.text(val + 20, i, str(val), va="center")

    # Show plot
    plt.tight_layout()
    plt.show()


def plot_genre_distribution(df, top_n=15):
    """
    Plot top genres
    See: analyze_genres in analyze_data.py
    """

    _, ax = plt.subplots(figsize=(14, 8))

    # Get top genres data
    top_genres = analyze_genres(df, top_n)

    # Bar plot
    ax.bar(range(len(top_genres)), top_genres.values)

    # Main title
    ax.set_title(f"Top {top_n} Genres on Netflix")

    # Y axis
    ax.set_ylabel("Number of Titles")

    # X axis
    ax.set_xticks(range(len(top_genres)))
    # Rotate x labels for better readability
    ax.set_xticklabels(top_genres.index, rotation=45, ha="right")
    ax.set_xlabel("Genre")

    # Accessibility
    ax.grid(axis="x", alpha=0.3, linestyle="--")

    # Show plot
    plt.tight_layout()
    plt.show()
