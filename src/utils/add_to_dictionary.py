from . import fetch_tweets_by_user


def add_to_dictionary(aggregate_dictionary: dict, value: dict):
    aggregate_dictionary.update(value)
