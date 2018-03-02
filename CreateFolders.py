# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:37:38 2017

@author: Kyle Marchuk

For use at the Biological Imaging Development Center (BIDC) at UCSF. 

This is a small GUI designed to populate a folder with a series of subfolders 
sequentially named.

"""

import os
from tkinter import Tk,Label,BOTH,FALSE,TRUE,W,E,END, RAISED
from tkinter import Frame,Button,Entry
from tkinter import filedialog


origPath = 'D:/Users/'
baseName = 'ROI'

class createGUI(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        
        self.parent = parent
        self.parent.title("Create Folders")       
        self.pack(fill=BOTH,expand = 1)
        self.centerWindow()
        self.initUI()
        
    def centerWindow(self):
        
        w = 500
        h = 120
        
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw-w)/2
        y = (sh-h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w,h,x,y))
        
        #self.style = Style()
        #self.style.theme_use("vista")
        
    def initUI(self):
        
        #self.style = Style()
        #self.style.theme_use("vista")
        
        topFrame = Frame(self,borderwidth=1,relief=RAISED)
        topFrame.pack(fill=BOTH,expand=TRUE)
        
        Label(topFrame, text = "Select Master Directory:").grid(row=0,column=0,padx=5,pady=5)      
        self.entryCreate = Entry(topFrame,width=50)
        self.entryCreate.grid(row=0,column=1,padx=5,pady=5)
        self.entryCreate.insert(END,origPath)
        Button(topFrame,width=2,text="...",command=self.dirOpen).grid(row=0,column=2,sticky=W)
        
        secondFrame = Frame(self,borderwidth=1,relief=RAISED)
        secondFrame.pack(fill=BOTH,expand=TRUE)
        secondFrame.columnconfigure(0,minsize=125)
        secondFrame.columnconfigure(1,minsize=125)
        secondFrame.columnconfigure(2,minsize=25)
        secondFrame.columnconfigure(3,minsize=125)
        
        Label(secondFrame, text = "Start:").grid(row=1,column=0,padx=0,pady=5,sticky=E)
        self.entryStart = Entry(secondFrame,width=15)
        self.entryStart.grid(row=1,column=1,padx=0,pady=5)
        
        Label(secondFrame, text = "End:").grid(row=1,column=2,padx=0,pady=5,sticky=E)
        self.entryEnd = Entry(secondFrame,width=15)
        self.entryEnd.grid(row=1,column=3,padx=0,pady=0)
        
        thirdFrame = Frame(self,borderwidth=1,relief=RAISED)
        thirdFrame.pack(fill=BOTH,expand=TRUE)
        thirdFrame.columnconfigure(0,minsize=100)
        thirdFrame.columnconfigure(1,minsize=100)
        thirdFrame.columnconfigure(2,minsize=100)
        thirdFrame.columnconfigure(3,minsize=100)
        thirdFrame.columnconfigure(4,minsize=100)
        
        Label(thirdFrame, text = "Root Name:").grid(row=0,column=1,padx=0,pady=5,sticky=E)
        self.entryRoot = Entry(thirdFrame,width=10)
        self.entryRoot.grid(row=0,column=2,padx=0,pady=5)
        self.entryRoot.insert(END,baseName)
        
        
        Button(thirdFrame,width=20,text = "Create Folders",command=self.runCreate).grid(row=0,column=3,pady=5,sticky=W)

    def dirOpen(self):

        dirName = filedialog.askdirectory()           
               
        if dirName != '':
            self.entryCreate.delete(0,END)
            self.entryCreate.insert(END,dirName)
            
    def runCreate(self):        
       createPath = self.entryCreate.get()
       baseName = self.entryRoot.get()
       
       startNum = self.entryStart.get()
       endNum = self.entryEnd.get()
       
       for num in range(int(startNum),int(endNum)+1):
         os.makedirs(createPath+'/'+baseName+str(num).zfill(2))
           

def main():
    
    root = Tk()
    createGUI(root)
    root.resizable(width=FALSE,height=FALSE)
    root.mainloop()
    
if __name__ == '__main__':
    main()