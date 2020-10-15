
#***********************************************HOMEPAGE*****************************************************#


#import modules============================================

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from webpage import web
import random
import time


#working on GUI==================================================================================

win1 = Tk()
win1.geometry("499x250")
win1.config(bg='white')
win1.title("ABES EC Library")
win1.iconbitmap("Book-256.ico")
win1.resizable(0, 0)
p = ImageTk.PhotoImage(Image.open('ABESEC_logo.jpg'))
p1 = ImageTk.PhotoImage(Image.open('photo-1519744792095-2f2205e87b6f.jpeg'))

#College_Logo & Name===============================================================
Label(win1, image=p1, relief="flat", bg="white").place(x=-3, y=-3)
Button(win1, image=p, borderwidth=0, command=web, bg="black",).grid(row=0, column=0)

#-----------------------------------------------------

count = 0
Blank_text = ''
text = " ABES ENGINEERING COLLEGE "
color1 = ['brown4','gold']
def first ():
    global count,Blank_text
    if count >=len(text):
        count=-1
        Blank_text=''
        m.config(text=Blank_text)


    else:
        Blank_text+=text[count]
        m.config(text=Blank_text)
    count+=1
    m.after(150,first)
def color():
    colour=random.choice(color1)
    m.config(fg=colour)
    m.after(20,color)

Label(win1,text='   ',width=20,height=1,font=("georgia ", '20', 'bold'),bg='brown4').place(x=140,y=7)
m=Button(win1, text=' ABES Engineering College ', font=("georgia ", '15', 'bold'), fg='gold',bg='brown4' , relief='solid' , borderwidth=0,command=web,)
m.place(x=140,y=7)
first()
color()

#Student Login Check=============================================

def db():
    import mysql.connector as mydb
    sql = mydb.connect(host="localhost", user='root', password = 'I$0piyush9001', database="abes_library")
    mycursor = sql.cursor()
    mycursor.execute("select addmission_id,password from id_pass")
    temp = 0
    global a
    for j in mycursor:
        if j[0] == e1.get() and j[1] == e2.get():
            temp += 1
            a = e1.get()
    if temp == 1:
        messagebox.showinfo("Access Found","Successfully Log In!")

#Login button click window----------------------------------------------------------
        win1.withdraw()
        win2=Toplevel()
        win2.resizable(0,0)
        win2.geometry("500x600")
        win2.resizable(0, 0)
        win2.title("Administrator")
        win2.iconbitmap("Book-256.ico")
        Back = ImageTk.PhotoImage(Image.open('photo-1519744792095-2f2205e87b61.jpeg'))
        Label(win2, image=Back, relief = "flat", bg = "white").place(x=-3, y=-3)
        p=ImageTk.PhotoImage(Image.open('ABESEC_log.png'))
        Label(win2, image=p, bg='black', borderwidth=0).grid(row=0, column=0, sticky = E)
        Label(win2, text=' ABES Engineering College ', font=("georgia ", '15', 'bold'), fg='gold', bg='brown4', relief='solid', borderwidth=1).grid(row=0,column=1,columnspan=2)

        import mysql.connector as mydb
        sql1 = mydb.connect(host="localhost", user='root', password='I$0piyush9001', database="abes_library")
        mycursor = sql1.cursor()
        text1 = ""
        mycursor.execute("select first_name,last_name,sem,course from detail where admission_id='{}'".format(a))
        for i in mycursor:
            text1 += i[0]+" "+i[1]
            sem = i[2]
            course = i[3]
        def destroy():
            win2.withdraw()
            win1.deiconify()
        text = ""
        mycursor1 = sql1.cursor()
        mycursor1.execute("select book,Date,Time from book where admission_Id='{}'".format(a))
        for i in mycursor1:
            temp = str(i[0])
            text += '\n'+"====|>"+temp+"\n"+"("+i[1]+" "+i[2]+")"
        e = Text(win2, width=50, relief='ridge', borderwidth=1, height=24, font=("arial", "10", "bold"), bg="brown4", fg='gold')
        e.insert(END, text)
        e.place(x=50, y=150)
        Label(win2, text=text1, relief="groove", bg="brown4", fg='gold', font=("Alternity", '10'), borderwidth=5, width=25).grid(row=2,column=1)
        Label(win2, text = str(course)+" SEM->"+str(sem), relief="groove", bg="brown4", fg='gold', font=("Alternity", '10'),borderwidth=5,width=25).grid(row=3,column=1)
        Button(win2, text = "Close!", borderwidth=2,relief="ridge",bg="brown4",fg='gold',font=("alexa",'13','bold'),command=destroy,width=12,).place(x=300,y=550)
        e2.delete(0,END)
        #Live_clock***********************
        def tick():
            time_live=time.strftime("%I:%M:%S %p")
            clock.config(text=time_live)
            clock.after(200,tick)
        clock=Label(win2,font=("Trendy University","10",""),fg="gold",bg="black",width=10,relief="flat")
        clock.place(x=4,y=550)
        tick()
        win2.mainloop()
    else:
        messagebox.showerror("Failed","Combination not found!")
        e1.delete(0,END)
        e2.delete(0,END)


