with open("24data/24-215.txt") as f:
    a = f.read()


c = 0
count = 0
maxi = 0

for i in range(len(a)-1):
    if c > 0:
        c-=1
        continue
    if a[i] in "ABC" and a[i+1] in "123":
        count += 1
        c = 1
    else:
        maxi = count if maxi < count else maxi
        count = 0

print(maxi)
# ответ 183