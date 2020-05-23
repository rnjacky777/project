import random
print('welcome to play blackjack')
mycard = []
compcard = []
allcard = []

for i in range(1,54,1):    
    allcard.append(i)
 
def printcard(number):
    if number <= 13:
        name = 'Spade '
    elif number > 13 and number <= 26:
        number -= 13
        name = 'Heart '
    elif number > 26 and number <= 39:
        number -= 26
        name = 'Diamond '
    elif number > 39 and number <= 52:
        number -= 39
        name = 'Club  '
    else:
        pass
        
    if number < 11:
        name += str(number)
        point = number
        return name , point
    elif number == 11:
        name += 'J'
        point = 10
        return name , point
    elif number == 12:
        name += "Q"
        point = 10
        return name , point
    elif number == 13:
        name += "K"
        point = 10
        return name , point
    else:
        pass

def getcard(playername):
    a = random.choice(allcard)
    allcard.remove(a)
    name,point = printcard(a)
    playername.append(name)
    return point
point =  getcard(mycard)
compoint = getcard(compcard)   
result = False
end =   False
while True:
    if end == True:
        break
    print('1.抽牌')
    print('2.不抽(直接比大小)')
    a = input()
    if a == '1':
        point += getcard(mycard)
        compoint += getcard(compcard)
        print(mycard)
    elif a == '2':
        result = True
    else:
        continue
        
    if point >= 21 or result == True or compoint >= 21:
        if (point > compoint and result == True) or compoint >= 21:
            print('你贏了')
            print('你的點數為'+str(point)+' 電腦為'+str(compoint))
            end = True
        elif (point < compoint and result == True) or point >= 21:
            print('你輸了')
            print('你的點數為'+str(point)+' 電腦為'+ str(compoint))
            end = True
    else:
        pass
    
    while end:
        print('你要在玩一次嗎 1.Yes 2.No')
        b = input()
        if b == '1':
            for i in range(0,54,1):    
                allcard.append(i)
            mycard = []
            compcard = []
            point =  getcard(mycard)
            compoint = getcard(compcard)   
            result = False
            end =   False
        elif b == '2':
            break
        else:
            pass
        
            
    
    
#a = random.choice(allcard)
#name , point = printcard(a)
#print('名稱 ' + name + " "+'點數 '+ str(point))
    