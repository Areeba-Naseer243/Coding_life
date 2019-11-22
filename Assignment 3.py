# Ans 1
print('Ans 1\n-------')
print('Simple Calculator \nSelect Operation \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Power')
while True:
    choice=int(input('Enter your choice(1/2/3/4/5): '))
    num1=int(input('Enter first number: '))
    num2=int(input('Enter second number: '))
    if choice==1:
        print(num1+num2)
    elif choice==2:
        print(num1-num2)
    elif choice==3:
        print(num1*num2)
    elif choice==4:
        print(num1/num2)
    elif choice==5:
        print(num1**num2)
    else:
        print('Invalid Input')
    select=input('Do you want to continue \nIf yes enter Yes \nIf no enter No')
    if select=='Yes':
        continue
    else:
        break


print('---------------------------------------------------------------')

# Ans 2
print('Ans 2\n-------')
List=['1','apple','56','a']
for i in List:
    print(i.isdigit())
            
 
print('---------------------------------------------------------------')

# Ans 3
print('Ans 3\n-------')
D={'This':1,'is':2,'Computer':3}
D.update({'Programming':4})
print(D)


print('---------------------------------------------------------------')

# Ans 4
print('Ans 4\n-------')
D={'This':1,'is':2,'Computer':3,'Programming':4}
print(sum(D.values()))

print('---------------------------------------------------------------')

# Ans 5
print('Ans 5\n-------')
List=[]
length=int(input("Enter the length of the list: "))
for i in range(length):
    element=int(input("Enter the element of the list: "))
    List.append(element)
print(List)
for j in range(length):
    for k in range(j+1,length):
        if List[j]==List[k]:
            print(List[j])

print('---------------------------------------------------------------')

# Ans 6
print('Ans 6\n-------')
D={'This':1,'is':2,'Computer':3,'Programming':4}
x=input('Enter key')
if x in D.keys():
    print('Already Exist')
else:
    print('not present')
