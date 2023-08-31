"""
    Script for getting list of file with current extensions_dirty.txt in current directory and subdirectories

    Pavel Klimovskoy
    31.08.2023
"""

import sys
from FileFinder import FileFinder

if __name__ == '__main__':
    FileFinder(arguments=sys.argv)
