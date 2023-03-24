#GRAPHICAL USER INTERFACE (GUI):
import email.policy
import time
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

#LISTBOX = A listing of selectable text items within it's own container
# from tkinter import *
# def submit():
    #order = listbox.get(listbox.curselection())
    # #We use .curselection() to get the current selected values.#SINGLE selection
    # We may or may not store that in a variable
    # food = []
    # for index in listbox.curselection(): #it is going to iterate once for each item that we selected.
    #     food.insert(index,listbox.get(index)) #index = index of a current selection. get(index) = the name/value of the
       # element referred to that index

    # print ('You have ordered: ')
    # for i in food: #we make a for loop to print iterate through the items.
    #     print (i)


# def add():
#     listbox.insert(listbox.size(),entrybox.get()) #for the add function we must insert an element on the listbox
#to insert a element, we need to pick the index of this element, and what element will be.
#listbox.size() gives us the current amount of elements of our list.
#entrybox.get() will give us the value inside the entrybox. That is, all the user input for the new item/element.
    # listbox.config(height=listbox.size() + 2) #for each new item, our list will be ajusted. We have already write
# this code down bellow, but this is necessary for after running changes.
# def delete():
#    listbox.delete(listbox.curselection()) #deletes our listbox current selection #for SINGLE selection
    # for index in reversed(listbox.curselection()): #We used 'reversed' to not change the indexes after we delete an item
    #     listbox.delete(index)
    # listbox.config(height=listbox.size() + 2) #to adjust our list height after we change an item.
# window = Tk()
#
# listbox = Listbox(window,fg='#fcba03', bg='black',font=('Ink free',20),
#                   selectmode=MULTIPLE #Allows you to select multiple items. #But it obly us to make some
                  # changes in our code. We have to turn the functions into functions for multiples items (for loop).
                  # )
# listbox.pack()
# listbox.insert(1,"pizza") #We pick an index and place a value for that index.
# listbox.insert(2,"cake")
# listbox.insert(3,"bread")
# listbox.insert(4,"salad")
# listbox.insert(5,"chicken")
#
# listbox.config(height=listbox.size()+2) #We use .config to change any options.
# In this case, we are configuring a height for our listbox, that height equals the listbox size. That is,
#the height of our list will be adjusted by the size (amount and size of elements in) that list
#if we add or remove an element, it will automatically change the height of our list.
#we can add a value to that function in order to have some space in our list. This value equals to a invisible element
#so it'll have the same font's size.
#this code placed here only adjusts for before running changes

# entrybox = Entry(window)
# entrybox.pack()
#
# addButton = Button(window,text='Add an item',command=add)
# addButton.pack()
#
# deleteButton = Button(window,text='Delete an item',command=delete)
# deleteButton.pack()
#
# submitbutton = Button(window,text='submit',command=submit)
# submitbutton.pack()
#
# window.mainloop()
# ---------------------------------------------------------------------------

#MESSAGE BOX =

# from tkinter import *
# from tkinter import messagebox #import the messagebox library submodule

# def click():
    #messagebox.showinfo(title='This is an info messagebox', message='you are a person') #displays a simple message
    #messagebox.showwarning(title='WARNING',message='VIRUS')#you can put within a while(True) loop to keep warning
    #displays with an alert icon
    #messagebox.showerror(title='ERROR',message='Something went wrong!') #displays an error icon
    # if messagebox.askokcancel(title='Ask OK CANCEL',message='Are you sure?'): #if it's True
    #     print ('You agreed with terms')
    # else: #if it's False (cancel/quit)
    #     print('You did not agree with terms')
    #it displays a message with the OK and Cancel options. It returns True (OK) or False (Cancel).
    # if messagebox.askretrycancel(title='Ask Retry Cancel',message='Dou you want to retry?'):
    #     print ('You retried a thing')
    # else:
    #     print ('You canceled a thing')
    # if messagebox.askretrycancel(title='Ask Retry Cancel',message='Dou you want to retry?'):
    #     print ('You retried a thing')
    # else:
    #     print ('You canceled a thing')
    # if messagebox.askyesno(title='Yes or No',message='Dou you like cake?'): #it returns a True or False answer
    #     print ('Nice')
    # else:
    #     print ('Why?')
    # answer = messagebox.askquestion(title='Ask Question',message='Dou you like pie?') #it returns a string of yes or no
    # if answer == 'yes':
    #     print ('Nice')
    # else:
    #     print ('Why?')
    # resp = (messagebox.askyesnocancel(title='Yes No Cancel',#Returns True (Yes), False (No) or None (Cancel/quit)
    #                                   message='Do you like to code?',
    #                                   icon='info'))#we can set a icon, 'warning','info','error'.
    # if resp == True:
    #     print ('You like to code :)')
    # elif resp == False:
    #     print ('But is such a nice thing')
    # else:
    #     print('You have dodged the question')
