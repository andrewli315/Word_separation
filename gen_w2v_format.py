import sys

def gen_file(inputfile, outputfile):
    out = open(outputfile, 'w' , encoding='utf-8')
    with open(inputfile, 'r', encoding='utf-8') as data:
        for line in data:
            first = True
            row = line.split(',')
            for word in row:
                if first is True:
                    first = False
                    continue
                out.write(word.strip('\n') + ' ')
    out.close()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit()
    gen_file(sys.argv[1], sys.argv[2])
