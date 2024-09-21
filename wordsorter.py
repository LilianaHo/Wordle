import sys

# simple word sorter
def sort_txt(filename, outputname):
    words = str(filename)
    word_list = []
    with open(words) as f:
        count = sum(1 for _ in f)
    with open(words) as f:
        for _ in range(count):
            line = f.readline()[:5]
            word_list.append(line)
    word_list.sort()
    with open(outputname, "w") as f:
        for i in range(len(word_list)):
            f.write(str(word_list[i]))
            if i < len(word_list) - 1:
                f.write("\n")


if __name__ == '__main__':
    input = str(sys.argv[1])
    output = str(sys.argv[2])
    sort_txt(input, output)