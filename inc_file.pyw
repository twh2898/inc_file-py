from sys import argv
import os
import re
import datetime
import shutil


FILENAME_PATTERN = re.compile(r'(?:(\d+) (.+) \d{4})\Z')


def clean_name(file_path):
    ''' Take a given path and seperate the path, basename, and extension '''
    base = os.path.basename(file_path)
    path = file_path[:-len(base)]
    (filename, extension) = os.path.splitext(base)
    return (path, filename, extension)


def is_formatted(filename):
    ''' Check if the filename is already formatted with version and date '''
    return FILENAME_PATTERN.match(filename) != None


def increment_filename(file_path):
    '''
    Return the new file_path with the filename formatted and incremented

    If the filename in the path is already formated as <version> <name> <date>
    this method will increment version and replace date with the current date.
    If the filename is not already formatted, this method will use the entire
    basename for the file as name, set version to 1, and use the current date.
    '''
    (path, filename, extension) = clean_name(file_path)
    matches = FILENAME_PATTERN.match(filename)

    if matches and len(matches.groups()) == 2:
        version = int(matches.group(1)) + 1
        filename = matches.group(2)
    else:
        version = 1

    date = datetime.date.today().strftime("%m%d")
    return '%s%d %s %s%s' % (path, version, filename, date, extension)


def main():
    ''' Main method '''
    if len(argv) < 2:
        print 'Please enter a file path as an argument'
        return

    new_file = increment_filename(argv[1])
    shutil.copy2(argv[1], new_file)


if __name__ == '__main__':
    main()
