import csv


def Map():
    name = "raw_data/Train_data.csv"

    with open(name, 'r') as f:
        reader = csv.reader(f)
        nrows = list(reader)
        header = nrows[0]
        for i in range(1, len(nrows)):
            rows = nrows[i]

            # 1. delete some dirty data
            # missing attributes
            if rows[-1] == "":
                continue

            # rating_count = 0 while average_rating != 0
            if 0 < float(rows[3]) <= 5 and int(rows[8]) == 0:
                continue

            # pages = 0
            if int(rows[7]) == 0:
                continue

            # garbled character
            if "�" in str(rows[1]) or "�" in str(rows[2]) or "�" in str(rows[-1]):
                continue

            # 2. split record into key-value
            for index in range(1, 12):
                pair = str(int(rows[0])).strip() + "--" + header[index].strip() + "--" + str(rows[index]).strip()
                # output.append(pair)
                print(pair)

Map()






