#dictonary = A changeable, unordered collection of unique key:values pairs.
#They are fast because they use hashing, allow us to acess the value quickly
#They are changeable, by that means, we can change them after our programming is running.
import time


#capitais = {'Brasil':'Brasília',
            #'Argentina':'Buenos Aires',
            #'EUA':'Wahington DC',
            #'Japão':'Tóquio',}

#capitais.update({'Itália':'Roma'})
#capitais.pop(Japão)
#capitais.clear()
#capitais.update({'EUA':'Las Vegas'}) #We changed the capital of EUA by adding another value to it.

#for key,value in capitais.items():
   # print(key,value)
#print(capitais['Japão'])
#print (capitais.get('Alemanha')) #The get function helps us to verify is the key exists in our dicionary.
#It gets us the value
#print (capitais.keys()) #It prints only the keys of our dicionary
#print (capitais.values())#It prints only the values of our dicionary
#print (capitais.items()) #It prints both the key and values of our dicionary

#for i in capitais:  #it prints the keys, unordered.
    #print (i)
#for key,value in capitais.items():
    #print (key,value)

#Index operator []= gives us acess to a sequence's elements (str, list,tuples)

#nome = 'daniel vaz'
#if nome[0].islower():
    #nome= nome.capitalize()
    #nome=nome.upper()
    #print('Olá '+ nome)

#pnome=nome[:6].capitalize()
#snome=nome[7:].capitalize()
#print(pnome+' ' +snome)

#FUNCION = a block of code wich is executed only when it is called. Inoking a function
#Functions avoids repetition
#If you want to input some data to function, there has to be some parameters inside the parentheses
#That parameter needs to match in the function block of code. This is where the
#Input data will go.
#The inputed information name is Arguments. They are the information you are sendind to a function
#Arguments can be strings, integers, floats, variables, lists, tuples...

#def hello(name):
    #print ('Feliz aniversário '+ name)

#hello('Daniel')

#def olá (nome,sobrenome):
   # print ('Olá, '+ nome + ' '+sobrenome)
   #print('Você tem '+ str(idade)+ 'anos de idade)
#nome= 'Daniel' #The arguments does not need to be the same as the parameter. It could be first_name instead
#sobrenome = 'Vaz Sampaio Moura'
#idade=21
#olá (nome,sobrenome,idade)

#def bronca():
   # pergunta = input('Foi você que fez isso? ')
    #if pergunta.find('sim'):
        # ('Você não deveria ter feito isso, mas eu vou perdoar já que você admitiu.')
    #elif pergunta.find('não'):
        #print ('Além de vândalo é desonesto, vou chamar a polícia.')
    #else:
        #time.sleep(1)
        #print ('Vou chamar a polícia.')

#bronca()

#Return Statement = Funcions send Python values/objects back to the caller
#These values/objects are known as the function's return value.

#def multiplicar(number1,number2):
    #resultado=number1*number2
    #return resultado
#x =multiplicar(6,8)
#print (x)

#def multiplicar(number1,number2):
    #return number1*number2
#print (multiplicar(6,8)) #This way is wrtitten in less lines of code
dicio = {'Dois':'2','Cinco':'5','Seis':'6'}
for key,value in dicio.items():
    print (value)




#Keywords arguments = arguments preceded by an identifier when we pass tem to a function.
#The order of the arguments does not matter, unlike positional arguments.
#Python knows the names of the arguments that our function receives.

#def olá (nome,sobrenome,apelido):
    #print ('Olá, '+nome + ' '+sobrenome+'. Também conhecido como, '+apelido)
#olá(apelido='Vazsm',sobrenome='Vaz Sampaio Moura',nome='Daniel')
#the arguments are assigned by using the same parameter as the parameters inside the parentheses.

#Nested functions calls = function calls inside other funcion calls
#innermost funciont calls are resolved first
#returned value is used as argument for the next outer function

#num = input('Digite um número inteiro: ')
#num = float(num)
#num = abs(num)
#num = round(num)
#print (num)
#this can be written in a smaller amount of lines:

