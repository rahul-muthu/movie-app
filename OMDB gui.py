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
        self.root.bind("<Return>", lambda x: self.searchCheck(searchbar.get()))
        dropdownbox.config(indicatoron=0)
        #baking
        titlelabel.grid(row=0, column=0, columnspan=2)
        dropdownbox.grid(row=1, column=0)
        searchbar.grid(row=1,column=1)
        centerframe.place(relx=0.5, rely=0.5, anchor=CENTER)

    def searchCheck(self, searchval):
        if searchval != "":
            self.resultsPage()

    def resultsPage(self):
        for i in self.root.winfo_children():
            i.destroy()



root = Tk()
app(root)
root.mainloop()