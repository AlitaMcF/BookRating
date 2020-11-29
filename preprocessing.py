import numpy as np
import pandas as pd
from collections import Counter

train = pd.read_csv('raw_data/Train_data_2.csv')
test = pd.read_csv('raw_data/Test_data_2.csv')
train_header = train.columns
test_header = test.columns
train = np.array(train)
test = np.array(test)
print(train_header)
print(test_header)

# processing language feature
lang = train[:, 6]
unique_element = np.unique(lang)
print('unique_element:\n', unique_element, '\n')

lang_count = Counter(lang)
lang_count = dict(lang_count)
lang_count = sorted(lang_count.items())
lang_count = dict(lang_count)
print('lang_count:\n', lang_count, '\n')

lang_avg_rating = []
for i in range(len(unique_element)):
    lang_avg_rating.append(np.mean([train[j, 3] for j in range(len(lang)) if lang[j] == unique_element[i]]))
lang_avg_rating = np.around(lang_avg_rating, 2)
print('lang_avg_rating:\n', lang_avg_rating, '\n')
total_avg_rating = np.mean(lang_avg_rating)
total_avg_rating = np.around(total_avg_rating, 2)
print('total_avg_rating:\n', total_avg_rating, '\n')

# use Bayesian average
bayesian_avg_lang_rating = []
for i in range(len(unique_element)):
    element_num = lang_count[unique_element[i]]
    bayesian_avg_lang_rating.append(5/(5+element_num)*total_avg_rating + (element_num/(element_num+5))*lang_avg_rating[i])
bayesian_avg_lang_rating = np.around(bayesian_avg_lang_rating, 2)
print('bayesian_avg_lang_rating:\n', bayesian_avg_lang_rating, '\n')

# replace all language feature of trainset and testset
for i in range(len(unique_element)):
    for j in range(len(lang)):
        if lang[j] == unique_element[i]:
            lang[j] = bayesian_avg_lang_rating[i]
train[:, 6] = lang

# replace test set language
lang_test = test[:, 6]
unique_element_test = np.unique(lang_test)
print('unique_element_test:\n', unique_element_test, '\n')

for i in range(len(unique_element_test)):
    for j in range(len(lang_test)):
        if lang_test[j] == unique_element[i]:
            lang_test[j] = bayesian_avg_lang_rating[i]
for j in range(len(lang_test)):
    if isinstance(lang_test[j], str):
        lang_test[j] = total_avg_rating

test[:, 6] = lang_test

# processing nation feature
nations = train[:, 5]
unique_nation = np.unique(nations)
print('unique_nation:\n', unique_nation, '\n')

nation_count = Counter(nations)
nation_count = dict(nation_count)
nation_count = sorted(nation_count.items())
nation_count = dict(nation_count)
print('nation_count:\n', nation_count, '\n')

nation_avg_rating = []
for i in range(len(unique_nation)):
    nation_avg_rating.append(np.mean([train[j, 3] for j in range(len(nations)) if nations[j] == unique_nation[i]]))
nation_avg_rating = np.around(nation_avg_rating, 2)
print('nation_avg_rating:\n', nation_avg_rating, '\n')
total_avg_rating = np.mean(nation_avg_rating)
total_avg_rating = np.around(total_avg_rating, 2)
print('total_avg_rating:\n', total_avg_rating, '\n')

# use Bayesian average
bayesian_avg_nation_rating = []
for i in range(len(unique_nation)):
    element_num = nation_count[unique_nation[i]]
    bayesian_avg_nation_rating.append(5/(5+element_num)*total_avg_rating+(element_num/(element_num+5))*nation_avg_rating[i])
bayesian_avg_nation_rating = np.around(bayesian_avg_nation_rating, 2)
print('bayesian_avg_nation_rating:\n', bayesian_avg_nation_rating, '\n')

# replace all nation feature of trainset and testset
for i in range(len(unique_nation)):
    for j in range(len(nations)):
        if nations[j] == unique_nation[i]:
            nations[j] = bayesian_avg_nation_rating[i]
train[:, 5] = nations

# replace test set nation
nation_test = test[:, 5]
unique_element_test = np.unique(nation_test)
print('unique_element_test:\n', unique_element_test, '\n')

for i in range(len(unique_element_test)):
    for j in range(len(nation_test)):
        if nation_test[j] == unique_nation[i]:
            nation_test[j] = bayesian_avg_nation_rating[i]
for j in range(len(nation_test)):
    if isinstance(nation_test[j], str):
        nation_test[j] = total_avg_rating
test[:, 5] = nation_test

# preprocessing author feature
author_train = train[:, 2]
author_all = []
author_unique = []
for i in range(len(author_train)):
    authors = author_train[i].split('/')
    for j in range(len(authors)):
        author_all.append(authors[j])
