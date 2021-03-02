# Thank you Captain DeadBones
# for the initial code

from Tkinter import * 
from tkSimpleDialog import askstring
from tkFileDialog   import asksaveasfilename
from tkMessageBox   import askokcancel          
class Quitter(Frame):                        
    def __init__(self, parent=None):          
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack()
    def quit(self):
        ans = askokcancel('Verify exit', "Really quit?")
        if ans: Frame.quit(self)

class ScrolledText(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)               
        self.makewidgets()
        self.settext(text, file)
    def makewidgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN)
        sbar.config(command=text.yview)                  
        text.config(yscrollcommand=sbar.set)           
        sbar.pack(side=RIGHT, fill=Y)                   
        text.pack(side=LEFT, expand=YES, fill=BOTH)     
        self.text = text
    def settext(self, text='', file=None):
		text = open(file, 'r').read()
		self.text.delete('1.0', END)
		self.text.insert('1.0', text)
		self.text.insert(END,'sr')
		self.text.focus()                                
    def gettext(self):                               
        return self.text.get('1.0', END+'-1c')         



class SimpleEditor(ScrolledText):                        
    def __init__(self, parent=None, file=None): 
        frm = Frame(parent)
        frm.pack(fill=X)
        Button(frm, text='Save',  command=self.onSave).pack(side=LEFT)
        Quitter(frm).pack(side=LEFT)
        ScrolledText.__init__(self, parent, file=file) 
        self.text.config(font=('courier', 9, 'normal'))
    def onSave(self):
        filename = asksaveasfilename()
        if filename:
            alltext = self.gettext()                      
            open(filename, 'w').write(alltext)          
                            

SimpleEditor(file='simple-gui.py').mainloop()