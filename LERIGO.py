import random
import math
import time

#import give us access to all a module has to offer.
#random is actually pseudo-random. They don't generate true random values.
#x = random.randint(1,19) # it give us a integer random number inside the range
#y = random.random() #it give us a random float number between 1 and 0
#print(x)
#print(y)
#print ('{:.2f}'.format(y))
#print ('O resultado do sorteio foi: '+ (str((int(round(y*1000))))))

#lista= ['pedra','papel','tesoura']
#print (random.choice(lista))
#or
#z= random.choice(lista)
#print(z)

#SHUFFLE METHOD
#cards= [1,2,3,4,5,6,7,8,9,'J','Q','K','A']
#random.shuffle(cards) #it will shuffle(embaralhar) a list or other collection for you.
#print(cards)
#print(cards[:7])


#EXCEPTION = events detected during execution that interrupt the flow of a program
#Is good to use exception when writing a dangerous code
#or when you are accepting any input, because we don't know what the user is going to type in
#try:
 #   numerador = int(input('Digite um número para ser dividido: '))
 #   denominador = int(input('Digite um número para dividir o outro: '))
#    result = numerador / denominador
#    print(result)
#except ZeroDivisionError as e:
#    print (e)
#    print ('Você não pode dividir por zero! Canalha!')
#except ValueError as e:
#    print(e)
#    print ('Use apenas números inteiros')
#except Exception: #this is a global except, it expect every possible except, but it doesn't explicit the error
#    print ('Alguma coisa deu errado, tente novamente.')
#else:
    #print(result)
#finally:
    #print('finally sempre executará, acontecendo uma exceção ou não.')
#Quando há um evento que interrompe um código, o traceback dirá qual é a origem do erro
#Nesse caso, um erro acontecerá se tentarmos dividir o numerador por 0(denominador)-ZeroDivisionError
#Ou se tentarmos dividir por uma palavra, como 'pizza'-ValueError
#É um bom hábito especificar os eventos de erros. ex: expect ValueError.
#Para direcionar melhor o usuário sobre qual é o erro.

#try:
    #batman=None
    #while bool(batman) is False:
        #batman=(input('Batman is a ____? '))
        #print(batman)


#lista= ['elemento1','elemento2','elemento3'] # []ordenado, mutável, indexável
#outralista= ['ta1','ta2','ta3']
#receita = ['ovo','manteiga','açúcar']
#lista2d= [lista,outralista,receita] # Lista de listas. Lista multidimensional
#tuple= ('casco1','casco2','casco3') # ()ordenado, imutável, indexável
#sete={'gude1','gude2','gude3'} # {} desordenado, mutável, não é indexável
#dictionary= {'key','value'} #ordenado, mutável e único par de chaves,valores/ Key,Value
#dic= {'8':'oito','5':'cinco','2':'dois','4':'quatro'}
#for key,value in dic.items():
  #  print(value)
#print (dic.values())
#print (dic.items())
#print(lista2d[1][1])
#print(lista.index('elemento1'))
#lista.append('elemento4')
#sete.update(lista)
#print(lista
#print(tuple)
#print(set)

#for i in lista:
    #print(i,end=' ')
#for j in tuple:
    #print (j,end=' ')
#for k in set:
    #print(k,end=' ')

#nome = 'daniel vaz'
#if nome[0].islower():
   # nome= nome.capitalize()
  #  nome=nome.upper()
 #   print('Olá '+ nome)

#pnome=nome[:6].capitalize()
#snome=nome[7:].capitalize()
#print(pnome+' ' +snome)

#tartaruga = ('casco','patas','cabeça','rabo')
#print(type(tartaruga))
#print(tartaruga)
#tarta = tartaruga[0:3]
#print(tarta)

#def mult(*args):
 #   times= 1
   # for i in args:
     #   times*=i
    #return times

#print (mult(6,2,3))
#while True:
    #import random

    #escolhas = ['pedra','papel','tesoura']
    #computador = random.choice(escolhas)
    #player= None
    #while player not in escolhas:
     #   player = input('pedra, papel ou tesoura?: ').lower()

    #if player == computador:
        #print ('player: '+player)
       # print ('computador: '+computador)
      #  time.sleep(1)
     #   print ('Empate!')
    #elif player == 'pedra':
        #if computador == 'papel':
            #print('player: ' + player)
           # print('computador: ' + computador)
          #  time.sleep(1)
         #   print ('Você perdeu!')
        #elif computador == 'tesoura':
        #    print('player: ' + player)
       #     print('computador: ' + computador)
      #      time.sleep(1)
     #       print('Você ganhou!')
    #elif player == 'papel':
        #if computador == 'tesoura':
           # print('player: ' + player)
          #  print('computador: ' + computador)
         #   time.sleep(1)
        #    print ('Você perdeu!')
       # elif computador == 'pedra':
       #     print('player: ' + player)
      #      print('computador: ' + computador)
     #       time.sleep(1)
    #        print('Você ganhou!')
    #elif player == 'tesoura':
        #if computador == 'pedra':
         #   print('player: ' + player)
          #  print('computador: ' + computador)
         #   time.sleep(1)
          #  print ('Você perdeu!')
        #elif computador == 'papel':
           # print('player: ' + player)
          #  print('computador: ' + computador)
         #   time.sleep(1)
        #    print('Você ganhou!')
   # jogar = input('Você deseja jogar novamente? (Sim/Não) ').upper()
    #print (jogar)
    #if jogar != 'SIM':
        #break


