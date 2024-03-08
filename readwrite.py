# module will provide function to operate on files

import os
import re

from collections import defaultdict
from collections import Counter

import csv
import fileinput

def read_text_file(filepath):
    ''' read a text file and return list of lines'''
    lines = []
    with open(filepath) as fp:
        for line in fp:
            lines.append(line)

    return lines


def read_csv_file(csvpath, delimiter=','):
    ''' read a csv file and return list of lines'''

    lines = []

    with open(csvpath) as csvfp:
        csvfp = csv.reader(csvfp, delimiter=delimiter)
        for line in csvfp:
            lines.append(line)

    return lines

def read_excel_file(excelpath):
    ''' read a excel file '''
    pass

def write_text_file(filepath):
    ''' write a text file '''
    pass

def write_csv_file(csvpath):
    ''' write a csv file '''
    pass

def write_excel_file(excelpath):
    ''' write a excel file '''
    pass

def count_words_in_line(line, delimiter=' '):
    ''' return count of words in a line '''
    count = 0
    words = line.split(delimiter)
    for word in words:
        word = word.strip()
        if len(word) > 0:
            count += 1

    return count


def words_with_count_in(line, delimiter=' '):
    ''' return count with words in a line '''

    words_with_count = defaultdict(int)

    words = line.split(delimiter)
    for word in words:
        word = word.strip()
        if len(word) > 0:
            words_with_count[word] += 1

    return words_with_count

def words_with_count_from_list(words):
    ''' return count with words from a list '''

    words_with_count = defaultdict(int)

    for word in words:
        word = word.strip()
        if len(word) > 0:
            words_with_count[word] += 1

    return words_with_count


def count_words_in_file(filepath, delimiter=' '):
    ''' return count of words in a file '''

    word_count = 0

    with open(filepath) as fp:

        for line in fp:
            count = count_words_in_line(line, delimiter=delimiter)
            word_count += count

    return word_count


def words_with_count_from(filepath, delimiter=' ', counter=True):
    ''' return count with words from a file '''

    words_with_count = Counter({}) if counter else {}

    with open(filepath) as fp:

        for line in fp:
            line_words_with_count = words_with_count_in(line, delimiter=delimiter)

            if counter:
                words_with_count += Counter(line_words_with_count)

            else:
                for word in list(line_words_with_count):
                    if word in words_with_count:
                        words_with_count[word] = words_with_count[word] + line_words_with_count[word]
                    else:
                        words_with_count[word] = line_words_with_count[word]

    return words_with_count


def count_words_in_csv(csvpath, delimiter=','):
    ''' count words in a csv file '''

    word_count = 0

    with open(csvpath) as csvfp:

        csvfp = csv.reader(csvfp, delimiter=delimiter)

        for line in csvfp:
            count = len(line)
            word_count += count

    return word_count


def words_with_count_from_csv(csvpath, delimiter=',', counter=True):
    ''' return words with count from csv file '''

    words_with_count = Counter({}) if counter else {}

    with open(csvpath) as csvfp:

        csvfp = csv.reader(csvfp, delimiter=delimiter)

        for line in csvfp:
            line_words_with_count = words_with_count_from_list(line)

            if counter:
                words_with_count += Counter(line_words_with_count)

            else:
                for word in list(line_words_with_count):
                    if word in words_with_count:
                        words_with_count[word] = words_with_count[word] + line_words_with_count[word]
                    else:
                        words_with_count[word] = line_words_with_count[word]

    return words_with_count


def read_files_with_fileinput(filepaths):
    with fileinput.input(files=filepaths) as fp:
        # first io stream will be taken as fp and all lines printed.
        # then next io stream will be taken as fp and its all lines printed.
        for line in fp:
            print(line)


def read_line_by_seek(filepath, seekcount=0):
    # fp.seek : will change pointer by position
    # fp.tell : will return current pointer by position
    with open(filepath) as fp:
        print('os.SEEK_CUR', os.SEEK_CUR)
        print('os.SEEK_SET', os.SEEK_SET)
        print('os.SEEK_END', os.SEEK_END)

        fp.seek(seekcount)

        print('os.SEEK_CUR', os.SEEK_CUR)

        current_pos = fp.tell()

        print('current pos by fp.tell()' , current_pos)

        for line in fp:
            print(line)


def replace_word_in_file(filepath, word, rplword):
    # loading whole content in memory
    with open(filepath, 'r') as fp:
        content = fp.read()

    replaced = re.subn(word, rplword, content)

    if replaced[1] > 1:
        content = replaced[0]
        with open(filepath, 'w+') as fp:
            fp.write(content)


def replace_word_in_iterator(filepath, word, rplword):
    # read an replace a word in file all location without loading in memory
    replace_count = 0
    pattern = re.compile(word)
    with open(filepath, 'r+') as fp:
        END_FILE_FLAG = False
        while not END_FILE_FLAG:
            current_pos = fp.tell()
            line = fp.readline()

            replaced = pattern.subn(rplword, line)
            if replaced[1] > 0:
                fp.seek(current_pos)
                fp.writelines([replaced[0]])
                replace_count += replaced[1]

            next_pos = fp.tell()

            if current_pos == next_pos:
                END_FILE_FLAG = True

    return replace_count

def read_csv_file2(csvpath, delimiter=','):
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









