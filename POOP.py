#Python Object Oriented Programming
#An object is an instance of a class.
#Objects have attributes and methods
#Attributes = What an object is/has. Ex: name, age, height
#Methods = What an object can do. Ex: talk,fly,drive, stop
#To create an object we will need to create a class.
#A class functions as an blueprint (projeto/diagrama/desenho técnico) and it will
#describe what attributes and methods our object will have.
#You can create a class in your main module if your project or class is small, or you can create in another module
#To create a class, we write 'class' followed by the name of the object we'd to create
#The first letter of the name is Capital
#class Car:
#attributes
#methods
#the innit method will construct object for us. In other languages is known by constructors.
    #def __init__(self): #allows us to assign our objects unique values
      #  make = None      #we can set up arguments to our innit method
      #  model = None
       # year = None
       # color = None
    # wheels = 4 #This is an class variable wich acts like a default attribute for all objects of this class
    # def __init__(self,make,model,year,color): #it have 5 parameters, but we only
    #     self.make = make   #need to put 4 arguments, because in python the self argument is done automaticlly
    #     self.model = model #self.model reffers to the model of our object
    #     self.year = year   #model is our parameter to receive arguments
    #     self.color = color #arguments will be assigned to our object attributes
    #The values declared inside of the constructor are INSTANCE VARIABLES
    #Class variables are declared inside the class, but outside the constructor __innit__
import functools
# def drive(self): #self reffers to the object that is using this method
    #     print ('This car is car is driving')
    # def stop(self):
    #     print ('This '+str(self.model)+' is sttoped')
#
# car1 = Car('Jaguar','F-PACE',2023,'silver')
# print (car1.make)
# print (car1.model)
# print (car1.year)
# print (car1.color)
# print (car1.wheels)
# car1.wheels = 2 #you can change a class variable for an object
# print (car1.wheels)
# Car.wheels = 3 #you can change a class variable outside the class
# print (Car.wheels)
# car1.drive()
# car1.stop()
# a class can function like a blueprint to create objects we can assign attributes and methods
#within our class we have the __innit__ method that can assign arguments to each object's attributes
#after we create an class, we can reuse it and create several distinct objects
#as car2, or car3 with different make,model,year and colors.
#-------------------------------------------------------------

#Inheritance = When a class (child class) receives attributes and or methods from another class (parent).
#But the child class can still implementate it's unique attributes and methods
# class Animal:
#     alive = True
#     def eat(self):
#         print ('This animal is eating')
#     def sleep(self):
#         print ('This animal is sleeping')
#
# class Dog(Animal):
#     def bark(self):
#         print ('This dog is barking')
#
# dog_border = Dog()
# dog_border.bark()
# class Rabbit(Animal):
#     def jump(self):
#         print ('This Rabbit is jumping')
# class Hawk(Animal):
#     def fly(self):
#         print ('This hawk is flying')
# class Fish(Animal):
#     def swim(self):
#         print ('This fish is swimming')
# rabbit = Rabbit() #by creating a 'variable' that contains as value a class, we create an object
# hawk = Hawk() #object 'hawk' has attributes and methods from the Hawk() class
# fish = Fish()
#
# print (rabbit.alive) #alive is a class variable, so it needs to be printed
# hawk.sleep() #methods doesn't need the print fucntion, because they're already a function.
# fish.eat() #this subclass/child class has access to all the methods and attributes from the parent class
           #because the inheritance. It avoids copying the same code again and again
           #And has the bennefit: when you make some change in the parent class, this will apply to all subclasses

#------------------------------------------------------------

#Multilevel Inheritance = When a derived (child/sub) class inherits from another derived (child) class

#class Organism: #parent class. But acts like the grandparent.
    # alive = True
