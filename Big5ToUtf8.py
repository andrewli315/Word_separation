
import sys

def Big5ToUtf8(input_file, output_file):

	out = open(output_file, 'w', encoding='utf-8')
	with open(input_file, 'r', encoding='big5') as data:
		for line in data:
			out.write(line)
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage :")
		print("python3 %s [input_file] [output_file]", sys.argv[0])
		sys.exit()
	Big5ToUtf8(sys.argv[1], sys.argv[2])