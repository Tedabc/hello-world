import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
from tkinter import messagebox as mb
from datetime import datetime
from PIL import Image, ImageTk
import random


class Milestone(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Luxun')
        self.geometry("1150x900")
        self.dtVar = tk.StringVar() 

        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageDate):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.talk = ['时间就像海绵里的水，只要愿挤，总还是有的.', '倘只看书，便变成书橱。', '我好像是一只牛，吃的是草，挤出的是奶、血。','其实地上本没有路，走的人多了，也便成了路。','哪里有天才，我只不过是把别人喝咖啡的时间都用在工作上了。','沉着、勇猛、有辨别、不自私。','必须敢于正视，这才可望敢想、敢说、敢做、敢当。','曾经阔气的要复古，正在阔气的要保持现状，未曾阔气的要革新，大抵如此，大抵！']

        self.controller = controller

        canvas = Canvas(self, width=1150, height=900)
        canvas.pack()

        img = (Image.open("1.jpeg"))

        resized_image = img.resize((1150, 800), Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(resized_image)

        canvas.create_image(10, 10, anchor=NW, image=self.new_image)

        btnIntroduction = tk.Button(self, text="introduction",
                                    command=self.click_introduction)
        btntime = tk.Button(self, text="Time",
                            command=self.click_date)
        btntalk = tk.Button(self, text="talk",
                            command=self.click_talk)

        btnIntroduction.place(x=300, y=850)
        btntime.place(x=800, y=850)
        btntalk.place(x=1000, y=850)

    def click_introduction(self):
        mb.showinfo("personal info",
                    "鲁迅原名周树人，中国近代的奥林匹克冠军，因为乒乓球打的好，在近代奥运会上经常夺得跳水冠军")

    def click_percept(self):
        mb.showinfo("percept", "你们抓鲁迅，关我周树人什么事情")

    def click_talk(self):
        mb.showinfo('talk', random.choice(self.talk))

    def get_current_time(self):
        now = datetime.now()
        current_time = now.strftime("%Y/%M/%D  %H:%M:%S")
        print(current_time)
        return "Current Time is :", current_time

    def click_date(self):
        self.controller.dtVar.set(self.get_current_time())
        self.controller.show_frame("PageDate")


class PageDate(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, textvariable=self.controller.dtVar,
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = Milestone()
    app.mainloop()
