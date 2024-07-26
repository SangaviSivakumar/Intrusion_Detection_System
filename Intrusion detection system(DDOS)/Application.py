import numpy as np


import pandas as pd
import pickle

import click

from tensorflow.keras.models import *
#RSA

from tkinter import *
from tkinter import ttk  
from tkinter import Menu  
from tkinter import messagebox as mbox  
# import filedialog module
from tkinter import filedialog
flg=0;
import tkinter as tk
model = load_model('bilstm_training.h5')
    
# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a CSV File",
                                          filetypes = (("text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
    global f
    f = filename


def start():

    print("Process Started")
    dataset = pd.read_csv(
    f, sep=",",header=None)

    #dataset=dataset.dropna(how="any")
    print(dataset)

    print(dataset.info())

    X = dataset.iloc[:,4:41].values

    # load the model from disk
    ypred = model.predict(X)
        
    import numpy as np

    y_pred=np.argmax(ypred,axis=1)

    print(y_pred)
    
    
    app = tk.Tk()
    if(y_pred[0]==0):
        print("Normal")
        label_file_explorer.configure(text="Result for the request: The Input Request is Normal")
        app.title("Attack Detection")
        ttk.Label(app, text="Result for the request: The Input Request is Normal").grid(column=0,row=0,padx=20,pady=30)  
        menuBar = Menu(app)
        app.config(menu=menuBar)
    elif(y_pred[0]==1):
        print("neptune")
        label_file_explorer.configure(text="Result for the request: The Input Request is neptune")
        app.title("Attack Detection")
        ttk.Label(app, text="Result for the request: The Input Request is a neptune").grid(column=0,row=0,padx=20,pady=30)
        menuBar = Menu(app)
        app.config(menu=menuBar)
    elif(y_pred[0]==2):
        print("smurf")
        label_file_explorer.configure(text="Result for the request: The Input Request is smurf")
        app.title("Attack Detection")
        ttk.Label(app, text="Result for the request: The Input Request is a smurf").grid(column=0,row=0,padx=20,pady=30)
        menuBar = Menu(app)
        app.config(menu=menuBar)
    elif(y_pred[0]==3):
        print("portsweep")
        label_file_explorer.configure(text="Result for the request: The Input Request is portsweep")
        app.title("Attack Detection")
        ttk.Label(app, text="Result for the request: The Input Request is a portsweep").grid(column=0,row=0,padx=20,pady=30)
        menuBar = Menu(app)
        app.config(menu=menuBar)
    elif(y_pred[0]==4):
        print("satan")
        label_file_explorer.configure(text="Result for the request: The Input Request is satan")
        app.title("Attack Detection")
        ttk.Label(app, text="Result for the request: The Input Request is a satan").grid(column=0,row=0,padx=20,pady=30)
        menuBar = Menu(app)
        app.config(menu=menuBar)
    
    elif(y_pred[0]==5):
        print("teardrop")
        label_file_explorer.configure(text="Result for the request: The Input Request is teardrop")
        app.title("Attack Detection")
        ttk.Label(app, text="Result for the request: The Input Request is a teardrop").grid(column=0,row=0,padx=20,pady=30)
        menuBar = Menu(app)
        app.config(menu=menuBar)
    
        
if __name__ == '__main__':
    window = Tk()
  
    # Set window title
    window.title('Application')
      
    # Set window size
    window.geometry("700x400")
      
    #Set window background color
    window.config(background = "white")
    import tkinter
    from tkinter import *
    from PIL import Image, ImageTk
    # Create a photoimage object of the image in the path
    image1 = Image.open("bg.jpg")
    test = ImageTk.PhotoImage(image1)

    label1 = tkinter.Label(image=test)
    label1.image = test

    # Position image
    label1.place(x=0, y=0)

    def on_enter(e):
       button_explore.config(background='OrangeRed3', foreground= "white")

    def on_leave(e):
       button_explore.config(background= 'SystemButtonFace', foreground= 'black')

    def on_enter1(e):
       button_start.config(background='OrangeRed3', foreground= "white")

    def on_leave1(e):
       button_start.config(background= 'SystemButtonFace', foreground= 'black')
    def on_enter2(e):
       button_exit.config(background='OrangeRed3', foreground= "white")

    def on_leave2(e):
       button_exit.config(background= 'SystemButtonFace', foreground= 'black')
      
    # Create a File Explorer label
    label_file_explorer = Label(window,
                                text = "Please give Input Request",
                                width = 100, height = 4,
                                fg = "blue")
         
    button_explore = Button(window,
                            text = "Browse Request Files",
                            command = browseFiles, height = 5)
    button_exit = Button(window,
                         text = "exit",
                         command = exit, height = 5, width=10)  
    button_start = Button(window,
                         text = "Start Analyzing Request",
                         command = start, height = 5)

       
    # Grid method is chosen for placing
    # the widgets at respective positions
    # in a table like structure by
    # specifying rows and columns
    label_file_explorer.grid(column = 1, row = 1, padx=1, pady=5)
    button_explore.grid(column = 1, row = 2, padx=5, pady=5)
    button_exit.grid(column = 1,row = 3, padx=5, pady=5)
    button_start.grid(column = 1,row = 4, padx=5, pady=5)
      
    # Let the window wait for any events
    
    
    window.mainloop()


    
