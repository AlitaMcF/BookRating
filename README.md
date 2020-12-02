# BookRating

Predict book average rating with some simple models.

### files

* __map.py__: clear data

* __reduce.py__: transform publication_date feature.

   Train_data.csv --> Train_data_1.csv

* __process_isbn13_to_nation.py__: extract nation info from isbn13

   Train_data_1.csv --> Train_data_2.csv

   Test_data.csv --> Test_data_2.csv

* __preprocessing.ipynb__: Code is almost the same as __preprocessing.py__. Transform features language, nation, author, publisher, date with Bayesian Target Encoding.

   Train_data_2.csv --> train_processed_language_author_publisher_nation_date.csv

   Test_data_2.csv --> test_processed_language_author_publisher_nation_date.csv
   
* __date_score_relation.py__: used to plot date graph.

* __plot.py__: plot some other graph.


### Preprocessing Steps

1. Run `python map.py | reduce.py`
2. Run `python process_isbn13_to_nation.py`
3. Run `python preprocessing.py`

Then, you can get processed files under `processed_file` direction.

### Preprocessing detail

#### Clear data

Use mapreduce to clear the noise and transform the date feature.

#### Feature selection

1. __author__

   The authors feature is string type data. According to the experience, author is an important aspect which can affect the rating score significantly. Every single book may have several different authors. So, when we select authors as one of the necessary features, the impact of author number should be considered. According to our preprocessing, there are 8442 different authors in training data.

2. __isbn13__

   The feature isbn13 contains some implicit information, such as nation, language and publisher. Nation and language is related to the existing feature language_code, and publisher is already existing in our raw data. So, isbn13 will be abandoned.

3. __language__

   Language_code is a related feature to the final average rating. It's also a string type feature, so we need to transform it into numeric value before utilizing it. There are 26 different languages in training data, and their average rating are shown below.
   ![language average score](https://github.com/AlitaMcF/BookRating/blob/master/chart/lang_avg_rating.png)
   We see that there are some gaps between the average rating of different languages. So, language can be a useful feature for us to predict the test data.

4. __num_pages__

   According to experience, the page number of a book can affect its rating score to some extent. Therefore, it's useful in our prediction models. Before using this feature, we should normalize it and other features into the same magnitude.
   
5. __ratings_count__

   The ratings_count feature can also affect the average rating of a book. As we known, if the rating count is too small, the book's rating score is easier to be extreme, such as near 0 or near 5. Thus, we regard ratings_count as a useful feature to predict the book average rating.
   
6. __text_review_count__

   Text review is always related to the rating level. We will not abandon it here. The value of text_review_count may be too big when compared with some other numeric feature, so the normalization step is necessary.
   
7. __publication_date__

   Publication_date is a date data. In order to confirm whether it can be useful for our models or not, we plot the total date data with rating score. It's shown as follow.
   ![general data rating](https://github.com/AlitaMcF/BookRating/blob/master/chart/generl_date_score.png)
   We cannot detect any useful information. Because the average rating is almost steady from begin to the end. But it may be existing some implicit period information. so we plot the month average rating from year 2000 to 2004. As shown below.
   ![2000-2004 month average rating](https://github.com/AlitaMcF/BookRating/blob/master/chart/2000-2004_month_score.png)
   Unfortunately, we still cannot observe period mode from figure 3. So we decided to abandon publication_date feature in the end.
   
8. __publisher__

   The publisher feature is similar to authors. There may be several publishers take in charge one book. So we need to consider the effect of publisher number. According to our preprocessing, there are 2130 different publishers in training data.
   
9. __isbn__

   Just abandon it since there is isbn13 here.
   
10. __bookID__

    Abandon.
   
11. __title__

    Abandon.
   
##### Brief summary

The features we used here are authors, language_code, num_pages, ratings_count, text_review_count and publisher. And the normalization step is necessary. The encoding method we used in string type data is __Bayesian Target Encoding__.

### Models

1. Linear Regression
2. Decision Tree
3. MLP
4. AdaBoost
5. Bagging with MLP
6. SVR
7. Random Forest

### Performance

Based on 10-fold cross validation.

![performance](https://github.com/AlitaMcF/BookRating/blob/master/chart/MSE_models.png)

### Feature importance

Based on Random Forest model. RF model can explore the importance of features.

![features importances](https://github.com/AlitaMcF/BookRating/blob/master/chart/feature_importance.png)

