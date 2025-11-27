import matplotlib.pyplot as plt
from analyze_data import analyze_countries


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

    # X axis
    ax.set_xlabel("Number of Titles")
    ax.set_ylabel("Country")

    # Accessibility
    ax.grid(axis="x", alpha=0.3, linestyle="--")

    # Add value labels
    for i, val in enumerate(top_countries.values):
        # Add some padding between the bar and the text (20 units)
        ax.text(val + 20, i, str(val), va="center")

    # Show plot
    plt.show()
