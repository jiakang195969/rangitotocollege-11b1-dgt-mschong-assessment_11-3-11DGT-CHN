import random
from tkinter import *

window = Tk()
questionpicture=PhotoImage(file="question.png")
questionpicture1=questionpicture.subsample(2,2)
def choice1():
    choice_win = Toplevel()
    choice_win.title("choose")
    mode_var = IntVar(value=1)
    yes_button = Radiobutton(choice_win, text="Yes", variable=mode_var, value=1)
    no_button = Radiobutton(choice_win, text="No", variable=mode_var, value=2)
    yes_button.pack()
    no_button.pack()
    def yesorno():
        select = mode_var.get()  
        choice_win.destroy()      
        click1(select)           
    buttonyon = Button(choice_win, text="confirm", command=yesorno)
    buttonyon.pack()
def click1(mode):
    game1 = Toplevel()
    game1.title("21 games")
    back = PhotoImage(file="normal.png")
    background=back.subsample(2,2)
    totalnumber=21
    canvas1 = Canvas(game1, width=background.width(), height=background.height(), highlightthickness=0)
    canvas1.pack()
    canvas1.background = background
    canvas1.create_image(0, 0, anchor="nw", image=background)
    text_=canvas1.create_text(480, 65, text=f"Total number:{totalnumber}",font=("Ariel",40))
    listplayer=[]
    listcomputer=[]
    text1=canvas1.create_text(480,110,text=f"you: {listplayer}", font=("Ariel",20))
    text2=canvas1.create_text(480,140,text=f"computer: {listcomputer}", font=("Ariel",20))
    if mode==2:
        import random
        a=random.randint(1,3)
        totalnumber-=a
        listcomputer.append(a)
        canvas1.itemconfig(text2,text=f"computer: {listcomputer}")
        canvas1.itemconfig(text_,text=f"Total number:{totalnumber}")
    def gameover(mode,game1):
        over=Toplevel()
        over.title("game over")
        labelover= Label(over, text="You lose!")
        def play_again():
            over.destroy()
            game1.destroy()
            choice1()
              
        def back_to_menu():
            over.destroy()
            game1.destroy()           
        labelover.pack()
        buttonplayagain= Button(over, text="Play Again", command=play_again)
        buttonplayagain.pack()
        buttonbacktomenu= Button(over, text="Back to Menu", command=back_to_menu)
        buttonbacktomenu.pack()
    def gamewin(mode,game1):
        win=Toplevel()
        win.title("you win")
        labelwin= Label(win, text="You win!")
        def play_again():
            win.destroy()
            game1.destroy()
            choice1()
            click1(mode)              
        def back_to_menu():
            win.destroy()
            game1.destroy()           
        labelwin.pack()
        buttonplayagain= Button(win, text="Play Again", command=play_again)
        buttonplayagain.pack()
        buttonbacktomenu= Button(win, text="Back to Menu", command=back_to_menu)
        buttonbacktomenu.pack()               
    def click11():
        game11=Toplevel()
        game11.title("rules")
        bkk=PhotoImage(file="1.1.png")
        bk2 = bkk.subsample(2,2)
        label11= Label(game11, image=bk2)
        label11.pack()
        game11.mainloop()
        game11=Toplevel()
        game11.title("rules")
        bk=PhotoImage(file="1.1.png")
        bk1 = bk.subsample(2,2)
        label11= Label(game11, image=bk1)
        label11.pack()
    def add1():
        if mode==1:
            nonlocal totalnumber
            totalnumber-=1    
            listplayer.append(1)
            canvas1.itemconfig(text1,text=f"you: {listplayer}")
            canvas1.itemconfig(text_,text=f"Total number:{totalnumber}")
            if totalnumber<=0:
                gameover(mode,game1)
                return
            else:
                totalnumber-=3
                listcomputer.append(3)
                canvas1.itemconfig(text2,text=f"computer: {listcomputer}")
                canvas1.itemconfig(text_,text=f"Total number:{totalnumber}")
                
        else:
            
            totalnumber-=1    
            listplayer.append(1)
            canvas1.itemconfig(text1,text=f"you: {listplayer}")
            canvas1.itemconfig(text_,text=f"Total number:{totalnumber}")
            if totalnumber<=0:
                gameover(mode,game1)
                return  
            else:
                import random
                a=random.randint(1,3)
                totalnumber-=a
                listcomputer.append(a)
                canvas1.itemconfig(text2,text=f"computer: {listcomputer}")
                canvas1.itemconfig(text_,text=f"Total number:{totalnumber}")
                if totalnumber<=0:
                    gamewin(mode,game1)
                    return              
    def add2():
        if mode==1:
            nonlocal totalnumber
            totalnumber-=2    
            listplayer.append(2)
            canvas1.itemconfig(text1,text=f"you: {listplayer}")
            canvas1.itemconfig(text_,text=f"Total number:{totalnumber}")
            if totalnumber<=0:
                gameover(mode,game1)
                return
            else:
                totalnumber-=2
                listcomputer.append(2)
                canvas1.itemconfig(text2,text=f"computer: {listcomputer}")
                canvas1.itemconfig(text_,text=f"Total number:{totalnumber}")
                if totalnumber<=0:
                    gamewin(mode,game1)
                    return
        else:
            
            totalnumber-=2    
            listplayer.append(2)
            canvas1.itemconfig(text1,text=f"you: {listplayer}")
            canvas1.itemconfig(text_,text=f"Total number:{totalnumber}")
            if totalnumber<=0:
                gameover(mode,game1)
                return
            else:
                import random
                a=random.randint(1,3)
                totalnumber-=a
                listcomputer.append(a)
                canvas1.itemconfig(text2,text=f"computer: {listcomputer}")
                canvas1.itemconfig(text_,text=f"Total number:{totalnumber}")
                if totalnumber<=0:
                    gamewin(mode,game1)
                    return
    def add3():
        if mode==1:
            nonlocal totalnumber
            totalnumber-=3    
            listplayer.append(3)
            canvas1.itemconfig(text1,text=f"you: {listplayer}")
            canvas1.itemconfig(text_,text=f"Total number:{totalnumber}")
            if totalnumber<=0:
                gameover(mode,game1)
                return
            else:
                totalnumber-=1
                listcomputer.append(1)
                canvas1.itemconfig(text2,text=f"computer: {listcomputer}")
                canvas1.itemconfig(text_,text=f"Total number:{totalnumber}")
                if totalnumber<=0:
                    gamewin(mode,game1)
                    return
        else:
            
            totalnumber-=3    
            listplayer.append(3)
            canvas1.itemconfig(text1,text=f"you: {listplayer}")
            canvas1.itemconfig(text_,text=f"Total number:{totalnumber}")
            if totalnumber<=0:
                gameover(mode,game1)
                return
                gameover(mode,game1)
            else:
                import random
                a=random.randint(1,3)
                totalnumber-=a
                listcomputer.append(a)
                canvas1.itemconfig(text2,text=f"computer: {listcomputer}")
                canvas1.itemconfig(text_,text=f"Total number:{totalnumber}")
                if totalnumber<=0:
                    gamewin(mode,game1)
                    return
    buttona1 = Button(game1,borderwidth=0, highlightthickness=0,image=questionpicture1)
    buttona1.place(x=10,y=100,width=50,height=50)
    buttona1.config(command=click11)
    buttonone = Button(game1, text="1",bg="#41AB4C",font=("Ariel",40))
    buttonone.place(x=180,y=250,width=150,height=150)
    buttontwo = Button(game1,text="2",bg="#41AB4C", font=("Ariel",40))
    buttontwo.place(x=406,y=250,width=150,height=150)
    buttonthree = Button(game1,text="3",bg="#41AB4C", font=("Ariel",40))
    buttonthree.place(x=632,y=250,width=150,height=150)
    buttonone.config(command=add1)
    buttontwo.config(command=add2)
    buttonthree.config(command=add3)
