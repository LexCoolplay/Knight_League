N = int(input())
res = [""]
k = 0
i=""
length=0
for _ in range(N):
    i+= input()[:-5]
for j in i.split():
    if (length + len(j)+4 <= 280):
        length+=len(j)+4
        res[k] += j + " "
    elif(length+len(j)>280):
        res[k]+="("+str(k+1)+"/"
        res.append("")
        k+=1
for a in range(len(res)):
    if(res[a][-5]!='('):
        res[a] += '('+str(k+1)+'/'
    res[a] += str(k+1) + ")"

print(*res,sep="\n")


# 2
# Winter!... The peasant breathes a sign, (1/2)
# renews his sledge, and makes his way. (2/2)
