#�����, ��� �������� �� ���)

def tabtospaces(filename, n):#������ ��������� �� �������
    file = open(filename, 'r')
    data = file.read()
    file.close()
    file = open(filename, 'w')
    file.write(data.expandtabs(tabsize = n))
    file.close()

def spacestotab(filename, n):#������ �������� �� ���������
    file = open(filename, 'r')
    data = file.read()
    file.close()
    file = open(filename, 'w')
    file.write(data.replace(' ' * n,'   '))
    file.close()