def choice2():
    choice_win = Toplevel()
    choice_win.title("choose")
    modevar = IntVar(value=1)
    yesbutton = Radiobutton(choice_win, text="Yes", variable=modevar, value=1)
    nobutton = Radiobutton(choice_win, text="No", variable=modevar, value=2)
    yesbutton.pack()
    nobutton.pack()
    def yesor_no():
        select = modevar.get()  
        choice_win.destroy()      
        click1(select)           
    buttonyon = Button(choice_win, text="confirm", command=yesor_no)
    buttonyon.pack()
def click2(mode):
    game2 = Toplevel()
    game2.title("Tic Tac Toe")
    back = PhotoImage(file="normal.png")
    background=back.subsample(2,2)
    label2 = Label(game2, image=background)
    label2.pack()
    def click22():
        game22=Toplevel()
        game22.title("rules")
        bkk=PhotoImage(file="2.1.png")
        bk2 = bkk.subsample(2,2)
        label22= Label(game22, image=bk2)
        label22.pack()
        game22.mainloop()
    
    borders = Frame(game2, bg="black")
    borders.place(x=250, y=60, width=456, height=456)
    buttont1 = Button(borders, borderwidth=0, bg="white")
    buttont1.place(x=2, y=2, width=150, height=150)
    buttont2 = Button(borders, borderwidth=0, bg="white")
    buttont2.place(x=153, y=2, width=150, height=150)
    buttont3 = Button(borders, borderwidth=0, bg="white")
    buttont3.place(x=304, y=2, width=150, height=150)
    buttont4 = Button(borders, borderwidth=0, bg="white")
    buttont4.place(x=2, y=153, width=150, height=150)
    buttont5 = Button(borders, borderwidth=0, bg="white")
    buttont5.place(x=153, y=153, width=150, height=150)
    buttont6 = Button(borders, borderwidth=0, bg="white")
    buttont6.place(x=304, y=153, width=150, height=150)
    buttont7 = Button(borders, borderwidth=0, bg="white")
    buttont7.place(x=2, y=304, width=150, height=150)
    buttont8 = Button(borders, borderwidth=0, bg="white")
    buttont8.place(x=153, y=304, width=150, height=150)
    buttont9 = Button(borders, borderwidth=0, bg="white")
    buttont9.place(x=304, y=304, width=150, height=150)
    list_=[buttont1,buttont2,buttont3,buttont4,buttont5,buttont6,buttont7,buttont8,buttont9]
    if mode==2:
        import random
        a=random.choice(list_)
        a.config(text="O", state=DISABLED, font=("Ariel",100))
    def gameoverr1():
        overi=Toplevel()
        overi.title("You win!")
        labeloveri= Label(overi, text="You win!")
        buttona= Button(overi, text="Play again?", command=lambda:[overi.destroy(),game2.destroy(),click2(mode)])
        buttonb= Button(overi, text="Back to menu", command=lambda:[overi.destroy(),game2.destroy()])
        labeloveri.pack()
        buttona.pack()
        buttonb.pack()
    def gameoverr2():
        overi=Toplevel()
        overi.title("You lose!")
        labeloveri= Label(overi, text="You lose!")
        buttona= Button(overi, text="Play again?", command=lambda:[overi.destroy(),game2.destroy(),click2(mode)])
        buttonb= Button(overi, text="Back to menu", command=lambda:[overi.destroy(),game2.destroy()])
        labeloveri.pack()
        buttona.pack()
        buttonb.pack()
    def gameoverr3():
        overi=Toplevel()
        overi.title("It's a draw!")
        labeloveri= Label(overi, text="It's a draw!")
        buttona= Button(overi, text="Play again?", command=lambda:[overi.destroy(),game2.destroy(),click2(mode)])
        buttonb= Button(overi, text="Back to menu", command=lambda:[overi.destroy(),game2.destroy()])
        labeloveri.pack()
        buttona.pack()
        buttonb.pack()
    def check_winner():
        winning_combinations = [(buttont1, buttont2, buttont3),(buttont4, buttont5, buttont6),(buttont7, buttont8, buttont9),(buttont1, buttont4, buttont7),(buttont2, buttont5, buttont8),(buttont3, buttont6, buttont9),(buttont1, buttont5, buttont9),(buttont3, buttont5, buttont7)]
        for combo in winning_combinations:
            texts = [btn.cget("text") for btn in combo]
            if texts == ["X", "X", "X"]:
                gameoverr1()
                return
            elif texts == ["O", "O", "O"]:
                gameoverr2()
                return
        if all(btn.cget("state") == DISABLED for btn in list_):
            gameoverr3()
    def changex():
        for btn in list_:
            if btn.cget("text") == "":
                btn.config(text="X", state=DISABLED, font=("Ariel",100))
                break
    def changeo():
        for btn in list_:
            if btn.cget("text") == "":
                btn.config(text="O", state=DISABLED, font=("Ariel",100))
                break
    def player():
        if mode==1:
            for btn in list_:
                btn.config(command=changex)
                break
            check_winner()

    buttonta2 = Button(game2,borderwidth=0, highlightthickness=0,image=questionpicture1)
    buttonta2.place(x=10,y=100,width=50,height=50)
    buttonta2.config(command=click22)

    game2.mainloop()
