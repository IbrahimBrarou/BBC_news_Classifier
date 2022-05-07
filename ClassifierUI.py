import tkinter as tk
from tkinter import filedialog
import os
import pickle

root=tk.Tk()
root.title('classifier')
Article="";
def addText():
    for widget in frame.winfo_children():
        widget.destroy()
        
    file= filedialog.askopenfile(initialdir="/",title="Select File",
    filetypes=[("Text files","*.txt")]);
    abs_path = os.path.abspath(file.name)
    with open(os.path.join(os.path.dirname(__file__), abs_path), 'r') as input_file:
        Article = input_file.read()
    label=tk.Label(frame,text=Article, bg="white")
    label.bind('<Configure>', lambda e: label.config(wraplength=label.winfo_width()))
    label.pack()
    Classify(Article)
    
def Classify(Article):
        clf_filename='naive_bayes_classifier.pkl'
        nb_clf=pickle.load(open(clf_filename,'rb'))
        vec_filename='count_vectorizer.pkl'
        vectorizer=pickle.load(open(vec_filename,'rb'))
        pred=nb_clf.predict(vectorizer.transform([Article]))
        pred[0]=pred[0].capitalize()
        label2=tk.Label(frame2,text=pred[0],height=150, bg="yellow",font=('Helvatical bold',20))
        label2.bind('<Configure>', lambda e: label2.config(wraplength=label2.winfo_width()))
        label2.pack()

canvas = tk.Canvas(root,height=700,width=1000,bg="#263D42")
canvas.pack()

root.resizable(width=False,height=False)
frame= tk.Frame(root,bg="white")
frame.place(relheigh=0.8,relwidth=0.8,relx=0.1,rely=0.1)


frame2= tk.Frame(root,bg="yellow")
frame2.place(relheight=0.1,relwidth=0.4,relx=0.3)



openFile=tk.Button(root,text="Open Article",padx=15,pady=10,fg="white",bg="#263D42",command=addText)
openFile.pack()


root.mainloop()