# class Animal(Organism): #child class and parent class. But acts like the 'parent'
#     def eat(self):
#         print ('This animal is eating')
#     def sleep(self):
#         print ('This animal is sleeping')
#
# class Dog(Animal): #child class
#     def bark(self):
#         print ('This dog is barking')
# dog = Dog()
# print (dog.alive)
# dog.eat()
# dog.bark()
#-------------------------------------------------------------
#
# MULTIPLE INHERITANCE = When a child class is derived from more than one parent class
#
# class Predator:
#     def hunting(self):
#         print('This animal is hunting')
# class Prey:
#     def flee(self):
#         print('This animal flees')
# class Rabbit(Prey):
#     pass
# class Hawk(Predator):
#     pass
# class Fish(Prey,Predator): #we can add more than one parent class by adding comma between the classes
#     pass             #by doing that, this child class will have access to both parent classes content
#
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
#
# rabbit.flee()
# hawk.hunting()
# fish.flee()
# fish.hunting()
#----------------------------------------------------------------------

#METHOD OVERRRIDING = Is the ability of an object oriented programming language to allow a subclass/child class
#to provide an specific implementation of a method that is already provided by one of it's parent class.

# class Animal:
#     alive = True
#     def eat(self): #Method's name 'eat' + parameters 'self' = method's signature
#         print ('this animal is eating')
# class Dog(Animal):
#     def eat(self): #It has the same method's signature as it's parent class
#         print('this dog is eating a steak')
# dog = Dog()
# print (dog.alive) #the class Dog has access to the class variable 'alive' from it's parent class
# dog.eat() #but the eat function for the Dog class is not that inherits by Animal class
#That's because an object will use a method that is more closely associated with itself
#first before relying on a method that it may inherit from a parent class
#--------------------------------------------------------

#METHOD CHAINING = Calling multiple methods sequentially
# each call performs an action on the same object and returns self

# class Car:
#     def turn_on(self):
#         print ('You start the enginge')
#         return self
#     def drive(self):
#         print ('You drive the car')
#         return self
#     def stop(self):
#         print ('You step on the breaks')
#         return self
#     def turn_of(self):
#         print ('You turn off the engine')
#         return self
# car = Car()
# car.turn_on()
# car.drive()
# car.stop()
# car.turn_of()
#Or we can execute this methods in one line of code. But for this we need to add 'return self'
#That way, after each method, the value returned will be self, that corresponds as the object itself
# car.turn_on().drive().stop().turn_of()
#if the line of code gets to extensive, you can press enter after some methods parentheses
# car.turn_on().drive()\     #the back slash means continuation character
#     .stop().turn_of()
#------------------------------------------------------------------

#SUPER FUNCTION = A function used to give access to the methods of a parent class.
#                 Returns a temporary object of a parent class when used.

# class Rectangle:
#     pass
# class Square(Rectangle):
#     def __init__(self,width,length):
#         self.width = width
#         self.length = length
# class Cube(Rectangle):
#     def __init__(self,width,length,height):
#         self.width = width
#         self.length = length
#         self.height = height
#We can see the attributes inside the square class are the same as some of the attributes of the cube class
#so we can select what is in common and copy the code to the parent class (Rectangle).
#In this case, the common part is the __init__ method, so to access that from the parent class, we will
#use the super function 'super()'

# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
# class Square(Rectangle):
#     def __init__(self,width,length):
#         super().__init__(width,length) #the super function access/refers parent class without naming them
# it search hierarchically for a method. In this case, it searchs for the init method
#from the parent class. The super function will behave/value as the block of code from the init method
#This is usefull because we need the constructor to assign our object's attributes so we can create
#another function with those attributes.
    # def area(self):
    #     return self.length*self.width
# class Cube(Rectangle):
#     def __init__(self,width,length,height):
#         super().__init__(width,length)
#         self.height = height
#     def volume(self):
#         return self.length*self.width*self.height
#
# square = Square(3,3)
# cube = Cube(3,3,3)
# print(cube.volume())
# print(square.area())
#-----------------------------------------------------------

