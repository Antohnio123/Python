import os
def copyfile(sourse :str, destination :str) :
    try:
        with open(sourse,'r') as file :
            d = file.read()
        if os.path.exists(destination) is True:
            raise FileExistsError
        with open(destination,'w') as file :
            file.write(d)
    except FileExistsError :
        print( "Error file exists")
    except FileNotFoundError :
        print("Error file not found")

s = "C:/Users/OVD/PycharmProjects/Course Phyton/file_test.txt"
d = "C:/Users/OVD/PycharmProjects/Course Phyton/d_file_test.txt"
copyfile(s,d)