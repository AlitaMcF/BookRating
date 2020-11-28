import numpy as np
import pandas as pd
from sklearn.ensemble import AdaBoostRegressor
from sklearn.model_selection import cross_val_score


train = pd.read_csv('./processed_data/train_processed_language_author_publisher.csv')
test = pd.read_csv('./processed_data/test_processed_language_author_publisher.csv')

# get x_train, y_train, x_test and y_test
x_train = train.drop(columns=['bookID', 'title', 'average_rating', 'isbn', 'publication_date', 'isbn13'])
y_train = train.loc[:, 'average_rating']
x_test = test.drop(columns=['bookID', 'title', 'average_rating', 'isbn', 'publication_date', 'isbn13'])

# normalization
num_train = len(x_train)
x_all = pd.concat([x_train, x_test], axis=0)
x_all = (x_all-x_all.mean()) / x_all.std()
x_train = x_all.iloc[0:num_train, :]
x_test = x_all.iloc[num_train:, :]

# cross-validate 10 fold
regr = AdaBoostRegressor(n_estimators=50, random_state=0)
score = -np.mean(cross_val_score(regr, x_train, y_train, cv=10, scoring='neg_mean_squared_error'))
print('10-CV mse:', score)
# 10-CV mse: 0.03451884765373522

# predict test set
regr2 = AdaBoostRegressor(n_estimators=50, random_state=0)
regr2.fit(x_train, y_train)
y_test_pred = regr2.predict(x_test)
# write to file
test['average_rating'] = y_test_pred.round(2)
test.to_csv('./result/adaboost_test_res.csv', index=None)

