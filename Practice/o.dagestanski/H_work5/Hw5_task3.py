from tempfile import mktemp
from os import remove
class WrapStrToFile(object) :
    def __init__(self):
        self.filepath = mktemp("txt","tempfile")
    @property
    def content(self):
        try :
            file = open(self.filepath,"r")
            outdata = file.read()
            file.close()
            self._content = " OutData: {}".format(outdata)
        except IOError :
            self._content = "File does not exist."
        return self._content

    @content.setter
    def content(self, value):
        file = open(self.filepath, "w")
        file.write(value)
        file.close()

    @content.deleter
    def content(self):
        remove(self.filepath)

wstf = WrapStrToFile()
print(wstf.content)
wstf.content = "test_str"
print(wstf.content)
wstf.content = "text 2"
print(wstf.content)
del wstf.content
print(wstf.content)