import isbnlib
import numpy as np
import pandas as pd
from collections import Counter

train = pd.read_csv('raw_data/Train_data_1.csv')
test = pd.read_csv('raw_data/Test_data.csv')
train_header = train.columns
test_header = test.columns
train = np.array(train)
test = np.array(test)
# print(train_header)
# print(test_header)

# process train set
isbn13_train = train[:, 5]
nations = []
for i in range(len(isbn13_train)):
    isbn13 = isbnlib.to_isbn13(str(isbn13_train[i]))
    # none replaced by English language
    if isbn13 == "":
        nation = "English language"
    else:
        nation = isbnlib.info(isbn13)
        if nation == "":
            nation = "English language"
    nations.append(nation)
train[:, 5] = nations

# process test set
isbn13_test = test[:, 5]
nations_test = []
for i in range(len(isbn13_test)):
    isbn13 = isbnlib.to_isbn13(str(isbn13_test[i]))
    # none replaced by English language
    if isbn13 == "":
        nation = "English language"
    else:
        nation = isbnlib.info(isbn13)
        if nation == "":
            nation = "English language"
    nations_test.append(nation)
test[:, 5] = nations_test


# write to file
train = pd.DataFrame(train)
train.to_csv('./raw_data/Train_data_2.csv', header=train_header, index=None)
test = pd.DataFrame(test)
test.to_csv('./raw_data/Test_data_2.csv', header=test_header, index=None)
print("write file complete!")

