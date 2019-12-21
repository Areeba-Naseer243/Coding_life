print('Q1')
def factorial(n):
    if n>1:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        print('Factorial is',fact)
    elif (n==0 or n==1):
        print('Factorial is 1')
    else:
        print('Factorial not exist')
factorial(9)


print('\n')
print('Q2')
def string(n):
    a=0
    b=0
    for i in (n):
        if (i.islower()):
            a=a+1
        elif (i.isupper()):
            b=b+1
    print('The number of lower string',a)
    print('The number of upper string',b)
string('PAkisTan')


print('\n')
print('Q3')
def even():
    List=[3,9,2,1,4,6,78,456,345678]
    for i in (List):
        if i%2==0:
            print(i)
even()


print('\n')
print('Q4')    
def reverseit(s):
    s1=('')
    for i in s:
        s1=i+s1
    if(s==s1):
        print(s,'is a palindrome')
    else:
        print(s,'is not a palindrome')
reverseit('civic')


print('\n')
print('Q5')
def prime(n):
    if n>1:
        for i in range(2,n):
            if(n%i==0):
                print(n,'is a constant')
                break
        else:
            print(n,'is a prime')
    else:
        print(n,'is a constant')
prime(7)


print('\n')
print('Q6')
def item(*args):
    print('All items you bought are')
    for i in args:
        print (i)
print('Welcome to Super Market')
x=int(input('How many items do you want to buy'))
z=[]
for i in range (x):
    y=input('Enter')
    z.append(y)
item(*z)
        
        



                  
            
