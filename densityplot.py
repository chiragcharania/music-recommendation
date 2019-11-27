from pandas import read_csv
import matplotlib.pyplot as plt
data = read_csv('data/SpotifyFeatures2.csv')
data = data.drop(['id', 'danceability'], axis=1)
data.plot(kind='density')
plt.show()