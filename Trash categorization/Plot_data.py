import matplotlib.pyplot as plt
import os
from sklearn.datasets import make_blobs
import pandas as pd
import numpy as np
import matplotlib.pyplot as pp


###############################################"
# Importing data and adding label section
# "

frame = pd.read_csv(r"C:\Users\kizer\E-bin project\Data\Data.csv", sep=",", encoding="utf-8") #Load frame
print(frame)
frame.info() 




val = 0. # this is the value where you want the data to appear on the y-axis.
ar = frame['Constant'] # just as an example array
#pp.plot(ar, np.zeros_like(ar) + val, 'x')
#pp.show()

#Apply K-means method for clustering
from sklearn.cluster import KMeans
km = KMeans(
    n_clusters=5, tol=0.01 
)
frame["label"] = km.fit_predict(frame[['Constant']])
print(frame.sample(50))

pp.scatter(frame['Constant'], frame['label'])

#frame['Constant'] = str(frame['Constant'])

#pp.show()

#Create new CSV file
#frame.to_csv("C:\\Users\\kizer\\E-bin project\\Trash categorization\\frame.csv")


###############################################"
# Model training section
# "
from sklearn.utils import Bunch
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

#Turn the files into Bunchs with respect to each columns
frame = Bunch(data = frame["Constant"].fillna('').to_list(), target=frame["label"].fillna('').to_list())
#print(frame.target)
#print(frame.data)

frame.data = np.vstack((frame.data, np.zeros_like(frame.data))).T
print(frame.data)

# Create and train the RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(frame.data, frame.target)

#Naive Bayers Test
#text_clf2 = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB()),])
#text_clf2 = text_clf2.fit(frame.data, frame.target)

To_predict = [[25, 0]]

predicted = clf.predict(To_predict)
#accuracy = clf.score(frame.data, frame.target)
print(predicted)

#predicted = text_clf2.predict(To_predict)
#print (predicted)
