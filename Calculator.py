from tkinter import *;import webbrowser as web;from tkinter import messagebox;from tkinter import ttk; from tkinter import filedialog as fd
import random;import pytz;import time;from datetime import *;import string; import wikipedia
root=Tk()
root.title('Tkinter')
answers=[]

(entry:=Entry(root,width=30)).grid(row=0,column=0,columnspan=4)

class button:
    def __init__(self,name,row,column):
        self.name=name
        self.row=row
        self.column=column
    def click(self):entry.insert(END,self.name)
    def draw(self,columns=1):
        self.self=Button(root,text=self.name,height=2,width=5,command=self.click)
        self.self.grid(row=self.row,column=self.column,columnspan=columns)

#C aka clear       
(a:=button('C',1,3)).draw()
def clear(): entry.delete(0,END)
a.self['command']=clear

#backspace
(a:=button('⌫',1,2)).draw()
def delete(): entry.delete(len(entry.get())-1)
a.self['command']=delete

buttons=['1','2','3','+','4','5','6','-','7','8','9','*','.','0','=','/']
for a in range(2,6):
    for b in range(4):
        buttons[b+(a-2)*4]=button(buttons[b+(a-2)*4],a,b)
        buttons[b+(a-2)*4].draw()

# equals
def calculate():
    global answers
    answers.append(entry.get())
    box.insert(END,entry.get())
    answer=eval(entry.get())
    entry.delete(0,END)
    entry.insert(0,answer)
buttons[14].self['command']=calculate

(y:=Frame(root)).grid(row=6,columnspan=4,column=0)
scroll=Scrollbar(y,orient=VERTICAL)
box=Listbox(y,yscrollcommand=scroll.set)
scroll.config(command=box.yview)

#history
buttons.append(button('History',1,0))
buttons[16].draw(2)
def show():
    y.grid(row=6,columnspan=4,column=0)
    scroll.pack(side=RIGHT,fill=Y)
    box.pack(side=LEFT, fill=BOTH, expand=1)
    buttons[16].self['command']=hide
def hide():
    y.grid_forget()
    buttons[16].self['command']=show
buttons[16].self['command']=show
buttons[16].self['width']=10
curselection=False
try:
    while True:
        if box.curselection() and box.curselection()!=curselection:
            entry.delete(0,END)
            entry.insert(0,answers[box.curselection()[0]])
            curselection=box.curselection()
        root.update()
except: pass














root.mainloop()


##(Label(root,text='Name')).grid(row=0,column=0)
##(Label(root,text='Date of Birth')).grid(row=2,column=0)
##(Label(root,text='Email')).grid(row=3,column=0)
##(Label(root,text='Password')).grid(row=4,column=0)
##(Label(root,text='Confirm Password')).grid(row=5,column=0)
##(Label(root,text='Month')).grid(row=1,column=1)
##(Label(root,text='Day')).grid(row=1,column=2)
##(Label(root,text='Year')).grid(row=1,column=3)
##
##(name:=Entry(root)).grid(row=0,column=1,columnspan=3)
##(email:=Entry(root)).grid(row=3,column=1,columnspan=3)
##(password:=Entry(root,show='*')).grid(row=4,column=1,columnspan=3)
##(password2:=Entry(root,show='*')).grid(row=5,column=1,columnspan=3)
##
##month,day,year=StringVar(),StringVar(),StringVar()
##months,days,years=list(range(1,13)),list(range(1,31)),list(range(2000,2020))
##(OptionMenu(root,month,*months)).grid(row=2,column=1)
##(OptionMenu(root,day,*days)).grid(row=2,column=2)
##(OptionMenu(root,year,*years)).grid(row=2,column=3)
##
##def create():
##    if not(name.get() and email.get() and password.get() and password.get()==password2.get() and month.get() and day.get() and year.get()):
##        return messagebox.showwarning('Fail','Issue')
##    x=open('info.txt','w')
##    birth=month.get()+' / '+day.get()+' / '+year.get()+'\n'
##    x.write(name.get()+'\n'+birth+email.get()+'\n'+password.get())
##    x.close()
##    messagebox.showinfo('Success','Account created')
##(Button(root,text='Create Account',command=create)).grid(row=6,columnspan=4)


