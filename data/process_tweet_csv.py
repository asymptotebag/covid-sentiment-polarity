import pandas as pd

TWEETS_SIZE = 250000
TWEETS_FILE = 'raw/corona_tweets_402.csv'
FINAL_FILE = 'hydrated/tweets_402.csv'

data = pd.read_csv(TWEETS_FILE, header=None)  # columns = id, sentiment
data = data.drop(data.iloc[:,1:2], axis=1)
data = data.iloc[:TWEETS_SIZE]
data.to_csv(FINAL_FILE, index=False, header=None)