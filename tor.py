#def tabom():
   # print ('Está bem')
#def fome():
    #print ('Preciso comer alguma cosia')


# questions = {'Qual o seu nome? ':'D','Qual o nome da sua mãe? ':'A',
#              'Qual o nome do seu pai?':'D','Qual o nome do seu irmão?':'D'}
# options = [['A.André','B.Bruno','C.Carlos','D.Daniel'],
#                 ['A.Acidália','B.Bianca','C.Cida','D.Dália'],
#                 ['A.Antônio','B.Bob','C.Caio','D.Davi'],
#                 ['A.Ariel','B.Beto','C.Caique','D.David']]
#
# def new_game():
#     guesses = []
#     correct_guesses = 0
#     questions_num = 1
#
#     for key in questions:
#         print ('------------------------')
#         print(key)
#         for i in options[questions_num-1]:
#             print (i)
#         guess = input ('Enter (A,B,C,D)')
#         guess = guess.upper()
#         guesses.append(guess)
#         questions_num += 1
#         correct_guesses += check_anwser(questions.get(key),guess)
#     display_score(correct_guesses,guesses)
#
# def check_anwser(answer,guess):
#     if answer == guess:
#         print ('CORRECT!')
#         return 1
#     else:
#         print ('WRONG!')
#         return 0
#
# def display_score(correct_guesses,guesses):
#     print ('--------------------')
#     print ('RESULTS')
#     print ('--------------------')
#     print ('Answers: ', end='')
#     for i in questions:
#         print (questions.get(i), end='')
#     print()
#
#     print ('Guesses: ', end='')
#     for i in guesses:
#         print (i, end='')
#     print ()
#
#     score = int((correct_guesses/len(questions))*100)
#     print ('Seu score foi: '+str(score) +' pontos')
# def play_again():
#     response = input('Do you want to play again?: (yes or no)')
#     response = response.upper()
#     if response == 'YES':
#         return True
#     else:
#         return False
#
# new_game()
# while play_again():
#     new_game()
