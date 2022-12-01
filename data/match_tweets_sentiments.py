import pandas as pd

HYDRATED_FILE = 'hydrated/hydrated_402.csv'
SENTIMENTS_FILE = 'raw/corona_tweets_402.csv'
FINAL_FILE = 'matched/tweets_with_sentiment_402.csv'

hydrated = pd.read_csv(HYDRATED_FILE)[['id','text','retweet_id']]
print(hydrated.shape)
hydrated = hydrated[hydrated.retweet_id.isnull()].drop(columns=['retweet_id'])  # only keep original tweets

sentiments = pd.read_csv(SENTIMENTS_FILE, header=None)
sentiments.columns = ['id','sentiment']

merged = pd.merge(hydrated, sentiments, on='id')
print(merged.shape)
merged.to_csv(FINAL_FILE)