#print (round(abs(float(input('Digite um número inteiro: ')))))
#the input function return a value that becomes the argument for the outer function.
#and it keeps going until the print function.


#scope = The region that a variable is recognized.
#A variable is only available from inside the region it is created.
#A global an locally scoped versions of a variable can be created.

nome = 'Daniel' #a global scope (available inside and outside functions)

#def mostrar_nome():
    #nome='Vaz' #a local scope (available only inside this function)
  #  print(nome)
#mostrar_nome()
#print (nome)
#the priority sequence of scopes is LEGB (Local version, Enclousing, Global version, Built-in)

#*args = parameter that wil pack all arguments into a tuple
#useful so that a function can accept a varying amount of arguments

#def soma(n1,n2):
    #soma=n1+n2
   # print(soma)
#soma(4,5)
#this is how we would do this math, but this way we couldn't add more arguments, more values.
#a way to change that is:

#def add(*args): #the important thing is the '*'.
    #sum=0
    #for i in args:   #For being a tuple, we cannot change the values of the given arguments
        #sum+=i       # For that, turn the tuple (unchangeble and ordered) into a list (changeble and ordered)
   # return sum
#print (add(3,4,5,12))

#def add(*args): #the important thing is the '*'.
 #   sum=0
  #  for i in args:
   #     sum+=i
    #return sum
#print (add(3,4,5,12))


#def adicionar(*args):
    #soma=0
    #args=list(args)
   # args[0]=0   #we turn the tuple into a list and we can change the args value
   # for i in args:
     #   soma+=i
  #  return soma
#print (adicionar(9,1,12,8))


#**kwargs = Parameter that will pack all arguments into a dictionary
#useful so that a function can accept a varying amount of keyword arguments

#def olá(**kwargs):

    #print('Olá, ', end='')
    #for key,value in kwargs.items():
        #print(value,end=' ')

#olá(meio='Vaz Sampaio',nome='Daniel',final='Moura')

#print ('Olá, '+kwargs['nome']+ ' '+kwargs['meio']+' '+kwargs['final'])

#str.format() = optional method that give users more control when displaying output

#animal = 'vaca'
#item = 'lua'
#print ('A '+animal+' pulou a '+item)
#print ('A {} pulou a {}'.format(animal,item))
#print ('A {0} pulou a {1}'.format(animal,item)) #Positional arguments
#print ('A {animal} pulou a {item}'.format(animal='vaca',item='lua'))
#text='A {} pulou a {}'
#print(text.format('vaca','lua'))

#As chaves/curly braces are kwown as the format fields,They function as a placeholder for
# a value or a variable. They work in order the first format field will insert the
# first value/parameter

#def conto(animal,item):
    #print ('A {} pulou a {} durante o crepúsculo'.format(animal,item))

#conto('vaca','lua')

#nome ='Daniel'
#print ('Olá, meu nome é {}. Prazer em conhecê-la'.format(nome))
#print ('Olá, meu nome é {:10}. Prazer em conhecê-la'.format(nome)) #it spaces ten times to the right
#print ('Olá, meu nome é {:<10}. Prazer em conhecê-la'.format(nome))#it spaces ten of times to the right
#print ('Olá, meu nome é {:>10}. Prazer em conhecê-la'.format(nome))#it spaces ten of times to the left
#print ('Olá, meu nome é {:^10}. Prazer em conhecê-la'.format(nome))#it spaces five to the left and 5 to the right.
#print ('Olá, meu nome é {nome:>10}. Prazer em conhecê-la'.format(nome='Daniel'))

number = 3.14159
print('The number Pi is {:.2f}'.format(number)) #f means float, and 2 is the number of decimals portions
#its good to remember that this trick rounds the float.
#number=100000000
#print('The number is equal to {:,}'.format(number))
#print('The number is equal to {:b}'.format(number)) #it is a binary representation of your number
#print('The number is equal to {:o}'.format(number)) #it is a octal representation of your number
#print('The number is equal to {:X}'.format(number)) #it is a hexadecimal representation
#print('The number is equal to {:x}'.format(number))
#print('The number is equal to {:E}'.format(number)) #it is a scientifc notation representation