#ABSTRACT CLASSES = Prevents a user from creating an object out of that class +
# + compels the user to override abstract methods in a child class
#abstract class = a class wich contains one or more abstract methods
#abstract methods = a method that have a declaration but does not have an implementation
#you have to import the abc (abstract based class)
# from abc import ABC, abstractmethod

# class Vehicle(ABC): #the parent class import from abc classes, that contains abstract methods
#     @abstractmethods #This method in top of other method, turns the method into abstract method.
#     def go(self):    #this abs method impedes the user from creating an vehicle object, and it
#         pass  #compels the user to override (write the same method's signature[method name+parameter]
              #so its usefull to force the child class to have this function.
        # When its an important function that must not be forgotten
# class Car(Vehicle):
#     def go(self):
#         print ('You drive the car')
# class Motorcycle(Vehicle):
#     def go(self):
#         print ('You ride the motorcycle')

# vehicle = Vehicle()
# car = Car()
# bike = Motorcycle()

# vehicle.go()
# car.go()
# bike.go()
#--------------------------------------------------------

#PASS OBJECTS INTO ARGUMENTS:
# class Car:
#     color = None
# class Motorcycle:
#     color = None
# def change_color(vehicle,color): #this function can be used by any object that contains 'color' as attribute
    #it has to have parameters for the arguments, one for the object that we want to change color
    #and other for the color we would like to put in this object
    #both MUST BE LOWERCASE
    # vehicle.color = color #vehicle.color refers to the color attribute of the object we want.
                          #color will be the color we will assign the object with.
# car1 = Car()
# car2 = Car()
# car3 = Car()
# bike1 = Motorcycle()
#
# change_color(car1,'green')
# change_color(car2,'blue')
# change_color(car3,'silver')
# change_color(bike1,'black')
# print (car1.color)
# print (car2.color)
# print (car3.color)
# print (bike1.color)
#we can pass objects as arguments to a function much like what we've been doing with variables
# however the type of objects that we pass in may be limited based on
# the required attributes and methods that that given class or object might have
# -------------------------------------------------------------------

#DUCK TYPING = Concept where the class of an object is less important than the it's methods/attributes
               # class type is not checked if minimun methods/attributes are present
               # 'If it walks like a duck, and it quacks like a duck, then it must be a duck.'

# class Duck:
#     def walk(self):
#         print ('This duck is walking')
#     def talk(self):
#         print ('This duck is quacking')
# class Chicken:
#     def walk(self):
#         print ('This chicken is walking')
#     def talk(self):
#         print ('This chicken is clucking')
# class Person:
#     def catch(self,duck): #it could be animal
#         duck.walk() #it coul be animal
#         duck.talk()
#         print ('You catch this animal')
# duck = Duck()
# chicken = Chicken()
# person = Person()
# person.catch(duck)  #The catch function requers one argument to fill the parameter
# person.catch(chicken)#Despite being a duck.walk() method inside the catch method, you can put the
# chiken as argument, because the Chicken class has also the walk and talk method, so it can execute.
# By other means, in duck typing, you can accept other classes if they have the required methods/attributes
# If the chicken object didn't have a walk method, python would not have accepted it, because it's missing
#As the chicken can walk and talk, like a duck, it counts as a duck
#------------------------------------------------

#WALRUS OPERATOR :=
#new to python 3.8
#assginment expression aka walrus operator
#assigns values to variables as part of a larger expression

#happy = True
# print (happy)
# print (happy := True) #The walrus operator creates a larger expression, but in less lines of codes
                        #It states that happy = true, and print happy.
#foods = list()
#while True:
   # food = input('What food do you like?')
 #   foods.append(food)
  #  if food == 'quit':
   #     break
#Using the walrus operator, the code should be this:
# foods = list()
# while food := input('What food do you like?: ')  != 'quit':
#     foods.append(food)
#We used less lines of code to create the same program
#--------------------------------------------------

#ASSIGN FUNCTION TO A VARIABLE:

