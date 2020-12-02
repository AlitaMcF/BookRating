import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# # histogram of different models
# models = ['Random_Forest', 'LR', 'Adaboost', 'Decision_Tree', 'MLP', 'SVR', 'Bagging_MLP']
# mse_all = [0.02581458599347049, 0.033991320447980825, 0.03451884765373522, 0.048541398495801996, 0.033640165513129094,
#            0.034156111040382645, 0.029683751581600464]
# mse_all = np.around(mse_all, 4)
# plt.figure()
# plt.title('MSE of different models')
# plt.xlabel('models')
# plt.ylabel('MSE')
# plt.bar(range(len(models)), mse_all, color=['red', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey'], align='center')
# plt.xticks(range(len(models)), models, rotation=-30)
# for x, y in zip(range(len(models)), mse_all):
#     plt.text(x, y, '%.4f' % y, ha='center', va='bottom')
# plt.xlim([-1, len(models)])
# plt.show()


# # plot language average rating
# lang = ['ara', 'en-CA', 'en-GB', 'en-US', 'eng', 'enm', 'fre', 'ger', 'gla', 'glg', 'grc',
#         'ita', 'jpn', 'lat', 'msa', 'mul', 'nl', 'nor', 'por', 'rus', 'spa', 'srp', 'swe',
#         'tur', 'wel', 'zho']
# avg_rating = [3.55, 4.03, 3.93, 3.92, 3.94, 3.87, 3.98, 3.94, 4.47, 3.36, 3.47, 4.1,  4.27, 4.35,
#               4.11, 4.13, 4.18, 3.6,  3.96, 4.26, 3.94, 0.0, 3.46, 4.42, 5.0, 4.53]
# plt.figure()
# plt.title('language average rating')
# plt.xlabel('language')
# plt.ylabel('average rating')
# plt.bar(range(len(lang)), avg_rating, color='grey', align='center')
# plt.xticks(range(len(lang)), lang, rotation=-30)
# for x, y in zip(range(len(lang)), avg_rating):
#     plt.text(x, y, y, ha='center', va='bottom')
# plt.show()


# plot bayesian language target encoding
lang = ['ara', 'en-CA', 'en-GB', 'en-US', 'eng', 'enm', 'fre', 'ger', 'gla', 'glg', 'grc',
        'ita', 'jpn', 'lat', 'msa', 'mul', 'nl', 'nor', 'por', 'rus', 'spa', 'srp', 'swe',
        'tur', 'wel', 'zho']
baye_avg_rating = [3.82, 3.96, 3.93, 3.92, 3.94, 3.88, 3.98, 3.94, 3.98, 3.79, 3.62, 3.98, 4.23, 4.06,
                   3.92, 4.08, 3.93, 3.83, 3.93, 3.99, 3.94, 3.23, 3.76, 3.97, 4.07, 4.34]
plt.figure()
plt.title('language bayesian target encoding')
plt.xlabel('language')
plt.ylabel('encoding')
plt.bar(range(len(lang)), baye_avg_rating, color='grey', align='center')
plt.xticks(range(len(lang)), lang, rotation=-30)
for x, y in zip(range(len(lang)), baye_avg_rating):
    plt.text(x, y, y, ha='center', va='bottom')
plt.show()
