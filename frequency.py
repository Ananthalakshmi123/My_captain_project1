#frequency

string = str(input("Input the string\n"))
dict = {}
for i in string:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

print(dict)

        