#
# window = Tk()

# button = Button(window, command=click,text='click me')
# button.pack()
#
# window.mainloop()
#-------------------------------------------------------------------------------
from tkinter import *
from tkinter import colorchooser #submodule
# def click():
    # color = colorchooser.askcolor() #from the colorchooser submodule, ask color function.
    # print (color) #prints our color RGB (Red, Green,Blue) values, and our hexadecimal representention values
    # colorhex = color[1] #we create a second variable to store the hexadecimal value (index 1)
    # print (colorhex) #we don't need any of these print functions rn. It's only for context.
    # window.config(bg=colorhex) #we config our window background to be equal as the color we pick.
    #without the print lines, we have only 3 lines of code, but we can make it into 2 or 1 line of code.
    # colorhex = colorchooser.askcolor()[1]
    # window.config(bg=colorhex)
    ####### or
    # window.config(bg=colorchooser.askcolor()[1]) #it's a nice feature for customizing things
# window = Tk()
# window.geometry('420x420')
# button = Button(text='click me',command=click)
# button.pack()
# window.mainloop()
#-------------------------------------------------------------------------

#TEXT WIDGET/AREA  = Function like a text area, you can enter multiple lines of text
# from tkinter import *

# def submit():
#     texto = (text.get('1.0',END)) #1.0 refers to the first index from our text area. END includes everything till end.
#     print(texto)#you can print directly, or assign the text value to a variable to have more options to work with.
# window = Tk()
#
# text = Text(window, #we have a area in our window to create some text, but we need a button to submit the input.
#             bg='light yellow',
#             font=('Ink Free',20), #the text area sizes corresponds directly to the font size.
#             So the bigger the font is, the bigger the text area will be
            # height=8, #it is the amount of characters the text area is tall.
            # width=20, #it is the amount of characters the text area is long.
            # padx=20,
            # pady=20,
            # fg='purple') #it changes the foreground (the letter's color)
# text.pack()

# submitButton = Button(window,text='submit',command=submit)
# submitButton.pack()

# window.mainloop()
# -----------------------------------------------------------------------------

#FILE DIALOG (OPEN FILE)

# from tkinter import *
# from tkinter import filedialog
#
# def openFile():
#     filepath = filedialog.askopenfilename(initialdir='C:\\Users\\Vazsm\\PycharmProjects\\EstudandoPython',
#                                           title='Open File', #it changes the filedialog's title
#                                           filetypes=(('text files','*.txt'), #it sets the initial type of file to search
#                                                      ('all files','*.*'))) #is an option to search for all files
    #this is function is going to return a string that contains your file's path. So we store the value in a variable
    #we can set the initial directory path when you open a filedialog to search for a file.
    #print(filepath) #it returns our file's path: C:/Users/Vazsm/Desktop/termos ingles.txt
    #the filepath may return the FileNotFoundError, when we close the filedialog without select a file.
    #so we need to except error command.
    # file = open(filepath,'r') #this function opens our file using the Read mode ('r').
    # print (file.read()) #the function to read our file
    # file.close() #it is useful to close your file after you opened it

# window = Tk()

# button = Button(window,text='Open File',command=openFile)
# button.pack() #we created a button that will launch our file dialog so we can select a file.
# window.mainloop()
#----------------------------------------------------------------------

#FILEDIALOG (SAVE A FILE) =
#we need to create a window and place a save button, as well a text area.

