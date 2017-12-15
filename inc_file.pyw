from sys import argv
from os.path import splitext, basename
import datetime
import shutil


def clean_name(file_path):
    base = basename(file_path)
    path = file_path[:-len(base)]
    (filename, extension) = splitext(base)
    return (path, filename, extension)


def increment(file_path):
    (path, filename, extension) = clean_name(file_path)

    if filename.count(' ') > 1:
        try:
            version = int(filename[:filename.index(' ')]) + 1
            old_date = int(filename[filename.rindex(' ') + 1:])
            filename = filename[filename.index(
                ' '):filename.rindex(' ')].strip()
        except:
            version = 1
    else:
        version = 1

    today = datetime.date.today()
    date = today.strftime("%m%d")
    return "%s%d %s %s%s" % (path, version, filename, date, extension)


def main():
    if len(argv) < 2:
        print 'Please enter a file path as an argument'
        return

    new_file = increment(argv[1])
    shutil.copy2(argv[1], new_file)


if __name__ == '__main__':
    main()
