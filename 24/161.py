with open("24data/24-s1.txt") as f:
    a = f.read().split("\n")

with open("24data/24-s1.txt") as f:
    a_full = f.read()



# ищет максимальный встречающийся символ в строке и в случае
# нескольких таких символов выбирает крайний по алфавиту
def finder(a,flag = False,letter = "?"):
    dc = {}
    for i in a:
        dc[i] = dc.setdefault(i,0) + 1
    
    # для заветной буквы
    if flag:
        return dc[letter]

    s_dc = sorted(dc.items(),key = lambda x: x[1])
    mini = min([i for i in dc.values() if i != 0])
    # проверка
    s_dc = list(filter(lambda x: x[1] == mini,s_dc))
    return sorted(s_dc,key = lambda x: x[0])[0]



# поиск строки с самым малым количеством символов
arr = []
maxi = 0
for i in a:
    c = i.count("Q")
    # должна быть хотя бы 1 A
    if c == 0:
        continue
    if c > maxi:
        maxi = c
        arr.clear()
        arr.append(i)
    elif c == maxi:
        arr.append(i)

s = arr[-1]
# заветная буква
letter = finder(s)[0]
print(letter)
print(finder(a_full,flag=True,letter=letter))

# ответ
#C38412