#!/usr/bin/env python3.4

class Btn(object):
    ''' Btn decorator handles button click event and, just pass button widget 
    as argument to decorator'''
    def __init__(self, btn, label = None):
        #Decorator init
        self.btn = btn # function defined
        self.label = label
        self.__canv = label
        
    def __call__(self,f):
        # decorator callvaht to do next after decorating
        if(type(self.btn)==str):
            #def wraper(arg):
             #   f(arg)
            self.__canv.bind(self.btn, f)#wraper)
            
        elif(str(type(self.btn)) == "<class 'tkinter.Menu'>"):
            self.btn.add_command(label=self.label, command=lambda : f(self.btn,None))
        else:
            self.btn.configure(command = lambda : f(self.btn,None))
        return f

        #menubar.add_command(label="hi", command=hi)
    
class Refr(object):
    '''Refr decorator refreshs "widg" widget with rate ms default is 5000ms
    it uses asincronous function "after"
    '''
    def __init__(self, widg ,delay = 5000):
        '''Decorator init'''
        self.widg = widg # function defined
        self.delay = delay

    def __call__(self,f):
        ''' decorator callvaht to do next after decorating'''
        widg = self.widg
        def count():
                f()
                widg.after(self.delay,count)
        count()


class Event(Btn):
    '''implementing event class with internal key binding'''
    def __init__(self, canvas, event_string):
        super().__init__(event_string, label = canvas)
        self.canvas = canvas
        self.event = event_string

        
if __name__ == "__main__" :
    "event library demo code"
    from tkinter import *
    import random
    
    root = Tk()
    root.title("currency converter USD to GEL")
    
    usd = StringVar()
    gel = StringVar()
    
    usdentry = Entry(root, width = 7, textvariable = usd)
    usdentry.grid(column = 2, row = 1, sticky = (W,E))
    
    Label(root,textvariable=gel).grid(column =2, row = 2, sticky=(W,E))
    
    tkb = Button(root,text = "convert")
    tkb.grid(column = 1, row = 2, sticky = W)
    
    
    @Btn(tkb)
    def convert(sender,evantargs):
        gl =  2.4 * float(usd.get())
        gel.set("{:.2f} ლარი".format(float(gl)))
        print("event sender udi: "+str(sender))
    
    
    usdentry.focus()
    
    # ------------------------------ counter ------------------------------
    
    lb = Label(root, fg = "green")
    lb.grid(row = 3, column = 0)
    
    cnt = 0
    
    @Refr(delay = 1000, widg = lb)
    def counter():
        global cnt
        cnt += 1
        lb.config(text = str(cnt))
    
    btn = Button(root, text = "Close", width = 25, command=root.destroy)
    btn.grid(row = 3,column = 1)

    ######### -----------------------------------------------
    main_menu = Menu(root)
    menubar = Menu(main_menu, tearoff=0)
    print(type(menubar))
    @Btn(menubar,label = 'hi')
    def hi(sender, eventargs):
        print('hi you!')
    # cmd = hi
    #menubar.add_command(label="hi", command=lambda: print('ehehehe'))
    print([n for n in dir(Menu) if 'enu' in n])
    menubar.add_separator()
    main_menu.add_cascade(label='Some', menu=menubar)
    
    root.config(menu=main_menu)
    ######### -----------------------------------------------

    # -------------------- events --------------------
    '''
    bind(code, function)
    Codes:
    <Button-1> - left mouse click
    <B1-Motion> - movement with pressed button
    <ButtonRelease-1> - mouse release
    <Double-Button-1> - double click
    <Enter> - entering some area
    <Leave> - leaving area
    <FocusIn>
    <FocusOut>
    <Return> (Cancel, BackSpace, Tab, Return, Shift_L (any Shift key), Control_L (any Control key), Alt_L (any Alt key), Pause, Caps_Lock, Escape, Page Up, Page Down, End, Home, Left, Up, Right, Down, Print, Insert, Delete, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, Num_Lock, and Scroll_Lock.)
    <Key> to use this don't forget focus_set()
    <Shift-Up>The user pressed the Up arrow, while holding the Shift key pressed. You can use prefixes like Alt, Shift, and Control.
    a – pressed specific button. [a - Z]
    <Configure> - resizing of widget.
    '''

    root.mainloop()


    
