import pandas as pd


def create_csv(data: dict):
    try:
        data_frame = pd.DataFrame.from_dict(data)
        data_frame.columns = map(str.capitalize, data_frame.columns)
        data_frame.to_csv("tweets.csv", encoding="utf-8")

        print("=========================")
        print("          Done           ")
        print("=========================")
    except Exception as error:
        print("Error while creating csv:\n", error)
