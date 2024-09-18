import numpy as np

def accuracy_score(y_true, y_pred):
    correct_preds = np.sum(y_true == y_pred)
    return (correct_preds / len(y_true))

y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 0, 1, 0, 1])
output = accuracy_score(y_true, y_pred)
print(output)