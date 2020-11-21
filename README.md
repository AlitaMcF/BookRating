# BookRating
Predict book average rating.

### Preprocessing
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
3. language