# def hello():
#     print('Hello!')
#hello() #hello it's the name of the function, while '()' is what calls the function to use.
#print (hello) #this will print only wher in our memory address the function is placed/located. Hexadecimal
# hi = hello #you are adressing the memory address of the hello function to the hi variable.
#if you put the set of parentheses: hi = hello()  it would call the function
# and return it's result to hi, printing ''Hello!''
#but now hi and hello have the same memory address, and hi function as an alias/nickname to hello.
# hi() #as hi is a nickname to hello, by adding a set of parentheses after
# hi() calls the same as the function hello()
# say = print
# say ('Amazing, it works!')
#we can replace print for hi by assign the function to a variable.
#----------------------------------------------------------

#Higher Order Function = a function that either:
#1.accepts a function as arguments
#or
#2.returns a function
#(In Python, functions are also treated as objects)

#1.
# def loud(text):
#     return text.upper()
# def quiet(text):
#     return text.lower()
# def talk(func): #its the higher order function, it accepts functions as arguments
#     print (func('Eu vou dar o meu melhor'))

# talk(loud) #what is happening, is that the talk function accepted loud as an argument to func parameter
#the talk function will execute it's print function that has now (loud('Eu vou dar o meu melhor'))
#the loud function will accept 'Eu vou dar o meu melhor' as an argument to the text parameter
#then the loud function will return this text all uppercase.
# talk(quiet) #the quiet function accepted in the talk function will return the text all lowercase.

#2.

#def dividir(x,y):        #this how i would do instead of Higher Order Function
 #   return x/y
#div = dividir(10,2)
#print(div)
#print (dividir(10,2))
#print(dividir(30,3))

#This is how we do in Higher Order Function:
# def divisor(x):
#     def dividend(y):
#         return y/x
#     return dividend
# half=divisor(2) #the variable half equals calling the divisor function with x being equal to 2
# terço = divisor(3) #the divisor function will return dividend, skipping the dividend function because
# print (half(30)) #it was not called.Half has the same memory address as the dividend function.
# print (terço(30))#So, half = dividend then we will be printing dividend(30), being 30 equals to y.
#And by adding the set of parentheses, we are calling the dividend function.
#--------------------------------------------------

#LAMBDA FUNCTION = function written in 1 line of code using lambda keyword
#                  accepts any number of arguments, but only has one expression
#                  (think of it as a shortcut)
#                  (used if needed for a short period of time, throw away)
#variable = lambda parameters:expression
#print (variable(arguments))

# double = lambda x:x*2
# multiply = lambda x,y,z:x*y*z
# add = lambda x,y,z,w:x+y+z+w
# full_name = lambda first_name,last_name:first_name+' '+last_name
# age_check = lambda x:True if x >=18 else False
# print (double(5))
# print (multiply(2,3,4))
# print (add(4,10,18,22))
# print (full_name('Daniel','Vaz'))
# print (age_check(21))
#We add any number of arguments, but the expression is written in only one line of code.
#--------------------------------------------------------

#SORT DATA: (sort = organizar alfabeticamente, ou em ordem crescente ou decrescente)
#sort() method = used with lists
#sort() function = used with iterables

# students = ['Daniel','Davi','Acidália','David',]
# students.sort()
# for i in students:
#     print (i)
# students.sort(reverse=True)
# for i in students:
#     print(i)

# students = ('Daniel','Davi','Acidália','David',) #Now it's a tupple, and it can not be changed
# students_sortt = sorted(students) # so we need to create another list #we could write 'sorted(students,reverse=True)
# for i in students_sortt: #we will print the values with a for loop of the new list we created
#     print (i)

#students = [('Daniel',21,'A'),
            # ('Davi',57,'B'),
            # ('Acidália',52,'C'),
            # ('David',25,'D')]
#students.sort() #it would sort our list of tuples by alphabetical order
# but we can't order by the second or third collumn

# age = lambda ages:ages[1] #we created a function with lambda
# name = lambda names:names[0] #we can create one object for each collumn for easy management
# other = lambda others:others[2]
#and we created an object by adding this function to a variable
#students.sort(key=age) #we set key equal to an object #we sorted our list of tuples by the key argument age
#for i in students: #that is an object, a variable that contains a function that gives us a index element
    #print(i)#of the collumn we want
