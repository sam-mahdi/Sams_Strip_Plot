from tkinter import *
from tkinter import filedialog
import os

hnca=()
hnca_directory=()
hncacb=()
hncacb_directory=()
hnco=()
hnco_directory=()
hncaco=()
hncaco_directory=()
hncoca=()
hncoca_directory=()
NOE=()
NOE_directory=()


class newTopLevel(object):
    def __init__(self, root):
        self.newWindow = Toplevel(root)
        self.newWindow.title("Peaklist Files")
        self.newWindow.geometry("600x600")
        Label(self.newWindow, text="HNCA File\n Use Browse Button").grid(row=0)
        self.pdb_line = Entry(self.newWindow)
        self.pdb_line.grid(row=0, column=1)
        self.newWindow.btn = Button(self.newWindow,text='browse',command=self.input_hnca)
        self.newWindow.btn.grid(row=0,column=2)
        Label(self.newWindow, text="HNCACB File\n Use Browse Button").grid(row=1)
        self.pdb_start_line = Entry(self.newWindow)
        self.pdb_start_line.grid(row=1, column=1)
        self.newWindow.btn = Button(self.newWindow,text='browse',command=self.input_hncacb)
        self.newWindow.btn.grid(row=1,column=2)
        Label(self.newWindow, text="HNCO File\n Use Browse Button").grid(row=2)
        self.pdb_end_line = Entry(self.newWindow)
        self.pdb_end_line.grid(row=2, column=1)
        self.newWindow.btn = Button(self.newWindow,text='browse',command=self.input_hnco)
        self.newWindow.btn.grid(row=2,column=2)
        Label(self.newWindow, text="HNCOCA File\n Use Browse Butoon").grid(row=3)
        self.pdb_chain_line = Entry(self.newWindow)
        self.pdb_chain_line.grid(row=3, column=1)
        self.newWindow.btn = Button(self.newWindow,text='browse',command=self.input_hncoca)
        self.newWindow.btn.grid(row=3,column=2)
        Label(self.newWindow, text="HNCACO File\n Use Browse Butoon").grid(row=4)
        self.pdb_chain_line = Entry(self.newWindow)
        self.pdb_chain_line.grid(row=4, column=1)
        self.newWindow.btn = Button(self.newWindow,text='browse',command=self.input_hncaco)
        self.newWindow.btn.grid(row=4,column=2)
        Label(self.newWindow, text="NOE File\n Use Browse Butoon").grid(row=5)
        self.pdb_chain_line = Entry(self.newWindow)
        self.pdb_chain_line.grid(row=5, column=1)
        self.newWindow.btn = Button(self.newWindow,text='browse',command=self.input_NOE)
        self.newWindow.btn.grid(row=5,column=2)

    def input_hnca(self):
        fullpath = filedialog.askopenfilename(parent=self.newWindow, title='Choose a file')
        global hnca
        global hnca_directory
        hnca_directory=os.path.dirname(fullpath)
        hnca= os.path.basename(fullpath)
        label3=Label(self.newWindow,text=fullpath).grid(row=0,column=1)
    def input_hncacb(self):
        fullpath = filedialog.askopenfilename(parent=self.newWindow, title='Choose a file')
        global hncacb
        global hncacb_directory
        hncacb_directory=os.path.dirname(fullpath)
        hncacb= os.path.basename(fullpath)
        label3=Label(self.newWindow,text=fullpath).grid(row=1,column=1)
    def input_hnco(self):
        fullpath = filedialog.askopenfilename(parent=self.newWindow, title='Choose a file')
        global hnco
        global hnco_directory
        hnco_directory=os.path.dirname(fullpath)
        hnco= os.path.basename(fullpath)
        label3=Label(self.newWindow,text=fullpath).grid(row=2,column=1)
    def input_hncoca(self):
        fullpath = filedialog.askopenfilename(parent=self.newWindow, title='Choose a file')
        global hncoca
        global hncoca_directory
        hncoca_directory=os.path.dirname(fullpath)
        hncoca= os.path.basename(fullpath)
        label3=Label(self.newWindow,text=fullpath).grid(row=3,column=1)
    def input_hncaco(self):
        fullpath = filedialog.askopenfilename(parent=self.newWindow, title='Choose a file')
        global hncaco
        global hncaco_directory
        hncaco_directory=os.path.dirname(fullpath)
        hncaco= os.path.basename(fullpath)
        label3=Label(self.newWindow,text=fullpath).grid(row=4,column=1)
    def input_NOE(self):
        fullpath = filedialog.askopenfilename(parent=self.newWindow, title='Choose a file')
        global NOE
        global NOE_directory
        NOE_directory=os.path.dirname(fullpath)
        NOE= os.path.basename(fullpath)
        label3=Label(self.newWindow,text=fullpath).grid(row=5,column=1)

def variables():
    return hnca,hnca_directory,hncacb, hncacb_directory, hnco, hnco_directory, hncaco, hncaco_directory, hncoca, hncoca_directory, NOE, NOE_directory