# from tkinter import *
# from tkinter import filedialog
#
# def saveFile():
#     file = filedialog.asksaveasfile(initialdir='C:\\Users\\Vazsm\\PycharmProjects\\EstudandoPython',
#                                     defaultextension='.txt', #sets the default extension to save our files.
#                                     filetypes=[('Text file','.txt'),#it needs 2 strings, one for the type name
#                                                ('HTML file','.html'),#and one for the file extension
#                                                ('All files','.*')])#to save the extension is '.*'
    #this function asks us a place, a name and a file type to create our file.
    #if we don't set a filetype to save, it will just save as file.
    #filetext = str(text.get('1.0',END)) #stores all the texts that we have written in our text area.
    # And we convert it into a string
    #To get some text, we could use the console window instead of the text area
    # filetext= input('Write something to save')
    # if file is None:
    #     return #it avoids a NotFoundFileError.
    # file.write(filetext) #we write the filetext inside our file
    # file.close()
    #we kind of create an empty file and after we fill him with the filetext within our text area/widget.
# window  = Tk()
#
# button = Button(text='Save',command=saveFile)
# button.pack()
#
# text = Text(window)
# text.pack()
#
# window.mainloop()
#_------------------------------------------------------

#MENUBAR =
#We will create and add a menubar to a window, and we will add menus to our menubar. Each menu will function like
#a dropdown menu with items that execute actions.
# from tkinter import *
#
# def openfile():
#     print ('File has been opened')
# def savefile():
#     print('File has been saved')
# def cutfile():
#     print('File has been cut')
# def copyfile():
#     print('File has been copied')
# def pastefile():
#     print('File has been pasted')
#
# window = Tk()
#
# img= PhotoImage(file='hotdog.png')
#
# menubar = Menu(window) #we have created a menu and assigned him to our window.
# window.config(menu=menubar) #we can set the menu of the windnow as the menu that we created
# fileMenu = Menu(menubar,tearoff=0) #to create menu tabs we need to create another menu, but add them to our menubar.
### tearoff 0 diables the annoying line
# menubar.add_cascade(label='File',menu=fileMenu) #it creates a dropdown for the menu tabs.
### We assigned an area with contains a text/image (label) with the name of our menu tab.
###We assigned a menu tab to a menubar label and it's dropdown. And now we need to create options for this fileMenu.
# fileMenu.add_command(label='Open',command=openfile) #it creates a clickable option
# fileMenu.add_command(label='Save',command=savefile)
# fileMenu.add_separator() #separetes our different commands from each other within the menu
# fileMenu.add_command(label='Exit',command=quit) #quit is a shortcut for exiting something, so we don't need a function
#
# editMenu = Menu(menubar,tearoff=0,font=('Ink Free',16)) #we can costumize our menus.
# menubar.add_cascade(label='Edit',menu=editMenu)
# editMenu.add_command(label='Cut',command=cutfile,image=img,compound='left') #we can add images to each command
# editMenu.add_command(label='Copy',command=copyfile)
# editMenu.add_command(label='Paste',command=pastefile)
#
# window.mainloop()
# -------------------------------------------------------------------------

### FRAME = A rectangular container to group and hold widgets together.

# window = Tk()
#
# frame = Frame(window,bg='pink',bd=5,relief=SUNKEN)
###We add a frame to our window, and we add our buttons to our frame.
# frame.pack(side='bottom')
##or
# frame.place(x=10,y=80) #we place our frame by coordinates. Our widgets added to our frame moves along with our frame.
#
# Button(frame,text='W',font=('Arial',20),width=3).pack(side='top')
# Button(frame,text='S',font=('Arial',20),width=3).pack(side='left')
# Button(frame,text='A',font=('Arial',20),width=3).pack(side='left')
# Button(frame,text='D',font=('Arial',20),width=3).pack(side='left')
##If you don't plan in using this button again as a variable, you just need to pack it.
##This way when we expand our window, the buttons will set apart. So, we add them to a FRAME instead of window
#
# window.mainloop()
#------------------------------------------------------------------------------

# WAYS TO CREATE WINDOW IN PYTHON =

# from tkinter import *
#
# def createWindow():
#     new_window = Tk() #it creates a new and independent window
#     new_window = Toplevel() #Toplevel() is a new window created on top of other windows.
    # It is linked to a 'bottom' window. If we close our bottom window, the top window will close as well.
    #In this case, our main window is serving as the bottom window, and our new_window is serving as the top window.
    # old_window.destroy()
    #when we press the button, a new window will be created, and the old window will be destroyed/closed out.
