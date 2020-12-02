import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

train = pd.read_csv('raw_data/Train_data.csv')
train_header = train.columns
train = np.array(train)

score = train[:, 3]
date = train[:, -2]
print("original date: ", date)
print("score: ", score)


def draw_graph(xlist, ylist, show_xlabel):
    plt.figure()
    plt.title('date and score')
    plt.xlabel("date")
    plt.ylabel("score")
    plt.plot(xlist, ylist)
    if show_xlabel:
        plt.xticks(rotation=-75)
    else:
        plt.xticks((), rotation=-75)
    plt.show()


def date_score_mapping(date):
    """
    :param date: extracted from original date
    :return:
    """

    date_count = Counter(date)
    date_count = dict(date_count)
    date_count = sorted(date_count.items())
    date_count = dict(date_count)
    print("count of date: ", date_count)

    date_total_score = {}
    for i in range(len(date)):
        if date_total_score.get(date[i], -1) == -1:
            date_total_score[date[i]] = score[i]
        else:
            date_total_score[date[i]] += score[i]
    date_total_score = dict(sorted(date_total_score.items()))
    print("total score of date:", date_total_score)

    date_avg_score = {}
    for key, value in date_total_score.items():
        date_avg_score[key] = value / date_count[key]
    print("date_avg_score: ", date_avg_score)

    # draw graph
    xlist = list(date_avg_score.keys())  # [-12:]
    ylist = list(date_avg_score.values())  # [-12:]
    draw_graph(xlist, ylist, show_xlabel=False)


def plot_interval(date, start, end):
    date_count = Counter(date)
    date_count = dict(date_count)
    date_count = sorted(date_count.items())
    date_count = dict(date_count)
    print("count of date: ", date_count)

    date_total_score = {}
    for i in range(len(date)):
        if date_total_score.get(date[i], -1) == -1:
            date_total_score[date[i]] = score[i]
        else:
            date_total_score[date[i]] += score[i]
    date_total_score = dict(sorted(date_total_score.items()))
    print("total score of date:", date_total_score)

    date_avg_score = {}
    for key, value in date_total_score.items():
        date_avg_score[key] = value / date_count[key]
    print("date_avg_score: ", date_avg_score)

    # plot
    whatineed_score = []
    whatineed_date = []
    keys = date_avg_score.keys()
    for key in keys:
        if start <= int(key.split('/')[0]) <= end:
            whatineed_score.append(date_avg_score[key])
            whatineed_date.append(key)
    print(whatineed_score)
    print(whatineed_date)
    draw_graph(whatineed_date, whatineed_score, show_xlabel=True)


if __name__ == '__main__':

    year_month = [d.split("/")[2] + "/" + d.split("/")[0] for d in date]
    months = [d.split("/")[0] for d in date]

    # method 1
    # 1900/1, 1900/2, ... ,2020/1, 2020/2
    date_score_mapping(year_month)

    # # method 2
    # # 1,2,3,...,12
    # date_score_mapping(months)

    # draw month score from 2000 to 2004
    plot_interval(year_month, 2000, 2004)