def click3():
    game3 = Toplevel()
    game3.title("Find planes' head")
    back = PhotoImage(file="normal.png")
    background=back.subsample(2,2)
    canvasplane=Canvas(game3, width=background.width(), height=background.height(), highlightthickness=0)
    canvasplane.pack()
    canvasplane.background = background
    canvasplane.create_image(0, 0, anchor="nw", image=background)
    zero=0
    steps=canvasplane.create_text(830,150,text=f"Steps:{zero}", font=("Ariel",30))
    def increasesteps():
        nonlocal zero
        zero+=1
        canvasplane.itemconfig(steps,text=f"Steps:{zero}")
    def click33():
        game33 = Toplevel()
        game33.title("rules")
        game333 = PhotoImage(file="3.1.png")
        bk3 = game333.subsample(2,2)
        label33 = Label(game33, image=bk3)
        label33.image = bk3  
        label33.pack()
    def playagain():
        yey= Toplevel()
        yey.title("game over")
        labelyey= Label(yey, text="You win!")
        bback = Button(yey, text="Back to Menu", command=lambda:[yey.destroy(),game3.destroy()])
        bagain = Button(yey, text="Play Again", command=lambda:[yey.destroy(),game3.destroy(),click3()])
        labelyey.pack()
        bback.pack()
        bagain.pack()
    def plane1():
        def stopplane():
            s3 = buttons3.cget("state")
            s64 = buttons64.cget("state")
            if s3 == DISABLED and s64 == DISABLED:
                playagain()
        def plane11red():
            buttons3.config(bg="red")
            increasesteps()
            buttons3.config(state=DISABLED)
            stopplane()
        buttons3.config(command=plane11red)
        
        def plane11blue1():
            buttons11.config(bg="blue")
            increasesteps()
            buttons11.config(state=DISABLED)
        buttons11.config(command=plane11blue1)
        def plane11blue2():
            buttons12.config(bg="blue")
            increasesteps()
            buttons12.config(state=DISABLED)
        buttons12.config(command=plane11blue2)
        def plane11blue3():
            buttons13.config(bg="blue")
            increasesteps()
            buttons13.config(state=DISABLED)
        buttons13.config(command=plane11blue3)
        def plane11blue4():
            buttons14.config(bg="blue")
            increasesteps()
            buttons14.config(state=DISABLED)
        buttons14.config(command=plane11blue4)
        def plane11blue5():
            buttons15.config(bg="blue")
            increasesteps()
            buttons15.config(state=DISABLED)
        buttons15.config(command=plane11blue5)
        def plane11blue6():
            buttons23.config(bg="blue")
            increasesteps()
            buttons23.config(state=DISABLED)
        buttons23.config(command=plane11blue6)
        def plane11blue7():
            buttons32.config(bg="blue")
            increasesteps()
            buttons32.config(state=DISABLED)
        buttons32.config(command=plane11blue7)
        def plane11blue8():
            buttons33.config(bg="blue")
            increasesteps()
            buttons33.config(state=DISABLED)
        buttons33.config(command=plane11blue8)
        def plane11blue9():
            buttons34.config(bg="blue")
            increasesteps()
            buttons34.config(state=DISABLED)
        buttons34.config(command=plane11blue9)
        def plane12red():
            buttons64.config(bg="red")
            increasesteps()
            buttons64.config(state=DISABLED)
            stopplane()
        buttons64.config(command=plane12red)
        def plane12blue1():
            buttons45.config(bg="blue") 
            increasesteps()
            buttons45.config(state=DISABLED)
        buttons45.config(command=plane12blue1)
        def plane12blue2():
            buttons55.config(bg="blue")
            increasesteps()
            buttons55.config(state=DISABLED)
        buttons55.config(command=plane12blue2)
        def plane12blue3():
            buttons57.config(bg="blue") 
            increasesteps()
            buttons57.config(state=DISABLED)
        buttons57.config(command=plane12blue3)
        def plane12blue4():
            buttons65.config(bg="blue")  
            increasesteps()
            buttons65.config(state=DISABLED) 
        buttons65.config(command=plane12blue4)
        def plane12blue5():
            buttons66.config(bg="blue")
            increasesteps()
            buttons66.config(state=DISABLED)
        buttons66.config(command=plane12blue5)
        def plane12blue6():
            buttons67.config(bg="blue")  
            increasesteps()
            buttons67.config(state=DISABLED)   
        buttons67.config(command=plane12blue6)
        def plane12blue7():
            buttons75.config(bg="blue")
            increasesteps()
            buttons75.config(state=DISABLED)
        buttons75.config(command=plane12blue7)
        def plane12blue8():
            buttons77.config(bg="blue") 
            increasesteps()
            buttons77.config(state=DISABLED)
        buttons77.config(command=plane12blue8)
        def plane12blue9():
            buttons85.config(bg="blue")
            increasesteps()
            buttons85.config(state=DISABLED)
        buttons85.config(command=plane12blue9)
        def set_defaults():
            def make_click(btn):
                def on_click():
                    increasesteps()
                    btn.config(state=DISABLED)
                return on_click
            for w in border.winfo_children():
                if isinstance(w, Button):
                    if not w.cget("command"):
                        w.config(command=make_click(w))
        set_defaults()

    def plane2():
        def stopplanes():
            s34 = buttons34.cget("state")
            s75 = buttons75.cget("state")
            if s34 == DISABLED and s75 == DISABLED:
                playagain()
        def plane21red():
            buttons34.config(bg="red")
            increasesteps()
            buttons34.config(state=DISABLED)
            stopplanes()
        buttons34.config(command=plane21red)
        def plane21blue1():
            buttons3.config(bg="blue")
            increasesteps()
            buttons3.config(state=DISABLED)
        buttons3.config(command=plane21blue1)
        def plane21blue2():
            buttons4.config(bg="blue")
            increasesteps()
            buttons4.config(state=DISABLED)
        buttons4.config(command=plane21blue2)
        def plane21blue3():
            buttons5.config(bg="blue")
            increasesteps()
            buttons5.config(state=DISABLED)
        buttons5.config(command=plane21blue3)
        def plane21blue4():
            buttons14.config(bg="blue")
            increasesteps()
            buttons14.config(state=DISABLED)
        buttons14.config(command=plane21blue4)
        def plane21blue5():
            buttons22.config(bg="blue")
            increasesteps()
            buttons22.config(state=DISABLED)
        buttons22.config(command=plane21blue5)
        def plane21blue6():
            buttons23.config(bg="blue")
            increasesteps()
            buttons23.config(state=DISABLED)
        buttons23.config(command=plane21blue6)
        def plane21blue7():
            buttons24.config(bg="blue")
            increasesteps()
            buttons24.config(state=DISABLED)
        buttons24.config(command=plane21blue7)
        def plane21blue8():
            buttons25.config(bg="blue")
            increasesteps()
            buttons25.config(state=DISABLED)
        buttons25.config(command=plane21blue8)
        def plane21blue9():
            buttons26.config(bg="blue")
            increasesteps()
            buttons26.config(state=DISABLED)
        buttons26.config(command=plane21blue9)
        def plane22red():
            buttons75.config(bg="red")
            increasesteps()
            buttons75.config(state=DISABLED)
            stopplanes()
        buttons75.config(command=plane22red)
        def plane22blue1():
            buttons54.config(bg="blue")
            increasesteps()
            buttons54.config(state=DISABLED)
        buttons54.config(command=plane22blue1)
        def plane22blue2():
            buttons62.config(bg="blue")
            increasesteps()
            buttons62.config(state=DISABLED)
        buttons62.config(command=plane22blue2)
        def plane22blue3():
            buttons64.config(bg="blue")
            increasesteps()
            buttons64.config(state=DISABLED)
        buttons64.config(command=plane22blue3)
        def plane22blue4():
            buttons72.config(bg="blue")
            increasesteps()
            buttons72.config(state=DISABLED)
        buttons72.config(command=plane22blue4)
        def plane22blue5():
            buttons73.config(bg="blue")
            increasesteps()
            buttons73.config(state=DISABLED)
        buttons73.config(command=plane22blue5)
        def plane22blue6():
            buttons74.config(bg="blue")
            increasesteps()
            buttons74.config(state=DISABLED)
        buttons74.config(command=plane22blue6)
        def plane22blue7():
            buttons82.config(bg="blue")
            increasesteps()
            buttons82.config(state=DISABLED)
        buttons82.config(command=plane22blue7)
        def plane22blue8():
            buttons84.config(bg="blue")
            increasesteps()
            buttons84.config(state=DISABLED)
        buttons84.config(command=plane22blue8)
        def plane22blue9():
            buttons94.config(bg="blue")
            increasesteps()
            buttons94.config(state=DISABLED)
        buttons94.config(command=plane22blue9)
        def set_defaults():
            def make_click(btn):
                def on_click():
                    increasesteps()
                    btn.config(state=DISABLED)
                return on_click
            for w in border.winfo_children():
                if isinstance(w, Button):
                    if not w.cget("command"):
                        w.config(command=make_click(w))
        set_defaults()
    def plane3():
        def stopplaness():
            s36 = buttons36.cget("state")
            s83 = buttons83.cget("state")
            if s36 == DISABLED and s83 == DISABLED:
                playagain()
        def plane31red():
            buttons36.config(bg="red")
            increasesteps()
            buttons36.config(state=DISABLED)
            stopplaness()
        buttons36.config(command=plane31red)
        def plane31blue1():
            buttons44.config(bg="blue")
            increasesteps()
            buttons44.config(state=DISABLED)
        buttons44.config(command=plane31blue1)
        def plane31blue2():
            buttons45.config(bg="blue")
            increasesteps()
            buttons45.config(state=DISABLED)
        buttons45.config(command=plane31blue2)
        def plane31blue3():
            buttons46.config(bg="blue")
            increasesteps()
            buttons46.config(state=DISABLED)
        buttons46.config(command=plane31blue3)
        def plane31blue4():
            buttons47.config(bg="blue")
            increasesteps()
            buttons47.config(state=DISABLED)
        buttons47.config(command=plane31blue4)
        def plane31blue5():
            buttons48.config(bg="blue")
            increasesteps()
            buttons48.config(state=DISABLED)
        buttons48.config(command=plane31blue5)
        def plane31blue6():
            buttons56.config(bg="blue")
            increasesteps()
            buttons56.config(state=DISABLED)
        buttons56.config(command=plane31blue6)
        def plane31blue7():
            buttons65.config(bg="blue")
            increasesteps()
            buttons65.config(state=DISABLED)
        buttons65.config(command=plane31blue7)
        def plane31blue8():
            buttons66.config(bg="blue")
            increasesteps()
            buttons66.config(state=DISABLED)
        buttons66.config(command=plane31blue8)
        def plane31blue9():
            buttons67.config(bg="blue")
            increasesteps()
            buttons67.config(state=DISABLED)
        buttons67.config(command=plane31blue9)
        def plane32red():
            buttons83.config(bg="red")
            increasesteps()
            buttons83.config(state=DISABLED)
            stopplaness()
        buttons83.config(command=plane32red)
        def plane32blue1():
            buttons52.config(bg="blue")
            increasesteps()
            buttons52.config(state=DISABLED)
        buttons52.config(command=plane32blue1)
        def plane32blue2():
            buttons53.config(bg="blue")
            increasesteps()
            buttons53.config(state=DISABLED)
        buttons53.config(command=plane32blue2)
        def plane32blue3():
            buttons54.config(bg="blue")
            increasesteps()
            buttons54.config(state=DISABLED)
        buttons54.config(command=plane32blue3)
        def plane32blue4():
            buttons63.config(bg="blue")
            increasesteps()
            buttons63.config(state=DISABLED)  
        buttons63.config(command=plane32blue4)
        def plane32blue5():
            buttons71.config(bg="blue")
            increasesteps()
            buttons71.config(state=DISABLED)
        buttons71.config(command=plane32blue5)
        def plane32blue6():
            buttons72.config(bg="blue")
            increasesteps()
            buttons72.config(state=DISABLED)
        buttons72.config(command=plane32blue6)
        def plane32blue7():
            buttons73.config(bg="blue")
            increasesteps()
            buttons73.config(state=DISABLED)
        buttons73.config(command=plane32blue7)
        def plane32blue8():
            buttons74.config(bg="blue")
            increasesteps()
            buttons74.config(state=DISABLED)
        buttons74.config(command=plane32blue8)
        def plane32blue9():
            buttons75.config(bg="blue")
            increasesteps()
            buttons75.config(state=DISABLED)
        buttons75.config(command=plane32blue9)
        def set_defaults():
            def make_click(btn):
                def on_click():
                    increasesteps()
                    btn.config(state=DISABLED)
                return on_click
            for w in border.winfo_children():
                if isinstance(w, Button):
                    if not w.cget("command"):
                        w.config(command=make_click(w))
        set_defaults()
    def plane4():
        def stopplaness():
            s8 = buttons36.cget("state")
            s97 = buttons83.cget("state")
            if s8 == DISABLED and s97 == DISABLED:
                playagain()
        def plane41red():
            buttons8.config(bg="red")
            increasesteps()
            buttons8.config(state=DISABLED)
            stopplaness()
        buttons8.config(command=plane41red)
        def plane41blue1():
            buttons16.config(bg="blue")
            increasesteps()
            buttons16.config(state=DISABLED)
        buttons16.config(command=plane41blue1)
        def plane41blue2():
            buttons17.config(bg="blue")
            increasesteps()
            buttons17.config(state=DISABLED)
        buttons17.config(command=plane41blue2)
        def plane41blue3():
            buttons18.config(bg="blue")
            increasesteps()
            buttons18.config(state=DISABLED)
        buttons18.config(command=plane41blue3)
        def plane41blue4():
            buttons19.config(bg="blue")
            increasesteps()
            buttons19.config(state=DISABLED)
        buttons19.config(command=plane41blue4)
        def plane41blue5():
            buttons20.config(bg="blue")
            increasesteps()
            buttons20.config(state=DISABLED)
        buttons20.config(command=plane41blue5)
        def plane41blue6():
            buttons28.config(bg="blue")
            increasesteps()
            buttons28.config(state=DISABLED)
        buttons28.config(command=plane41blue6)
        def plane41blue7():
            buttons37.config(bg="blue")
            increasesteps()
            buttons37.config(state=DISABLED)
        buttons37.config(command=plane41blue7)
        def plane41blue8():
            buttons38.config(bg="blue")
            increasesteps()
            buttons38.config(state=DISABLED)
        buttons38.config(command=plane41blue8)
        def plane41blue9():
            buttons39.config(bg="blue")
            increasesteps()
            buttons39.config(state=DISABLED)
        buttons39.config(command=plane41blue9)
        def plane42red():
            buttons97.config(bg="red")
            increasesteps()
            buttons97.config(state=DISABLED)
            stopplaness()
        buttons97.config(command=plane42red)
        def plane42blue1():
            buttons67.config(bg="blue")
            increasesteps()
            buttons67.config(state=DISABLED)
        buttons67.config(command=plane42blue1)
        def plane42blue2():
            buttons68.config(bg="blue")
            increasesteps()
            buttons68.config(state=DISABLED)
        buttons68.config(command=plane42blue2)
        def plane42blue3():
            buttons69.config(bg="blue")
            increasesteps()
            buttons69.config(state=DISABLED)
        buttons69.config(command=plane42blue3)
        def plane42blue4():
            buttons78.config(bg="blue")
            increasesteps()
            buttons78.config(state=DISABLED)
        buttons78.config(command=plane42blue4)
        def plane42blue5():
            buttons86.config(bg="blue")
            increasesteps()
            buttons86.config(state=DISABLED)
        buttons86.config(command=plane42blue5)
        def plane42blue6():
            buttons87.config(bg="blue")
            increasesteps()
            buttons87.config(state=DISABLED)
        buttons87.config(command=plane42blue6)
        def plane42blue7():
            buttons88.config(bg="blue")
            increasesteps()
            buttons88.config(state=DISABLED)
        buttons88.config(command=plane42blue7)
        def plane42blue8():
            buttons89.config(bg="blue")
            increasesteps()
            buttons89.config(state=DISABLED)
        buttons89.config(command=plane42blue8)
        def plane42blue9():
            buttons90.config(bg="blue")
            increasesteps()
            buttons90.config(state=DISABLED)
        buttons90.config(command=plane42blue9)
        def set_defaults():
            def make_click(btn):
                def on_click():
                    increasesteps()
                    btn.config(state=DISABLED)
                return on_click
            for w in border.winfo_children():
                if isinstance(w, Button):
                    if not w.cget("command"):
                        w.config(command=make_click(w))
        set_defaults()
    border = Frame(game3, bg="black")
    border.place(x=230, y=50, width=473, height=473)
    buttons1 = Button(border, borderwidth=0, bg="white")
    buttons1.place(x=2, y=2, width=46, height=46)
    buttons2 = Button(border, borderwidth=0, bg="white")
    buttons2.place(x=49, y=2, width=46, height=46)
    buttons3 = Button(border, borderwidth=0, bg="white")
    buttons3.place(x=96, y=2, width=46, height=46)
    buttons4 = Button(border, borderwidth=0, bg="white")
    buttons4.place(x=143, y=2, width=46, height=46)
    buttons5 = Button(border, borderwidth=0, bg="white")
    buttons5.place(x=190, y=2, width=46, height=46)
    buttons6 = Button(border, borderwidth=0, bg="white")
    buttons6.place(x=237, y=2, width=46, height=46)
    buttons7 = Button(border, borderwidth=0, bg="white")
    buttons7.place(x=284, y=2, width=46, height=46)
    buttons8 = Button(border, borderwidth=0, bg="white")
    buttons8.place(x=331, y=2, width=46, height=46)
    buttons9 = Button(border, borderwidth=0, bg="white")
    buttons9.place(x=378, y=2, width=46, height=46)
    buttons10 = Button(border, borderwidth=0, bg="white")
    buttons10.place(x=425, y=2, width=46, height=46)
    buttons11 = Button(border, borderwidth=0, bg="white")
    buttons11.place(x=2, y=49, width=46, height=46)
    buttons12 = Button(border, borderwidth=0, bg="white")
    buttons12.place(x=49, y=49, width=46, height=46)
    buttons13 = Button(border, borderwidth=0, bg="white")
    buttons13.place(x=96, y=49, width=46, height=46)
    buttons14 = Button(border, borderwidth=0, bg="white")
    buttons14.place(x=143, y=49, width=46, height=46)
    buttons15 = Button(border, borderwidth=0, bg="white")
    buttons15.place(x=190, y=49, width=46, height=46)
    buttons16 = Button(border, borderwidth=0, bg="white")
    buttons16.place(x=237, y=49, width=46, height=46)
    buttons17 = Button(border, borderwidth=0, bg="white")
    buttons17.place(x=284, y=49, width=46, height=46)
    buttons18 = Button(border, borderwidth=0, bg="white")
    buttons18.place(x=331, y=49, width=46, height=46)
    buttons19 = Button(border, borderwidth=0, bg="white")
    buttons19.place(x=378, y=49, width=46, height=46)
    buttons20 = Button(border, borderwidth=0, bg="white")
    buttons20.place(x=425, y=49, width=46, height=46)
    buttons21 = Button(border, borderwidth=0, bg="white")
    buttons21.place(x=2, y=96, width=46, height=46)
    buttons22 = Button(border, borderwidth=0, bg="white")
    buttons22.place(x=49, y=96, width=46, height=46)
    buttons23 = Button(border, borderwidth=0, bg="white")
    buttons23.place(x=96, y=96, width=46, height=46)
    buttons24 = Button(border, borderwidth=0, bg="white")
    buttons24.place(x=143, y=96, width=46, height=46)
    buttons25 = Button(border, borderwidth=0, bg="white")
    buttons25.place(x=190, y=96, width=46, height=46)
    buttons26 = Button(border, borderwidth=0, bg="white")
    buttons26.place(x=237, y=96, width=46, height=46)
    buttons27 = Button(border, borderwidth=0, bg="white")
    buttons27.place(x=284, y=96, width=46, height=46)
    buttons28 = Button(border, borderwidth=0, bg="white")
    buttons28.place(x=331, y=96, width=46, height=46)
    buttons29 = Button(border, borderwidth=0, bg="white")
    buttons29.place(x=378, y=96, width=46, height=46)
    buttons30 = Button(border, borderwidth=0, bg="white")
    buttons30.place(x=425, y=96, width=46, height=46)
    buttons31 = Button(border, borderwidth=0, bg="white")
    buttons31.place(x=2, y=143, width=46, height=46)
    buttons32 = Button(border, borderwidth=0, bg="white")
    buttons32.place(x=49, y=143, width=46, height=46)
    buttons33 = Button(border, borderwidth=0, bg="white")
    buttons33.place(x=96, y=143, width=46, height=46)
    buttons34 = Button(border, borderwidth=0, bg="white")
    buttons34.place(x=143, y=143, width=46, height=46)
    buttons35 = Button(border, borderwidth=0, bg="white")
    buttons35.place(x=190, y=143, width=46, height=46)
    buttons36 = Button(border, borderwidth=0, bg="white")
    buttons36.place(x=237, y=143, width=46, height=46)
    buttons37 = Button(border, borderwidth=0, bg="white")
    buttons37.place(x=284, y=143, width=46, height=46)
    buttons38 = Button(border, borderwidth=0, bg="white")
    buttons38.place(x=331, y=143, width=46, height=46)
    buttons39 = Button(border, borderwidth=0, bg="white")
    buttons39.place(x=378, y=143, width=46, height=46)
    buttons40 = Button(border, borderwidth=0, bg="white")
    buttons40.place(x=425, y=143, width=46, height=46)
    buttons41 = Button(border, borderwidth=0, bg="white")
    buttons41.place(x=2, y=190, width=46, height=46)
    buttons42 = Button(border, borderwidth=0, bg="white")
    buttons42.place(x=49, y=190, width=46, height=46)
    buttons43 = Button(border, borderwidth=0, bg="white")
    buttons43.place(x=96, y=190, width=46, height=46)
    buttons44 = Button(border, borderwidth=0, bg="white")
    buttons44.place(x=143, y=190, width=46, height=46)
    buttons45 = Button(border, borderwidth=0, bg="white")
    buttons45.place(x=190, y=190, width=46, height=46)
    buttons46 = Button(border, borderwidth=0, bg="white")
    buttons46.place(x=237, y=190, width=46, height=46)
    buttons47 = Button(border, borderwidth=0, bg="white")
    buttons47.place(x=284, y=190, width=46, height=46)
    buttons48 = Button(border, borderwidth=0, bg="white")
    buttons48.place(x=331, y=190, width=46, height=46)
    buttons49 = Button(border, borderwidth=0, bg="white")
    buttons49.place(x=378, y=190, width=46, height=46)
    buttons50 = Button(border, borderwidth=0, bg="white")
    buttons50.place(x=425, y=190, width=46, height=46)
    buttons51 = Button(border, borderwidth=0, bg="white")
    buttons51.place(x=2, y=237, width=46, height=46)
    buttons52 = Button(border, borderwidth=0, bg="white")
    buttons52.place(x=49, y=237, width=46, height=46)
    buttons53 = Button(border, borderwidth=0, bg="white")
    buttons53.place(x=96, y=237, width=46, height=46)
    buttons54 = Button(border, borderwidth=0, bg="white")
    buttons54.place(x=143, y=237, width=46, height=46)
    buttons55 = Button(border, borderwidth=0, bg="white")
    buttons55.place(x=190, y=237, width=46, height=46)
    buttons56 = Button(border, borderwidth=0, bg="white")
    buttons56.place(x=237, y=237, width=46, height=46)
    buttons57 = Button(border, borderwidth=0, bg="white")
    buttons57.place(x=284, y=237, width=46, height=46)
    buttons58 = Button(border, borderwidth=0, bg="white")
    buttons58.place(x=331, y=237, width=46, height=46)
    buttons59 = Button(border, borderwidth=0, bg="white")
    buttons59.place(x=378, y=237, width=46, height=46)
    buttons60 = Button(border, borderwidth=0, bg="white")
    buttons60.place(x=425, y=237, width=46, height=46)
    buttons61 = Button(border, borderwidth=0, bg="white")
    buttons61.place(x=2, y=284, width=46, height=46)
    buttons62 = Button(border, borderwidth=0, bg="white")
    buttons62.place(x=49, y=284, width=46, height=46)
    buttons63 = Button(border, borderwidth=0, bg="white")
    buttons63.place(x=96, y=284, width=46, height=46)
    buttons64 = Button(border, borderwidth=0, bg="white")
    buttons64.place(x=143, y=284, width=46, height=46)
    buttons65 = Button(border, borderwidth=0, bg="white")
    buttons65.place(x=190, y=284, width=46, height=46)
    buttons66 = Button(border, borderwidth=0, bg="white")
    buttons66.place(x=237, y=284, width=46, height=46)
    buttons67 = Button(border, borderwidth=0, bg="white")
    buttons67.place(x=284, y=284, width=46, height=46)
    buttons68 = Button(border, borderwidth=0, bg="white")
    buttons68.place(x=331, y=284, width=46, height=46)
    buttons69 = Button(border, borderwidth=0, bg="white")
    buttons69.place(x=378, y=284, width=46, height=46)
    buttons70 = Button(border, borderwidth=0, bg="white")
    buttons70.place(x=425, y=284, width=46, height=46)
    buttons71 = Button(border, borderwidth=0, bg="white")
    buttons71.place(x=2, y=331, width=46, height=46)
    buttons72 = Button(border, borderwidth=0, bg="white")
    buttons72.place(x=49, y=331, width=46, height=46)
    buttons73 = Button(border, borderwidth=0, bg="white")
    buttons73.place(x=96, y=331, width=46, height=46)
    buttons74 = Button(border, borderwidth=0, bg="white")
    buttons74.place(x=143, y=331, width=46, height=46)
    buttons75 = Button(border, borderwidth=0, bg="white")
    buttons75.place(x=190, y=331, width=46, height=46)
    buttons76 = Button(border, borderwidth=0, bg="white")
    buttons76.place(x=237, y=331, width=46, height=46)
    buttons77 = Button(border, borderwidth=0, bg="white")
    buttons77.place(x=284, y=331, width=46, height=46)
    buttons78 = Button(border, borderwidth=0, bg="white")
    buttons78.place(x=331, y=331, width=46, height=46)
    buttons79 = Button(border, borderwidth=0, bg="white")
    buttons79.place(x=378, y=331, width=46, height=46)
    buttons80 = Button(border, borderwidth=0, bg="white")
    buttons80.place(x=425, y=331, width=46, height=46)
    buttons81 = Button(border, borderwidth=0, bg="white")
    buttons81.place(x=2, y=378, width=46, height=46)
    buttons82 = Button(border, borderwidth=0, bg="white")
    buttons82.place(x=49, y=378, width=46, height=46)
    buttons83 = Button(border, borderwidth=0, bg="white")
    buttons83.place(x=96, y=378, width=46, height=46)
    buttons84 = Button(border, borderwidth=0, bg="white")
    buttons84.place(x=143, y=378, width=46, height=46)
    buttons85 = Button(border, borderwidth=0, bg="white")
    buttons85.place(x=190, y=378, width=46, height=46)
    buttons86 = Button(border, borderwidth=0, bg="white")
    buttons86.place(x=237, y=378, width=46, height=46)
    buttons87 = Button(border, borderwidth=0, bg="white")
    buttons87.place(x=284, y=378, width=46, height=46)
    buttons88 = Button(border, borderwidth=0, bg="white")
    buttons88.place(x=331, y=378, width=46, height=46)
    buttons89 = Button(border, borderwidth=0, bg="white")
    buttons89.place(x=378, y=378, width=46, height=46)
    buttons90 = Button(border, borderwidth=0, bg="white")
    buttons90.place(x=425, y=378, width=46, height=46)
    buttons91 = Button(border, borderwidth=0, bg="white")
    buttons91.place(x=2, y=425, width=46, height=46)
    buttons92 = Button(border, borderwidth=0, bg="white")
    buttons92.place(x=49, y=425, width=46, height=46)
    buttons93 = Button(border, borderwidth=0, bg="white")
    buttons93.place(x=96, y=425, width=46, height=46)
    buttons94 = Button(border, borderwidth=0, bg="white")
    buttons94.place(x=143, y=425, width=46, height=46)
    buttons95 = Button(border, borderwidth=0, bg="white")
    buttons95.place(x=190, y=425, width=46, height=46)
    buttons96 = Button(border, borderwidth=0, bg="white")
    buttons96.place(x=237, y=425, width=46, height=46)
    buttons97 = Button(border, borderwidth=0, bg="white")
    buttons97.place(x=284, y=425, width=46, height=46)
    buttons98 = Button(border, borderwidth=0, bg="white")
    buttons98.place(x=331, y=425, width=46, height=46)
    buttons99 = Button(border, borderwidth=0, bg="white")
    buttons99.place(x=378, y=425, width=46, height=46)
    buttons100 = Button(border, borderwidth=0, bg="white")
    buttons100.place(x=425, y=425, width=46, height=46)

    planelist=[plane1,plane2,plane3]
    random.choice(planelist)()
    buttona3 = Button(game3,borderwidth=0, highlightthickness=0,image=questionpicture1)
    buttona3.place(x=10,y=100,width=50,height=50)
    buttona3.config(command=click33)
