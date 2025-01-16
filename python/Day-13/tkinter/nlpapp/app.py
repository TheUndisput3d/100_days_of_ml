from tkinter import *
from my_db import Database
from tkinter import messagebox
from sent import Sent
from my_api import api
import json

class NLPApp:

  def __init__(self):

    # load the GUI
    self.root = Tk() # create a window
    self.root.title("NLP App") # set the title of the window

    self.database = Database() # create an instance of the Database class
    self.sent = Sent()
    self.apio = api()

    # self.root.iconbitmap("") # set the icon of the window
    self.root.geometry("350x600") # set the size of the window
    self.root.configure(bg='#34495E') # set the background color of the window



    self.login_gui()


    self.root.mainloop()

  def login_gui(self):

    self.clear() # clear the window

    heading = Label(self.root, text='NLP App', bg='#34495E', fg='white') # create a label
    heading.pack(pady=(30, 30)) # add the label to the window
    heading.configure(font=('verdana', 24, 'bold')) # set the font of the label

    label1 = Label(self.root, text='Enter your Email', bg='#34495E', fg='white') # create a label
    label1.pack(pady=(10, 10))
    label1.configure(font=('verdana', 12))

    self.email_input = Entry(self.root, width=30) # create an input field
    self.email_input.pack(pady=(5, 10), ipady=3) # add the input field to the window


    label2 = Label(self.root, text='Enter your password', bg='#34495E', fg='white') # create a label for password
    label2.pack(pady=(10, 10))
    label2.configure(font=('verdana', 12))

    self.password_input = Entry(self.root, width=30, show='*') # create an input field
    self.password_input.pack(pady=(5, 10), ipady=3) # add the input field to the window

    login_btn = Button(self.root, text='Login', width=13, height=2, command=self.perform_login)
    login_btn.pack(pady=(10, 10))
    login_btn.configure(font=('verdana', 12))

    label3 = Label(self.root, text='Not a member?', bg='#34495E', fg='white')
    label3.pack(pady=(20, 10))
    label3.configure(font=('verdana', 12))

    redirect_btn = Button(self.root, text='Register Now', width=13, height=2, command=self.register_gui)
    redirect_btn.pack(pady=(10, 10))
    redirect_btn.configure(font=('verdana', 12))

  def register_gui(self):

    self.clear()

    heading = Label(self.root, text='NLP App', bg='#34495E', fg='white') # create a label
    heading.pack(pady=(30, 30)) # add the label to the window
    heading.configure(font=('verdana', 24, 'bold')) # set the font of the label

    label0 = Label(self.root, text='Enter your Name', bg='#34495E', fg='white') # create a label
    label0.pack(pady=(10, 10))
    label0.configure(font=('verdana', 12))

    self.name_input = Entry(self.root, width=30) # create an input field
    self.name_input.pack(pady=(5, 10), ipady=3) # add the input field to the window

    label1 = Label(self.root, text='Enter your Email', bg='#34495E', fg='white') # create a label
    label1.pack(pady=(10, 10))
    label1.configure(font=('verdana', 12))

    self.email_input = Entry(self.root, width=30) # create an input field
    self.email_input.pack(pady=(5, 10), ipady=3) # add the input field to the window


    label2 = Label(self.root, text='Enter your password', bg='#34495E', fg='white') # create a label for password
    label2.pack(pady=(10, 10))
    label2.configure(font=('verdana', 12))

    self.password_input = Entry(self.root, width=30, show='*') # create an input field
    self.password_input.pack(pady=(5, 10), ipady=3) # add the input field to the window

    register_btn = Button(self.root, text='Register', width=13, height=2, command=self.perform_registration)
    register_btn.pack(pady=(10, 10))
    register_btn.configure(font=('verdana', 12))

    label3 = Label(self.root, text='Already logged in?', bg='#34495E', fg='white')
    label3.pack(pady=(20, 10))
    label3.configure(font=('verdana', 12))

    redirect_btn = Button(self.root, text='Login Now', width=13, height=2, command=self.login_gui)
    redirect_btn.pack(pady=(10, 10))
    redirect_btn.configure(font=('verdana', 12))

    
  def clear(self):
    for i in self.root.pack_slaves():
      i.destroy()
  
  def perform_login(self):
    email = self.email_input.get()
    password = self.password_input.get()

    response = self.database.authenticate(email, password)
    
    if response:
      if response == 1:
        messagebox.showinfo('Login Sucessful', 'Welcome to NLP App')
        self.home_gui()
      else:
        messagebox.showerror('Error', 'Wrong Password')
    else:
      messagebox.showerror('Error', 'User not found')
    

  def perform_registration(self):
    name = self.name_input.get()
    password = self.password_input.get()
    email = self.email_input.get()

    response = self.database.add_user(name=name, email=email, password=password)

    if response == 1:
      messagebox.showinfo('Registration Sucessful', 'User added successfully')
    else:
      messagebox.showerror('Error', 'Email already exists')


  def home_gui(self):

    self.clear()

    heading = Label(self.root, text='NLP App', bg='#34495E', fg='white') # create a label
    heading.pack(pady=(30, 30)) # add the label to the window
    heading.configure(font=('verdana', 24, 'bold')) # set the font of the label

    ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=2, command=self.ner_gui)
    ner_btn.pack(pady=(10, 10))
    ner_btn.configure(font=('verdana', 12))

    sen_btn = Button(self.root, text='Sentiment Analysis', width=30, height=2, command=self.sen_gui)
    sen_btn.pack(pady=(10, 10))
    sen_btn.configure(font=('verdana', 12))

    emo_btn = Button(self.root, text='Emotion Prediction', width=30, height=2, command=self.emo_gui)
    emo_btn.pack(pady=(10, 10))
    emo_btn.configure(font=('verdana', 12))

    logout_btn = Button(self.root, text='Logout', width=13, height=2, command=self.login_gui)
    logout_btn.pack(pady=(10, 10))
    logout_btn.configure(font=('verdana', 12))

  def sen_gui(self):
    self.clear()

    heading = Label(self.root, text='NLP App', bg='#34495E', fg='white') # create a label
    heading.pack(pady=(30, 30)) # add the label to the window
    heading.configure(font=('verdana', 24, 'bold')) # set the font of the label

    heading1 = Label(self.root, text='Sentiment Analysis', bg='#34495E', fg='white') # create a label
    heading1.pack(pady=(10, 20))
    heading1.configure(font=('verdana', 20))

    label = Label(self.root, text='Enter the text', bg='#34495E', fg='white')
    label.pack(pady=(10, 10))

    self.sen_input = Entry(self.root, width=70)
    self.sen_input.pack(pady=(5, 10), ipady=3)

    sen_btn = Button(self.root, text='Analyze', width=30, height=2, command=self.perform_sen)
    sen_btn.pack(pady=(10, 10))
    sen_btn.configure(font=('verdana', 12))

    self.result = Label(self.root, text='', bg='#34495E', fg='white')
    self.result.pack(pady=(20, 20))
    self.result.configure(font=('verdana', 12))

    sen_btn = Button(self.root, text='Go Back', width=30, height=2, command=self.home_gui)
    sen_btn.pack(pady=(10, 10))
    sen_btn.configure(font=('verdana', 12))
  
  def perform_sen(self):

    text = self.sen_input.get()
    result = self.apio.analyze_sent(text)

    self.result['text'] = result

    # res = self.sent.analyze_sent(text)
    # messagebox.showinfo('Sentiment', f'The sentiment of the text is {res}')
    
  def ner_gui(self):
    pass

  def emo_gui(self):
    pass


nlp = NLPApp()