#def kwarg(**opa): #it accepts varying amounts of values. But it must have key and value
    #like a dictionary. the arguments must be assigned to something
    #for key,value in opa.items():
       # print (value)
#kwarg(a='ola',b='dan',d=17,c=22)

#dicio= {'vogal':'aeiou','consoante':'bcdfgh'}

#for key,value in dicio.items():
    #print(key,end=' ')

#x = random.randint(1,19) # it give us a integer random number inside the range
#y = random.random() #it give us a random float number between 1 and 0
#print(x)
#print(y)
#print ('{:.2f}'.format(y))
#print ('O resultado do sorteio foi: '+ (str((int(round(y*1000))))))
##print ('valor: {} + {}'.format((str(int(round(y*2000)))),x))
#
#lista= ['ta',3,'ok']
#tuple= ('po','ra','nenhuma')
#set = {'oq',2,'tirando'}
#sera= [lista,tuple,set]
#random.shuffle(lista)
#print(lista)
#print (sera[0][0])


import os #import os module to file access
#file detection

#lugar = 'C:\\Users\\Vazsm\\Pictures\\texto.txt' #we create a variable to contain as value the
                                                # file path/endereço/local
#You need to double the backslashes
#if os.path.exists(lugar): #this code verify if the location of the file exists.
    #print ('That location exists')
    #if os.path.isfile(lugar): #this code verify if the location/path is a file
   #     print("It's a file")
  #  elif os.path.isdir(lugar):
 #       print ("It is a directory")#this code verify if the location/path is a folder/directory
#else:
    #print ("That location doesn't exist.")


#Open Files:
#try:
    #with open('C:\\Users\\Vazsm\\Pictures\\texto.txt') as file:
       # print (file.read())
#except FileNotFoundError as e:
    #print (e)
#print (file.closed)
#It may be the file path or the file name, if it is already inside the project
# Use 'with open' closes the file automatically

#Writing files:

#texto= 'Você é foda cara, não desista\nSeus esforços lhe darão bons resultados\nVocê terá uma vida boa'
#The '\n' goes to a new line of text. Acts like 'enter'.
#with open('teste.txt','w') as file: #with open can be used to create a file
    #by adding the file name, comma, and the "w" of write function
    #file.write(texto) #this write the content we want.
#with open('teste.txt','a') as file:
    #file.write('Acrescenta isso ai') #It adds a newline, but it does not
                                 #overwrite whats has already been written.
#with open has 3 options: 'r' to read, 'w' to write, 'a' to append/add.

#Copy Files:

import shutil
#copyfile() = copies contents of a file
#copy()= copyfile() + permission mode + destination can be a directory
#copy2() = copy() + copies metadata (file's creation and modification times)

#shutil.copyfile('teste.txt','copia.txt') #source and destination
#shutil.copy('teste.txt','copia.txt')
#shutil.copy2('teste.txt','copia.txt')

#Moving Files:
import os

source = 'teste.txt' #the file you want to move. It can be a folder as well
destination = 'C:\\Users\\Vazsm\\Desktop\\teste.txt' #The destination you want to put the file
#it can be a folder as well
#try: #to except an error
    #if os.path.exists(destination): #to verify if the destination has already a file with the same name
     #   print ('There is already a file there')
   # else: #if there is no file in the destination
    #    os.replace(source,destination) #os.replace will move the source to the destination
   #     print(source+" was moved")
#except FileNotFoundError: #except if the file index was not found.
   # print (source+" was not found")


#Delete a file

import os
import shutil

#os.remove('copia.txt') #it can be the path/endereço of the file, or it can be its name
                       #if the file is already inside the project folder
#path = 'C:\\Users\\Vazsm\\PycharmProjects\oimundo\\teste'
#try:
  #  os.remove(path) #deletes a file
  #  os.rmdir(path) #it only deletes empty folders
 #   shutil.rmtree(path) #it deletes folders/diriectory with files
  #shutil.rmthree() IS A DANGEROUS FUNCTION
#except FileNotFoundError:
 #   print ('The file was not found')
#except PermissionError as e:
  #  print (e)
#except OSError as e: #The folder contains files
  #  print (e)



#module = a file containg python code. It may contain functions, classes, etc.
#used with a modular programming, wich is to separate a program into parts

import tor
#or
import tor as t
#from tor import fome,tabom
#from tor import * #Não recomendável, pois pode causar conflito de variáveis
#tor.fome()
#or t.fome()
#or fome()
#tor.tabom()
#or t.tabom()
#or tabom()

#help('modules') #It lists all available modules
# or you can go to python official documentation: docs.python.org

#escolha = 'ta'
#escolha = escolha.upper()
#print (escolha)
