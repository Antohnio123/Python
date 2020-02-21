import tempfile
import os


class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp()

    @property
    def content(self):
        try:
            tmp_file = open(self.filepath, "r")
            tmp_filecont = tmp_file.read()
            tmp_file.close()
            return tmp_filecont
        except FileNotFoundError:
            return "Файл не существует"

    @content.setter
    def content(self, value):
        try:
            tmp_file = open(self.filepath, "w")
            tmp_file.write(value)
            tmp_file.close()
        except FileExistsError:
            return "Ошибка записи. Файл не существует"

    @content.deleter
    def content(self):
        os.remove(self.filepath)

wstf = WrapStrToFile()
print(wstf.content) # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content) # Output: test_str
wstf.content = 'text 2'
print(wstf.content) # Output: text 2
del wstf.content # после этого файла не существует