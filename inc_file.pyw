from sys import argv
import os
import re
import datetime
import shutil


FILENAME_PATTERN = re.compile(r'(?:\d+ .+ \d{4})\Z')


def clean_name(file_path):
    ''' Take a given path and seperate the path, basename, and extension '''
    base = os.path.basename(file_path)
    path = file_path[:-len(base)]
    (filename, extension) = os.path.splitext(base)
    return (path, filename, extension)


def is_formatted(filename):
    ''' Check if the filename is already formatted with version and date '''
    return FILENAME_PATTERN.match(filename)


def increment(file_path):
    (path, filename, extension) = clean_name(file_path)

    if is_formatted(filename):
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
