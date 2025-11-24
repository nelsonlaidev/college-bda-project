def clean_data(df):
    """
    We will clean the data by:
    See docs/Cleaning_Data.md for more details.

    - Removing duplicates
    - Handling missing values
      - Director: Fill missing with "Unknown"
      - Cast: Fill missing with "No information"
      - Country: Fill missing with "Unknown"
      Since there are only a few missing values in these columns, we can drop the rows directly.
        - Date added: Remove rows
        - Rating: Remove rows
        - Duration: Remove rows
    - Categorize ratings into age groups
      Read: https://rating-system.fandom.com/wiki/Netflix

    Notes:
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

    return cleaned_df
