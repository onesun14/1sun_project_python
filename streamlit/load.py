from glob import glob
id = input("enter the id:")
ps = input("enter the ps:")
path = "./josa/"
load = glob("./josa/{}_{}.txt".format(id, ps))
if load != "":

    f = open(path+"{}_{}.txt".format(id, ps), 'r')

    lines = f.readlines()
    for i in range(len(lines)):
        print(lines[i])
    f.close()
elif load == "":
    print("사용자를 찾을 수 없습니다.")

#평균 구해서 하는거 갯수나
#예시로는 남자는 몇명이고 여자는 몇명이다. 같은 개념으로 말이다.