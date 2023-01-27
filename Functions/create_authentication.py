import yaml, tweepy


def create_authentication():
    with open("config.yaml", "r") as file:
        twitter_api_credentials = yaml.safe_load(file)["twitter_api"]
        consumer_key = twitter_api_credentials["consumer_key"]
        consumer_secret = twitter_api_credentials["consumer_secret"]
        bearer_token = twitter_api_credentials["bearer_token"]  # not needed for now
        access_token = twitter_api_credentials["access_token"]
        access_token_secret = twitter_api_credentials["access_token_secret"]
        auth = tweepy.OAuth1UserHandler(
            consumer_key, consumer_secret, access_token, access_token_secret
        )

    return auth