##(text:=Text(root)).pack()
##menu=Menu(root)
##file=Menu(menu,tearoff=0)
##file_name=None
##
##def new():
##    text.delete('1.0',END)
##    global file_name
##file.add_command(label='New',command=new)
##
##def save():
##    global file_name
##    if file_name==None: file_name=fd.asksaveasfilename()
##    x=open(file_name,'w')
##    x.write(text.get('0.0',END))
##    x.close()
##file.add_command(label='Save',command=save)
##
##def open_file():
##    global file_name
##    file_name=fd.askopenfilename()
##    x=open(file_name,'r')
##    text.delete('0.0',END)
##    while (line:=x.readline()):
##        text.insert(END,line)
##file.add_command(label='Open',command=open_file)
##
##file.add_separator()
##file.add_command(label='Exit',command=root.destroy)
##menu.add_cascade(label='File',menu=file)
##root.config(menu=menu)


##(Label(root,text='Search')).grid(row=0,column=0)
##(entry:=Entry(root)).grid(row=0,column=1)
##(answer:=Text(root,width=30)).grid(row=1,columnspan=3)
##def search():
##    answer.delete('1.0',END)
##    answer.insert(END,wikipedia.summary(entry.get(),sentences=1))
##(Button(root,command=search,text='Submit')).grid(row=0,column=2)


##info={}
##x=open('info.txt','r')
##while (a:=x.readline()):
##    a=a.split(' ')
##    info[a[0]]=a[1][:-1]
##x.close()
##
##notebook=ttk.Notebook(root)
##Login,Register,Reset,Unsubscribe=Frame(notebook),Frame(notebook),Frame(notebook),Frame(notebook)
##notebook.add(Login,text='Login')
##notebook.add(Register,text='Register')
##notebook.add(Reset,text='Reset Password')
##notebook.add(Unsubscribe,text='Unsubscribe')
##notebook.pack()
##
###login
##(Label(Login,text='Username')).grid(row=0,column=0)
##(Label(Login,text='Password')).grid(row=1,column=0)
##(username:=Entry(Login)).grid(row=0,column=1)
##(password:=Entry(Login,show='*')).grid(row=1,column=1)
##
##def login():
##    if not username.get() in list(info.keys()): return messagebox.showwarning('Login failed','Username not found')
##    if info[username.get()]!=password.get(): return messagebox.showerror('Login failed','The password is incorrect')
##    messagebox.showinfo('Login Success','Login successful')
##(Button(Login,text='Login',command=login)).grid(row=2,column=1)
##
###register
##(Label(Register,text='Username')).grid(row=0,column=0)
##(Label(Register,text='Password')).grid(row=1,column=0)
##(new_username:=Entry(Register)).grid(row=0,column=1)
##(new_password:=Entry(Register,show='*')).grid(row=1,column=1)
##
##def register():
##    if new_username.get() in list(info.keys()):return messagebox.showerror('Username taken','Username is already used')
##    info[new_username.get()]=new_password.get()
##    x=open('info.txt','a+')
##    x.write((new_username.get()+' '+new_password.get()+'\n'))
##    messagebox.showinfo('Registration Successful','Registration succeded')
##(Button(Register,text='Register',command=register)).grid(row=2,column=1)
##
###Reset
##(Label(Reset,text='Username')).grid(row=0,column=0)
##(Label(Reset,text='Password')).grid(row=1,column=0)
##(reset_username:=Entry(Reset)).grid(row=0,column=1)
##(reset_password:=Entry(Reset,show='*')).grid(row=1,column=1)
##
##def reset():
##    if not reset_username.get() in list(info.keys()): return messagebox.showwarning('Reset failed','Username not found')
##    info[reset_username.get()]=reset_password.get()
##    x=open('info.txt','w')
##    for a in info: x.write((a+' '+info[a]+'\n'))
##    messagebox.showinfo('Reset Successful','Reset succeded')
##(Button(Reset,text='Reset',command=reset)).grid(row=2,column=1)
##
###Unsubscribe
##(Label(Unsubscribe,text='Username')).grid(row=0,column=0)
##(Label(Unsubscribe,text='Password')).grid(row=1,column=0)
##(unsubscribe_username:=Entry(Unsubscribe)).grid(row=0,column=1)
##(unsubscribe_password:=Entry(Unsubscribe,show='*')).grid(row=1,column=1)
##
##def unsubscribe():
##    if not unsubscribe_username.get() in list(info.keys()): return messagebox.showwarning('Unsubscribe failed','Username not found')
##    del info[unsubscribe_username.get()]
##    x=open('info.txt','w')
##    for a in info: x.write((a+' '+info[a]+'\n'))
##    messagebox.showinfo('Unsubscribe Successful','Unsubscribe succeded')
##(Button(Unsubscribe,text='Unsubscribe',command=unsubscribe)).grid(row=2,column=1)


