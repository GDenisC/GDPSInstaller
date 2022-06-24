
from pathlib import Path
import tkinter as gui
from logs import logsinit, log
from gdinst import installGD
from coding import checkURL, CreateGDPS
from sys import argv

if '--debug' in argv:
    logsinit()

def database() -> str:
    return entryDatabase.get()

def installGD_call():
    installGD()
    buttonInstall.configure(state='disabled')

def checkURL_call():
    if checkURL(database()):
        buttonCreate.config(state='normal')
    else:
        buttonCreate.config(state='disabled')

def GDPSCreate_call():
    checkURL_call()
    if not buttonCheck['state'] == 'disabled':
        buttonCreate.config(state='disabled')
        CreateGDPS(database())

log('app start')

# app
window = gui.Tk()

if not '--fix' in argv:
    window.eval('tk::PlaceWindow . center') # python 3.x
window.resizable(False, False)
try:
    window.iconbitmap('gdpsico.ico')
except:
    pass
window.title('GDPS Installer v1')
window.geometry('310x165')

# gui

label1 = gui.Label(text='Input database: http://')
label1.grid(column=1, row=1)

entryDatabase = gui.Entry(width=31) # www.boomlings.com/database width
entryDatabase.grid(column=2, row=1)

buttonInstall = gui.Button(window, text=' Install GD 2.113 ', command=installGD_call)
buttonInstall.place(anchor=gui.CENTER, y=50, relx=0.5)

buttonCheck = gui.Button(window, text=' Check URL ', command=checkURL_call)
buttonCheck.place(anchor=gui.CENTER, y=80, relx=0.5)

buttonCreate = gui.Button(window, text=' Create GDPS ', command=GDPSCreate_call, font=('Arial', 20), state='disabled')
buttonCreate.place(anchor=gui.CENTER, y=130, relx=0.5)

#

if Path('Geometry.Dash').exists():
    log('Geometry.Dash already created, buttonInstall disabled')
    buttonInstall.configure(state='disabled')

window.mainloop()
log('app stop')
