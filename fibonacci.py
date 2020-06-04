#fibonacci
n = int(input("The number of terms to be printed in a Fibonacci sequence\n"))
list=[0,1]
for j in range(0,n-2):
    list.append(list[j]+list[j+1])
print(list)
