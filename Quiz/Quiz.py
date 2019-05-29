import pandas as pd
import random
from tkinter import *
'''Include report generation to separate excel file if required df.to_csv('filename', index=False)

Offset specification: startrow, startcol if required

'''
report = {'qn':[],'u_ans' : [], 'r_ans': []}
df = pd.read_excel('Questions.xlsx',"Sheet1")
df.set_index('Sln', inplace=True)
n_o_quest = df.shape[0] - 1
cq_df = None
qover = [] #questions already asked, so no repetition
defcolor = '#d4d0c8'
q_ask = 5#number of questions that are going to be asked
q_asked = 0
uanswer = None
score = 0

def calc():
    global q_ask, score
    for widget in topframe.winfo_children():
        widget.destroy()
    for widget in botframe.winfo_children():
        widget.destroy()
    infolabel = Label(topframe,text = 'Scorecard',font = ('Helvetica', 16),bg = 'blue',fg='White')
    infolabel.pack(anchor = CENTER)
    wans = q_ask - score
    uscore = ('Right Answers: ' + str(score) + '\nScore: ' + str(score) + '\nWrong Answers: ' + str(wans))
    scorelabel = Label(topframe,text=uscore,font = ('Helvetica', 16),bg = 'blue',fg='White').pack()
    
def clicked():
    global score
    report['qn'].append(cq_df['Question'])
    report['u_ans'].append(uanswer)
    report['r_ans'].append(cq_df['Correct Answer'])
    if(uanswer == cq_df['Correct Answer']):
        score+=1
    if(q_asked<q_ask):
        for widget in topframe.winfo_children():
            widget.destroy()
        for widget in botframe.winfo_children():
            widget.destroy()
        askq()
    else:
        calc()
    

def selected():
    global radiovar,uanswer
    uanswer = radiovar.get()

def askq():
    global q_asked,cq_df,qover
    while(True):
        qsel = random.randint(1,n_o_quest)
        if qsel not in qover:
            qover.append(qsel)
            break
    cq_df = df.loc[qsel]
    q_asked+=1
    qlabel = Label(topframe,text = cq_df['Question'],bg = 'blue',font = ('Helvetica', 16),fg='white')
    qlabel.pack(side = LEFT)
    r1 = Radiobutton(botframe,text = cq_df['Option 1'],font = ('Helvetica', 16),variable = radiovar, value = cq_df['Option 1'],command=selected)
    r1.pack(anchor = W)
    r2 = Radiobutton(botframe,text = cq_df['Option 2'],font = ('Helvetica', 16),variable = radiovar, value = cq_df['Option 2'],command=selected)
    r2.pack(anchor = W)
    r3 = Radiobutton(botframe,text = cq_df['Option 3'],font = ('Helvetica', 16),variable = radiovar, value = cq_df['Option 3'],command=selected)
    r3.pack(anchor = W)
    r4 = Radiobutton(botframe,text = cq_df['Option 4'],font = ('Helvetica', 16),variable = radiovar, value = cq_df['Option 4'],command=selected)
    r4.pack(anchor = W)
    submit = Button(botframe, text = 'Submit',fg = 'white', bg='green',bd=0,relief=FLAT,font = (16),activebackground = 'grey',command = clicked)
    submit.pack()
    infolabel = Label(botframe,text = 'Once submitted, answer cannot be changed',font = ('Helvetica', 16))
    infolabel.pack(side = LEFT,anchor=S)
    
def start():
    root.geometry('972x300')
    global radiovar
    radiovar = StringVar()
    radiovar.set('String')
    askq()
    


def closeMain():
    botframe.config(bg=defcolor)
    btnstart.destroy()
    q_label.destroy()
    start();
 
               
root = Tk()
root.iconbitmap(r'Resources\\deutsch.ico')
topframe = Frame(root, bg='blue')
topframe.pack(side=TOP, fill=BOTH)
qlogo = PhotoImage(file='Resources\\qlogo.png')
q_label = Label(topframe,image=qlogo,bg='blue')
q_label.image = qlogo
q_label.pack()
botframe = Frame(root,bg ='blue')
botframe.pack(side=BOTTOM, fill=BOTH)
beginquiz = PhotoImage(file='Resources\\bq.png')
btnstart = Button(botframe, image = beginquiz, relief = FLAT, border = 0,command=closeMain)
btnstart.image = beginquiz
btnstart.pack()
root.mainloop()

