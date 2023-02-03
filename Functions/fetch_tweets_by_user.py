import tweepy
from .create_authentication import api, client
from .fetch_tweets_by_id import fetch_tweets_by_id


def fetch_tweets_by_user(user: str, number_of_tweets: int = 1):
    api_response = api.user_timeline(screen_name=user, count=number_of_tweets)
    tweets = []

    for tweet in api_response[:number_of_tweets]:
        tweet_id = validate_value(tweet, "id")
        tweet_statistics = fetch_tweets_by_id(tweet_id)

        # I really need to refactor this
        tweets.append(
            {
                "url": tweet_url_builder(tweet_id),
                "date": validate_value(tweet, "text"),
                "content": validate_value(tweet, "text"),
                "id": tweet_id,
                "user": validate_value(tweet.user, "name"),
                "retweet_count": tweet_statistics.public_metrics["retweet_count"],
                "like_count": tweet_statistics.public_metrics["like_count"],
                "quote_count": tweet_statistics.public_metrics["quote_count"],
                "conversation_id": validate_value(tweet, "conversation_id"),
                "lang": validate_value(tweet, "lang"),
                "source": validate_value(tweet, "source"),
                "coordinates": validate_value(tweet, "place"),
            }
        )

    return {user: [tweets]}


def validate_value(tweet, key):
    try:
        # refactor later to take list of keys
        return getattr(tweet, key)
    except AttributeError:
        return None


def tweet_url_builder(id):
    return f"https://twitter.com/twitter/statuses/{id}"
