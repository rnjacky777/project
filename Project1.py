import os ,json ,time
with open('account.json','r') as f:
    data = json.load(f)

print(data["accountlist"])
while True:
    login = False
    print('1.login')
    print('2.Create new account')
    print('3.exit')
    try:
        a = int(input())
    except:
        pass
    if a != 1 and a != 2 and a != 3:
        print('please enter 1 or 2')
        continue
        
    if a == 1:
        while True:
            print('Input your username')
            account = input('')
            if account in data["accountlist"]:
                print('it is ok')
                pass
            else:
                print('Unknown account,please input account again')
                continue
            print('Input your password')
            password = input('')
            if password == data["accountlist"][account]:
                login = True
                print('login')
                break
            else:
                print('wrong')
                continue
    elif a == 2:
        while True:
            print('input username you want to create')
            account = input()
            if account in data["accountlist"]:
                print('This username has been used')
                continue
            print('This username can be used')
            while True:
                print('enter the password')
                password = input()
                print('enter the password again')
                password2 = input()
                if password != password2:
                    print('Your password is not the same')
                    continue
                else:
                    data["accountlist"][account] = password
                    f=  open('account.json','w')
                    
                    json.dump(data,f)
                    
                    f.close()
                    break
            break
    elif a == 3:
        break
    print('輸入 Help 了解指令')
    while True:
        
        b = input()
        if b.lower() == 'help':
            print('exit 離開')
            print('time 看時間')
        elif b.lower() == 'time':
            now = time.asctime( time.localtime(time.time()) )
            print(now)
    
        elif b.lower() == 'exit':
            print('感謝使用')
            break
        else:
            print('請輸入可使用的指令')
    break
            
    