author_unique = list(set(author_all))
author_unique = sorted(author_unique)
print('author total num:', len(author_unique), '\n')

# count author num
author_num = Counter(author_all)
author_num = dict(author_num)
author_num = sorted(author_num.items())
author_num = dict(author_num)

# count author rating
author_rating = []
for i in range(len(author_unique)):
    author_rating.append(np.mean([train[j, 3] for j in range(len(author_train)) if author_unique[i] in author_train[j]]))

# count total average rating of author
total_avg_author_rating = np.mean(author_rating)
total_avg_author_rating = np.around(total_avg_author_rating, 2)
print('total_avg_author_rating:', total_avg_author_rating, '\n')

# count author bayesian average rating
bayesian_avg_author_rating = []
for i in range(len(author_unique)):
    element_num = author_num[author_unique[i]]
    bayesian_avg_author_rating.append(element_num/(element_num+2)*author_rating[i] + 2/(element_num+2)*total_avg_author_rating)
bayesian_avg_author_rating = np.around(bayesian_avg_author_rating, 2)
print('bayesian_avg_author_rating:', bayesian_avg_author_rating, '\n')

# replace train set author feature
for i in range(len(author_train)):
    authors = author_train[i].split('/')
    score = 0
    for j in range(len(authors)):
        score += bayesian_avg_author_rating[author_unique.index(authors[j])]
    author_train[i] = score/len(authors)
author_train = np.around(np.float64(author_train), 2)
train[:, 2] = author_train

# replace test set author feature
author_test = test[:, 2]
for i in range(len(author_test)):
    authors = author_test[i].split('/')
    score = []
    for j in range(len(authors)):
        if authors[j] in author_unique:
            score.append(bayesian_avg_author_rating[author_unique.index(authors[j])])
        else:
            score.append(total_avg_author_rating)
    author_test[i] = np.mean(score)
author_test = np.around(np.float64(author_test), 2)
test[:, 2] = author_test

# preprocessing publisher feature
publisher_train = train[:, 11]
publisher_all = []
publisher_unique = []
for i in range(len(publisher_train)):
    publisher_all.append(publisher_train[i])
publisher_unique = list(set(publisher_all))
publisher_unique = sorted(publisher_unique)
print('publisher total num:', len(publisher_unique), '\n')

# count publisher num
publisher_num = Counter(publisher_all)
publisher_num = dict(publisher_num)
publisher_num = sorted(publisher_num.items())
publisher_num = dict(publisher_num)

# count publisher rating
publisher_rating = []
for i in range(len(publisher_unique)):
    publisher_rating.append(np.mean([train[j,3] for j in range(len(publisher_train)) if publisher_unique[i] in publisher_train[j]]))

# count total average rating of publisher
total_avg_publisher_rating = np.mean(publisher_rating)
total_avg_publisher_rating = np.around(total_avg_publisher_rating, 2)
print('total_avg_publisher_rating:', total_avg_publisher_rating, '\n')

# count publisher bayesian average rating
bayesian_avg_publisher_rating = []
for i in range(len(publisher_unique)):
    element_num = publisher_num[publisher_unique[i]]
    bayesian_avg_publisher_rating.append(element_num/(element_num+2)*publisher_rating[i] + 2/(element_num+2)*total_avg_publisher_rating)
bayesian_avg_publisher_rating = np.around(bayesian_avg_publisher_rating, 2)
print('bayesian_avg_publisher_rating:', bayesian_avg_publisher_rating, '\n')

# replace train set publisher feature
for i in range(len(publisher_train)):
    publisher_train[i] = bayesian_avg_publisher_rating[publisher_unique.index(publisher_train[i])]
publisher_train = np.around(np.float64(publisher_train), 2)
train[:, 11] = publisher_train

# replace test set publisher feature
publisher_test = test[:, 11]
for i in range(len(publisher_test)):
    if publisher_test[i] in publisher_unique:
        publisher_test[i] = bayesian_avg_publisher_rating[publisher_unique.index(publisher_test[i])]
    else:
        publisher_test[i] = total_avg_publisher_rating
publisher_test = np.around(np.float64(publisher_test), 2)
test[:, 11] = publisher_test


# preprocessing test_data datetime
date = test[:, -2]
for i in range(len(date)):
    date[i] = date[i].split("/")[0]
test[:, -2] = date

# correct the headers of train and test
train_header = np.array(train_header)
train_header[2] = 'authors'
test_header = np.array(test_header)
test_header[7] = 'num_pages'

# write to file
train = pd.DataFrame(train)
train.to_csv('./processed_data/train_processed_language_author_publisher_nation.csv', header=train_header, index=None)

test = pd.DataFrame(test)
test.to_csv('./processed_data/test_processed_language_author_publisher_nation.csv', header=test_header, index=None)

print("done!")
