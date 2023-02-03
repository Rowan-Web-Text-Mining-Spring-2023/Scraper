import tweepy
from .create_authentication import api, client


def fetch_tweets_by_id(tweet_id):
    # wrap this in try-catch eventually
    return client.get_tweet(
        id=tweet_id,
        tweet_fields=["public_metrics"],
        expansions=["attachments.media_keys"],
        media_fields=["public_metrics"],
        user_auth=True,
    ).data
