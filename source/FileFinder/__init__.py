import os
import sys


class FileFinder:

    def __is_extension(self, string: str) -> bool:
        """
        Проверка, что строка представляет собой расширение файла,
        а именно содержит одну точку вначале
        :param string:
        :return:
        """
        return string.count('.') == 1 and string[0] == '.'

    def __is_correct_input_argument(self, arguments) -> bool:
        """
        Проверка, что аргумента командной строки представляет собой расширение
        :return:
        """
        return len(arguments) == 2 and self.__is_extension(arguments[1])

    def __find_in_directory(self, extension: str = 'py', directory: str = ".") -> None:
        """
        Поиск во всех подкаталогах файла с заданным расширением
        :param extension:
        :param directory:
        :return:
        """
        for file_name in os.listdir(directory):
            if f'.{file_name.split(".")[-1]}' == extension:
                self.founded_files.append(f"{directory}/{file_name}")

            if os.path.isdir(f"{directory}/{file_name}/"):
                self.__find_in_directory(extension, f"{directory}/{file_name}")

    def __show_launch_message(self) -> None:
        print(f'\nCurrent directory is:\n{os.getcwd()}\n')

        print(f'extension={self.file_extension}\n')

    def __get_extension_from_args(self, arguments: list) -> str | None:
        """
        Получение расширения файла из аргументов командной строки
        :param arguments:
        :return:
        """

        if len(arguments) > 1:
            return arguments[1]
        else:
            return None

    def __show_error_message(self) -> None:
        """
        Вывод сообщения в случае некорректно переданного формата
        :return:
        """

        if len(sys.argv) > 1:
            print(f'Incorrect file extension {sys.argv[1]}')
        else:
            print(f'need file extension in argument')

    def __show_founded_files(self) -> None:
        """
        Вывод найденных файлов
        :return:
        """

        print(f"Founded {len(self.founded_files)} files")

        for file in self.founded_files:
            print(file)

    def __init__(self, arguments: list):
        self.arguments = arguments
        self.founded_files = []

        if self.__is_correct_input_argument(self.arguments):
            self.file_extension = self.__get_extension_from_args(arguments=arguments)
            self.__show_launch_message()

            self.__find_in_directory(extension=self.file_extension)

            self.__show_founded_files()
        else:
            self.__show_error_message()
