"""
Netflix Movies and TV Shows - Data Analysis Python Script
HPIT4008 Big Data Analytics Project
"""

import pandas as pd


def check_missing_data(df):
    missing = df.isnull().sum()
    print(f"Missing Data: \n{missing}")


def main():
    raw_data = "./data/raw/netflix_titles.csv"
    cleaned_data = "./data/cleaned/netflix_cleaned.csv"

    df = pd.read_csv(raw_data)

    check_missing_data(df)


if __name__ == "__main__":
    main()
