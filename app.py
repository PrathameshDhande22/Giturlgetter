from tkinter import *
from extractor import GTExtract
import config
from PIL import Image, ImageTk
import webbrowser
import tktooltip
import threading
import clipboard


class TokenNotGivenException(Exception):
    def __init__(self):
        self.message = "Please Provide the Github Api Token from Github.com"

    def __str__(self) -> str:
        return self.message


class GUI(Tk):

    def __init__(self):

        super().__init__()
        self.__verify()
        self.geometry("600x500+400+140")
        self.title("Github URL Extractor")
        self.minsize(width=600, height=500)
        self.wm_iconbitmap(config.ICON)
        self.config(bg="white")

        self.__gui()

    def __verify(self):
        if config.TOKEN_INSERTED == False:
            raise TokenNotGivenException

    def __gui(self):
        self.img = Image.open(config.LOGO).resize((200, 90))
        self.img = ImageTk.PhotoImage(self.img)
        self.img1 = Image.open(config.SEARCH).resize((50, 50))
        self.img1 = ImageTk.PhotoImage(self.img1)
        self.logolbl = Label(image=self.img, bg="white")
        self.logolbl.pack(side="top", anchor="center")
        self.searched = StringVar(value="Enter Your Github Username")
        self.searchtxt = Entry(bg="white", font=(
            "Consolas", 16), bd=2, insertborderwidth=2, relief="solid", textvariable=self.searched)
        self.searchtxt.pack(anchor="w", pady=30, padx=60)
        self.searchbtn = Button(image=self.img1, bg="white", relief="flat",
                                command=lambda: threading.Thread(target=self.searchbutton).start())
        self.searchbtn.place(x=310, y=110)
        self.scrollbar_txt = Scrollbar(
            self, orient=HORIZONTAL, command=self.searchtxt.xview)
        self.scrollbar_txt.place(x=57, y=158, width=250, height=20)
        self.searchtxt.config(xscrollcommand=self.scrollbar_txt.set)
        self.searchtxt.bind("<Button-1>", lambda e: self.searched.set(""))
        self.statusbar_txt = StringVar(value=" Loaded Successfully")
        self.status_bar_lbl = Label(self, textvariable=self.statusbar_txt, bg="white", font=(
            "Calibri", 12), relief="flat", anchor="w")
        self.status_bar_lbl.pack(
            expand=True, fill="x", side="bottom", anchor="s")
        self.img2 = Image.open(config.GITHUB_LOGO).resize((40, 40))
        self.img2 = ImageTk.PhotoImage(self.img2)
        self.setStatusbar("Loaded Successfully")
        self.gh_logo = Label(image=self.img2, bg="white", relief="flat")
        self.gh_logo.pack(side="right", anchor="ne",
                          before=self.logolbl, ipadx=10, ipady=10)
        tktooltip.ToolTip(self.gh_logo, "Repo URL",
                          follow=True, **{"bg": "white"})
        tktooltip.ToolTip(self.searchbtn, "Search",
                          follow=True, **{"bg": "white"})
        self.gh_logo.bind(
            "<Button-1>", lambda e: webbrowser.open_new(config.URL))
        self.frame1 = Frame(self, bg="#00B6FF", bd=2, relief="solid")
        self.frame1.pack(anchor="sw", side="left", pady=10,
                         fill="y", padx=10, expand=True)
        self.listofrepos = Listbox(self.frame1, font=(
            "Times new roman", 14), width=25, height=25, bg="yellow", selectmode="single")
        self.listofrepos.pack(side="left", anchor="nw",
                              pady=10, padx=20, fill="y", expand=True)
        self.reposcrollbar = Scrollbar(
            self.frame1, command=self.listofrepos.yview)
        self.listofrepos.config(yscrollcommand=self.reposcrollbar.set)
        self.reposcrollbar.pack(side="left", anchor="e",
                                expand=True, fill="y", pady=10, padx=2)
        Label(self.frame1, text="LIST OF REPOSITORY : ", font=("Times new roman", 16, "bold"), anchor="w",
              bg="#00B6FF", fg='white').pack(side="top", anchor="center", before=self.listofrepos, pady=5)
        self.giturl = StringVar(value="")
        Label(self, text="GIT URL : ", font=(
            "Times new roman", 18), bg="white").place(x=315, y=190)
        self.urltxt = Entry(bg="white", font=("cambria", 16), bd=2, insertborderwidth=2,
                            relief="solid", textvariable=self.giturl, state="readonly")
        self.urltxt.place(x=315, y=230)
        self.scrollbar_url = Scrollbar(
            self, orient=HORIZONTAL, command=self.urltxt.xview)
        self.scrollbar_url.place(x=315, y=270, width=245)
        self.urltxt.config(xscrollcommand=self.scrollbar_url.set)
        Button(text="COPY", font=("Arial", 18), bg="light green", activebackground="#00B6FF",
               relief="ridge", bd=3, command=self.copy_to_clipboard).place(x=385, y=300)
        Label(text="©Copyright Prathamesh Dhande 2022", font="calibri 8",
              bg="white").pack(side="bottom", anchor="sw", expand=True, fill="x")
        self.listofrepos.bind("<<ListboxSelect>>", lambda e: threading.Thread(
            target=self.getGiturl).start())

    def searchbutton(self):
        self.uname = self.searched.get()
        self.delrepolst()
        self.setStatusbar("Searching...")
        self.exdata = GTExtract()
        if self.exdata.isValidUser(self.searched.get()) == False:
            self.setStatusbar("NO Username Found")
        else:
            self.setStatusbar("Username Found")
            for repo in self.exdata.get_all_user_repos:
                self.getRepos(repo.name)

    def getGiturl(self):
        self.setStatusbar("Generating Url")
        index = self.listofrepos.curselection()
        reponame = self.listofrepos.get(index[0])
        self.giturl.set(self.exdata.geturl(reponame, self.uname))
        self.setStatusbar("Generated")

    def setStatusbar(self, text):
        self.statusbar_txt.set(text)
        self.status_bar_lbl.after(3000, lambda: self.statusbar_txt.set(" "))

    def copy_to_clipboard(self):
        data = self.giturl.get()
        clipboard.copy(data)
        self.setStatusbar("Copied to Clipboard")

    def getRepos(self, name):
        self.listofrepos.insert(END, name)

    def delrepolst(self):
        self.listofrepos.delete(0, END)
