import pandas as pd


def create_csv(tweets_array):
    try:
        data_frame = pd.DataFrame(tweets_array)
        data_frame.to_csv("tweets.csv", encoding="utf-8-sig")

        print("*=======================*")
        print("*          Done         *")
        print("*=======================*")
    except Exception as error:
        print("Error while creating csv:\n", error)
