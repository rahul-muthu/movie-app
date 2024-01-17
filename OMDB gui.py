from tkinter import *
from tkinter import ttk
import requests
from tmdb import tmdbdata
from PIL import Image, ImageTk

class app:
    def __init__(self, root):
        self.root = root
        root.title("OMBD")
        self.root.resizable(False, False)
        self.searchPage()
        #placing the app in the center of the screen
        appheight = 600
        appwidth = 900
        screenheight = root.winfo_screenheight()
        screenwidth = root.winfo_screenwidth()
        X = (screenwidth-appwidth) / 2
        Y = (screenheight-appheight) / 2
        root.geometry(f"{appwidth}x{appheight}+{int(X)}+{int(Y)}")

    def searchPage(self):
        for i in self.root.winfo_children():
            i.destroy()
        #making
        centerframe = Frame(self.root, bg="black")
        searchtype = StringVar()
        searchtype.set("Movie")
        titlelabel = Label(centerframe, text="TMDb", font=("Nexa", "50", "bold"), fg="orange", bg="black")
        dropdownbox = OptionMenu(centerframe, searchtype, "Movie", "TV")
        dropdownbox.config(borderwidth=0)
        searchbar = Entry(centerframe, width=50, bg="white", font=("Helvetica", 15))
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
            self.resultsPage(searchval, searchtype, 1)

    def resultsPage(self, searchval, searchtype, pagenum):
        for i in self.root.winfo_children():
            i.destroy()
        #making
        data, totalpages = tmdbdata(searchval, searchtype, pagenum)
        #making the scrollbar
        outerframe = Frame(self.root, bg="black")
        scrollcanvas = Canvas(outerframe, bg="black")
        scrollbar = Scrollbar(outerframe, orient=VERTICAL, command=scrollcanvas.yview)
        innerframe= Frame(scrollcanvas, bg="black")
        #top elements of the page
        titlelabel = Label(innerframe, text="TMDb", font=("Nexa", "20", "bold"), bg="black", fg="orange")
        toolbar = Frame(innerframe, bg="white", highlightbackground="black", pady=1, padx=1)
        backbutton = Button(toolbar, text="⌂", command=lambda: self.searchPage(), bg="orange", fg="white", borderwidth=0, width=5)
        resultdisplay = Label(toolbar, text=f"Showing results for [{searchtype}] {searchval}", bg="white", font=("Helvetica", 15, "bold"))
        #pages footer
        footerframe = Frame(innerframe)
        #inbetweeners
        scrollcanvas.config(yscrollcommand=scrollbar.set)
        scrollcanvas.bind("<Configure>", lambda x: scrollcanvas.config(scrollregion=scrollcanvas.bbox("all")))
        scrollcanvas.create_window((375, 0), window=innerframe, width=880)

        #baking
        outerframe.pack(fill=BOTH, expand=1)
        scrollcanvas.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar.pack(side=RIGHT, fill=Y, expand=0)

        titlelabel.pack()
        backbutton.pack(side=LEFT, fill=Y)
        resultdisplay.pack(side=LEFT)
        toolbar.pack(fill=X)
        #exception handling of no poster available
        NPoriginalphoto = Image.open(requests.get("https://movienewsletters.net/photos/000000h1.jpg", stream=True).raw).resize((200, 300))
        NPposterimage = ImageTk.PhotoImage(NPoriginalphoto)
        # making the frames of each movie
        for i in data:
                movieframe = Frame(innerframe)
                #handling the posters
                if i['poster'] == "https://image.tmdb.org/t/p/originalNone":
                    posterlabel = Label(movieframe, image=NPposterimage)
                    posterlabel.image = NPposterimage
                else:
                    originalphoto = Image.open(requests.get(i['poster'], stream=True).raw).resize((200, 300))
                    posterimage = ImageTk.PhotoImage(originalphoto)
                    posterlabel = Label(movieframe, image=posterimage, bg="white")
                    posterlabel.image = posterimage
                #handling the title and rating box and description
                titlebox = Frame(movieframe, bg="white", pady=2)
                title = Label(titlebox, text=i['name'], font=("Helvetica", 22), bg="white", wraplength=580, justify=LEFT)
                rating = Label(titlebox, text=f"Popularity: {i['rating']}", bg="white", font=("Helvetica", 11, "bold"), fg="orange")
                description = Label(movieframe, text=i['description'], wraplength=650, justify=LEFT, anchor=NW, bg="white", font=("Helvetica", 10))

                movieframe.pack(fill=X)
                posterlabel.pack(side=LEFT)
                title.pack(side=LEFT, fill=X)
                rating.pack(side=RIGHT)
                titlebox.pack(side=TOP, fill=X)
                description.pack(side=LEFT, fill=BOTH, expand=1)

        #making the pages footer
        for i in range(1, totalpages+1):
            if i == pagenum:
                pagebgcolour = "#ff4d01"
            else: pagebgcolour = "orange"
            pagebutton = Button(footerframe, text=str(i), command=lambda x=searchval, y=searchtype, z=i: self.resultsPage(x, y, z),
                                borderwidth=1,
                                bg=pagebgcolour,
                                fg="white",
                                width=3)
            pagebutton.pack(side=LEFT)
        footerframe.pack()





root = Tk()
root.config(bg="black")
app(root)
root.mainloop()