# old_window = Tk()
#
# Button(old_window,text='Create New Window',command=createWindow).pack()
#
# old_window.mainloop()
#-----------------------------------------------------------------------------------------

# WINDOW TABS =
# In order to create tabs for our GUI application, we are going to need access to a widget called Notebook
#That is found in a different module
#To create tabs, we need to create frames

# from tkinter import *
# from tkinter import ttk #gives us access to several widgets that are not usually available to us.
#
# window = Tk()
#
# notebook = ttk.Notebook(window) #Widget that manages a collection of windows/displays
#
# tab1 = Frame(notebook) #new frame for tab1
# tab2 = Frame(notebook) #new frame for tab2
#
# notebook.add(tab1,text='Tab 1') #We add to our notebook a tab frame and a tab name. notebook.add(frame,text='frame')
# notebook.add(tab2,text='Tab 2')
# notebook.pack(expand=True,fill='both') #expand = this will expand to fill any space.
                                        #fill = will fill space on x and y axis.

# Label(tab1,text='You are in tab1',font=('Arial',40),fg='#00FF00',bg='black',width=20,height=10).pack()
# Label(tab2,text='You are in tab2',font=('Arial',40),fg='#00FF00',bg='black',width=20,height=10).pack()
#We are adding a label to a tab.

# window.mainloop()
# ----------------------------------------------------------------------------

# GRID() = A geometry manager that organizes widgets in a table like structure in parent
        #Organized by rows and columns like spreadsheet. Starting by row 0 and column 0.

# from tkinter import *
#
# window = Tk()
#
# titleLabel = Label(window,text='Enter your info: ',font=('Arial',12,'bold')).grid(row=0,column=0,columnspan=2)
#
# firstname_label = Label(window,text='First name: ',width=20).grid(row=1,column=0)
# firstname_entry = Entry(window).grid(row=1,column=1)
#
# lastname_label = Label(window,text='Last name: ',width=20).grid(row=2,column=0)
# lastname_entry = Entry(window).grid(row=2,column=1)
#
# emailLabel = Label(window,text='Email:',width=20).grid(row=3,column=0)
# emailEntry = Entry(window).grid(row=3,column=1)
#when we use pack(), the items will be placed in one big column.

# submitButton = Button(window,text='Submit').grid(row=4,column=0,columnspan=2)
# A widget can be placed within more than one column. To do that, we set a number to columnspan.
# That number is the amount of columns that will take place, including the one that is currently in.
#
#The column width is directly dependent of the largest widget that it contains.
#So we just need to set 1 widget's width, and if it is the largest, all column will follow that width
#But this only changes the column width, not the widgets width
# window.mainloop()
# ---------------------------------------------------------------------------------------------------

# PROGRESS BAR =

# from tkinter import *
# from tkinter.ttk import *
# import time
# def start():
#     tasks = 10
#     x = 0
#     while x<tasks: #we create a condition that allows us to increase the progressbar a limited amount of times.
#         time.sleep(0.5)
#         bar['value'] +=10 #Increase the value of our progress bar by some amount.
#         x +=1 #at the end of each iteration, x increases by one. Ten times untill it equals the tasks value.
#         percent.set(str(int((x/tasks)*100)) +'%')
#         text.set(str(x)+'/'+str(tasks)+' Tasks completed')
#         window.update_idletasks() #this will update our window at each iteration
#
# window = Tk()
#
# percent= StringVar() #allows us to update a variable with new values (texts).
# text = StringVar()
#
# bar = Progressbar(window,orient=HORIZONTAL,length=300)
# bar.pack(pady=10)
#
# percentLabel = Label(window,textvariable=percent).pack() #textvariable so we can update this label after each iteration
# taskLabel = Label(window,textvariable=text).pack()
#
# button = Button(window,text='Download',command=start).pack()
#
# window.mainloop()
#--------------------------------------------------------------------------

#CANVAS = Widget that is used to draw graphs, plots, images in a window

