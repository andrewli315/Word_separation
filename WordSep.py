# -*- coding: utf-8 -*-

import jieba
import csv
import sys

def seperate(infile, outfile):
    stopwords = set()
    with open('./stopword.txt', 'r',encoding='utf-8') as data:
        for stopword in data:
            stopwords.add(stopword.strip('\n'))
    output = open(outfile,'w',encoding='utf-8')    
    first = True
    with open(infile, 'r' ,encoding='utf-8') as data:
        csvread = csv.reader(data,delimiter=',')        
        for row in csvread:
            if first == True:
                first = False
                time_index = row.index("post_time")
                content_index = row.index("content")
                continue
            # jieba 
            tmp_words = jieba.cut(row[content_index].replace('\n',''))
            """
                1
                2
                3
                ->
                123
                
            """
            result = []
            ret = row[time_index] + ','
            for word in tmp_words:
                if word not in stopwords:
                    result.append(word)
            ret += ",".join(result)
            output.write(ret+'\n')      
    output.close()


def main(input_file, output_file):
    seperate(input_file, output_file)



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("python3 %s [input file] [output file]" % sys.argv[0] )
        sys.exit()
    main(sys.argv[1], sys.argv[2])

