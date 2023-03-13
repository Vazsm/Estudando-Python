# A for loop is a statement that will execute it's block of code a limited amount of times
# His block of code can be 'print ()'
#'for () in' is short for 'for loop'
#range estipulates an amount of numbers; It contains start:stop:step
#i+1 adds 1 to every number in range.
#The stop in range is exclusive. To solve that, add '+1' to the stop value.
#For loop can also be used in strings. This way, there will be one line of code for each carachter.
#To creat a count down, we can use a for loop. We need to import time
#We'll use a for () in range () that contains a start, a stop and a minus step
#For that to work, the start must be bigger than the stop.
#We write 'print ()' on its block of code, and write 'time.sleep(seconds)'
#Than we will have a count down, that can be followed by a print that says something.
#for i in range (10):
    #print (i+1)
import time

#for i in range (15,19+1):
    #print (i)

#for i in range (20,32,2):
    #print (i)

#for i in 'Daniel':
    #print (i)

#import time
#for segundos in range (10,0,-1):
   # print (segundos)
    #time.sleep(1)
#print ('Feliz ano novo')

#Nested loop. It means a inner loop inside a outer loop.
#The inner loop will run all of it's iterations before finishing one iteration of the outer loop.
#Creates a rectangle
#We create variables with input values on it. Then we create a loop inside a loop.

#linhas = int(input('Quantas linhas você quer?: '))
#colunas = int(input('Quantas colunas você quer?: '))
#symbol = input ('Insira o síbomolo que você deseja: ')

#for i in range (linhas):
  #  for j in range (colunas):
   #     print (symbol, end='')
 #   print ()

#Loop Control Statements = change a loops execution from ites normal sequence

#break = used to terminate the loop entirely
#continue = skips to the next iteration of the loop
#pass = does noething, acts as a place holder

#while True:
    #name = input('Coloque o seu nome: ')
    #if name != '':
        #break

#telefone = '123,456,7890'
#for i in telefone:
    #if i == ',':
        #continue
    #print (i, end='')

#for i in range (1,21):
    #if i == 13:
        #pass
    #else:
       # print (i, end=' ')

#list = used to store multiple items in a single variable. A list can contain others lists inside.
#Each item in a list is referred as an element.
#A list can Always be updated.

#janta = ['pizza','hamburger','batata frita','churrasco']
#doces = ['oreo','milkshake','pudim','bolo','chocolate']
#comida = [janta,doces]
#janta.append('lasanha') #it increases elements
#doces.pop() #it removes the last element of a list
#doces.remove('bolo') #it removes the element you want
#janta.insert(2,'aipim frito')
#janta.clear #it removes/clears all elements of a list

#print(janta)
#print(doces)
#print (type(comida))
#janta[3] = 'sushi'
#used to replace an element by another.
#to display the elements of a list you can do a for loop
#for i in janta:
    #print (i)
#print(comida[1][0])
#print(comida[0])

#2D Lists = Multidimensional lists. A list of lists


#Tuples = collection wich is ordered and unchangeable
#Are used to group together related data

#estudante = ('Daniel',21,'Homem')
#print (estudante.count(21)) #It counts how many times an element shows up.
#print (estudante.index('Homem')) #It displays wich position is an element.

#if 'Daniel' in estudante:
    #print ('Olá, Daniel')
#for i in estudante:
    #print (i, end='')

#SET= collection wich is unordered, unidexable. No duplicate variables.

#talheres = {'faca','garfo','colher'}
#louça= {'prato','vasilha','panela','colher'}
#mesa = talheres.union(louça)
#print (mesa)
#talheres.add('espátula')
#talheres.remove('garfo')
#talheres.clear()
#talheres.update(louça) #this adds all the elements within louça to the talheres'set.
# print (talheres.difference(louça)) #it prints what talheres have that louça does not.
#print (talheres.intersection(louça)) #it prints what talheres and louça have in common


#for x in talheres: #in a set, the for loop does not necessary display the values in order
    #print(x)       #and it does not display elements with the same value

















