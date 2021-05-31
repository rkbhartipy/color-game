from tkinter import *
from tkinter.font import Font
from random import *
from tkinter import messagebox



class colorgame_app:
    def __init__(self,window):
        self.window=window
        self.count=1
        self.points=0
        self.count_123=[4,3,2,1,"go"]
        self.color_list=["red","green","orange","purple","yellow","blue","pink"]
        self.go_value=""
        self.random_clr=""
        self.current_go=""
        self.entered_clr=""
        self.time_remain=30
        self.color_no=0
        self.text_color=["red","green","orange","purple","yellow","blue","pink"]
        self.random_text_fg=""
        self.yes_or_no=""


        ## top frame
        self.frame_top=Frame(window,bg="white",height=300)
        self.frame_top.pack(padx=0,side=TOP,fill=X)

        ## bottm frame
        self.frame_btm=Frame(window,bg="#ffd54f",height=500)
        self.frame_btm.pack(side=BOTTOM,fill=X)

        ## start btn if player is ready
        self.start_btn=Button(self.frame_top,text="start",bd=5,bg="red",width=10,command=lambda x=1:self.top_btn(x))
        self.start_btn.place(x=250,y=20)

    def top_btn(self,x):
        if x==1:
            pass
        
    
        ## note
        self.label_note=Label(self.frame_top,text="Type color of text not excate text",font=("Century",20),bg="white",fg="red")
        self.label_note.place(x=80,y=110)

        ## font style
        style=Font(size=20,weight="bold")

        ## score label
        self.label_point=Label(self.frame_top,text="Point :",font=("Bookman Old Style",20),bg="white")
        self.label_point.place(x=10,y=190)

        ##score values
        self.label_score=Label(self.frame_top,text="0" + "/9",bg="white",font=("verdana",20),fg="green")
        self.label_score.place(x=30,y=220)

        ## start in label
        self.label_countdown=Label(self.frame_top,text="starts in :",font=("Bookman Old Style",20),bg="white")
        self.label_countdown.place(x=230,y=190)

        ## countdown no (3,2,1,go)
        self.label_start=Label(self.frame_top,text="",font=("verdana",20),bg="white")
        self.label_start.place(x=270,y=220)

        

        ## calling a function
        self.countdown_fun()

        

        ## timeleft label
        self.label_remaining_time=Label(self.frame_top,text="Timeleft:",font=("Bookman Old Style",20),bg="white")
        self.label_remaining_time.place(x=460,y=190)

        ## 30 to 0 countdown
        self.label_timing=Label(self.frame_top,text="30",bg="white",font=("verdana",20),fg="red")
        self.label_timing.place(x=500,y=220)

        ## changing color name
        self.label_color_name=Label(self.frame_btm,text="",font=("verdana",20,"bold"),bg="#ffd54f",width=15)
        self.label_color_name.place(x=150,y=50)

        ## entry box
        self.entry_box=Entry(self.frame_btm,width=20,bd=5,font=style)
        self.entry_box.place(x=140,y=120)
        
        ## enter btn
        self.entry_enter_btn=Button(self.frame_btm,text="Enter",bd="4",font=(10),width=15,command=self.insert_clr_fun(None))
        self.entry_enter_btn.place(x=220,y=190)

        ## catch enter button event
        self.window.bind("<Return>",self.insert_clr_fun)




    def countdown_fun(self):
        if self.count<5:
            self.label_start.config(text=self.count_123[self.count])
            self.label_start.after(1000,self.countdown_fun)
            self.go_value=self.count_123[self.count]
            self.count+=1
            self.current_go=self.go_value

        else:
            ## calling method to insert clr
            self.diaplay_clr()

            self.count_30_to_0()
            
            self.insert_clr_fun(None)
            
    def diaplay_clr(self):
        if self.time_remain>=0 and self.time_remain<=30:
            self.color_no+=1
            self.random_clr=choice(self.color_list)
            
            self.random_text_fg=choice(self.text_color)
            print(self.random_text_fg)
            
            self.label_color_name.config(text=str(self.color_no) + " : " + self.random_clr, fg=self.random_text_fg,bg="white")
            self.label_color_name.after(3500,self.diaplay_clr)
            
        

            
        
            
    def insert_clr_fun(self,event):
        
        self.entered_clr=self.entry_box.get()

        if self.time_remain>=0 and self.time_remain<=30:
            if (self.random_text_fg==self.entered_clr):
                self.entry_box.delete(0,END)
                self.label_score.config(text=str(self.points) + "/9" )
                self.points+=1
    
            elif self.entered_clr=="":
                pass

            elif self.entered_clr!=self.random_clr:
                self.entry_box.delete(0,END)

            

    def count_30_to_0(self):
        if self.time_remain>=0 and self.time_remain<=30:
            self.label_timing.config(text=self.time_remain)
            self.time_remain-=1
            self.label_timing.after(1000,self.count_30_to_0)
            
        

root=Tk()
root.title("color game")
root.geometry("600x600+350+100")
root.resizable(False,False)

app=colorgame_app(root)

root.mainloop()










