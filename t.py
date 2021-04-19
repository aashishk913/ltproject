from tkinter import *
import tkinter as ttk
from selenium  import webdriver
#from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.by import By
import time
import requests
import threading     
def callselenium():
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome('D:\Selenium\chromedriver',options=option)
    for key,value in dictlist.items():
        print("the2 loop")
        driver.get("https://in.investing.com/equities/"+key)
        val =driver.find_element_by_xpath("/html/body/div[1]/div[4]/section[2]/div/header/div/div[2]/div[1]/div[1]/bdo")
        a = float(val.text.replace(',', '')) 
        if a >= float(value):
            print("BUY SIGNAL CALLING IFTTT the2")
            params = {"value1":key,"value2":value}
            r = requests.get('https://maker.ifttt.com/trigger/ALERT_NOTFI/with/key/bPcy-xG957JR6HG8a2Cw-v',params=params)
    



#------------------------------GUI--------------------------------------------
root = Tk()
root.title("STOCK NOTIFCATIONS")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = { 'lt-technology-services-ltd-ns','state-bank-of-india','infosys','axis-bank','icici-bank-ltd','housing-development-finance','gsk-pharmaceuticals'}
tkvar.set('Scripts') # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose a Stock").grid(row = 0, column = 0)
popupMenu.grid(row = 1, column =0)
dictlist = {}
# on change dropdown value
y = ""

def clickMe():
    print(E1.get())
    print(tkvar.get())
    dictlist[tkvar.get()] = E1.get()
    print("now list")
    print(dictlist)
label = Label( mainframe, text="PRICE")
label.grid(column = 3, row = 0)
    
E1 = Entry(mainframe, bd =5)
E1.grid(column = 3 ,row = 1)
submit = Button(mainframe, text ="ADD", command = clickMe)
submit.grid(column = 3 ,row = 2)

submit1 = Button(mainframe, text ="submit", command = callselenium)
submit1.grid(column = 3 ,row = 3)




def change_dropdown(*args):
    
    print("hiii")
    #name = ttk.Entry(root)
    #nameEntered = ttk.Entry(mainframe, width = 15, textvariable = name)
    #nameEntered.grid(column = 0, row = 1)
    #button = ttk.Button(mainframe, text = "Click Me", command = clickMe)
    #button.grid(column= 0, row = 2)
    
    


# link function to change dropdown
tkvar.trace('w', change_dropdown)

root.mainloop()
#-----------------------------GUI--------------------------------
print("endeddd ht drop")