# from tkinter import *
#
# window = Tk()
#
# canvas = Canvas(window,height=500,width=500,bg='green')
# canvas.create_line(0,0,500,500,fill='orange',width=5) #when we create a line, we need a start point and an end point
### (startX,startY,endingX,endingY)
# canvas.create_line(0,500,500,0,fill='pink',width=5) #it's overlapping a part of the orange line because the pink
# was created after, so it's 'prioritizing'.
# redline = canvas.create_line(250,0,250,500,fill='red',width=5)
#you can create a canvas object if it will be used later, by moving the graphic, or something else
# canvas.create_rectangle(100,100,200,200,fill='#998C00') #the starting coordinates go for the top left of our rectangle.
# The ending coordinates go for the bottom right of our rectanlge
# canvas.create_polygon(50,10,140,70,70,200,fill='yellow',outline='black',width=3) #outline is a border for the graphic.
#we can create several types of shapes, it depends on how many coordinates we will give.
# coordinates = [10,20,20,30,100,200,70,50,350,91]
#we can also pass a list/tuple as the coordinates
# canvas.create_polygon(coordinates,fill='blue')
# canvas.create_arc(10,10,100,100,fill='grey',style=PIESLICE,start=90,extent=180) #don't really know. #ARC,CHROD,PIESLICE.
##start is the start position in degrees (90,180,270,360) for our arc.
##extent is the degrees that our arc have.

# canvas.create_arc(0,0,500,500,fill='red',extent=180,width=8)
# canvas.create_arc(0,0,500,500,fill='white',start=180,extent=180,width=8)
# canvas.create_line(0,250,500,250,fill='black',width=10)
# canvas.create_oval(200,200,300,300,fill='white',outline='black',width=10)
##you can think oval as a circle that is inside a square.
# This circle has a diameter that touches the height and width of the square.
#Our circle starts a the middle of these diameters. So we need to think where we want to place our circle
#And think a diameter for our circle. And the startingX and startingY coordinates will have to be a diameter away from
#the endingX and endingY coordinates.
# canvas.pack()
#
#
# window.mainloop()
#------------------------------------------------------------------------------------------

# KEYBORD EVENTS =

# from tkinter import *

#We can bind a key event and a function to a widget or a window. So when we press a certain key or do something, the
#function will be triggered to perform some action for us.
#widgets and windows have access to a bind() function.
#So window.bind(event,function) #the bind function takes 2 arguments, a trigger and a function name.

# def run(event): #we need to set ONE parameter for this function. we place 'event' as an argument.
#     print ('You are running! You pressed: '+ event.keysym) #event.keysym corresponds to the key symbol we pressed.
#     label.config(text=event.keysym) #this will set our label text to the key symbol we put in.
# window = Tk()
#
#
# window.bind('<w>',run)
# window.bind('<s>',run)
# window.bind('<a>',run)
# window.bind('<d>',run)
# window.bind('<Up>',run) #Responds to up arrow
# window.bind('<Down>',run) #Responds to down arrow
# window.bind('<Left>',run)#Responds to left arrow
# window.bind('<Right>',run) #Responds to right arrow
# window.bind('<Return>',run) #Responds when we press enter
# window.bind('<Key>',run) #Responds to almost every key


# label =Label(window,font=('Arial',50),text='Escolha uma letra')
# label.pack()
#--------------------------------------------------------------------------------------

# MOUSE EVENTS =

# from tkinter import *

# def dosomething(event):
#     print('Mouse coordinates: ' + str(event.x)+','+str(event.y))
    #It displays where this event occurred (where in the window we clicked).
# window =Tk()

# window.bind('<Button-1>',dosomething) #Responds to mouse's left clicks
# window.bind('<Button-2>',dosomething) #Responds when we press mousewheel.
# window.bind('<Button-3>',dosomething) #Responds to mouse's right clicks
# window.bind('<ButtonRelease>',dosomething) #Responds when we release the click
# window.bind('<Enter>',dosomething) #Responds when we enter our binded window or widget. IT IS NOT the enter keyboard.
# window.bind('<Leave>',dosomething) #Responds when we leave our binded window or widget.
# window.bind('<Motion>',dosomething) #Responds only when the mouse is moving.
# window.mainloop()
#---------------------------------------------------------------------------------------

# DRAG AND DROP WIDGETS =

# from tkinter import *
#
# def dragitem(event):
    # label.startX = event.x #we are assign a new variable/attribute from our label to where the even occurred in x axis.
    # label.startY = event.y #only the events within our label
    #but this way, we are only storing attributes for label1. If we want to use this function to more labels we must do:
    # widget = event.widget #It gets the widget of the event that we are dealing and renaming as widget
    # widget.startX = event.x
    # widget.startY = event.y
