import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # df = tweets[tweets['content'].str.len() > 15] 
    df = tweets[tweets['content'].apply(lambda x: len(x) > 15)]

    return df[['tweet_id']]