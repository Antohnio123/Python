from tempfile import mktemp
from os import remove


class WrapStrToFile:

    def __init__(self):
        self.filepath = mktemp(".txt", "temporary")#Deprecated since version 2.3: Use mkstemp() instead.
#Для tempfile.mkstemp, который создаёт файл и возвращает кортеж из файлового дескриптора и пути до файла
#реализацию придумать не смог


    @property
    def content(self):
        try:
            file = open(self.filepath, "r")
            data = file.read()
            file.close()
            return "Output: {}".format(data)
        except IOError:
            return "Output: File doesn't exist"


    @content.setter
    def content(self, value):
        file = open(self.filepath, "w")
        file.write(value)
        file.close()
        return file

    @content.deleter
    def content(self):
        remove(self.filepath)


wstf = WrapStrToFile()
print(wstf.content)#file doesn't exist
wstf.content = 'test str'
print(wstf.content)#test str
wstf.content = 'text 2'
print(wstf.content)#text 2
del wstf.content
print(wstf.content)#file doesn't exist