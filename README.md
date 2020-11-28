# BookRating
Predict book average rating.

### Preprocessing

#### file

1. map.py 清洗 reduce.py 处理格式  Train_data.csv  --> Train_data_1.csv

2. process_isbn13_to_nation.py   isbn13提取国家 

   Train_data_1.csv --> Train_data_2.csv

   Test_data.csv --> Test_data_2.csv

3. Preprocessing.ipynb  用贝叶斯平均处理language,nation,author, publisher 

   Train_data_2.csv --> train_processed_language_author_publisher_nation.csv

   Test_data_2.csv -->  test_processed_language_author_publisher_nation.csv

#### Steps

1. 运行 python map.py|python reduce.py
2. 运行process_isbn13_to_nation.py
3. 运行preprocessing.ipynb





#### Outline
1. num_page: do nothing
2. Rating count: do nothing
3. text review: do nothing
4. ISBN: 舍弃，因为其中包含的语言跟出版社信息已经在数据中了
5. ISBN13: 舍弃
6. title: 舍弃
7. author: target encoding
8. Language: one-hot encoding或者target encoding
9. publisher: target encoding
10. 日期：可视化然后观察是否有周期或趋势，if yes, 提取date_of_month, date_of_week, date_of_year等数据; if not, 舍弃
11. bookid: 舍弃

#### Detail
1. Target Encoding在本Proj的应用中目前最优选择可能是Bayesian Target Encoding，Bayesian Mean的本质就是考虑了smoothing.
2. author: 每本书的author可能有好几个，对于train set与test set，我们只用train set中数据计算出的encoding来映射test set中的数据。对于有多个作者的情况，就把所有作者的书考虑进去求平均，对于test集中author的缺失值，用所有作者的平均分来替代
3. language: 处理思路同author，利用train set中的Bayesian Meaning来编码language feature.
