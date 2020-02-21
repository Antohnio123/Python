import itertools


def combo(x,y,z):
    cmb = list(itertools.chain(x,y,z))
    print(cmb)


xx = [1, 2, 3]
yy = [4, 5]
zz = [6, 7]
combo(xx, yy , zz)



###################################################
print()

ll = ['hello', 'i', 'write', 'cool', 'code']


def lessfive(l):
    dl = []
    for i in l:
        if len(i) >= 5:
            dl.append(i)
    print(dl)

lessfive(ll)


###################################################
print()


def psw(ln):
    dl = list(itertools.combinations(ln, 4))
    print(dl)

line = "password"

psw(line)
