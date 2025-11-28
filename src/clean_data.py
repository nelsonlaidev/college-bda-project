"""
See docs/Cleaning_Data.md for more details
"""

import pandas as pd


def categorize_rating(rating):
    kids_ratings = ["TV-Y", "TV-PG", "TV-G", "TV-Y7", "TV-Y7-FV", "PG", "G"]
    teens_ratings = ["TV-14", "PG-13"]
    mature_ratings = ["TV-MA", "R", "NC-17"]
    unrated = ["UR", "NR"]

    if rating in kids_ratings:
        return "Kids"
    elif rating in teens_ratings:
        return "Teens"
    elif rating in mature_ratings:
        return "Adults"
    elif rating in unrated:
        return "Unrated"
    else:
        return "Other"


def clean_data(df):
    """
    - inplace means the operation will modify the original dataframe directly
    """

    # Copy the original dataframe
    cleaned_df = df.copy()

    # Remove duplicate rows
    cleaned_df.drop_duplicates(inplace=True)

    # Handle missing values
    # Director, Cast, Country
    cleaned_df.fillna(
        {"director": "Unknown", "cast": "No information", "country": "Unknown"},
        inplace=True,
    )
    # Date added
    cleaned_df.dropna(subset=["date_added"], inplace=True)
    # Rating
    cleaned_df.dropna(subset=["rating"], inplace=True)
    # Duration
    cleaned_df.dropna(subset=["duration"], inplace=True)

    cleaned_df["rating_category"] = cleaned_df["rating"].apply(categorize_rating)

    cleaned_df["date_added"] = pd.to_datetime(cleaned_df["date_added"].str.strip())
    cleaned_df["year_added"] = cleaned_df["date_added"].dt.year
    cleaned_df["month_added"] = cleaned_df["date_added"].dt.month
    cleaned_df["month_name"] = cleaned_df["date_added"].dt.month_name()

    return cleaned_df
