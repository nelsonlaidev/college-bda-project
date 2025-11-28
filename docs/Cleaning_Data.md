# Cleaning Data

Missing Data:

| Column       | Missing Values |
| ------------ | -------------- |
| show_id      | 0              |
| type         | 0              |
| title        | 0              |
| director     | 2634           |
| cast         | 825            |
| country      | 831            |
| date_added   | 10             |
| release_year | 0              |
| rating       | 4              |
| duration     | 3              |
| listed_in    | 0              |
| description  | 0              |

## Duplicates

We drop all duplicate rows.

## Handling Missing data

We handle missing data as follows:

- Director: Fill missing with "Unknown"
- Cast: Fill missing with "No information"
- Country: Fill missing with "Unknown"

Since there are only a few missing values in these columns, we can drop the rows directly.

- Date added: Remove rows
- Rating: Remove rows
- Duration: Remove rows

## Categorizing Ratings

Based on [Netflix Rating System](https://rating-system.fandom.com/wiki/Netflix), We categorize the ratings into the following groups:

- Kids: TV-Y, TV-PG, TV-G, TV-Y7, TV-Y7-FV, PG, G
- Teens: TV-14, PG-13
- Adults: TV-MA, R, NC-17
- Unrated: UR, NR

## Date Processing

The `date_added` column is processed to extract additional time-based features:

- Convert `date_added` to datetime format
- Extract `year_added` from the date
- Extract `month_added` from the date
- Extract `month_name` from the date for better readability
