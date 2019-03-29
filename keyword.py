import jieba.analyse
import csv
import sys
from collections import OrderedDict

def word_count(input_file, output_file):
    wordcount = {}
    outfile = open(output_file, 'w', encoding='utf-8')
    with open(input_file, 'r', encoding='utf-8') as data:
        for line in data:
            words = line.split(' ')
            for word in words:
                try:
                    wordcount[word] = wordcount[word] + 1
                except:
                    wordcount[word] = 1
    sorted_result = OrderedDict(sorted(wordcount.items(), key=lambda x: x[1]))
    for key, value in sorted_result.items():
        outfile.write(key + '\t' + str(value) + '\n')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage :")
        print("python3 %s [input file] [output file]" % sys.argv[0])
        sys.exit()
    word_count(sys.argv[1],sys.argv[2])
