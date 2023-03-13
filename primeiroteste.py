#Input é a entrada de dados pelo usuário
#Quando atribuímos input à uma variável, o valor da variável será de acordo com o dado de input
#Ou seja, a variável corresponderá ao valor emitido pelo usuário
#nome = input ('Qual o seu nome? ')
#age = int(input('Qual a sua idade? '))
#altura = float(input('Qual a sua altura?'))
#print ('Parabéns, ' +nome + '! Você acaba de se inscrever no nosso curso de programação.')
#print ('Você tem ' +str(age)+ ' anos de idade')
#print ('Você tem ' + str(altura) + ' metros de altura')
#ananas = int(input('Quantas bananas você comeu hoje? '))
#bananas = bananas*5
#print ('então amanhã você terá que comer '+ str(bananas) + ' bananas.' )
import math

#dia = int(input('que dia é hoje? '))
#dia = dia+7
#print ('semana que vem será dia ' + str(dia))

#import math
pi=3.14
x= 2134
y=5413
z=3123
print (round(pi))
print (math.ceil(pi))
print (math.floor(pi))
print (abs(pi))
print (pow(pi,2))
print (math.sqrt(pi))
print (min(x,y,z))
print (max(x,y,z))

#Slicing create a substring by extracting elements from another string
#It can be indexing[] or slicing()
# [start:stop:step] (start,stop,step)
# Remember that start is inclusive and stop is exclusive.
# Se você colocar somente os dois pontos o programa abrangerá o início ou final [4:]
#Start corresponde ao elemento inicial do seu corte (inclusivo
#Stop corresponde ao elemento final do seu corte (exclusivo)
#Step seleciona e corta elementos a partir de um ponto, obedecendo um intervalo estabelecido
#cortar = 'Alguma coisa'
#print ('leinad'[::-1])
#cortado = cortar[0:6]
#print (cortado)
#cortado_em_partes = cortar[1::2]
#print (cortado_em_partes)

#slicing()
#this kind of slicing creates a object that can be reusable
#all elements have a positive index and a negative index
#positive index start on the first element of the left by the value of 0
#negative index starts on the first element of the right by the value of -1
#website1 = 'http://google.com'
#website2 = 'http://wikepedia.com'
#slice = slice(7,-4)
#print (website1[slice])
#print (website2[slice])

#if statement is a line of code that will execute only if it's condition is true.
#age= int(input('quantos anos você tem?'))
#if age>=48:
    #print ('já tem vaga prioritária')
#elif age>=18:
   # print ('Já pode ser preso, cuidado.')
#elif age<0:
   # print ('você ainda não nasceu')
#else:
    #print ('você ainda é uma criança')

#logical operators (and, or, not)= used to check if two or more conditional statements are true.
#logical operator 'not' flips true into false, and false into true.
#temp = int(input('Qual é a temperatura de hoje?: '))

#if not (temp ==74 or temp <= 30):
    #print ('a temperatura está boa hoje')


#name = '1234567'
#while len(name) < 8:
    #name = input('Crie uma senha com pelo menos 8 caracteres: ')
#print ('Sua nova senha é: '+name)

#nome = None
#while not nome:
    #nome=input('qual o seu nome?')
#print ('olá, '+nome)




