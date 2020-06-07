#frequency

string = str(input("Input the string\n"))
dict = {}
for i in string:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

sorted_dict = sorted(dict, key=dict.get, reverse=True)
for r in sorted_dict:
    print(r+"="+str(dict[r]))

