#HEHEHHE
# if __name__ == '__main__':
#Python interpreter sets ''special variables'', one of wich is __name__
#An module can be run directly (when we run the module) or indirectly (when other module imports from the module)
#When we run a module, python automaticly stablish an special variable, in this case, __name__
#When we run a module(1) directly, the special variable __name__ equals to '__main__'
#This kind of say this is the main running module.
#When we run a module(1) indirectly, __name__ equals to the name we set when we created the module/python.file
#This means that we are executing another module(2), and in it's code(2), we have imported from the module(1).
#So we can have some use of the values of __name__ when the module runs directly or indirectly. That's why we use:
# if __name__ == '__main__':
#So we can stablish when something should run. If it should run only by it's directly module or if it can run indirectly
#1.Module can run be run as a standalone program (Directly)
#2.Module can be imported and used by other modules (Indirectly)
#This expression gives our modules some flexibility
import time

# if __name__ == '__main__':
#     print ('Running this module directly!')
# else: #if __name__ != '__main__' that means that some of what is running have been imported from other module
#     print ('Running other module indirectly!')
# print (__name__) #if this module were imported, the result would be the name we gave to the module/python.file
                 #but as we run the module directly, the result is "__main__"
# import Jane
# print(Jane.__name__) #The result is 'Jane' because Jane is running indirectly, it is not the main module running.

# def hello():
#     print('Hello')
# if __name__ == '__main__':
#     hello() #This way, when this module is imported, __name__ won't be equal to '__main__'
    # and it won't call the hello() function.
# if __name__ == '__main__':
#     print ('Isso é um teste') #If this module runs indirectly, it will not print anything.
# def main():
#     print ('Could be the main body of your program')
# if __name__ == '__main__':
#     main() #The main body of your program will execute if the module runs directly.
#--------------------------------------------------------------------


#TIME MODULE
import time
#epic or epoch = a date and time from wich a computer measures system time.
#epoch = Date and time wich you computer think times began. Is a reference point.
# print (time.ctime(0)) #this method will convert a time expressed in seconds since Epoch to a readable string.
#as we passed 0 as it's time, it will print our epoch, our date and time reference point.
# print (time.ctime(1006177700)) #This time expressed in seconds since epoch, will print a date and time.
# print (time.time()) #This prints the exactly amount of time in seconds that has passed since epoch.
#Return current seconds since epoch, using our computer's clock. If we change our computer's clock(date/time),
#the time expressend in seconds will also change

# print (time.ctime(time.time())) #It gives us the date and time since epoch converted in readable string. We use the
#time.time() to return us the current seconds since epoch. The current seconds converted in a readable string give us
#the date and time

#another way to retrive the current date and time is to use:
# time_object = time.localtime() #the time.localtime() method allows us to create a variable called time_object
                               #based on current time
#a time_object is also referred as a struct_time object. It is made of different keywords arguments.
#it has a year, a month, a day, a hour, a minute, a second, a day of the week, a day of the week,
# and a daylight savings time
# print (time_object)
#there's some uses for the time_object. We can format them however we want. As it is not in a readable format.
#to convert the time_object into a readable function we need to call the function:
# local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)
# print(local_time)
#this function needs two arguments, a format and a time(our time object)
#format in time = a string of different directives. The directives can be embedded in the format string that
# we are passing as arguments.
#Each directive has a respective meaning that will be displayed as the time_object respective value.
#You can add any combination of directives, not necessarily one.
# %B = name of the month ; %d = day ; %Y = year ; %H for the hour; %M = minutes; %S = seconds
#We created an object that contains the time.localtime() function. It is not readable, so we now create another object
#that contains the time.strftime() function that convert an object (time_object) to an readable string.
#and then we print the new object (local_time) to get the current date and time.

#You can also get the UTC time = Coordinated Universal Time, that is the primary time standard
# by wich world regulates time clocks and time. It is within about 1 second of mean solar time at 0º longitude.
#And it's not adjusted for daylight saving time.
#if you need that:
# time_object1 = time.gmtime()
# local_time = time.strftime("%B %d %Y %H:%M:%S",time_object1)
# print(local_time)

