#to print positive nos
list1 = []
n = int(input("Enter the no of elements\n"))
for i in range(0,n):
    no = int(input("Enter the elements"))
    list1.append(no)
for number in list1:
    if number>0:
        print(number)
    
 
