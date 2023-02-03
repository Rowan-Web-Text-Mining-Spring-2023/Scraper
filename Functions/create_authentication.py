import yaml, tweepy

with open("config.yaml", "r") as file:
    twitter_api_credentials = yaml.safe_load(file)["twitter_api"]
    consumer_key = twitter_api_credentials["consumer_key"]
    consumer_secret = twitter_api_credentials["consumer_secret"]
    bearer_token = twitter_api_credentials["bearer_token"]
    access_token = twitter_api_credentials["access_token"]
    access_token_secret = twitter_api_credentials["access_token_secret"]


def create_authentication():
    return tweepy.API(
        tweepy.OAuth1UserHandler(
            consumer_key, consumer_secret, access_token, access_token_secret
        )
    )


def create_client():
    return tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )
