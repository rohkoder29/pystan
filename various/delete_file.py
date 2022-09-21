'''
A minimal script to delete files whose paths are stored in a provided source file.
'''

__author__ = 'rohkoder'
__version__ = '0.1.0'
__license__ = 'MIT'

# imports
from genericpath import exists
from os import remove, unlink
from sys import argv

def main() -> None:
    '''  '''
    try:
        file_path = argv[-1]
        print(f"(Processing file) '{file_path}'")
        with open(file_path, "r", encoding="utf-8") as stream:
            paths = stream.readlines()
        for path in paths:
            if not exists(path.strip()):
                print(f"File '{path.strip()}' does not exist so not deleted.")
                continue
            unlink(path.strip())
            print(f"File '{path.strip()}' deleted!")
    except FileNotFoundError:
        print(f"[ERROR] We were unable to find the file '{file_path}'.")
    except PermissionError:
        print(f"[ERROR] You have no permission to delete the file '{path.strip()}'.")
    except OSError:
        print(f"[ERROR] File '{path.strip()}' is a read-only file system.")
    else:
        del_source_file = input("Would you like to delete the source file as well? [Y/N] ")
        if del_source_file in ["Y", "y"]:
            remove(file_path)
            print(f" File '{file_path}' deleted!")


if __name__ == '__main__':
    main()
