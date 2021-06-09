import tkinter as tk
from PIL import Image,ImageTk
import os
os.chdir("D:\CS-20\python-projects\PROJECT_ML_KAL\PYTHON_PROJECTS\LOVE_CALCULATOR")

# after button pushed it execute this function which gives in its command property
def get_data(ml,fml):
    import requests
    global root
     
    # here we simply use api of love calculator 
    # url = "put the url"
    # querystring = {"fname":ml,"sname":fml}
    # headers = {
    #     'x-rapidapi-key': "put your key here",
    #     'x-rapidapi-host': "put your host name here"
    #     }
    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    querystring = {"fname":ml,"sname":fml}

    headers = {
    'x-rapidapi-key': "97ef28b92emsh631d6e0f2e6f36ep1ad773jsn8239263212d2",
    'x-rapidapi-host': "love-calculator.p.rapidapi.com"
    }
    # in above we define the url and query and key 
    # here we have to convert this text in json for access easily 
    data = requests.get( url, headers=headers, params=querystring).json()
    score=data['percentage']
    msg=data["result"]

    # we simply make labels for displaying this
    res_scr=tk.Label(root,text=f"Score:\t{score}%",font=("Cambria",15),bg='#eff8ff')
    res_scr.place(relx=0.2,rely=0.6)

    res_msg=tk.Label(root,text=f"\n{msg}",font=("Cambria",15),bg='#eff8ff')
    res_msg.place(relx=0.2,rely=0.67)

if __name__ == '__main__':
            
    # we create windown as root and in it give title and size as follows
    root=tk.Tk()
    root.title("LOVE CALCULATOR")
    root.geometry("700x460")
    
    # we add image as background with pillow module which reads image in binary format
    im0= Image.open("bg.jpg")  
    render1=ImageTk.PhotoImage(im0)
    lbl0=tk.Label(root,image=render1)
    lbl0.pack()
    
    # here we take entry from user for boy's name 
    ml_entry=tk.Entry(root,width=20)
    ml_entry.place(relx=0.3,rely=0.5)
    
    # here we take entry from user for girl's name
    fml_entry=tk.Entry(root,width=20)
    fml_entry.place(relx=0.6,rely=0.5)
    
    # lable for title 
    lbl_lv=tk.Label(root,text="LOVE CALCULATOR",font=("okay",25,'bold'),bg='#fbaccc',fg='#1e212d')
    lbl_lv.place(relx=0.3,rely=0.03)
    
    # here text for identify ther input 
    ml=tk.Label(root,text="BOY'S NAME :",font=("Courier",9,'bold'),bg='#f8f1f1',fg='black')
    ml.place(relx=0.3,rely=0.45)
    
    # here text for identify ther input 
    fml=tk.Label(root,text="GIRL'S NAME :",font=("Courier",9,'bold'),bg='#fbaccc',fg='black')
    fml.place(relx=0.6,rely=0.45)
    
    # here we make button which run command (function) if it pushed
    go=tk.Button(root,text='GO',width=5,height=2,bg='lightgreen',fg='red',font=('okay',9,'bold'),command=lambda: get_data(ml_entry.get(),fml_entry.get()))
    go.place(relx=0.512,rely=0.55)
 
    root.mainloop()