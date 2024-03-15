import csv

def read_csv_file(csvpath, delimiter=','):
    ''' read a csv file and return list of lines'''

    lines = []

    with open(csvpath) as csvfp:
        csvfp = csv.reader(csvfp, delimiter=delimiter)
        for line in csvfp:
            lines.append(line)

    return lines

def csv_to_dict(csvpath, delimiter=','):
    ''' read a cvs file and return dict with values in list '''

    csv_dict = {}

    lines = read_csv_file(csvpath, delimiter=delimiter)

    columns = lines[0]

    for line in lines[1:]:
        name = line[0]
        csv_dict[(columns[0],name)] = []
        for index,data in enumerate(line[1:], start=1):
            csv_dict[(columns[0],name)].append({columns[index] : data})

    return csv_dict

def dict_to_csv(csv_dict, csvpath, delimiter=','):
    ''' wrtie dict to csvpath with specified delimiter '''

    # {'sitaram1': [{'nam': 'sitaram'}, {'dham': 'ayodhya'}, {'leela': 'ramleela'}, {'katha': 'ramayan'}],
    columns = []
    data = []
    for key,value in csv_dict.items():
        if columns == []:
            columns.append(key[0])
            for item in value:
                columns.append(list(item)[0])

        row = [key[1]]
        for item in value:
            row.append(list(item.values())[0])
        data.append(row)

    columns = delimiter.join(columns)
    data = [delimiter.join(row) for row in data]

    with open(csvpath, 'w') as fp:
        fp.write(columns + '\n')
        for row in data:
            fp.write(row + '\n')

    return csvpath