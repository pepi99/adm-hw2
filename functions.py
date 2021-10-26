import pandas as pd
from IPython.display import display
import datetime as dt

def summary(df):
    # number of elements in the whole data set
    print(f"Total elemnts in data set: {df.size :,}")

    # number of reviews in the whole data set
    print(f"Number of reviews: {df.shape[0] :,}")

    # number of attributes for each review
    print(f"Number of attributes for each review: {df.shape[1]}")

    attribute(df)

    # number of distinct games
    print(f"Number of distinct games: {len(df['app_name'].unique())}")

    # number of distinct languages
    print(f"Number of distinct languages: {len(df['language'].unique())}")

    # reviews time period
    first_review = dt.date.fromtimestamp(df['timestamp_created'].min())
    last_review = dt.date.fromtimestamp(df['timestamp_created'].max())
    print(f"Reviews range from {first_review} to {last_review}")


    return

def attribute(df):
    # extracting most important attribute from dataset
    most_relevant_attributes = df[['author.steamid', 'app_name', 'timestamp_created',
                                'language', 'review', 'weighted_vote_score', 'author.playtime_forever']].columns

    # naming the most_relevant_attribute index object
    most_relevant_attributes = most_relevant_attributes.set_names(['Attibutes of the review'])

    # buiding an array to describe each feature
    descriptions = ['Author identification number', 'Game name', 'Date of review',
                    'Language of the review', 'The review itself', 'Score of the review', 'Author total playtime']

    # display the result
    display(pd.DataFrame(descriptions, index=most_relevant_attributes, columns=['Description']))