# def motion(event):
    # x = label.winfo_x() - label.startX + event.x  #label.winfo_x() gets the topleft x coordinate from our label.
    # y = label.winfo_y() - label.startY + event.y
    # label.place(x=x,y=y)
    #or we can apply this function to any widgets:
    # widget = event.widget
    # x = widget.winfo_x() - widget.startX + event.x  # label.winfo_x() gets the topleft x coordinate from our label.
    # y = widget.winfo_y() - widget.startY + event.y
    # widget.place(x=x,y=y)
#the event.x is where (in x axis) my left clcik is in the window
#the label.startX is where (in x axis we clicked in our label
#the label.info_x() is where (in x axis) in the window is the topfelt corner from our widget.
#We need to know the initial topleft coordinates from our widget, then we click and hold, triggering both dragitem and
#motion functions. We subtract the label.startX(where we clicked) by event.X(where we are holding click now)
#The result of this subtraction will be how much coordinates have changed.
#We add the result to our initial topleft widget coordinates. So we have a new value with a new X coordinate.
#Now, during the motion function, we place our label by the new coordinate.
# window = Tk()
#
# label = Label(window,bg='red',width=10,height=5)
# label.place(x=0,y=0)
# label2 = Label(window,bg='blue',width=5,height=5)
# label2.place(x=100,y=100)
# label.bind('<Button-1>',dragitem)
# label.bind('<B1-Motion>',motion) #responds while we hold left click
# label2.bind('<Button-1>',dragitem)
# label2.bind('<B1-Motion>',motion)
# window.mainloop()
#----------------------------------------------------------------------------------------------

# MOVING WIDGETS/IMAGES ON WINDOW OR CANVAS=

# from tkinter import*
#
# def cima(event):
#     carLabel.place(x=carLabel.winfo_x(),y=carLabel.winfo_y()-10)
# def baixo(event):
#     carLabel.place(x=carLabel.winfo_x(),y=carLabel.winfo_y()+10)
# def esquerda(event):
#     carLabel.place(x=carLabel.winfo_x()-10,y=carLabel.winfo_y())
# def direita(event):
#     carLabel.place(x=carLabel.winfo_x()+10,y=carLabel.winfo_y())

# window = Tk()
# window.geometry('500x500')
# img = PhotoImage(file='car.png')
# carLabel = Label(window,image=img)
# carLabel.place(x=0,y=0)
# window.bind('<w>',cima) #it has to be binded to our window, because we don't have a way to select with keyboard?
# window.bind('<s>',baixo)
# window.bind('<a>',esquerda)
# window.bind('<d>',direita)
# window.bind('<Up>',cima)
# window.bind('<Down>',baixo)
# window.bind('<Left>',esquerda)
# window.bind('<Right>',direita)
#
# window.mainloop()
#---------------------------------------------------------------------------

# MOVING IMAGES/WIDGETS ON CANVAS:

# from tkinter import *
#
# def move_up(event):
#     canvas.move(carimg,0,-10) #canvas has a move function that accepts as argmunets the canvas image we want to move
    #followed by x and y coordinates.
# def move_down(event):
#     canvas.move(carimg,0, 10)
# def move_left(event):
#     canvas.move(carimg,-10,0)
# def move_right(event):
#     canvas.move(carimg,10, 0)



# window = Tk()
#
# canvas = Canvas(window,width=500,height=500)
# canvas.pack()
# img = PhotoImage(file='car.png') #we create a image, then we create a canvas image, by placing x and y coordinates
# carimg = canvas.create_image(0,0,image=img,anchor=NW) #and storing as canvas image our img.
#The 0,0 coordinates will cut off part of our image, so we can fix it by anchoring in North West(NW).

# window.bind('<w>',move_up)
# window.bind('<s>',move_down)
# window.bind('<a>',move_left)
# window.bind('<d>',move_right)
#
# window.mainloop()
#_---------------------------------------------------------------------------------

# ANIMATIONS =

