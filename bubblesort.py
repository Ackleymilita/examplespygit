def sort(n):
    for i in range(len(n)-1,0,-1):
        for j in range(i):
            if n[j]>n[j+1]:
                temp = n[j]
                n[j] = n[j+1]
                n[j+1] = temp
n = [ 5,3,8,6,7,2]

sort(n)
print(n)
