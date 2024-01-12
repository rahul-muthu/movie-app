from tkinter import *

class app:
    def __init__(self, root):
        self.root = root
        root.geometry("900x600")
        root.title("OMBD")
        self.searchPage()

    def searchPage(self):
        for i in self.root.winfo_children():
            i.destroy()
        #making
        centerframe = Frame(self.root)
        searchtype = StringVar()
        searchtype.set("Movie")
        titlelabel = Label(centerframe, text="OMDB", font=("Nexa", "20", "bold"))
        dropdownbox = OptionMenu(centerframe, searchtype, "Movie", "TV", "Celeb")
        searchbar = Entry(centerframe, width=100)
        #inbetweeners
        self.root.bind("<Return>", lambda x: self.searchCheck(searchbar.get(), searchtype.get()))
        dropdownbox.config(indicatoron=0)
        #baking
        titlelabel.grid(row=0, column=0, columnspan=2)
        dropdownbox.grid(row=1, column=0)
        searchbar.grid(row=1,column=1)
        centerframe.place(relx=0.5, rely=0.5, anchor=CENTER)

    def searchCheck(self, searchval, searchtype):
        if searchval != "":
            self.resultsPage(searchval, searchtype)

    def resultsPage(self, searchval, searchtype):
        for i in self.root.winfo_children():
            i.destroy()
        #making
        titlelabel = Label(self.root, text="OMDB", font=("Nexa", "20", "bold"))
        #inbetweeners
        #baking
        titlelabel.pack()



root = Tk()
app(root)
root.mainloop()