import matplotlib.pyplot as plt
import os
from sklearn.datasets import make_blobs
import pandas as pd
import numpy as np
import matplotlib.pyplot as pp

from sklearn.utils import Bunch
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


###############################################"
# Importing data and adding label section through clustering
############################################### "

frame = pd.read_csv(r"C:\Users\kizer\E-bin project\Data\Data.csv", sep=",", encoding="utf-8") 
#print(frame)
#frame.info() 

#Apply K-means method for clustering
from sklearn.cluster import KMeans
km = KMeans(
    n_clusters=3, tol=0.01 
)
frame["label"] = km.fit_predict(frame[['Constant']])

#Show a sample of 50 constants with their labels
print(frame.sample(50))

#Plot with Matplotlib the dielectric constants versus their labels
pp.scatter(frame['Constant'], frame['label'])
#pp.show()
#frame.to_csv("C:\\Users\\kizer\\E-bin project\\Trash categorization\\frame.csv")

###############################################"
# Model training section
############################################"

#Turn the files into Bunchs with respect to each columns
frame = Bunch(data = frame["Constant"].fillna('').to_list(), target=frame["label"].fillna('').to_list())
frame.data = np.vstack((frame.data, np.zeros_like(frame.data))).T
print(frame.data)

# Create and train the RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(frame.data, frame.target)

#Variable to test
To_predict = [[200, 0]]
predicted = clf.predict(To_predict) 
print(predicted)
