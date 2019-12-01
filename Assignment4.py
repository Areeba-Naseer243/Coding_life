#Qno:1
person = {
    'first_name': 'Sadia',
    'last_name': 'Razzaq',
    'age': 20,
    'city': 'karachi',
    }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
#Adding key value pair
person.update(Qualification = 'Intermediate' )
#Updating Qualification
person.update(Qualification = 'high academic level')
#deleteing key 
del person['Qualification']


#Qno:2
cities = {
    'Karachi': {
        'country': 'Pakistan',
        'population': 61580,
        'Fact': 'Hospitatlity',
        },
    'Dehli': {
        'country': 'India',
        'population': 87678906,
        'Fact': 'Economy',
        },
    'Dhaka': {
        'country': 'Bangladesh',
        'population': 1003285,
        'Fact': 'Education',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    Facts= city_info['Fact'].title()

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print("  This country is very famous because of" + Facts + "." )




#Qno:03

age=int(input("Enter Your age: "))
if age<3:
    print("Your Ticket is Free")
elif age>=3 and age<=12:
    print("Ticket price is $10")

elif age>12:
    print("Ticket price is $15")

else:
    print("Invalid Input")
    


#Qno:04

def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(title + " is one of my favorite books.")

favorite_book('The Abstract Wild')


#Qno:05

import random
guessesTaken = 0
print('Hello! What is your name?')
myName = input()
number = random.randint(1, 30)

print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 3:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.
    if guess > number:
            print('Your guess is too high.')
    if guess == number:
        break


if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
