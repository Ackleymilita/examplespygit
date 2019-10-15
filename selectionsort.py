def sort(n):
    for i in range(len(n)-1):
        minpos = i
        for j in range(i,len(n)):
            if n[j] < n[minpos]:
                minpos = j

            temp = n[i]
            n[i] = n[minpos]
            n[minpos] = temp

n = [ 5,3,8,6,7,2]

sort(n)
print(n)
