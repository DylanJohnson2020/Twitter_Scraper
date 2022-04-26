import pandas as pd
import numpy as np

# Loads scraped tweets file and formats the display so you can see all columns in console
dframe = pd.read_csv('scraped_tweets.csv')
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 11)

# Moves columns to left side of the DF
second_column = dframe.pop('followers')
dframe.insert(1, 'followers', second_column)

# Ranks the DF based on the amount of followers behind each username that tweeted the hashtag
dframe['max_rank'] = dframe['followers'].rank(method='max')
first_column = dframe.pop('max_rank')
dframe.insert(0, 'max_rank', first_column)

# Sorts the ranking from most followers to least
dframe['max_rank'] = dframe['followers'].rank(ascending=0)
dframe = dframe.set_index('max_rank')
dframe = dframe.sort_index()
print(dframe)

# Saves reformatted DF to CSV.file
dframe.to_csv('scraped_tweets.csv')
