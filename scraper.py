import nltk
from src.data.input.twitter_users import twitter_users as users
from src.utils.aggregate_tweets import aggregate_tweets
from src.utils.fetch_tweets_by_user import fetch_tweets_by_user
from src.utils.create_csv import create_csv


if __name__ == "__main__":
    NUMBER_OF_TWEETS = 100
    aggregate_array = []

    for user in users:
        tweets = fetch_tweets_by_user(user, NUMBER_OF_TWEETS)["tweets"]
        aggregate_tweets(aggregate_array, tweets)

    # flattens aggregate_array using list comprehension
    create_csv([item for items in aggregate_array for item in items])
