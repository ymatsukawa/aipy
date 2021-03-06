from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

learn_data = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

learn_result = [
    0,
    0,
    0,
    1
]

# learn
linearsSVC = LinearSVC()
linearsSVC.fit(learn_data, learn_result)

# predict
test_data = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
predict_result = linearsSVC.predict(test_data)

# accuracy check
print('result of prediction is: ', predict_result)
print('accuracy is: ', accuracy_score([0, 0, 0, 1], predict_result))

# 2020/03/29 result is 1.0 = 100%
