# Ans 1
print('Ans 1\n-------')
print("""twinkle, twinkle, little star,
\tHow I wonder What you are!
\t\tUp above the world so high,
\t\tLike a diamond in the sky
twinkle, twinkle, little star,
\tHow I wonder What you are!""")

print('---------------------------------------------------------------')

# Ans 2
print('Ans 2\n-------')
import sys
print('Version: ')
print(sys.version)
 
print('---------------------------------------------------------------')

# Ans 3
print('Ans 3\n-------')
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

print('---------------------------------------------------------------')

# Ans 4
print('Ans 4\n-------')
radius= float(input('Enter the radius of circle: '))
if radius>0:
    Area= 3.142* (radius**2)
    print('The Area of circle is', Area)
else:
    print('Invalid value')

print('---------------------------------------------------------------')

# Ans 5
print('Ans 5\n-------')
Fname=list(input('Enter your first name: '))
Lname=list(input('Enter your last name: '))
fullname=Lname[ : :-1]+[" "]+Fname[ : :-1]
for i in fullname:
    print(i,end="")

print('---------------------------------------------------------------')

# Ans 6
print('Ans 6\n-------')
num1=float(input('Number1: '))
num2=float(input('Number2: '))
Sum=num1+num2
print('The Sum of {0} and {1} is {2}'. format(num1,num2,Sum))
    
