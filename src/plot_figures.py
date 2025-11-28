import matplotlib.pyplot as plt
import analyze_data as analyze
import seaborn as sns


def plot_top_countries(df, top_n=10):
    """
    Plot top countries producing content
    See: analyze_countries in analyze_data.py
    """

    _, ax = plt.subplots(figsize=(12, 8))

    # Get top countries data
    top_countries = analyze.analyze_countries(df, top_n)

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
    top_genres = analyze.analyze_genres(df, top_n)

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


def plot_rating_distribution(df):
    """
    Plot distribution of content ratings on Netflix
    See: analyze_ratings in analyze_data.py

    Notes:
    - autopct: a function to display percentage values on the slices of a pie chart
    """

    _, ax = plt.subplots(1, 2, figsize=(16, 7))

    # Get ratings data
    ratings = analyze.analyze_ratings(df)

    # Pie plot
    ax[0].pie(
        ratings.values,
        labels=None,
        autopct=lambda p: f"{p:.1f}%" if p > 2 else "",  # show % only if >2%
    )
    ax[0].legend(ratings.index, loc="center left", bbox_to_anchor=(1, 0.5))
    ax[0].set_title("Content Ratings Distribution")

    category_counts = df["rating_category"].value_counts()

    # Pie plot
    ax[1].pie(category_counts.values, labels=category_counts.index, autopct="%1.1f%%")
    ax[1].set_title("Rating Category Distribution")

    # Show plot
    plt.tight_layout()
    plt.show()


def plot_content_type(df):
    """
    Plot content type distribution
    See: analyze_content_type in analyze_data.py
    """
    _, ax = plt.subplots(figsize=(10, 6))

    types = analyze.analyze_content_type(df)

    # Bar plot
    ax.bar(types.index, types.values)
    ax.set_title("Movies vs TV Shows on Netflix")

    # Y axis
    ax.set_ylabel("Number of Titles")

    # X axis
    ax.set_xlabel("Content Type")

    # Add value labels on bars
    for i, (_, val) in enumerate(types.items()):
        ax.text(i, val + 100, str(val), ha="center", va="bottom")

    # Accessibility
    ax.grid(axis="y", alpha=0.3, linestyle="--")

    # Show plot
    plt.tight_layout()
    plt.show()


def plot_yearly_trend(df):
    """
    Plot yearly trend of content additions on Netflix
    See: analyze_yearly_trend in analyze_data.py
    """

    _, ax = plt.subplots(figsize=(14, 6))

    yearly_data = analyze.analyze_yearly_trend(df)

    # Line plot
    yearly_data.plot(kind="line", ax=ax, marker="o")

    ax.set_title("Netflix Content Growth Over Years")

    # Y axis
    ax.set_ylabel("Number of Titles Added")

    # X axis
    ax.set_xlabel("Year")

    # Accessibility
    ax.grid(axis="x", alpha=0.3, linestyle="--")

    # Show plot
    plt.tight_layout()
    plt.show()


def plot_movie_duration(df):
    """
    Plot distribution of movie durations on Netflix
    See: analyze_movie_duration in analyze_data.py
    """

    _, ax = plt.subplots(figsize=(12, 6))

    durations = analyze.analyze_movie_duration(df)

    # Histogram plot
    ax.hist(durations, bins=30, edgecolor="black")

    # Add mean and median lines
    mean_duration = durations.mean()
    median_duration = durations.median()

    ax.axvline(
        mean_duration,
        color="blue",
        linestyle="--",
        label=f"Mean: {mean_duration:.0f} min",
    )
    ax.axvline(
        median_duration,
        color="red",
        linestyle="--",
        label=f"Median: {median_duration:.0f} min",
    )

    ax.set_title("Distribution of Movie Durations on Netflix")

    # Y axis
    ax.set_ylabel("Number of Movies")

    # X axis
    ax.set_xlabel("Duration (minutes)")

    # Accessibility
    ax.grid(axis="y", alpha=0.3, linestyle="--")

    # Show legend
    ax.legend()

    # Show plot
    plt.tight_layout()
    plt.show()


def plot_monthly_heatmap(df):
    """
    Plot heatmap of content additions by month and year on Netflix
    """

    _, ax = plt.subplots(figsize=(14, 8))

    pivot_table = df.pivot_table(
        values="show_id",
        index="year_added",
        columns="month_added",
        aggfunc="count",
        fill_value=0,
    )

    sns.heatmap(
        pivot_table,
        cmap="Reds",
        annot=True,
        fmt="g",
        cbar_kws={"label": "Number of Titles"},
        linewidths=0.5,
        ax=ax,
    )

    ax.set_title("Netflix Content Additions by Month and Year")

    # Y axis
    ax.set_ylabel("Year")

    # X axis
    ax.set_xlabel("Month")
    ax.set_xticklabels(
        [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
    )

    # Show plot
    plt.tight_layout()
    plt.show()
