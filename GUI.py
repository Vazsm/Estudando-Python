#GRAPHICAL USER INTERFACE (GUI):
from tkinter import *
#we import everything within tkinter module

# widgets = GUI elements: buttons, textboxes, label, images
# windows = Serves as a container to hold or contain these widgets.

# window = Tk() #instantiate an instance of a window for us #it creates our windows, but it does not display it
# we also cannot display our window how we would normally do: print (window)
#we use:
# window.geometry('600x450') #window.geometry('width x heigth') #
# window.title('Vaz Code - GUI') #it changes the title of our window
# icon = PhotoImage(file="logo.png") #it has to be in png format
#we choose the icon logo, but it does not have the tkinter format of picture,
# so we have to turn it into a PhotoImage.# and we create an object that equals to
# PhotoImage() function that must have as arguments file='name of the file'/"file's path"
#We can write the name of the file if we have already placed the photo inside our project folder ('oimundo')
#Otherwise, we must write the file's path
#Our original photo does not have the tkinter format of picture, so we have to turn it into a PhotoImage.
# window.iconphoto(True,icon)#it sets the iconphoto of our window as the icon object we created.
# window.config(background='#66bd7d') #it can be just the name of the color, black,green,grey,blue
#or it can be in hexadecimal color. You can find searching hex color picker. hashtag represents the hexadecimal value
# window.mainloop() #place window at our computer screen, and listen to events.

#we use windos.Tk() to create a window. and we use windos.mainloop() to display our window
#Whatever window function that is between these two functions, are going to personalize our window.
#---------------------------------------------------------------------
#This is how we can resize a image
# from PIL import Image
# img = Image.open('logo.png')
# width = img.width//10
# height = img.height//10
# img_resized = img.resize((width,height))
# img_resized.save('redmen.png')
#--------------------------------------------------------------

# LABEL = An area widget that holds text and/or an image withing a window

# from tkinter import *
# window = Tk() #we create a window to act like a container to hold a label/widget
# window.geometry('1690x2495') #It defines the dimension of the window.
# img = PhotoImage(file='redmen.png') #Create an photoimage object that contains as a file, a image's name or path
# label1 = Label(window,
#                text='Avatar', #Text may containg a string
#                font=('Papyrus',28,'bold'), #Font can contain a type, a size and a style like italic, underline...
#                fg='#00FF00',#Fg is short for foreground (primeiro plano). It is the string color.
#                You can put a name of a color, or a hex color value
               # bg='purple',
               # relief=RAISED, #It creates a border for our label. SUNKEN...
               # bd=5, #It sets the size of our border.
               # padx=16, #It sets a padding/ a space between the border label and the string. By the x axis
               # pady=16, #It sets a padding/ a space between the border label and the string. By the y axis
               # image=img, #We set a image to be in our label. But this way, the string will be fully replaced by img.
               # compound='bottom')#Doing this, both image and text can be in our label. Top, bottom, left or right
#The parentheses will act like the constructor, assigning values to label attributes. So we have to pass some
# keyword arguments inside the parentheses.
#window is the master for that widget, because window acts like a container for that label/widget.
#by adressing window as the label's master/container, it is not enough to display our widget
#to do that, we need to actually ADD the label to the window:
# label1.pack() #it adds the new label to the window.
#the pack function automatically places our widgets in the top center of our window. To choose the position of the label
#we have this option:
#label1.place(x=0,y=0) #it places our label by the amount of pixels that we want. It's like a coordinate for a position.
#Our label takes only the space that it needs, it have limitations. It can be increased or decreased to accommodate the
#components that it haves
# window.mainloop()
#---------------------------------------------------

#BUTTON = You click it, and it does stuff

# from tkinter import *
# count = 0
# def click():
#     global count #it lists count as a global variable so we can acess the count variable
#     count +=1
#     print ('You clicked the button {} times'.format(count))
#
#
# window = Tk() #creates the window to contain widgets
# photo = PhotoImage(file='pylogo.png') #the photo object must be created inside between Tk() and window.mainloop()
# button = Button(window, #button object = Button function, that has args for it's constructor '()', window is it's master
#                 text='Clique aqui', #we create some text to be put in our button widget
#                 font=('Arial',30,), #we choose the font style and size
#                 foreground='#00FF00', #we choose the font color
#                 bg='black', #we choose the background color
#                 activeforeground='#00FF00', #we choose the activeforeground color, the color when we click the button
#                 activebackground='black', #we choose the activebackground color, the color when we click the button
#                 command=click, #It's a callback, it calls a function when the button is active. Make sure
# the function name does not have the parentheses. When we click the button, it performs a callback, and it performs
# whatever is within the function.
                #state=DISABLED #When disabled, you can no longer click the button.
                # image=photo,
                # compound='bottom') #allows us to display both image and text. We can choose the direction of the image
# button.pack()
#
# window.mainloop()
#---------------------------------------------------------------------------------

#ENTRY BUTTON/BOX/WIDGET = Text box that accepts a single line of user input

# from tkinter import *
# def submit(): #The function must be created outside the window.
#     username = entry.get() #get is a function that return us the value of something, in this case the value of entry.
#     print ('Hello {}'.format(username))   #and this value is being stored on the variable username
#     entry.config(state=DISABLED) #after we submit, the entry box will be disabled
# def clean():
#     entry.delete(0,END) #It takes 2 positional arguments, we use the index 0 as start, and 'END' as the stop.
# def backspace():
#     entry.delete(len(entry.get()) -1,END) #To execute the backspace function we need to place the second last character
#     and the last index. So we get the entire length from the value returned from entry.get(), and subtract by one
    #this way, we will have the second last index
