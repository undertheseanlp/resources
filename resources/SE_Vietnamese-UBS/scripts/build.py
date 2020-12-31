from os.path import realpath, dirname, join
import os
import shutil


# build TC_Vietnamese-UBC
def convert_file(infile, outfile):
    def convert_line(line):
        tokens = line.split(" ")
        for i, token in enumerate(tokens):
            if token.startswith("__label__"):
                label = token.split("#")[0]
                tokens[i] = label
        line = " ".join(tokens)
        return line

    lines = open(infile).read().splitlines()
    lines = [convert_line(line) for line in lines]
    output = "\n".join(lines)
    with open(outfile, 'w') as f:
        f.write(output)


FOLDER = dirname(dirname(realpath(__file__)))
CORPUS_FOLDER = join(FOLDER, "datasets", "TC_Vietnamese-UBC")
shutil.rmtree(CORPUS_FOLDER, ignore_errors=True)
os.makedirs(CORPUS_FOLDER)
convert_file(join(FOLDER, "corpus", 'train.txt'), join(CORPUS_FOLDER, 'train.txt'))
convert_file(join(FOLDER, "corpus", 'test.txt'), join(CORPUS_FOLDER, 'test.txt'))
