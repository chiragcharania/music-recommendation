from pandas import read_csv
import matplotlib.pyplot as plt
data = read_csv('data/SpotifyFeatures2.csv')
data.plot.scatter(x='id', y='popularity')
plt.show()