#Sign up button part =================================================

def signup():
    win1.withdraw()
    wins=Toplevel()
    import webpage
    wins.geometry("430x350")
    wins.config(bg='white')
    wins.title("Sign Up")
    wins.iconbitmap("Book-256.ico")
    wins.resizable(0, 0)
    def connection():
        import mysql.connector as mydb
        sql=mydb.connect(host="localhost",user='root',password='I$0piyush9001',database="abes_library")
        mycursor=sql.cursor()
        try:
            play=str(e2.get())
            #pet animal name in lower case-------------------------------------------------
            pet=str(e8.get()).lower()
            play1=play.capitalize()
            #compare password and re-enter password field--------------------------------------------------
            if e6.get()==e7.get() and i.get()==1:
                mycursor.execute("insert into detail values('{}','{}','{}','{}',{},'{}')".format(e1.get(),play1,e3.get(),e4.get(),e5.get(),pet))
                mycursor.execute("insert into id_pass values('{}','{}')".format(e1.get(),e7.get()))
                sql.commit()
                messagebox.showinfo("Successfully Created",f"{play1} your account successfully created!")
                #clean entry box-------------------------------------------------------------
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)
                e5.delete(0,END)
                e6.delete(0,END)
                e7.delete(0,END)
                e8.delete(0,END)
            else:
                messagebox.showwarning("warning","Check password field or Check box!")
                e7.delete(0,END)
        except:
            messagebox.showwarning("Empty field","Check all fields again!")


#Back button coding in sign up page#####################

    def homepage():
        wins.withdraw()
        win1.deiconify()

