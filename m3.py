import pandas as pd
import warnings
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.model_selection import GridSearchCV

warnings.filterwarnings("ignore")

data = pd.read_csv('data/SpotifyFeatures2.csv')

X = data.iloc[:1000, 1:5].values
Y = data.iloc[:1000, -2].values

LabelEncoder_X = LabelEncoder()

X[:, 1] = LabelEncoder_X.fit_transform(X[:, 1])
X[:, 2] = LabelEncoder_X.fit_transform(X[:, 2])
X[:, 3] = LabelEncoder_X.fit_transform(X[:, 3])

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size=0.3)

clf = svm.SVC(kernel='linear')

#Cs = range(1, 20)
#clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), cv = 2)
clf.fit(X_Train, Y_Train.ravel())
print "Model Accuracy:", clf.score(X_Test, Y_Test)