##(y:=Frame(root)).grid(row=1)
##scroll=Scrollbar(y,orient=VERTICAL)
##box=Listbox(y,yscrollcommand=scroll.set)
##scroll.config(command=box.yview)
##scroll.pack(side=RIGHT,fill=Y)
##box.pack(side=LEFT, fill=BOTH, expand=1)
##(time:=Label(root)).grid(row=2)
##for a in pytz.all_timezones: box.insert(END,a)
##
##try:
##    while True:
##        if box.curselection(): time['text']=(datetime.now((pytz.timezone(pytz.all_timezones[box.curselection()[0]])))).strftime('%Y-%m-%d %H:%M:%S %p %Z')
##        root.update()
##except:
##    pass    
    

##(info:=Frame(root)).pack()
##(buttons:=Frame(root)).pack()
##(book:=Frame(root)).pack()
##
##(Label(info,text='Name')).grid(row=0,column=0)
##(Label(info,text='Phone')).grid(row=1,column=0)
##(name:=Entry(info)).grid(row=0,column=1)
##(phone:=Entry(info)).grid(row=1,column=1)
##
##scroll=Scrollbar(book,orient=VERTICAL)
##box=Listbox(book,yscrollcommand=scroll.set)
##scroll.config(command=box.yview)
##scroll.pack(side=RIGHT,fill=Y)
##box.pack(side=LEFT, fill=BOTH, expand=1)
##
##pb={'Smith, Bob':'333-3333','Smith, Joe':'222-2222','Smith, Sara':'111-1111',}
##for a in pb: box.insert(END,a)
##
##def add():
##    if not name.get(): return
##    pb[name.get()]=phone.get()
##    box.delete(0,END)
##    for a in pb: box.insert(END,a)
##
##def delete():
##    del pb[list(pb.keys())[box.curselection()[0]]]
##    box.delete(0,END)
##    for a in pb: box.insert(END,a)
##
##def search():
##    phone.delete(0,END)
##    phone.insert(0,pb[list(pb.keys())[name.get()]])
##
##(Button(buttons,text='Add',command=add)).grid(row=0,column=0)
##(Button(buttons,text='Delete',command=delete)).grid(row=0,column=1)
##(Button(buttons,text='Search',command=search)).grid(row=0,column=2)
##
##try:
##    while 1:
##        if box.curselection():
##            x=list(pb.keys())[box.curselection()[0]]
##            name.delete(0,END)
##            name.insert(0,x)
##            phone.delete(0,END)
##            phone.insert(0,pb[x])
##        root.update()
##except: print('fail')


##words=['python','code','computer','tech']
##word=random.choice(words)
##
##def attempt():
##    global word
##    if guess.get()==word:
##        messagebox.showinfo('Success','That was correct')
##        
##    else:
##        if messagebox.askretrycancel('Failure','Do you want to try again?'): return
##
##    instruction['text']='Click to start'
##    rword['text']='                                 '
##    guess.delete(0,END)
##    word=random.choice(words)
##
##def enter():
##    global word
##    instruction['text']='Guess the word'
##    rword['text']=('').join(random.sample(word,len(word)))
##
##(instruction:=Button(root,text='Click to start',bg='orange',command=enter,width=30)).grid(row=0,column=0,columnspan=2)
##
##(guess:=Entry(root)).grid(row=1,column=1)
##
##(rword:=Label(root,text='                ')).grid(row=1,column=0)
##
##(submit:=Button(root,text='Submit',command=attempt)).grid(row=2,column=1)

##num=random.choice(range(100))
##info={'Krish':'KrishKalra'}
##
##(Label(root,text='Guess the number (0-100)',font='Arial 14 bold')).grid(row=0,column=0)
##
##(number:=Entry(root)).grid(row=0,column=1)
##
##def clear():
##    number.delete(0,END)
##
##def login():
##    if int(number.get())<num:
##        messagebox.showinfo('','The number is higher')
##    elif int(number.get())>num:
##        messagebox.showinfo('','The number is lower')
##    elif int(number.get())==num:
##        messagebox.showinfo('','Your guess was correct!')
##    
##(Button(root,text='Clear',command=clear,fg='blue')).grid(row=2,column=1,sticky=W)
##(Button(root,text='Guess number',command=login,fg='green')).grid(row=2,column=0,sticky=W)
##(Button(root,text='Quit',command=exit,fg='red')).grid(row=2,column=1,sticky=E)