# window = Tk()
#
# entry = Entry(window,font=('Arial',30),
#               show="*") #It will only displays '*' when the user types something in the entry widget.
#                         But the text is only hidden in the entry widget, when we display it, the real word comes in.
#                         It useful for passwords
#entry.insert(0,'At index 0, display some default text')
# entry.pack(side=LEFT) #When you pack a widget you can set on what side they must be placed
#
# submit_button = Button(window,text='Submit',command=submit, #callback the submit function
#                        font=('Arial',20),foreground='#00FF00',background='black',
#                        activeforeground='#00FF00',activebackground='black')
# submit_button.pack(side=RIGHT)
#
# clean_button = Button(window,text='Clean',command=clean, #callback the submit function
#                        font=('Arial',20),foreground='#00FF00',background='black',
#                        activeforeground='#00FF00',activebackground='black')
# clean_button.pack(side=RIGHT)
#
# backspace_button = Button(window,text='BackSpace',command=backspace, #callback the submit function
#                        font=('Arial',20),foreground='#00FF00',background='black',
#                        activeforeground='#00FF00',activebackground='black')
# backspace_button.pack(side=RIGHT)
# window.mainloop()
#________________________________________________________________________

#CHECK BUTTON/BOX/WIDGET =

# from tkinter import *
# def display():
#     if x.get() == 1: #that means that x value is 1, that is, the button is toggled on.
#         print('You agree')
#     else:
#         print ("You don't agree")
# window = Tk()
# x = IntVar()  #IntVar for an integer value, StringVar for a string value, BooleanVar for a boolean value
#The x variable must be created inside the window instance.
# img = PhotoImage(file='pylogo.png')
# check_button = Checkbutton(window,
#                            text='i agree to something',
#                            variable=x, #checkbuttons stores in our variable by default 0 or 1. But we can change that
#                            onvalue=1, #If the button is toggled on, it's default value equals 1. It could be True
#                            offvalue=0, #It could be False
#                            command=display,
#                            font=('Arial',20),
#                            fg="#00FF00",
#                            bg='black',
#                            activeforeground='#00FF00',
#                            activebackground='black',
#                            padx=15,
#                            pady=15,
#                            image=img,
#                            compound='left')
# check_button.pack()
#
# window.mainloop()
#-------------------------------------------------------------

#RADIO BUTTONS = Similar to checkbox, but we can only select one from a group

# from tkinter import *
#
# food = ['pizza','hotdog','hamburger']
# def order():
#     if x.get() == 0:
#         print('You ordered pizza')
#     elif x.get() == 1:
#          print('You ordered hotdog')
#     elif x.get() == 2:
#         print('You ordered hamburger')
#     else:
#         print ()
# window = Tk()
# x = IntVar()
# pizza_img= PhotoImage(file='pylogo.png')
# hamburger_img= PhotoImage(file='hamburger.png')
# hotdog_img= PhotoImage(file='hotdog.png')
# food_img = [pizza_img,hotdog_img, hamburger_img]
# for index in range(len(food)): #Put the radio button in a for loop, so we can iterate with all items within our list
#     radio_button = Radiobutton(window,text=food[index],#we are instatiating one button for each item in the list.
#                                variable=x, #Groups radio buttons together if they share the same variable
#                                value=index, #Assigns each radio button a different value
#                                padx=10, #Adds padding on x-axis
#                                pady=10, #Adds padding on y-axis
#                                font=('Papyrus',15),
#                                image=food_img[index], #adds image to each radio button
#                                compound='right',
#                                indicatoron=0, #eliminates circle indicators. Turn the images/text into push buttons
#                                width=375, #sets width of radio buttons.
#                                command=order)
#
#     radio_button.pack(anchor=W) #W short for west.
# window.mainloop()
# --------------------------------------------------------------------

#SCALE =

# from tkinter import *
# def submit():
#     print ('It is {} degrees Celsius'.format(scale.get()))
#
# window = Tk()
# hot_image = PhotoImage(file='hotdog.png') #make sure to create the photo image after the window instance and
# before the scale widget. This way, the label will be on top of the window
# hot_label = Label(window,image=hot_image) #we create a label inside our window and set that label to contain a hot image
# hot_label.pack()
#
#
# scale = Scale(window,
#               from_=100, #we can set a 'from position' and a 'to position'. They'll be our scale range of values
#               to=0, #make sure to put the undersocre after from.
#               length=500, #sets the length of our scale.
#               orient=VERTICAL,#Orientation of scale. It can be vertical or horizontal
#               font=('Papyrus',20),
#               tickinterval=10, #numeric indicators for values on scale
#               showvalue=0, #hides the current value
#               troughcolor='blue', #it changes the trough color (sliding portion)(calha)
#               fg='#00FF00',
#               bg='black')
#
# scale.set((scale['from']+scale['to'])/2) #Sets a default start for our scale. In this case from doesn't have underscore
# scale.pack()
#
# cold_image = PhotoImage(file='pylogo.png')
# cold_label = Label(window,image=cold_image)#
# cold_label.pack()
# Adding a label inside the window instance and after the scale widget. This way, the label'll be on bototm of the window
# button = Button(window,text='Submit',command=submit)
# button.pack()



# window.mainloop()

#-----------------------
#tentando enviar pro git