# from tkinter import *
# import time
#
# HEIGHT = 500 #it's a constant. A variable/value that we don't plan on changing
# WIDTH = 500 #constants are commonly all uppercase.
# xvelocity = 2 #velocity/speed that our image is going to move in the x axis
# yvelocity = 5 #velocity/speed that our image is going to move in the y axis
# window = Tk()
#
# canvas= Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()
#
# spaceimg = PhotoImage(file='space.png') #the background must be created first, before all others canvas images
# background_photo = canvas.create_image(0,0,image=spaceimg)
#
# img = PhotoImage(file='car.png')
# carimg = canvas.create_image(0,0,image=img,anchor=NW)
#
#
# imgHeight = img.height()
# imgWidth = img.width()
#
# while True: #or can be while running. It returns a boolean value, that's only true when it's running,
# and false when it's paused or when you quit. It is most used in games.
#     coordinates = canvas.coords(carimg) #get the coordinates where our image is located
    ##print(coordinates) #print the coordinates #first number is the x position, and the second number is the y position
    # if ((coordinates[0]>= (WIDTH -imgWidth)) or (coordinates[0]<0)):
        #if our x coordinates is lesser than 0 or equal/greater than (500-Our image Width):
        # xvelocity = -xvelocity #or = xvelocity*-1 #this way the image will return after it reaches the border.
    # if ((coordinates[1]<0) or (coordinates[1]>=(500-imgHeight))):
    #     yvelocity = -yvelocity
#this way our image can bounce back when touches the borders.
    # canvas.move(carimg,xvelocity,yvelocity)
    #takes 3 arguments, what do you want to move, the x coordinate and the y coordinate
    #in this case, our coordinates will be our x an y velocities. That will increase our coordinate by their value
    # after each iteration. So it will move xvelocity pixels to the right
    # window.update() #we will update to any changes
    # time.sleep(0.01)
#
# window.mainloop()
#-------------------------------------------------------------------------------------------------

# MULTIPLE ANIMATIONS =

# from tkinter import *
# import time
#
# WIDTH = 500 #CONSTANTS
# HEIGHT = 500
#
# class Ball(): #we are going to use multiple types of balls, so we might aswell create a class
#     def __init__(self,canvas,x,y,diameter,xvelocity,yvelocity,color): #our constructor
#         self.canvas = canvas
#         self.image = canvas.create_oval(x,y,diameter,diameter,fill=color) #we create a canvas image/ball
#         self.xvelocity = xvelocity
#         self.yvelocity = yvelocity
#
#     def move(self): #we create a function that will move our balls.
#         coordinates = self.canvas.coords(self.image)
        #gets the topleft image coordinate and bottom right image coordinate inside our canvas.
        #it will be like [topleftX,topleftY,bottomrightX,bottomrightY]
        # if (coordinates[2])>=(self.canvas.winfo_width()) or coordinates[0]<0:
            #if our bottomrightX is greater than the canvas widht. Or if our topleftX is lesser than 0:
            #Our image bounces back at the right and left border from our canvas
            # self.xvelocity = -self.xvelocity #change direction
        # if (coordinates[3])>=(self.canvas.winfo_height()) or coordinates[1]<0:
        #     if our bottomrightY is greater than the canvas height. Or if our topleftY is lesser than 0:
            #Our image bounces back at the top and the bottom of our canvas.
            # self.yvelocity = -self.yvelocity #change direction
        # self.canvas.move(self.image,self.xvelocity,self.yvelocity)
        #we are going to move inside our canvas: our image, by the x and y velocity

#Our ball class is acting like a blueprint for how balls should be created and the behavior that they exhibit
# window = Tk()

# canvas = Canvas(window,width=WIDTH,height=HEIGHT) #We create animations using canvas.
# canvas.pack()
#
# volley_ball = Ball(canvas,0,0,100,1,1,'yellow') #we pass a canvas to wich we will be drawing our ball.
#we pass xy coordinates to place our ball inside our canvas
#we pass only a diameter because it is a circle, so the width and height are the same
#we pass a x an y velocity. That will be the amount our ball will move within the x and y axis.
#we pass a color to fill our ball.
# basket_ball = Ball(canvas,0,0,100,2,4,'orange')
# tennis_ball = Ball(canvas,0,0,30,8,6,'green')
#
# while True:
#     volley_ball.move()#while true, we will be calling our move function from our Ball class.
#     basket_ball.move()
#     tennis_ball.move()
#     window.update() #we update our window at each iteration
#     time.sleep(0.01)
# window.mainloop()
#------------------------------------------------------------------------------------------

