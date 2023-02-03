from . import fetch_tweets_by_user


def add_to_dictionary(aggregate_dictionary: dict, value: dict):
    user = list(value)[0]
    tweets = list(value.items())[0][1]
    aggregate_dictionary[user] = tweets
