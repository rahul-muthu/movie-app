from tkinter import *
from tkinter import ttk
import requests
from request_api import returnMovies
from PIL import Image, ImageTk

class app:
    def __init__(self, root):
        self.root = root
        root.geometry("900x600")
        root.title("OMBD")
        self.root.resizable(False,False)
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
        movies = returnMovies(searchval, searchtype)
        print(movies)
        #making the scrollbar
        outerframe = Frame(self.root)
        scrollcanvas = Canvas(outerframe)
        scrollbar = Scrollbar(outerframe, orient=VERTICAL, command=scrollcanvas.yview)
        innerframe= Frame(scrollcanvas, bg="RED")
        #top elements of the page
        titlelabel = Label(innerframe, text="OMDB", font=("Nexa", "20", "bold"))
        toolbar = Frame(innerframe)
        backbutton = Button(toolbar, text="⌂", command=lambda: self.searchPage())
        resultdisplay = Label(toolbar, text=f"Showing results for [{searchtype}] {searchval}")

        #inbetweeners
        scrollcanvas.config(yscrollcommand=scrollbar.set)
        scrollcanvas.bind("<Configure>", lambda x: scrollcanvas.config(scrollregion=scrollcanvas.bbox("all")))
        scrollcanvas.create_window((375, 0), window=innerframe, width=880)

        #baking
        outerframe.pack(fill=BOTH, expand=1)
        scrollcanvas.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar.pack(side=RIGHT, fill=Y, expand=0)

        titlelabel.pack()
        backbutton.pack(side=LEFT)
        resultdisplay.pack(side=LEFT)
        toolbar.pack(fill=X)

        # making the frames of each movie
        for i in movies:
            movieframe = Frame(innerframe, bg="green")
            originalphoto = Image.open(requests.get(i['Poster'], stream=True).raw)
            originalphoto.resize((200, 400))
            posterimage = ImageTk.PhotoImage(originalphoto)
            posterlabel = Label(movieframe, image=posterimage, bg="blue")
            posterlabel.image = posterimage
            movieframe.pack(fill=X)
            posterlabel.pack(side=LEFT)






root = Tk()
app(root)
root.mainloop()