# time_string = '20 April, 2020'
# string_converted_to_time_object = time.strptime(time_string,'%d %B, %Y')
# print (string_converted_to_time_object)
#this time.strptime() function converts a time string (readable) into a time object (not readable)
#this function have two arguments, the time_string we would like to convert, and the format of the time object that we
#would like to pass in.
#In this example, the time string is 20 April, 2020. So we have to create the time object format as %d for day,
# %B for the name of the month, and %Y for the year.
#we use the time.strptime() to create an object. And then we print this object.

#a time object has:
# (year, month, day, hours, minutes, seconds, day of the week, day of the year, and dst[daylight saving time]

# time.asctime(tuple,time_object) will convert a time object, or, a tuple representation of date and time into a
# readable time_string
# time_tuple = (2020,11,19,19,20,0,0,0,0) #we have to pass it 9 values to represent it as a time_object
# time_string = time.asctime(time_tuple)
# print(time_string)

# time_tuple = (2020,11,19,19,20,0,0,0,0)
# time_string = time.mktime(time_tuple) #it converts a tuple_time or a time_object into a string of the amount of seconds
# print(time_string)                    #since epoch.

#THREADING = A flow of execution. Like a separate order of instructions.
#           However, each thread takes a turn running to achieve concurrency (simultaneamente)
#GIL = Global Interpreter Lock. It allows only one thread to hold the control of the Python Intepreter at any one time
#Only one thread can be running at on time, but they can all take turns when one thread is idle(parado/inativo)
#They run concurrently, but not truly in parallel
# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
            # USE MULTIPROCESSING #They run concurrently, in parallel

# io bound = program/task spends most of it's time waiting for external events (USER input, web scrapping)
            # USE MULTITHREADING #They run multiple threads concurrently, but not truly in parallel

import threading
import time

# print (threading.active_count()) # We can count the number of threads that are concurrently running in the background
#whenever we run a program, we have one thread that is running that is in charge of executing our program
#that is our main thread
# print(threading.enumerate()) #It lists all of our active threads, the threads that are running.
#In this case we have only one thread running, that is responsable for executing our program.
#That is referred as the MainThread. It runs the main body of our program.
#We can have more than one thread running cuncurrently, but not truly in parallel. All the thread will take turns, while
#one of them is idle.
#The MainThread runs the main body of our program.
# But we can have more than one thread running, executing a countdown timer,for example.
#We can have different threads in charge of different parts of our program. They all take turns, while one is idle

#lets create a multithreading program:

# def eat_breakfast():
#     time.sleep(5)
#     print ('You eat breakfast')
# def drink_coffe():
#     time.sleep(4)
#     print ('You drank coffe')
# def study():
#     time.sleep(7)
#     print ('You finished studying')

#these functinons are IO bound. They take time waiting for external events. They are waiting for the sleep function
#expires before they finish their task
#eat_breakfast()
# drink_coffe()
# study()

#It takes 16 seconds to complete all of these functions. That's because we are running them with the main thread.
#So to complete each task, they have to wait for the time.sleep function to expires. Whe we do that, our whole program
#have to wait until the time has passed, before they can continue executing instructions.
#As we execute only with the main thread, we can not run these functions cuncurrently, as we would do in real life.
#We are completing these taks sequentially, not concurrently
#We have one thread to complete 3 tasks. So we what we would do is create 3 more threads, one for each task
# and remain our MainThread in charge of the main body of our program.
# x = threading.Thread(target=eat_breakfast,args=()) #using the threading module, we use the thread function that creates
# y = threading.Thread(target=drink_coffe,args=()) #a new thread to execute a target, assuming or not arguments.
# z = threading.Thread(target=study,args=()).start()
# x.start() #starts the new thread
# y.start()
# #z.start()
#REMEMBER to comment the calling functions within the mainthread, so we only execute them in our other threads.
#You can also pass arguments by doing : z =threading.Thread(target=study(),args=(arg1,arg2))
#if your functions has parameters.
#The program has finished in 7 seconds, as we executed them concurrently, not sequentially (as the mainthread would do)
#And the print functions has been displayed first, that's because the MainThread has executed them sequentially, without
#waiting for the time.sleep function from the 3 tasks to complete.
#The MainThread is in charge of create 3 additional threads, and execute it's own tasks.
# print (time.perf_counter()) #Performance counter from our time module.
#It displays how long our calling threads and our mainthread to finish executing it's set of instructions