#label,entry and button################

    Back=ImageTk.PhotoImage(Image.open('photo-1519744792095-2f2205e87b61.jpeg'))
    Label(wins,image=Back,relief="flat",bg="white").place(x=-3,y=-3)
    p=ImageTk.PhotoImage(Image.open('ABESEC_log.png'))
    Button(wins,image=p,bg='black',command=webpage.web,borderwidth=0).grid(row=0,column=0)
    Button(wins,text='ABES Engineering College',command=webpage.web,font=("times of roman ",'15','bold'),bg="brown4", fg="gold",relief='solid',borderwidth=1).grid(row=0,column=1)
    Label(wins, text=" ADMISSION NO ", relief="solid", bg="brown4", fg="gold", font=("dubai ",'10'), borderwidth=1).grid(row=1, column=0, sticky=E)
    Label(wins,text="   FIRST NAME   ",relief="solid",bg="brown4", fg="gold",font=("dubai ",'10'),borderwidth=1).grid(row=2,column=0,sticky=E)
    Label(wins,text="   LAST  NAME   ",relief="solid",bg="brown4", fg="gold",font=("dubai ",'10'),borderwidth=1).grid(row=3,column=0,sticky=E)
    Label(wins,text="      COURSE      ",relief="solid",bg="brown4", fg="gold",font=("dubai ",'10'),borderwidth=1).grid(row=4,column=0,sticky=E)
    Label(wins,text="    SEMESTER    ",relief="solid",bg="brown4", fg="gold",font=("dubai ",'10'),borderwidth=1).grid(row=5,column=0,sticky=E)
    Label(wins,text="   PASSWORD    ",relief="solid",bg="brown4", fg="gold",font=("dubai ",'10'),borderwidth=1).grid(row=6,column=0,sticky=E)
    Label(wins,text=" Re-enter PASS.  ",relief="solid",bg="brown4", fg="gold",font=("dubai ",'10'),borderwidth=1,).grid(row=7,column=0,sticky=E)
    Label(wins,text=" Name of your Pet ",relief="solid",bg="brown4", fg="gold",font=("dubai ",'10'),borderwidth=1,).grid(row=8,column=0,sticky=E)
    i=IntVar()
    Checkbutton(wins,text="I agree with term and condition",bg="black",fg='gold',variable=i).grid(row=9,column=1)
    e1=Entry(wins,width=30,borderwidth=4,relief="groove",font=("arial",11,"bold"),bg="brown4", fg="gold")
    e1.grid(row=1,column=1)
    e2=Entry(wins,width=30,borderwidth=4,relief="groove",font=("arial",11,"bold"),bg="brown4", fg="gold")
    e2.grid(row=2,column=1)
    e3=Entry(wins,width=30,borderwidth=4,relief="groove",font=("arial",11,"bold"),bg="brown4", fg="gold")
    e3.grid(row=3,column=1)
    e4=Entry(wins,width=30,borderwidth=4,relief="groove",font=("arial",11,"bold"),bg="brown4", fg="gold")
    e4.grid(row=4,column=1)
    e5=Entry(wins,width=30,borderwidth=4,relief="groove",font=("arial",11,"bold"),bg="brown4", fg="gold")
    e5.grid(row=5,column=1)
    e6=Entry(wins,width=30,borderwidth=4,relief="groove",show="*",font=("arial",11,"bold"),bg="brown4", fg="gold")
    e6.grid(row=6,column=1)
    e7=Entry(wins,width=30,borderwidth=4,relief="groove",show="*",font=("arial",11,"bold"),bg="brown4", fg="gold")
    e7.grid(row=7,column=1)
    e8=Entry(wins,width=30,borderwidth=4,relief="groove",show="*",font=("arial",11,"bold"),bg="brown4", fg="gold")
    e8.grid(row=8,column=1)
    Label(wins,text='',bg='black').grid(row=9,column=0)
    Button(wins,text="SUBMIT",borderwidth=1,relief="solid",bg="brown4", fg="gold",font=("alexa",'10','bold'),width=12,command=connection).grid(row=10,column=0,sticky=E)
    Button(wins,text="BACK",borderwidth=1,relief="solid",bg="brown4", fg="gold",font=("alexa",'10','bold'),width=10,command=homepage).grid(row=10,column=1)
    def tick():
        time_live=time.strftime("%I:%M:%S %p")
        clock.config(text=time_live)
        clock.after(200,tick)
    clock=Label(wins,font=("Trendy University","11",""),fg="gold",bg="black",width=10,relief="flat")
    clock.place(x=320,y=320)
    tick()
    wins.mainloop()

#window destruction======================================================

def admin():
    win1.withdraw()
    winna=Toplevel()
    from webpage import web
    winna.geometry("430x250")
    winna.resizable(0,0)
    winna.config(bg='white')
    winna.title("Administrator")
    winna.iconbitmap("Book-256.ico")
    Back=ImageTk.PhotoImage(Image.open('photo-1519744792095-2f2205e87b6f.jpeg'))
    Label(winna,image=Back,relief="flat",bg="white").place(x=-3,y=-3)

