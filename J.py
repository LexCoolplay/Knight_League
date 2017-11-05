N = int(input())
res = [""]
k = 0
i = ""
length = 0

for _ in range(N):
    inp = input().strip()
    i += inp[:inp.rfind('(')]
Array_length=list(map(lambda x:len(x),i.split()))
COUNT=sum(Array_length)//280
for j in i.split():
    if (len(res[k]) + len(j) + len('(' + str(k + 1) + '/'+str(COUNT) + ")")+1 <= 280):
        # print(len(res[k]) + len(j)+4,k)
        length += len(j) + 4
        res[k] += j + " "
    elif (len(res[k]) + len(j) + len('(' + str(k + 1) + '/'+str(COUNT) + ")")+1 > 280):
        res[k] += "(" + str(k + 1) + "/"
        res.append("")
        k += 1

for a in range(len(res)):
    if (len(res[a]) < 3 and res[a] or len(res[a]) >= 3 and res[a].rfind('(')==-1 ):
        res[a] += '(' + str(k + 1) + '/'
    if (res[a]):
        res[a] += str(k + 1) + ")"
if (N <= 0):
    k -= 1
print(k + 1)
print(*res, sep="\n")
