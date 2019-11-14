# Ans 1
print('Ans 1\n-------')
maths=int(input('Maths marks: '))
english=int(input('English marks: '))
science=int(input('Science marks: '))
social=int(input('Social marks: '))
urdu=int(input('Urdu marks: '))
Sum=maths+science+social+english+urdu
print('Maths:', maths,'\n'
      'English:' ,english,'\n'
      'Science:',science,'\n'
      'Social:',social,'\n'
      'Urdu:',urdu,'\n'
      '**SUM**', Sum)

if Sum>=500:
    print('The grade obtained is A*')
elif Sum>=450:
    print('The grade obtained is A')
elif Sum>=400:
    print('The grade obtained is B')
elif Sum>=350:
    print('The grade obtained is C')
elif Sum>=300:
    print('The grade obtained is D')
elif Sum>=250:
    print('The grade obtained is E')
else:
    print('The grade obtained is F')

print('---------------------------------------------------------------')

# Ans 2
print('Ans 2\n-------')
Num=int(input('Enter the Number that to checked: '))
if Num==0:
    print('0 is neither even nor odd')
elif Num%2==0:
    print('Number is even')
else:
    print('The Number is odd')
        
 
print('---------------------------------------------------------------')

# Ans 3
print('Ans 3\n-------')
l1=[2,4,6,7,1,5,1]
print(len(l1))

print('---------------------------------------------------------------')

# Ans 4
print('Ans 4\n-------')
l1=[1,2,9,6,7,3]
print(sum(l1))

print('---------------------------------------------------------------')

# Ans 5
print('Ans 5\n-------')
l1=[6,8,4,9,3,7]
print(max(l1))

print('---------------------------------------------------------------')

# Ans 6
print('Ans 6\n-------')
a=[1,1,2,3,5,8,13,21,34,55,89]
for i in range(11):
    if a[i]<5:
        print(a[i])
    else:
        None