#We can use the Thread Synchronization. It makes the MainThread to wait for another thread to finish before executing
#it's own set of instructions.
# x.join() #Thread Synchronization. The MainThread has to wait for the X Thread to finish.
# print ('The main thread has waited for the x thread to finish the job')
#When the calling threads are synchronized, they're no longer active, so it will not count/enumerate as an active thread
#--------------------------------------------------------------

#DAEMON THREADS = a thread that runs in the background, they are not important for program to run
#your program will not wait for daemon threads to complete before exiting.
# non daemon threads cannot normally be killed, they stay alive until task is complete

#ex: background tasks, garbage collection, waiting for input, long running process.

# import threading
# import time
#
# def timer(): #a function to print how long is running.
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print('This program is running for {} seconds'.format(count))
# x = threading.Thread(target=timer,daemon=True) #this is a deamon thread. And it'll be in charge of the timer() function
# x.start() #starts the x thread, running concurrentlt while the MainThread waits for some user input
# answer = input('Enter anything: ') #Our MainThread will be in charge for waiting some user input.
# When we receive some input, the MainThread will finish it's process along with all the daemon threads.
#The program will not exit if there is still Non-Daemon Threads running.
#The program will exit even when Daemon Threads are running. If there's no Non-Deamon Threads(Important threads) running
#When important Threads are running we cannot exit the program, unless we do so by brute force(Stop)
#x.setDaemon(False) #This change a thread to either a non deamon thread('False') or a daemon Thread('True')
#But this need to be placed/changed before the thread is running (before the x.start() function)
#print (x.isDaemon()) # It should return True (it is a Daemon Thread) or False (it is not a Daemon Thread)
#-----------------------------------------------------------------

#Python Multiprocessing
#MULTIPROCESSING = running tasks in parallel on different cpu cores, bypasses GIL used for thread
            #Multiprocessing = better for cpu bound tasks (heavy cpu usage) #We can create process, and each process
            #runs in parallel on a different cpu core.
            #Multithreading = better for io bound tasks (waiting around) #It is limited in python due to GIL,
            #runs threads concurrently, but not in parallel.

# from multiprocessing import Process,cpu_count
# import time

#If you're running  a windowithws system, put the main body of your program inside a if __name__ =='__main__)
#This way, it will avoid to create several child process from when you create a single child process.
#When our model is executed, it will copy our code, but it won't execute our main

# def counter(num):
#     count = 0
#     while count < num:
#         count += 1
# def main():
#     print (cpu_count()) #It counts the number of process you can create based on what your cpu is capable of.
    #creating more process than what you can, it will make your program run slower, because it's going to delete one
    #process to create another process. It hinders the perfomance of the computer.
    # a = Process(target=counter,args=(250000000,)) #we have created a process to execute the counter function, passing
    # b = Process(target=counter,args=(250000000,)) #a number as argument. It has to be a comma after, to act like a tuple
    # c = Process(target=counter,args=(250000000,))
    # d = Process(target=counter,args=(250000000,))
    # a.start()
    # b.start()
    # c.start()
    # d.start()

    # a.join()
    # b.join()
    # c.join()
    # d.join() #Process Synchronization. The main process will wait the child process finish before continuing
    # print ('Finished in {} seconds'.format(time.perf_counter()))
#It took about 56 seconds to finish our program that counts from 0 to 1 billion.
#We can speed things up by doind MULTIPROCESSING. So we create other process and we divide the args by 2,3,4...
#We divide the amount of work/task in 4, for 4 new process. It took abou 47 seconds
# if __name__ == '__main__':
#     main()


