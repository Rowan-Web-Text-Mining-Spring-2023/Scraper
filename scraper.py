import nltk
from src.data.Input.twitter_users import twitter_users as users
from src.utils.add_to_dictionary import add_to_dictionary
from src.utils.fetch_tweets_by_user import fetch_tweets_by_user
from src.utils.create_csv import create_csv


if __name__ == "__main__":
    aggregate_dictionary = {}

    for user in users:
        add_to_dictionary(aggregate_dictionary, fetch_tweets_by_user(user, 10))

    create_csv(aggregate_dictionary["tweets"])
