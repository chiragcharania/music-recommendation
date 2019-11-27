from pandas import read_csv
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
data = read_csv('data/SpotifyFeatures2.csv')
data = data[['id', 'popularity', 'danceability']]
data = data[:2000]
parallel_coordinates(data, 'id')
plt.show()