#Admin access check======================================================

    def db():
        import mysql.connector as mydb
        sql1=mydb.connect(host="localhost",user='root',password='I$0piyush9001',database="abes_library")
        if ee1.get() == 'root' and ee2.get()=='I$0piyush9001':
            messagebox.showinfo("Admin Control","Access found successfully!")
            winna.withdraw()


            #import modules===============================================

            winc=Toplevel()
            winc.geometry("200x100")
            winc.resizable(0,0)
            Back=ImageTk.PhotoImage(Image.open('code.jpeg'))
            Label(winc,image=Back,relief="flat",).place(x=-4,y=-20)

            winc.title("Key")
            winc.iconbitmap("Book-256.ico")
            value=random.choice(["a2314","hdjgd5","njdhdkjs5","jdsu87d4","sgcdv6","jdbjhvhdf","nd7ss"])
            m=open("secrt.txt",'w')
            m.write(value)
            m.close()
            e2=Label(winc,text='',bg="black").grid(row=0,column=1)
            e3=Label(winc,text='',bg="black").grid(row=1,column=0)
            e=Entry(winc,width=12,bg='brown4',fg='gold',borderwidth=2,show="*",font=("15"))
            e.grid(row=1,column=1)


            #Authentication and use file handling for secret code
            def authen():
                if e.get()==value:
                    messagebox.showinfo("Administrator","Access Found")
                    m=open("secrt.txt",'w')
                    m.write("")
                    m.close()
                    winc.withdraw()
            #------------------------------------------------------------------------------------------------------------#
                    #***************************ADMIN CONTROL PORTION************************************************************#


                    #import modules=============================
                    winad=Toplevel()
                    winad.geometry("450x250")
                    winad.title("Administrator")
                    winad.iconbitmap("Book-256.ico")
                    winad.resizable(0,0)

                    #Backgroung image of window------------------------------------

                    Back=ImageTk.PhotoImage(Image.open('photo.jpeg'))
                    Label(winad,image=Back,relief="flat").place(x=-50,y=-5)
                    Label(winad,text='',bg='black').grid(row=0,column=0)
                    p=ImageTk.PhotoImage(Image.open('ABESEC_log.png'))
                    Button(winad,image=p,bg='black',borderwidth=0,command=web).grid(row=0,column=0,padx=10)
                    Button(winad,text=' ABES Engineering College ',font=("georgia ",'14','bold'),fg='gold',bg='brown4',relief='solid',borderwidth=0,anchor=W,command=web).grid(row=0,column=1,)

                    #Goto Homepage throw home button+++++++++++++++++++++++++++++++

                    def home():
                        winad.withdraw()
                        win1.deiconify()

                    #Reset or found password of student account------------------------------------------------------

                    def reset():
                        winad.iconify()
                        winr=Toplevel()
                        winr.title("Reset Account")
                        winr.iconbitmap("Book-256.ico")
                        winr.geometry('200x80')
                        winr.resizable(0, 0)
                        Back=ImageTk.PhotoImage(Image.open('code.jpeg'))
                        Label(winr,image=Back,relief="flat",).place(x=-5,y=-15)
                        Button(winr,text="Delete Account",bg="brown4",fg="gold",command=delete,borderwidth=2,relief="sunken").place(x=35,y=5)
                        def password():
                            winr.destroy()
                            winp=Toplevel()
                            winp.geometry('300x80')
                            winp.title("Reset Account")
                            winp.iconbitmap("Book-256.ico")
                            Back=ImageTk.PhotoImage(Image.open('code.jpeg'))
                            Label(winp,image=Back,relief="flat",).place(x=-5,y=-9)
                            winp.resizable(0, 0)
                            def ok():
                                import mysql.connector as mydb
                                sql=mydb.connect(host="localhost",user='root',password='I$0piyush9001',database="abes_library")
                                mycursor=sql.cursor()
                                pet=0
                                mycursor.execute("select pet from detail where admission_id='{}'".format(e1.get()))
                                for i in mycursor:
                                    pet=str(i[0])
                                if E1.get()==pet:
                                    import mysql.connector as mydb
                                    sql=mydb.connect(host="localhost",user='root',password='I$0piyush9001',database="abes_library")
                                    E1.delete(0,END)
                                    mycursor=sql.cursor()
                                    mycursor.execute("select password from id_pass where addmission_id='{}'".format(e1.get()))
                                    for i in mycursor:
                                        E1.insert(0,i[0])
                                else:
                                    messagebox.showerror('Miss Match',"Not Match")
                            Label(winp,text="Pet Animal",bg="brown4",fg="gold",borderwidth=2,relief="flat").place(x=5,y=5)
                            E1=Entry(winp,bg="brown4",fg="gold",borderwidth=0,relief="sunken")
                            E1.place(x=80,y=5)
                            Button(winp,text="Show Password",command=ok,bg="brown4",fg="gold",borderwidth=3,relief="sunken").place(x=60,y=40)
                            winp.mainloop()
                        Button(winr,text="Show Password",bg="brown4",fg="gold",borderwidth=2,relief="sunken",command=password).place(x=35,y=40)
                        winr.mainloop()

                    def delete():
                        import mysql.connector as mydb
                        sql=mydb.connect(host="localhost",user='root',password='I$0piyush9001',database="abes_library")
                        mycursor=sql.cursor()
                        mycursor.execute("delete from detail where admission_id='{}'".format(e1.get()))
                        mycursor.execute("delete from id_pass where addmission_id='{}'".format(e1.get()))
                        mycursor.execute("delete from book where admission_id='{}'".format(e1.get()))
                        sql.commit()
                        sql.close()
                        messagebox.showinfo("Clear", "Successfully Deleted!")


                    #Student account verification--------------------------------------------------------------------------------

                    def verify():
                        temp=0
                        e2=str(E2.get()).capitalize()
                        import mysql.connector as mydb
                        sql=mydb.connect(host="localhost",user='root',password='I$0piyush9001',database="abes_library")
                        mycursor=sql.cursor()
                        mycursor.execute("select admission_id,first_name,Last_name from detail")
                        for i in mycursor:
                            if i[1]==e2 and i[0]==e1.get():
                                temp+=1
                                global a
                                a=e1.get()
                                global b
                                b=e2
                                global c
                                c=i[2]
                        if temp==1:
                            messagebox.showinfo("Match!","Combination found!")
                            Button(winad,text="Add Books",borderwidth=2,relief="ridge",fg='gold',bg="brown4",font=("alexa",'13','bold'),width=10,command=add_book).place(x=170,y=147)
                            Button(winad,text="Remove Books",borderwidth=2,relief="ridge",fg='gold', bg="brown4",font=("alexa",'13','bold'),width=13,command=delete_book).place(x=310,y=147)
                            Button(winad,text="Reset Account",borderwidth=2,relief="ridge",fg='gold', bg="brown4",font=("alexa",'13','bold'),width=13,command=reset).place(x=220,y=200)
                        else:
                            messagebox.showerror("Warning!","Combination not found!")



                    #Add new book in student account=====================================================================================

                    def add_book():
                        """from tkinter import *
                        from tkinter import messagebox
                        from PIL import Image,ImageTk"""
                        winad.withdraw()
                        wina=Toplevel()
                        wina.geometry("650x600")
                        wina.title("Administrator")
                        wina.iconbitmap("Book-256.ico")
                        wina.resizable(0,0)
                        p=ImageTk.PhotoImage(Image.open('ABESEC_log.png'))
                        Back=ImageTk.PhotoImage(Image.open('photo-1519744792095-2f2205e87b61.jpeg'))
                        Label(wina,image=Back,relief="flat",bg="white").place(x=-3,y=-3)
                        add=b+" "+c
                        def close():
                            wina.withdraw()
                            winad.deiconify()


                    # run query to insert books++++++++++++++++++++++++++++++++++++++++++++++

                        def db():
                            import mysql.connector as mydb
                            import time
                            p=time.ctime()
                            Time=time.strftime("%I:%M:%S %p")
                            Date=time.strftime('%d %A %m, %Y')
                            sql=mydb.connect(host="localhost",user='root',password='I$0piyush9001',database="abes_library")
                            e1=str(E1.get()).capitalize()
                            mycursor=sql.cursor()
                            if e1=="":
                                pass
                            else:
                                mycursor.execute("insert into book values('{}','{}','{}','{}')".format(a,e1,Date,Time))
                                sql.commit()
                                sql.close()

                            text=""
                            sql=mydb.connect(host="localhost",user='root',password='I$0piyush9001',database="abes_library")
                            mycursor1=sql.cursor()
                            mycursor1.execute("select book,Date,Time from book where admission_Id='{}'".format(a))
                            for i in mycursor1:
                                temp=str(i[0])
                                text+='\n'+"====|>"+temp+"\n"+"("+i[1]+" "+i[2]+")"
                            Label(wina,text="  ",bg="black").grid(row=5,column=1)
                            Label(wina,text="  ",bg="black").grid(row=6,column=1)
                            e=Text(wina,width=50,relief='ridge',borderwidth=3,height=20,fg='gold',bg='brown4')
                            e.insert(END,text)
                            E1.delete(0,END)
                            e.grid(row=7,column=1,sticky=W,)



                        Label(wina,image=p,bg='black',anchor='e').grid(row=0,column=0,sticky=E)
                        Label(wina,text=' ABES Engineering College ',font=("georgia ",'15','bold'),fg='gold',bg='brown4',relief='solid',borderwidth=1).grid(row=0,column=1)
                        Label(wina,text='',bg='black').grid(row=1,column=0)
                        Label(wina,text=add,relief="groove",fg='gold',bg='brown4',font=("Alternity",'10'),borderwidth=5,width=25).grid(row=2,column=1)
                        E1=Entry(wina,width=30,borderwidth=2,relief="groove",font=("georgia ",'15','bold'),fg='gold',bg='brown4')
                        E1.grid(row=3,column=1,sticky=W)
                        Button(wina,text="Add Books/View Book",borderwidth=2,relief="ridge",fg='gold',bg='brown4',font=("alexa",'13','bold'),width=17,command=db).grid(row=3,column=2,sticky=E)
                        Button(wina,text="Back",relief="ridge",fg='gold',bg='brown4',font=("alexa",'13','bold'),width=10,command=close).grid(row=4,column=2,sticky=E)

                        E2.delete(0,END)
                        def tick():
                            time_live= time.strftime("%I:%M:%S %p")
                            clock.config(text=time_live)
                            clock.after(200,tick)
                        clock=Label(wina,font=("Trendy University","11",""),fg="gold",bg="black",width=10,relief="flat")
                        clock.place(x=540,y=9)
                        tick()
                        wina.mainloop()

                    # Delete book from user account-----------------------------------------------------------------------------------------------------------

                    def delete_book():
                        winad.withdraw()
                        wind=Toplevel()
                        wind.geometry("690x600")
                        wind.title("Administrator")
                        wind.iconbitmap("Book-256.ico")
                        wind.resizable(0,0)
                        Back=ImageTk.PhotoImage(Image.open('photo-1519744792095-2f2205e87b61.jpeg'))
                        Label(wind,image=Back,relief="flat",).place(x=-3,y=-3)
                        p=ImageTk.PhotoImage(Image.open('ABESEC_log.png'))
                        add=b+" "+c
                        def close():
                            wind.withdraw()
                            winad.deiconify()
                        def db():
                            import mysql.connector as mydb
                            sql=mydb.connect(host="localhost",user='root',password='I$0piyush9001',database="abes_library")
                            e1=str(E1.get()).capitalize()
                            mycursor=sql.cursor()
                            if e1=="":
                                pass
                            else:
                                mycursor.execute("delete from book where book='{}' and admission_id='{}'".format(e1,a))
                                sql.commit()
                                sql.close()
                            text=""
                            sql=mydb.connect(host="localhost",user='root',password='I$0piyush9001',database="abes_library")
                            mycursor1=sql.cursor()
                            mycursor1.execute("select book,Date,Time from book where admission_Id='{}'".format(a))
                            for i in mycursor1:
                                i1=str(i[0])
                                text+='\n'+"====|>"+i1+"\n"+"("+i[1]+" "+i[2]+")"
                            Label(wind,text="  ",bg="black").grid(row=5,column=1)
                            Label(wind,text="  ",bg="black").grid(row=6,column=1)
                            e=Text(wind,width=50,relief='ridge',borderwidth=3,height=20,bg="brown4",fg="gold")
                            e.insert(END,text)
                            e.grid(row=7,column=1)

                        Label(wind,image=p,bg='black',anchor='e').grid(row=0,column=0,sticky=E)
                        Label(wind,text=' ABES Engineering College ',font=("georgia ",'15','bold'),fg='gold',bg='brown4',relief='solid',borderwidth=1).grid(row=0,column=1)
                        Label(wind,text='',bg='black').grid(row=1,column=0)
                        Label(wind,text=add,relief="groove",bg="brown4",fg="gold",font=("Alternity",'10'),borderwidth=5,width=25).grid(row=2,column=1)
                        E1=Entry(wind,width=30,borderwidth=2,relief="groove",font=("georgia ",'15','bold'),bg="brown4",fg="gold")
                        E1.grid(row=3,column=1,sticky=W)
                        Button(wind,text="Remove Books/View Book",borderwidth=2,relief="ridge",bg="brown4",fg="gold",font=("alexa",'13','bold'),width=19,command=db).grid(row=3,column=2,sticky=E)
                        Button(wind,text="Back",relief="ridge",bg="brown4",fg="gold",font=("alexa",'13','bold'),width=10,command=close).grid(row=4,column=2,sticky=S)
                        E2.delete(0,END)
                        def tick():
                            time_live= time.strftime("%I:%M:%S %p")
                            clock.config(text=time_live)
                            clock.after(200,tick)
                        clock=Label(wind,font=("Trendy University","11",""),fg="gold",bg="black",width=10,relief="flat")
                        clock.place(x=540,y=9)
                        tick()
                        wind.mainloop()

                    #Label and buttons of main window++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                    Label(winad,text="Student Admission Id",relief="solid",fg='gold',bg="brown4",font=("dubai ",'11'),borderwidth=1,width=16).grid(row=2,column=0,padx=5)
                    Label(winad,text=" Student First Name ",relief="solid",fg='gold',bg="brown4",font=("dubai ",'11'),borderwidth=1,width=16).grid(row=3,column=0)
                    e1=Entry(winad,width=28,borderwidth=3,relief="ridge",fg='gold',bg="brown4",font=("arial","12","bold"))
                    e1.grid(row=2,column=1)
                    E2=Entry(winad,width=28,borderwidth=3,relief="ridge",fg='gold',bg="brown4",font=("arial","12","bold"))
                    E2.grid(row=3,column=1)
                    Label(winad,text='   ',bg='black').grid(row=4,column=0)
                    Button(winad,text="Verify Profile",borderwidth=2,relief="ridge",fg='gold',bg="brown4",font=("alexa",'13','bold'),width=10,command=verify).grid(row=5,column=0)

                    #Add book--------------------------------------------------------------------

                    Button(winad,text="Add Books",borderwidth=2,relief="ridge",fg='gold',bg="brown4",font=("alexa",'13','bold'),width=10,state="disabled",).place(x=170,y=147)

                    #Remove book---------------------------------------------------------------------

                    Button(winad,text="Remove Books",borderwidth=2,relief="ridge",fg='gold',bg="brown4",font=("alexa",'13','bold'),width=13,state="disabled").place(x=310,y=147)

                    #Reset button-----------------------------------------------------------------------------

                    Button(winad,text="Reset Account",borderwidth=2,relief="ridge",fg='gold', bg="brown4",font=("alexa",'13','bold'),width=13,command=delete_book,state="disabled").place(x=220,y=200)

                    #Home button--------------------------------------------------

                    Button(winad,text="Home",borderwidth=2,relief="ridge",fg='gold', bg="brown4",font=("alexa",'13','bold'),width=13,state="normal",command=home).place(x=70,y=200)
                    def tick():
                            time_live=time.strftime("%I:%M:%S %p")
                            clock.config(text=time_live)
                            clock.after(200,tick)
                    clock=Label(winad,font=("Trendy University","9",""),fg="gold",bg="black",width=10,relief="flat")
                    clock.place(x=350,y=220)
                    tick()
                    winad.mainloop()



















            #------------------------------------------------------------------------------------------------------------------------#        
                else:
                    messagebox.showerror("Warning","Wrong Secret code")
                    m=open("secrt.txt",'w')
                    m.write("")
                    m.close()
                    winc.withdraw()
                    wina.deiconify()
            Button(winc,text="Access",command=authen,bg="brown4",fg='gold',relief="groove",borderwidth=3).place(x=128,y=18)
            def tick():
                    time_live=time.strftime("%I:%M:%S %p")
                    clock.config(text=time_live)
                    clock.after(200,tick)
            clock=Label(winc,font=("Trendy University","8",""),fg="gold",bg="black",width=10,relief="flat")
            clock.place(x=5,y=80)
            tick()
            winc.mainloop()

        else:
            messagebox.showerror("Admin Login","Please check User Id or Password!")

