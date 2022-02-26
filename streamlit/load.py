from glob import glob
files = glob("./josa/*.txt")
id = []
n = 0
for file in files:
    f = open(file, 'r')
    lines = f.readlines()
    #print(lines)
    for line in lines:
        temp = line.split(':')
        print(temp[1])


#f = open("{}.txt".format(str(len(flies) + 1)), "w")


#평균 구해서 하는거 갯수나
#예시로는 남자는 몇명이고 여자는 몇명이다. 같은 개념으로 말이다.
