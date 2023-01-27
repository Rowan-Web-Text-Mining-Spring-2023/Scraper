import nltk
from Data.Input.twitter_users import twitter_users as users
from Functions.add_to_dictionary import add_to_dictionary
from Functions.fetch_tweets_by_user import fetch_tweets_by_user


if __name__ == "__main__":
    aggregate_dictionary = {}

    for user in users:
        add_to_dictionary(aggregate_dictionary, fetch_tweets_by_user(user))

    print(aggregate_dictionary)