def click4():
    game4 = Toplevel()
    game4.title("Anagram")
    back = PhotoImage(file="normal.png")
    background=back.subsample(2,2)
    label4 = Label(game4, image=background)
    label4.pack()
    def click44():
        game44=Toplevel()
        game44.title("rules")
        bkkkk=PhotoImage(file="4.1.png")
        bk4 = bkkkk.subsample(2,2)
        label44= Label(game44, image=bk4)
        label44.pack()
        game44.mainloop()
    buttona4 = Button(game4,borderwidth=0, highlightthickness=0,image=questionpicture1)
    buttona4.place(x=10,y=100,width=50,height=50)
    buttona4.config(command=click44)
    list_=[]
    game4.mainloop()
photo = PhotoImage(file="1.png")
one= PhotoImage(file="1).png")
two= PhotoImage(file="2).png")
three= PhotoImage(file="3).png")
four= PhotoImage(file="4).png")
images = photo.subsample(2,2)
imageone = one.subsample(2,2) 
imagetwo = two.subsample(2,2)
imagethree = three.subsample(2,2)
imagefour = four.subsample(2,2) 
label = Label(window, image=images)
button1 = Button(window,text="",borderwidth=0, highlightthickness=0,image=imageone)
button1.place(x=227,y=99,width=202,height=157)
button2 = Button(window,text="",borderwidth=0, highlightthickness=0,image=imagetwo)
button2.place(x=525,y=99,width=202,height=157)
button3 = Button(window,text="",borderwidth=0, highlightthickness=0,image=imagethree)
button3.place(x=227,y=290,width=202,height=157)
button4 = Button(window,text="",borderwidth=0, highlightthickness=0,image=imagefour)
button4.place(x=525,y=290,width=202,height=157)
label.pack()
button1.config(command=choice1)
button2.config(command=click2)
button3.config(command=click3)
button4.config(command=click4)
window.mainloop()