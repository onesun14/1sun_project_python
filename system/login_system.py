#id 가 8자 이상 확인
#pwd 특수문자 !,@,#,$,% 5개중 무조건 하나가 들어가야됨
k = 0
id_list = ['aaaaaaaa', 'bbbbbbbb', 'cccccccc', 'dddddddd', 'eeeeeeee']
pwd_list = ['a!a', 'a@a', 'a#a', 'a$a', 'a%a']
while k == 0:
    a = input("sing up or sing in : ")
    if a == 'sing up':
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
    elif a == 'sing in':
        while True:
            count = 0
            b = input('Enter the id : ')
            for i in range(len(id_list)):
                if id_list[i] == b:
                    count += 1
                    break
            if count >= 1:
                print('id를 확인했습니다.')
                break
            if count == 0:
                print("{} 라는 id를 찾지 못했습니다. 다시 한번 시도해주세요".format(b))
        while True:
            count = 0
            c = input('Enter the pwd : ')
            for i in range(len(pwd_list)):
                if pwd_list[i] == c:
                    count += 1
                    break
            if count >= 1:
                print('로그인이 성공적으로 되었습니다.')
                k = 1
                break
            if count == 0:
                print('{} 라는 pwd를 찾지 못했습니다. 다시 한번 시도해주세요'.format(c))
    else:
        print("sing in 이나 sing up 중 선택해주세요")