#page destroation====================================================

    def homepage():
        winna.withdraw()
        win1.deiconify()

#Label and button coding===================================================

    p=ImageTk.PhotoImage(Image.open('ABESEC_log.png'))
    Button(winna,image=p,bg='black',command=web,borderwidth=0).grid(row=0,column=1)
    Button(winna,text=' ABES Engineering College ',command=web,font=("georgia ",'15','bold'),fg='gold',bg='brown4',relief='solid',borderwidth=1).grid(row=0,column=2,columnspan=2)
    Label(winna,text="       Admin Id         ",relief="solid",bg="brown4",fg="gold",font=("dubai ",'11'),borderwidth=1).grid(row=2,column=2)
    Label(winna,text=" Admin Password ",relief="solid",bg="brown4",fg="gold",font=("dubai ",'11'),borderwidth=1).grid(row=3,column=2)
    ee1=Entry(winna,width=30,borderwidth=4,relief="groove",show="@",bg="brown4",fg="gold")
    ee1.grid(row=2,column=3)
    ee2=Entry(winna,width=30,borderwidth=4,relief="groove",show="*",bg="brown4",fg="gold")
    ee2.grid(row=3,column=3)
    Label(winna,text='   ',bg='black').grid(row=5,column=0)
    Button(winna,text='Access',borderwidth=1,relief="solid",bg="brown4",fg="gold",font=("arial",'10','bold'),width=15,command=db).grid(row=6,column=2)
    Button(winna,text='HomePage',borderwidth=1,relief="solid",bg="brown4",fg="gold",font=("arial",'10','bold'),width=15,command=homepage).grid(row=6,column=3)
    def tick():
        time_live=time.strftime("%I:%M:%S %p")
        clock.config(text=time_live)
        clock.after(200,tick)
    clock=Label(winna,font=("Trendy University","10",""),fg="gold",bg="black",width=10,relief="flat")
    clock.place(x=10,y=220)
    tick()
    winna.mainloop()

