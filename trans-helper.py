# use this on an English source file to generate template file
import sys
import os
import glob
import xml.etree.ElementTree as ET

if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " <file or folder path>.")
    sys.exit()

num_file = 0


def prepare_for_trans(filepath):
    with open(filepath, "r+") as f:
        filebuff = f.readlines()
        f.seek(0)
        for line in filebuff:
            try:
                root = ET.fromstring(line)
                leading_spaces = len(line) - len(line.lstrip())
                f.write(" " * leading_spaces)
                f.write("<!-- " + root.text + " -->\n")
                f.write(" " * leading_spaces)
                f.write("<" + root.tag + "></" + root.tag + ">\n")
            except:
                f.write(line)
        f.truncate()


def generate_xls(filepath):
    pass


def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename, os.path.join(
            dir, titlePattern % title + ext))


def process_file(filepath):
    global num_file
    if '*' in filepath:
        new_name = filepath.replace('*', '_')
        os.rename(filepath, new_name)
        print(new_name)
    # prepare_for_trans(filepath)
    # generate_xls(filepath)
    num_file += 1


# argument can be file or directory
#
# if dir
if os.path.isdir(sys.argv[1]):
    for path, subdirs, files in os.walk(sys.argv[1]):
        for name in files:
            filepath = os.path.join(path, name)
            process_file(filepath)
# if file
elif os.path.isfile(sys.argv[1]):
    process_file(sys.argv[1])
else:
    print("File or foler not found")

print("File processed:", num_file)
