#id 가 8자 이상 확인
#pwd 특수문자 !,@,#,$,% 5개중 무조건 하나가 들어가야됨
id_list = []
pwd_list = []

for i in range(5):
    while True:
        count = 0
        temp_id = input("Enter the your id: ")
        for i in range(len(id_list)):
            if id_list[i] == temp_id:
                count = 1
        if count == 0:
            print("ok id check not overlap")
            break
        print("again try id overlap")

    id_list.append(temp_id)
    temp_pwd = input("Enter the your pwd: ")
    pwd_list.append(temp_pwd)
    print("id pwd make!!!! id : {} pwd {}".format(id_list, pwd_list))