#Help Button coding of homepage=============================================================

def help():
    import os
    os.startfile("Help.pdf")

#credit button coding--------------------------------------------------------------

def credit():
    messagebox.showinfo("Developer","   Piyush Chauhan\n\n    MCA 3rd Year\n\n  Mob.7906392985\n\n💥💥💟 जय श्री राम 💘💥💥\n    Version:1.3")

#label and entry part####################################################

user_id=Label(win1,text="Admission Id",relief="solid",bg="brown4",fg="gold",font=("dubai ",'10'),borderwidth=1,width=16,).grid(row=1,column=0,padx=30)
e1=entry_user=Entry(win1,width=25,borderwidth=2,relief="raise",bg="brown4",fg="gold",font=("arial","12","bold"))
e1.grid(row=1,column=1)
password=Label(win1,text="Password",relief="solid",bg="brown4",fg="gold",font=("dubai ",'10'),borderwidth=1,width=16).grid(row=2,column=0)
e2=entry_pass=Entry(win1,width=25,borderwidth=2,relief="raise",show="*",bg="brown4",fg="gold",font=("10"))
e2.grid(row=2,column=1)
#main window buttons-------------------------------------------------------------------------------------
login=Button(win1,text="Login",borderwidth=3,relief="groove",width=10,bg='brown4',fg="gold",font=("dubai","10","bold"),command=db).place(x=40,y=150)
signup=Button(win1,text="Signup",borderwidth=3,relief="groove",width=10,bg='brown4',fg="gold",font=("dubai","10","bold"),command=signup,).place(x=195,y=150)
admin=Button(win1,text="Admin",borderwidth=3,relief="groove",width=10,bg='brown4',fg="gold",command=admin,font=("dubai","10","bold")).place(x=350,y=150)
Button(win1,text="Help",borderwidth=3,relief="sunken",width=13,bg='black',fg="gold",command=help,font=("dubai","10","bold")).place(x=250,y=215)
Button(win1,text="Credit",borderwidth=3,relief="sunken",width=13,bg='black',fg="gold",command=credit,font=("dubai","10","bold")).place(x=370,y=215)


#Live_clock***********************
def tick():
    time_live=time.strftime("%I:%M:%S %p")
    clock.config(text=time_live)
    clock.after(200,tick)
clock=Label(win1,font=("Trendy University","10",""),fg="gold",bg="black",width=10,relief="flat")
clock.place(x=4,y=220)
tick()
win1.mainloop()
