import nltk, tweepy, yaml
from Data.Input.twitter_handles import twitter_handles
from Functions.create_authentication import auth as tweepy_auth

NUMBER_OF_TWEETS = 10

if __name__ == "__main__":
    pass

    # api = tweepy.API(auth)

    # public_tweets = api.home_timeline()

    # user = api.get_user(screen_name=twitter_handles[0])

    # tweets = api.user_timeline(screen_name=twitter_handles[0], count=NUMBER_OF_TWEETS)

    # for tweet in tweets[:NUMBER_OF_TWEETS]:
    #     print(tweet.text)
    #     print("==========")