#that is an object, a variable that contains a function that gives us a index element of the collumn we want
#(lambda function, wich accepts any number of args, but has only one expression)
#that will return us the index of the especific collumn that we want

#But if it's a tuple of tuples, we need to create an variable to contain the sorted tuple
# and then for loop the variable with the key we want to:
# students = (('Daniel',21,'A'),
#             ('Davi',57,'B'),
#             ('Acidália',52,'C'),
#             ('David',25,'D'))
#
# students_sorted = sorted(students,key=age)
# for i in students_sorted:
#     print (i)
#-------------------------------------------------

#MAP() FUNCTION = applies a function to each item in a iterable (lists, tuples, etc)

#map(function,iterable) #accepts two arguments
import math
import time


# store_dolar = [('shirt',20.0),
#          ("pants",25.0),
#          ("jacket",50.0),
#          ("sockets",10.14)]
# to_real = lambda valor: (valor[0],round(valor[1]*5.15)) #we create a tuple that contains both collumns (using index 0 and 1),
#and we make the expression for the one we want to change (multiply valor[1] by 5,15) and we round it.
#we have created a tuple with the modified values
# to_euro = lambda valor: (valor[0],float('{:.2f}'.format(valor[1]*0.94)))
#we turned the result of valor[1] into str with 2 decimals and then we typecasted it to float type.
# store_real = list(map(to_real,store_dolar)) #we created a map object that contains a map function that contains as args
#the function to modify the iterable, and the iterable. And we turned the result into a list.
# for i in store_real: #as store_real is a list, we can print it by doing a for loop.
#     print (i)
# store_euro = list(map(to_euro,store_dolar))
# for i in store_euro:
#     print (i)
#---------------------------------------------------------

#FILTER() FUNCTION = Creates a collection of elements from an iterable for wich a function returns True

#filter(function,iterable)

# friends = [("Rachel",19),
#            ("Monica",18),
#            ("Phoebes",17),
#            ("Joey",16),
#            ("Chandler",21),
#            ("Ross",20)]
#to use the filter function, we create a function/object that contains an expression. We would like to use lambda
# age = lambda ages:ages[1] >= 18 #we are kinda searching for results compatibles with the criteria
# drink_buddies = list(filter(age,friends)) #we filter our frinds list by the function age
#that only includes >= 18 years olds. Then we cast it into a list, and we turn it into a object by creating the variable
# for i in drink_buddies: #we print our new list/object by doing a for loop
#     print (i)
#------------------------------------------------------------------------------

#REDUCE() FUNCTION = apply a function to an iterable and reduce it to a single cumulative value.
#Performs function on the first two elements and repeats process until 1 value remains.
#objeto = functools.reduce(lambda x,y:expression,fatorial)

#you can import functoos. i didn't

# fatorial = [5,4,3,2,1]
# fatorado = functools.reduce(lambda x,y:x*y,fatorial)#it only accepts 2 arguments x,y. But in the expression you can
# letras = ["D","I","S","C","P","L","I","N","A"]      #several kinds of operations
# juntar_letras = functools.reduce(lambda x,y:x+y,letras) #We have a iterable (list) that we want to turn into a single
# print (fatorado)  #cumulative value, so now we create an object 'fatorado' that contains the reduce function
# print (juntar_letras) #functools.reduce() inside this function we need to put whithin a lambda function ONLY 2 arguments
#followed by our lambda expression that will acummulate our iterable. And we need to put our iterable (list)
# that we want to change. # the lambda expression will be performed in the first two elements, generating one value
#that will be now our first element. This process will continue until there's only one element left.
#----------------------------------------------------------

#LIST COMPREHENSION = A way to create a new list with less sintax. It can mimic certain lambda functions, easier to read
                     #list = [expression for item in iterable]
                     #list = [expression for item in iterable if conditional]
                     #list = [expression if/else for item in iterable]