###India
##India_flag=PhotoImage(file='india flag.png')
##
##(India:=Frame(root,width=150,height=150)).grid(row=0,column=0)
##
##(Label(India,text='India')).pack()
##
##(Label(India,image=India_flag)).pack()
##
##(India_time:=Label(India,text='')).pack()
##
###USA
##USA_flag=PhotoImage(file='us flag.png')
##
##(USA:=Frame(root,width=150,height=150)).grid(row=0,column=1)
##
##(Label(USA,text='USA')).pack()
##
##(Label(USA,image=USA_flag)).pack()
##
##(USA_time:=Label(USA,text='')).pack()
##
##while 1:
##    India_time['text']=(datetime.now((pytz.timezone('Asia/Calcutta')))).strftime('%Y-%m-%d %H:%M:%S %p %Z')
##    USA_time['text']=(datetime.now((pytz.timezone('US/Pacific')))).strftime('%Y-%m-%d %H:%M:%S %p %Z')
##    root.update()

##(password:=Label(root,text='Generated Password:',fg='blue',font='Arial 12 bold')).pack()
##(y:=Frame(root)).pack()
##(x:=Frame(root)).pack()
##
##(Label(x,text='Password Length:',font='Arial 12 bold')).pack(side=LEFT)
##
##(length:=Spinbox(x,from_=6,to=12)).pack(side=RIGHT)
##
##(Label(y,text='Password Strength:',font='Arial 12 bold')).pack(side=LEFT)
##
##strength=IntVar()
##(Radiobutton(y,text='Low',variable=strength,value=0)).pack(side=LEFT)
##(Radiobutton(y,text='Medium',variable=strength,value=1)).pack(side=LEFT)
##(Radiobutton(y,text='High',variable=strength,value=2)).pack(side=LEFT)
##
##def generate():
##    word='Generated Password: '
##    if strength.get()==0:
##        for a in range(int(length.get())):
##            word+=random.choice(string.ascii_letters)
##    if strength.get()==1:
##        for a in range(int(length.get())):
##            word+=random.choice(string.ascii_letters+string.digits)
##    if strength.get()==2:
##        for a in range(int(length.get())):
##            word+=random.choice(string.ascii_letters+string.digits+string.punctuation)
##    password['text']=word
##(Button(root,text='Generate',bg='lightgreen',font='Arial 12 bold',command=generate)).pack()

