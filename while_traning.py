password = 'a123456'

i = 3 #次數
while i > 0:
    i = i - 1
    password2 = input('請輸入密碼:')
    if password2 == password:
        print('登入成功!')
        break #跳出迴圈
    else:
        print('密碼錯誤!')
        if i > 0:
            print('還有', i, '次機會')
        else:
            print('你沒機會了!鎖你帳號!')
        



