import subprocess, os
def TypeMyFile(com_win  = "type ", filepath = "file_test.txt") :
    try:
        args = com_win + filepath
        subprocess.run(args,shell = True, encoding='utf-8',text = True)
        content= '0'
    except IOError:
        content = "File does not exist."
    return content

myfile = "file_test.txt"
com_w = "type "
print(TypeMyFile(com_w, myfile))
