import tweepy
from .create_authentication import (
    create_authentication as tweepy_auth,
    create_client as tweepy_client,
)  # import throws error when debugging, fix this sometime soon

api = tweepy_auth()
client = tweepy_client()


def fetch_tweets_by_user(user: str, number_of_tweets: int = 1):
    api_response = api.user_timeline(screen_name=user, count=number_of_tweets)
    tweets = []

    for tweet in api_response[:number_of_tweets]:
        tweet_id = validate_value(tweet, "id")
        conversation_id = 1
        url = tweet_url_builder(tweet_id)
        date = validate_value(tweet, "text")
        content = validate_value(tweet, "text")
        user = validate_value(tweet.user, "name")
        retweet_count = validate_value(tweet, "retweet_count")
        like_count = validate_value(tweet, "favorite_count")
        quote_count = 1
        lang = validate_value(tweet, "lang")
        source = 1
        coordinates = 1

        # response = client.get_tweet(id=tweet_id, user_auth=True)

        # print(response)

        tweets.append(
            {
                "url": url,
                "date": date,
                "content": content,
                "id": tweet_id,
                "user": user,
                "retweet_count": retweet_count,
                "like_count": like_count,
                "quote_count": quote_count,
                "conversation_id": conversation_id,
                "lang": lang,
                "source": source,
                "coordinates": coordinates,
            }
        )

    return {user: tweets}


def validate_value(tweet, key):
    try:
        # refactor later to take list of keys
        return getattr(tweet, key)
    except AttributeError:
        return None


def tweet_url_builder(id):
    return f"https://twitter.com/twitter/statuses/{id}"
