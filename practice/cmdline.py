# command line args : sys module, getopt module , argsparse module
# getopt module : this module works in combination of sys module. not very good.
# argsparse module : best for command line arguments.

import sys
import re
import argparse

# returns list of arguments passed from command starting from filename
# it does not put any restriction. just append all space separted values in list.
# parse sys.argv at your will. it can contain any number of unique or duplicate args.
# you can pass any style of arguments. not efficient.
args = sys.argv
print(args)


# argsparse module

# initialize parser
parser = argparse.ArgumentParser()
print(parser)
parser.add_argument('-p', '--pattern', help='pattern to search')
print(parser)
args = parser.parse_args()
print(args)

sentence = "amit=20 with sachin=20 with and or rajkumar=90 junior with rajesh=837"
all_values = re.findall("(\w+)=(\d+)", sentence) # return all non-overlapping matches of pattern in string, as a list of strings or tuples
print(all_values) # [('amit', '20'), ('sachin', '20'), ('rajkumar', '90'), ('rajesh', '837')]

sentence = "sitaram sitaram sitaram kahiye jako vidhi rakhe ram sitaram kahiye"
all_values = re.findall("sitaram|ram", sentence)
print(all_values) # ['sitaram', 'sitaram', 'sitaram', 'ram', 'sitaram']

sentence = "sitaram sitaram sitaram kahiye jako vidhi rakhe ram sitaram kahiye"
all_values = re.search("sitaram|ram", sentence) # scan for first occurance
print(all_values.group()) # sitaram

sentence = "sitaram sitaram sitaram kahiye jako vidhi rakhe ram sitaram kahiye"
all_values = re.match("ram", sentence) # scan for start only. it will not find ram.
print(all_values) # None








