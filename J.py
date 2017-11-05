from functools import reduce
N = int(input())
res = [""]
k = 0
i = ""
length = 0

for _ in range(N):
    inp = input().strip()
    i += inp[:inp.rfind('(')]
for COUNT in range(5,10):
    for j in i.split():
        if (len(res[k]) + len(j) + COUNT <= 280):
            # print(len(res[k]) + len(j)+4,k)
            length += len(j) + 4
            res[k] += j + " "
        elif (len(res[k]) + len(j) + COUNT > 280):
            res[k] += "(" + str(k + 1) + "/"
            res.append("")
            k += 1
    if(not reduce(lambda x,y:x or (len(y)>=280-COUNT),res, False)):
        break;

for a in range(len(res)):
    if (len(res[a]) < 3 and res[a] or len(res[a]) >= 3 and res[a].rfind('(')==-1 ):
        res[a] += '(' + str(k + 1) + '/'
    if (res[a]):
        res[a] += str(k + 1) + ")"
if (N <= 0):
    k -= 1
print(k + 1)
print(*res, sep="\n")
