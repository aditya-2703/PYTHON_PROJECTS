import tkinter as tk
from tkinter import Button, Label
from PIL import Image,ImageTk 
import sys
def exit():
    sys.exit()
def read_news():
    import requests
    # bfc1c1

    my_request="https://newsapi.org/v2/top-headlines?country=us&apiKey=dae117742ecb4bdbaa3d57412f02bf60"
    
    list_return_by_site=requests.get(my_request).json()

    list_consist_only_articless=list_return_by_site['articles']

    blanklist_consistof_titles=[]

    for articles in list_consist_only_articless:
        blanklist_consistof_titles.append(articles['title'])
        if len(blanklist_consistof_titles)==10:
            break   
    
    return blanklist_consistof_titles
    
def speak(sentence):
    from win32com.client import Dispatch

    sp=Dispatch("SAPI.SpVoice")
    sp.Speak(sentence)

    # engine=pyttsx3.init()
    # engine.say(sentence)
if __name__ == '__main__':
    # read_news()
    root=tk.Tk()
    root.title("NEW'S PAPER READER")
    root.wm_attributes("-transparentcolor")

    bg=Image.open("img.png")
    render=ImageTk.PhotoImage(bg)
    bg_img_lable=tk.Label(root,image=render,width=1080,height=720)
    bg_img_lable.pack()

    result_list=read_news()
    x=0.2
    y=0.34
    for i in range(len(result_list)):
        l1=Label(root,text=f"{i+1}."+result_list[i],font=("okay",10,'bold'),fg='black',bg='grey')
        l1.place(relx=x,rely=y)
        y+=0.04

        
    btn=Button(root,text="PLAY",font=("Courier",30,'bold'),fg='green',bg='black',command=lambda: speak(result_list))
    btn.place(relx=0.4,rely=0.76)

    ext_btn=Button(root,text="EXIT",font=("Courier",10,'bold'),fg='red',bg='black',command=exit)
    ext_btn.place(relx=0.85,rely=0.24)

    root.mainloop()
    