# Word Separation
Using Jieba to separate words of paragraph

## Getting started
Using **WodSep.py**, the file must be csv file.
I use the column name with **post_time** and **content** to get index of the column content.
### Usage
```
# convert big5 encoding file to utf-8 file
python3 Big5ToUtf8.py [input file] [output file]

# word separation
python3 WordSep.py [input file] [output file]

# generate the file for word2vec and keyword.py
python3 gen_w2v_format.py [input file] [output file]

# count words in file
python3 keyword.py [input file] [output file]

```

## Author
* **AndrewLi** 

## License
This project is licensed under the MIT License
