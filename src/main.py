"""
Netflix Movies and TV Shows - Data Analysis Python Script
HPIT4008 Big Data Analytics Project
"""

import pandas as pd
import plot_figures as plot
from clean_data import clean_data


def check_missing_data(df):
    missing = df.isnull().sum()
    print(f"\nMissing Data: \n{missing}")


def check_duplicate_data(df):
    duplicates = df.duplicated().sum()
    print(f"\nDuplicate Rows: {duplicates}")


def save_data(df, path):
    df.to_csv(path, index=False)
    print(f"\nData saved to {path}")


def main():
    raw_data_path = "./data/raw/netflix_titles.csv"
    cleaned_data_path = "./data/cleaned/netflix_cleaned.csv"

    df = pd.read_csv(raw_data_path)

    check_missing_data(df)
    check_duplicate_data(df)

    cleaned_data = clean_data(df)
    save_data(cleaned_data, cleaned_data_path)

    plot.plot_top_countries(cleaned_data)
    plot.plot_genre_distribution(cleaned_data)
    plot.plot_rating_distribution(cleaned_data)
    plot.plot_content_type(cleaned_data)


if __name__ == "__main__":
    main()
