id_list = ['aaaaaaaa', 'bbbbbbbb', 'cccccccc']
pwd_list = ['A!', 'B@', 'A!']
count = 0
temp_id = input("Enter the your id: ")
while True:
    for i in range(len(id_list)):
        if temp_id != id_list[i]:
            count = 1
            break
    if count >= 1:
        

temp_pwd = input("Enter the your pwd: ")