# squares = []   #create an empty list that will receive our values
# for i in range(1,11):  #We create a for loop wich 1 is inclusive and eleven is exclusive, like start and stop indexing.
#     squares.append(i*i) #It defines what each loop iteration should do. In this case,
                        # it will square each value in the range(1,11)
# print (squares)

#Or we can write the same program with less syntax using List Comprehension
# square = [i*i for i in range(1,11)]
# print (square)


# students = [100,90,80,70,60,50,40,30,0]
# approved_students = list(filter(lambda x:x>=60,students)) #we used the lambda function asssociated with filter function
# print (approved_students)

#or we can use List Comprehension instead of lambda function.
#aprovados = [i for i in students if i >= 60]
# print (aprovados)

#we can also put an else statement
# aprovados = [i if (i >= 60) else ("FAILED") for i in students] #the parentheses is optional for better read
# print(aprovados)
#----------------------------------------------------------------------

#DICIONARIES COMPREHENSION = Create dictionaries using an expressing. Can replace for loops and lambda functions
                            #dictionary = {key: expression for (key,value) in iterable}
#                            dictionary = {key: expression for (key,value) in iterable if conditional}
                            #dictionary = {key: expression if/else for (key,value) in iterable}
                            #dictionary = {key: function(value) for (key,value) in iterable}
#if the dictonary comprehension has if conditionals, the if statement must be on phrase's final. At the end of our dict
#if it has both if and else conditions, the if/else statement must be in the start, taking the place of the expression.
#if the expression is way too complex, you can also call a function instead of the expression.
#if its a dictionary, the iterable must be followed by '.items()'

# cities = {'New York':32,"Boston":75,"Los angeles":100,"Chicago":50}
# cities_C= {key:round((value-32)*(5/9)) for (key,value) in cities.items()}
# print(cities_C)
# hot_cities = {key:value for (key,value) in cities.items() if value>=60}
# print(hot_cities)
# disc_cities = {key:("warm" if value >= 70 else "cold") for (key,value) in cities.items()}
# print (disc_cities)
# weather = {'Bahia':"Quente","Sergipe":"Quente","Rio Grande do Sul":"Frio"}
# cold_states = {key:value for (key,value) in weather.items() if value =='Frio'}
# print(cold_states)
# def check_temp(value): #we created a function that is too big/complex to put in the dictionary comprehension
#     if value >= 70:    #this function will return one of these 3 values depending on the values stored in the our
#         return "HOT"   #dictonary.items()
#     elif 69 >= value >= 40:
#         return "WORM"
#     else:
#         return "COLD"
#
# checked_cities = {key:check_temp(value) for (key,value) in cities.items()}
# print(checked_cities)
#so it will print always the key, without changes, then the check_temp function will be called for each value in
#cities.items(), and for each value, some other value will return.
#---------------------------------------------------------------------

#ZIP(*ITERABLES) FUNCTION = Aggregate elements from two or more iterables (lists, tuples, sets, etc.)
#creates a zip object with paired elements stored in tuples for each elements.

# usernames = ["VazSM","F4stz1n","Luketa"]
# password = ("daniel23","slow123","luquinhas23")
# user_date = ["07/01/2023","07/03/2023","05/03/2023"]
#
# login = dict(list(zip(usernames,password))) #we created an zip object from a zip function, then we typecasted it as dict
# for key,value in login.items(): #For being a dict now, to print it we make a for loop with key,value-they are the values
#     print (key+": "+value)      #in login.items() - that is our collection/iterable.
# print (type(login)) #To se what type/class our object is. It is a dictonary, and we addressed username with passoword
#based on the same indexing

# logs = zip(usernames,password,user_date) #you can add more than 2 iterables
# for i in logs:
#     print(i)
#we created a zip object(logs) that contains username, password and user_date. So now we have paired them based on
#the same indexing.
#zip objects are iterable. And each one of it's elements is a tuple with paired values.