##(y:=Frame(root)).grid()
##(Label(y,text='Choose the items that you want to buy')).pack()
##milk,chocolate,eggs,bread,fruits=IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
##(Milk:=Checkbutton(y,text='Milk',variable=milk)).pack()
##(Chocolate:=Checkbutton(y,text='Chocolate',variable=chocolate)).pack()
##(Eggs:=Checkbutton(y,text='Eggs',variable=eggs)).pack()
##(Bread:=Checkbutton(y,text='Bread',variable=bread)).pack()
##(Fruits:=Checkbutton(y,text='Fruits',variable=fruits)).pack()
##(x:=Frame(root)).grid()
##(z:=Frame(root)).grid()
##(a:=Frame(root,bg='grey')).grid(row=0,column=0)
##(b:=Frame(root)).grid(row=0,column=1)
##(c:=Frame(root,bg='grey')).grid(row=0,column=2)
##(d:=Frame(root)).grid(row=0,column=3)
##    
##def clear():
##    Milk.deselect()
##    Chocolate.deselect()
##    Eggs.deselect()
##    Bread.deselect()
##    Fruits.deselect()
##
##def checkout():
##    z.grid_forget()
##    final=0
##    
##    (Label(a,text='Items',bg='grey')).pack()
##    (Label(b,text='Quantity')).pack()
##    (Label(c,text='Unit Price',bg='grey')).pack()
##    (Label(d,text='Total')).pack()
##    
##    if milk.get():
##        (Label(a,text='Milk',bg='grey')).pack()
##        (Label(b,text=milk.get())).pack()
##        (Label(c,text='$2',bg='grey')).pack()
##        (Label(d,text=str(2*int(milk.get())))).pack()
##        final+=2*int(milk.get())
##    if chocolate.get():
##        (Label(a,text='Chocolate',bg='grey')).pack()
##        (Label(b,text=chocolate.get())).pack()
##        (Label(c,text='$1',bg='grey')).pack()
##        (Label(d,text=chocolate.get())).pack()
##        final+=int(chocolate.get())
##    if eggs.get():
##        (Label(a,text='Eggs',bg='grey')).pack()
##        (Label(b,text=eggs.get())).pack()
##        (Label(c,text='$3',bg='grey')).pack()
##        (Label(d,text=str(3*int(eggs.get())))).pack()
##        final+=3*int(eggs.get())
##    if bread.get():
##        (Label(a,text='Bread',bg='grey')).pack()
##        (Label(b,text=bread.get())).pack()
##        (Label(c,text='$4',bg='grey')).pack()
##        (Label(d,text=str(4*int(bread.get())))).pack()
##        final+=4*int(bread.get())
##    if fruits.get():
##        (Label(a,text='Fruits',bg='grey')).pack()
##        (Label(b,text=fruits.get())).pack()
##        (Label(c,text='$5',bg='grey')).pack()
##        (Label(d,text=str(5*int(fruits.get())))).pack()
##        final+=5*int(fruits.get())
##        
##    (Label(root,text=('Final Price: '+str(final)))).grid(row=1,column=0,columnspan=4)
##
##def nextpage():
##    x.grid_forget()
##    y.grid_forget()
##    global milk; global chocolate; global eggs; global bread; global fruits
##
##    if milk.get():
##        (Label(z,text='Milk')).grid(row=0,column=0)
##        (milk:=Spinbox(z,from_=0,to=10)).grid(row=0,column=1)
##    if chocolate.get():
##        (Label(z,text='Chocolate')).grid(row=1,column=0)
##        (choclate:=Spinbox(z,from_=0,to=10)).grid(row=1,column=1)
##    if eggs.get():
##        (Label(z,text='Eggs')).grid(row=2,column=0)
##        (eggs:=Spinbox(z,from_=0,to=10)).grid(row=2,column=1)
##    if bread.get():
##        (Label(z,text='Bread')).grid(row=3,column=0)
##        (bread:=Spinbox(z,from_=0,to=10)).grid(row=3,column=1)
##    if fruits.get():
##        (Label(z,text='Fruits')).grid(row=4,column=0)
##        (fruits:=Spinbox(z,from_=0,to=10)).grid(row=4,column=1)
##
##    (Button(z,text='Checkout',command=checkout)).grid(row=5,column=0,columnspan=2)
##    
##(Button(x,text='Clear',command=clear)).pack(side=LEFT)
##(Button(x,text='Next',command=nextpage)).pack(side=RIGHT)

##score=0
##questions=[]
##question=0
##class Question:
##    def __init__(self, question, options, answer):
##        self.frame=Frame(root,bg='grey')
##        self.question=Label(self.frame,text=question,bg='grey')
##        self.answer=answer-1
##        self.options=[]
##        self.tracker=IntVar()
##        for a in options:
##            self.options.append(Radiobutton(self.frame,text=a,variable=self.tracker,value=options.index(a),bg='grey'))
##    def show(self):
##        self.frame.grid(row=1)
##        self.question.grid(row=0,column=0)
##        for a in self.options: a.grid(row=self.options.index(a)+1,column=0,sticky=W)
##    def hide(self):self.frame.forget()
##    def next(self):
##        if self.options[self.answer]['fg']!='green':return
##        global question
##        global questions
##        self.hide()
##        question+=1
##        Submit['command']=questions[question].submit
##        Next['command']=questions[question].next
##        questions[question].show()
##    def submit(self):
##        if self.options[self.answer]['fg']=='green':return
##        global score
##        self.options[self.tracker.get()]['fg']='red'
##        self.options[self.answer]['fg']='green'
##        if self.answer==self.tracker.get():
##            score+=1        
##            Score['text']='Score: '+str(score)
##        
##questions.append(Question('Who is the president of the USA?',['Barack Obama','Joe Biden','Donald Trump'],2))
##questions.append(Question('What is the name of our planet?',['Venus','Mars','Earth'],3))
##questions.append(Question('What is the capital of California?',['Sacremento','Little Rock','Montgomery'],1))
##
##(Score:=Label(root,text='Score: '+str(score))).grid(row=0)
##if question<len(questions): questions[question].show()
##(Submit:=Button(root,text='Submit',command=questions[question].submit)).grid(row=2,sticky=W)
##(Next:=Button(root,text='Next',command=questions[question].next)).grid(row=2, sticky=E)
