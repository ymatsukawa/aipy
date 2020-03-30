import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

iris_data = pd.read_csv('iris.csv', encoding='utf-8')

# iris data
x = iris_data.loc[:, ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
# iris label
y = iris_data.loc[:, 'Name']

# split data to test and train
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, shuffle = True)

# learn
svc = SVC()
svc.fit(x_train, y_train)

# predict
y_predict = svc.predict(x_test)
print('accuracy = ', accuracy_score(y_test, y_predict))

# result of prediction
# 0.9333333333333333 to 1.0
