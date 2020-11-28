import sys
import time
import datetime
import csv
import isbnlib


def isDateValid(date):
    """
    testify if the date is true
    :param date: str "month/day/year"
    :return: str
    """
    monthdict = {"1": "31", "2": "29", "3": "31", "4": "30", "5": "31", "6": "30",
             "7": "31", "8": "31", "9": "30", "10": "31", "11": "30", "12": "31"}
    datelist = date.split("/")
    month = datelist[0]
    day = datelist[1]
    year = datelist[2]
    if month != "2":
        if int(day) <= int(monthdict[month]):
            return date
        else:
            day = monthdict[month]
    else:
        if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
            if int(day) < 29:
                return date
            else:
                day = "29"
        else:
            if int(day) < 28:
                return date
            else:
                day = "28"
    return month + "/" + day + "/" + year


def writeCSV(row):
    name = "./raw_data/Train_data_1.csv"
    with open(name, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["bookID", "title", "authors",
                         "average_rating", "isbn", "isbn13",
                         "language_code", "num_pages",
                         "ratings_count", "text_reviews_count",
                         "publication_date", "publisher"])
        # row = [['1', 1, 1], ['2', 2, 2], ['3', 3, 3]]
        for r in row:
            writer.writerow(r)
    print("Write file complete!")


def Reduce():
    pre_key = ""
    output = []
    for line in sys.stdin:
        data = line.split("--")
        key = data[0]

        if data[1] == "average_rating":
            value = float(data[2].strip())

        elif data[1] == "num_pages" \
                or data[1] == "ratings_count" \
                or data[1] == "text_reviews_count":
            value = int(float(data[2].strip()))

        elif data[1] == "publication_date":
            date_modified = isDateValid(data[2])
            timeArray = time.strptime(date_modified.strip(), '%m/%d/%Y')
            timeStamp = int(time.mktime(timeArray))
            value = timeStamp

        elif data[1] == "isbn"or data[1] == "isbn13":
            if data[2].strip()[-1] != "X" and data[2].strip()[-1] != "x":
                value = str(int(float(data[2].strip())))
            else:
                value = str(data[2].strip())

        # elif data[1] == "isbn13":
        #     data[2] = isbnlib.to_isbn13(str(data[2].strip()))
        #     # none replaced by English language
        #     if data[2] == "":
        #         value = "English language"
        #     else:
        #         nation = isbnlib.info(str(data[2].strip()))
        #         if nation == "":
        #             value = "English language"
        #         else:
        #             value = nation

        # elif data[1] == "title" \
        #         or data[1] == "authors" \
        #         or data[1] == "publisher":
        #     # address garbled character
        #     value = data[2].replace("?", "").replace("�", "")

        else:
            value = data[2].strip()

        if pre_key != key:
            if pre_key != "":
                output.append(valuelist)
            pre_key = key
            valuelist = []
            valuelist.append(pre_key)

        valuelist.append(value)

    # print(output)
    print("Processing complete!")
    writeCSV(output)


Reduce()
