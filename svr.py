import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.model_selection import cross_val_score


train = pd.read_csv('./processed_data/train_processed_language_author_publisher.csv')
test = pd.read_csv('./processed_data/test_processed_language_author_publisher.csv')

# get x_train, y_train, x_test and y_test
x_train = train.drop(columns=['bookID', 'title', 'average_rating', 'isbn', 'publication_date'])
y_train = train.loc[:, 'average_rating']
x_test = test.drop(columns=['bookID', 'title', 'average_rating', 'isbn', 'publication_date'])

# normalization
num_train = len(x_train)
x_all = pd.concat([x_train, x_test], axis=0)
x_all = (x_all-x_all.mean()) / x_all.std()
x_train = x_all.iloc[0:num_train, :]
x_test = x_all.iloc[num_train:, :]

# cross-validate 10 fold
regr = SVR(gamma='auto')
score = -np.mean(cross_val_score(regr, x_train, y_train, cv=10, scoring='neg_mean_squared_error'))
print('10-CV mse:', score)
# 10-CV mse: 0.034156111040382645

# predict test set
regr2 = SVR(gamma='auto')
regr2.fit(x_train, y_train)
y_test_pred = regr2.predict(x_test)
# write to file
test['average_rating'] = y_test_pred.round(2)
test.to_csv('./result/svr_test_res.csv', index=None)
