import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt


train = pd.read_csv('./processed_data/train_processed_language_author_publisher_nation_date.csv')
test = pd.read_csv('./processed_data/test_processed_language_author_publisher_nation_date.csv')

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
regr = RandomForestRegressor(n_estimators=100)
score = -np.mean(cross_val_score(regr, x_train, y_train, cv=10, scoring='neg_mean_squared_error'))
print('10-CV mse:', score)
# 10-CV mse: 0.02581458599347049
# 10-CV mse: 0.025679084951578272

# # predict test set
# regr2 = RandomForestRegressor(n_estimators=100)
# regr2.fit(x_train, y_train)
# y_test_pred = regr2.predict(x_test)
# # write to file
# test['average_rating'] = y_test_pred.round(2)
# test.to_csv('./result/random_forest_test_res.csv', index=None)


# # grid search the best hyper-parameter n_estimator
# max_estimator = 200
# all_mse = []
# for i in range(5, max_estimator+1, 5):
#     regr = RandomForestRegressor(i)
#     score = -np.mean(cross_val_score(regr, x_train, y_train, cv=10, scoring='neg_mean_squared_error'))
#     all_mse.append(score)
# print(all_mse.index(min(all_mse)), min(all_mse))
# plt.figure()
# plt.title('Random_Forest: Grid-Search n_estimator')
# plt.xlabel('estimator number')
# plt.ylabel('MSE')
# plt.plot(range(5, max_estimator+1, 5), all_mse)
# plt.show()


# # feature importance
# forest = RandomForestRegressor(n_estimators=100)
# forest.fit(x_train, y_train)
# importances = forest.feature_importances_
# indices = np.argsort(importances)[::-1]
# std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
# print('Feature importances:')
# for i in range(len(importances)):
#     print(str(x_train.columns[indices[i]]).ljust(20, ' '), np.around(importances[indices[i]], 4))
# # plot
# plt.figure()
# plt.title("Feature importances")
# plt.xlabel('feature')
# plt.ylabel('importance')
# plt.bar(range(x_train.shape[1]), importances[indices], color="r", yerr=std[indices], align="center")
# plt.xticks(range(x_train.shape[1]), np.array(x_train.columns)[indices], rotation=-30)
# for x, y in zip(range(x_train.shape[1]), importances[indices]):
#     plt.text(x+0.05, y+0.005, '%.3f' % y)
# plt.xlim([-1, x_train.shape[1]])
# plt.show()
