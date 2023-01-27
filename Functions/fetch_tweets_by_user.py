import tweepy
from .create_authentication import (
    create_authentication as tweepy_auth,
)  # import throws error when debugging, fix this sometime soon

api = tweepy.API(tweepy_auth())


def fetch_tweets_by_user(user: str, number_of_tweets: int = 10):
    api_response = api.user_timeline(screen_name=user, count=number_of_tweets)
    tweets = []

    for tweet in api_response[:number_of_tweets]:
        tweets.append(tweet.text)

    return {user: tweets}
