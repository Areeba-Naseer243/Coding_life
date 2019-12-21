'''
QUESTION 1
----------
Object-oriented programming (OOP) refers to a type of computer programming (software design) in which programmers define the data type of a data structure, and also the types of operations (functions) that can be applied to the data structure.
In this way, the data structure becomes an object that includes both data and functions. In addition, programmers can create relationships between one object and another. For example, objects can inherit characteristics from other objects. Following are the features of OOP:
•	Abstraction: The process of picking out (abstracting) common features of objects and procedures.
•	Class: A category of objects. The class defines all the common properties of the different objects that belong to it.
•	Encapsulation: The process of combining elements to create a new entity. A procedure is a type of encapsulation because it combines a series of computer instructions.
•	Information hiding: The process of hiding details of an object or function. Information hiding is a powerful programming technique because it reduces complexity.
•	Inheritance: a feature that represents the "is a" relationship between different classes.
•	Interface: the languages and codes that the applications use to communicate with each other and with the hardware.
•	Messaging: Message passing is a form of communication used in parallel programming and object-oriented programming.
•	Object: a self-contained entity that consists of both data and procedures to manipulate the data.
•	Polymorphism: A programming language's ability to process objects differently depending on their data type or class.
•	Procedure: a section of a program that performs a specific task.
'''

'''
QUESTION 2
----------
•	It provides a clear modular structure for programs which makes it good for defining abstract datatypes in which implementation details are hidden
•	Objects can also be reused within an across applications. The reuse of software also lowers the cost of development. More effort is put into the object-oriented analysis and design, which lowers the overall cost of development.
•	It makes software easier to maintain. Since the design is modular, part of the system can be updated in case of issues without a need to make large-scale changes
•	Reuse also enables faster development. Object-oriented programming languages come with rich libraries of objects, and code developed during projects is also reusable in future projects.
•	It provides a good framework for code libraries where the supplied software components can be easily adapted and modified by the programmer. This is particularly useful for developing graphical user interfaces.
•	Better Productivity as OOP techniques enforce rules on a programmer that, in the long run, help her get more work done; finished programs work better, have more features and are easier to read and maintain. OOP programmers take new and existing software objects and "stitch" them together to make new programs.
        Because object libraries contain many useful functions, software developers don't have to reinvent the wheel as often; more of their time goes into making the new program.'''


'''
QUESTION 3
METHOD
•	Method is called by its name, but it is associated to an object (dependent).
•	A method is implicitly passed the object on which it is invoked.
•	It may or may not return any data.
•	A method can operate on the data (instance variables) that is contained by the corresponding class
FUNCTION
•	Function is block of code that is also called by its name. (independent)
•	The function can have different parameters or may not have any at all. If any data (parameters) are passed, they are passed explicitly.
•	It may or may not return any data.
•	Function does not deal with Class and its instance concept.
'''

'''
QUESTION 4
CLASS: Classes (OOP) In object-oriented programming, a class is a blueprint for creating objects (a particular data structure), providing initial
       values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects
       are created using the class keyword.

OBJECT: Each object is an instance of a particular class or subclass with the class's own methods or procedures and data variables.
        An object is what actually runs in the computer.

AATRIBUTES: In Object-oriented programming(OOP), classes and objects have attributes. Attributes are data stored inside a class or instance and
            represent the state or quality of the class or instance. In short, attributes store information about the instance. Also, attributes
            should not be confused with class functions also known as methods. One can think of attributes as noun or adjective, while methods are
            the verb of the class.

BEHAVIOR: A class's behavior determines how an instance of that class operates; for example, how it will "react" if asked to do something by another
          class or object or if its internal state changes. Behavior is the only way objects can do anything to themselves or have anything done to
          them.

'''


'''
QUESTION5
'''
class car():
    def __init__(self,model, name, color, brand, fuel_used):
        self.name= name
        self.model= model
        self.color= color
        self.brand=brand
        self.fuel_used=fuel_used
    def get_common_details(self):
        print('Name:' , self.name)
        print('Color:', self.color)
    def get_specific_details(self):
        print('Model:' , self.model)
        print('Brand:', self.brand)
        print('Fuel_used:', self.fuel_used)

car1=car('GDH-25','Corolla','White','Toyota','Petrol')
print('CAR1')
print('----------')
car1.get_common_details()
car1.get_specific_details()
car2=car('KSK-36','Camry','Silver','Toyota','CNG')
print('CAR2')
print('----------')
car2.get_common_details()
car2.get_specific_details()
car3=car('FAD-25','Picanto','Red','Kia', 'Diesel')
print('CAR3')
print('----------')
car3.get_common_details()
car3.get_specific_details()
car4=car('AKW-19','Aspire','White','Ford','Petrol')
print('CAR4')
print('----------')
car4.get_common_details()
car4.get_specific_details()
car5=car('LPW-18', 'Mustang','Blue','Ford','Diesel')
print('CAR5')
print('----------')
car5.get_common_details()
car5.get_specific_details()
        