# CLOCK PROGRAM =

# from tkinter import *
# from time import *
# def update(): #function to update time every second.
#     time_string = strftime('%H:%M:%S') #this is a time function that returns us the current time
    # based on the directives we selected
    # Conver a tuple of structure_time to a string as specified by the format argument (directives)
    # day_string = strftime('%A')
    # dayLabel.config(text=day_string)
    # date_string = strftime('%B %d, %Y')
    # dateLabel.config(text=date_string)
    # timeLabel.config(text=time_string) #it will update our timeLabel to display the variable time.
    # timeLabel.after(1000,update) #this function stablish a delay (in milisseconds), and after that, it calls a function.
    # In this case, we're calling the same function, that is a recursive function. this updates only a widget.
    # window.after(1000,update) #this updates all the window.
# window = Tk()

# timeLabel = Label(window,font=('Arial',50),fg='green',bg='black')
# timeLabel.pack()
#
# dayLabel = Label(window,font=('Ink Free',25))
# dayLabel.pack()
#
# dateLabel = Label(window,font=('Ink Free',25))
# dateLabel.pack()
#
# update() #we call the update function

# window.mainloop()
#--------------------------------------------------------------------------------

# SEND EMAIL =

# import smtplib #simple mail transfer protocal library
#
# sender = 'sender@gmail.com'
# receiver = 'receiver@email'
# password = 'passowrd123'
# subject = 'python email test'
# body = 'I wrote an email'
#
# message = f"""From: {sender} #triple quotes string can span multiple lines of text
# To: {receiver}
# Subject: {subject}\n
# {body}
# """
#
# server = smtplib.SMTP('smtp.gmail.com',587) #we create a server object #mail submission
# server.starttls() #transport layer security
# try :
#     server.login(sender,password)
#     print ('Logged in')
#     server.sendmail(sender,receiver,message)
#     print('Email has been sent')
# except smtplib.SMTPAuthenticationError:
#     print('Unable to sign in.')
# except smtplib.SMTPServerDisconnected:
#     print('Connection unexpectedly closed')
#-----------------------------------------------------------------------------------------

# RUN PYTHON FILES IN COMMAND PROMPT
# print ('hello world')
# print (input('What is your name?'))

##run .py files with cmd

##save file as .py (python file)
##go to command prompt
##navigate to your directory with your file: cd C:\Users\Vazsm\Desktop ##cd means change directory. Paste your file path
##invoke python interpreter + script: python + name of the .py file #python GUI.py

#Go to file, save as. Pick a name for your python file. Pick a location to save your file
# -------------------------------------------------------------------------------------

# Python PIP
#pip = package manager for packages and modules from Python Package Index (pypi.org)
#included for Python versions 3.4 +
#open command prompt
##      help: pip
##      check: pip --version
##      update: pip install --upgrade pip
##      installed packages: pip list
##      check outdated packages: pip list --outdated
##      update package: pip install ''package name'' --upgrade
##      install a package: pip install ''package name''
#----------------------------------------------------------------------------------------------

# .PY to .EXE =

### Windows defender may prevent you from running.
### Make sure pip and pyinstaller are installed/updated

### cd (change directory) to directory that contains your .py file

###py installer:
###         F               all in one file
###         w               removes terminal window
###         i icon.ico      adds custom icon to .exe
###         clock.py        name of your main python file

### .EXE is located in the dist folder

## We create a new folder to contain our file, in order to maintain things clean.

from tkinter import *
from time import *
import time

def clock():
    text = strftime('%H:%M:%S')
    timelabel.config(text=text)
    daytext = strftime('%A')
    daylabel.config(text=daytext)
    datetext = strftime('%d, %B, %Y')
    datelabel.config(text=datetext)
    window.after(1000,clock)

window = Tk()


daylabel = Label(window, font=('Ink free',20),width=20)
daylabel.pack()

timelabel = Label(window, font=('Arial',30),fg='green',bg='black',width=20)
timelabel.pack()

datelabel = Label(window,font=('Arial',20),width=20)
datelabel.pack()
clock()



window.mainloop()
