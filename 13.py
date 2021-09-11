#id 가 8자 이상 확인
#pwd 특수문자 !,@,#,$,% 5개중 무조건 하나가 들어가야됨
id_list = []
pwd_list = []


for i in range(5):
    while True:
        count = 0
        count1 = 0
        temp_id = input("Enter the your id: ")
        for i in range(len(id_list)):
            if id_list[i] == temp_id:
                count = 1
        if len(temp_id) <= 7:
            count1 = 1
        if count >= 1:
            print("id가 중복되었습니다.")
        if count1 >= 1:
            print("id를 8자 이상으로 적어주세요")
        if count == 0 and count1 == 0:
            print("id가 등록 되었습니다")
            break

    id_list.append(temp_id)
    while True:
        temp_pwd = input("Enter the your pwd: ")
        for h in range(len(temp_pwd)):
            if temp_pwd[h] == "!" or temp_pwd[h] == "@" or temp_pwd[h] == "#" or temp_pwd[h] == "$" or temp_pwd[h] == "%":
                count += 1
                break
        if count >= 1:
            pwd_list.append(temp_pwd)
            print("id와 pwd를 등록했습니다. id : {} pwd {}".format(id_list, pwd_list))
            break
        if count == 0:
            print("pwd에 !,@,#,$,% 가 1개 이상 들어가도록 해주세요")

