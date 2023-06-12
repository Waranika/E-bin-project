import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import pandas as pd
import numpy as np
import matplotlib.pyplot as pp

frame = pd.read_csv(r"C:\Users\kizer\E-bin project\Data\Data.csv", sep=",", encoding="utf-8")


print(frame)
frame.info() 
#frame.plot


val = 0. # this is the value where you want the data to appear on the y-axis.
ar = frame['Constant'] # just as an example array
#pp.plot(ar, np.zeros_like(ar) + val, 'x')
#pp.show()

from sklearn.cluster import KMeans

km = KMeans(
    n_clusters=5, tol=0.01
)

frame["label"] = km.fit_predict(frame[['Constant']])
print(frame.sample(50))

pp.scatter(frame['Constant'], frame['label'])
pp.show()


#ax = frame[frame['label']==0].plot.scatter(x='Constant', y='label', s=50, color='white', edgecolor='black')

#frame[frame['label']==1].plot.scatter(x='Constant', y='label', s=50, color='white', ax=ax, edgecolor='red')


#plt.scatter(km.cluster_centers_.ravel(), [0.5]*len(km.cluster_centers_), s=100, color='green', marker='*')
