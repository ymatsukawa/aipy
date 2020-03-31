import pandas as pd
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

wine = pd.read_csv('winequality-white.csv', sep=';', encoding='utf-8')

# get wine column
y = wine['quality']
# drop quality column
x = wine.drop('quality', axis = 1)

"""
# plots quality distribution

count_data = wine.groupby('quality')['quality'].count()
count_data.plot()
plot.savefig('win_plot.png')
"""

# label quality
newQualityDist = []
for value in list(y):
    if value <= 4:
        newQualityDist += [0]
    elif value <= 7:
        newQualityDist += [1]
    else:
        newQualityDist += [2]
y = newQualityDist

# split data to train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

# learn
randomForest = RandomForestClassifier()
randomForest.fit(x_train, y_train)

# prediction
y_pred = randomForest.predict(x_test)

print(classification_report(y_test, y_pred))
print('accuracy = ', accuracy_score(y_test, y_pred))

# accuracy 0.91 - 0.94
