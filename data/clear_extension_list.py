"""
    Список расширений взят с сайта:
    https://www.celitel.info/klad/rasch.htm

    31.08.2023
"""

import os


def get_cleaned_files(input_file_name: str) -> None:
    """
    Считывание информации из файлов с расширениями и запись их в другие файлы
    :param input_file_name:
    :return:
    """
    with open(input_file_name, "r", encoding='utf-8') as input_file:
        with open("extensions.csv", "w", encoding='utf-8') as csv_file:
            with open("extensions_list.txt", "w", encoding='utf-8') as output_file:
                for i, line in enumerate(input_file):
                    data = line.split()
                    extension = data[0]
                    description = "".join(data[:-1])

                    output_file.write(f"{extension}\n")
                    csv_file.write(f"{extension};{description}\n")


if __name__ == '__main__':
    get_cleaned_files("extensions_dirty.txt")
