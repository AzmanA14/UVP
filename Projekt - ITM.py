from tkinter import *

from datetime import *

class dnevnik():
    
    def __init__(self, master):

        menu = Menu(master)
        master.config(menu=menu)

        file_menu = Menu(menu)
        menu.add_cascade(label="Opravek", menu=file_menu)

        file_menu.add_command(label="Odpri", command=self.odpri)
        file_menu.add_command(label="Shrani", command=self.shrani)
        file_menu.add_separator()
        file_menu.add_command(label="Izhod", command=master.destroy)
  
        Label(master, text = "IZRAČUN ITM ZA OSEBE STAREJŠE OD 15 LET").grid(row = 0, columnspan = 4)

        self.a = IntVar()
        Label(master, text = "Izberi spol!").grid(row = 1, column = 0)
        self.gumb_zenska = Radiobutton(master,variable = self.a, value = 1, text = "ŽENSKA")
        self.gumb_zenska.grid(row = 1, column=1)
        self.gumb_moski = Radiobutton(master,variable = self.a, value = 2, text = "MOŠKI")
        self.gumb_moski.grid(row = 1, column=2)

        Label(master, text = "TEŽA [kg] ").grid(row = 2, column = 0)
        Label(master, text = "VIŠINA [m] ").grid(row = 2, column = 1)

        gumb_izracunaj = Button(master, text="Izračunaj!", command=self.izracunaj)
        gumb_izracunaj.grid(row = 2, rowspan = 2, column = 2)
        
        Label(master, text = "ITM").grid(row = 2, column = 3)

        self.lista = Listbox(master,selectmode=SINGLE)
        self.lista.grid(row = 4,rowspan = 2, column = 0, columnspan = 4, sticky=E+W+N+S)

        self.teza = DoubleVar(master, value = 0)
        self.visina = DoubleVar(master, value=0)
        self.itm = DoubleVar(master, value=0)

        polje_teza = Entry(master, textvariable = self.teza)
        polje_teza.grid(row = 3, column = 0)

        polje_visina = Entry(master, textvariable = self.visina)
        polje_visina.grid(row = 3, column = 1)

        polje_itm = Entry(master, textvariable=self.itm)
        polje_itm.grid(row = 3, column = 3)

        self.sez_liste =[]

        self.stanje = StringVar(value = "Niste še izpolnili vseh polj.")
        Label(master, text =  "VAŠE STANJE:").grid(row = 6, column = 0)
        napis_stanje = Label(master, textvariable = self.stanje)
        napis_stanje.grid(row = 6, column = 1, columnspan = 3)
        Label(master, text =  "Če želite shraniti datoteko, pritisnite meni Opravila in jo shranite pod vašim imenom.").grid(row = 7, columnspan = 4)

    def izracunaj(self):
        self.itm.set(self.teza.get() / (self.visina.get() * self.visina.get()))    
        self.lista.insert(0, str(date.today()) + " ~ " + str(self.itm.get()) + "  [ " + str(self.teza.get()) + " kg ... " + str(self.visina.get()) + " m ]")
        self.sez_liste += [str(date.today()) + " ~ " + str(self.itm.get()) + "  [ " + str(self.teza.get()) + " kg ... " + str(self.visina.get()) + " m ]"]
        
        if self.a.get() == 1:
            if self.itm.get() <= 18.4:
                self.stanje.set("Imate prenizko telesno težo.")
            elif self.itm.get() >= 18.5 and self.itm.get() <= 24.9:
                self.stanje.set("Vaša teža je primerna. Kar tako naprej!")
            elif self.itm.get() >= 25 and self.itm.get() <= 29.9:
                self.stanje.set("Imate prekomerno telesno težo. Znebite se odvečnih kilogramov.")
            elif self.itm.get() >= 20:
                self.stanje.set( "Ste v stanju debelosti. Poskrbite za vaše telo in s tem tudi za vaše zdravje!")
        elif self.a.get() == 2:
            if self.itm.get() <= 17.9:
                self.stanje.set("Imate prenizko telesno težo.")
            elif self.itm.get() >= 18 and self.itm.get() <= 24.8:
                self.stanje.set("Vaša teža je primerna. Kar tako naprej!")
            elif self.itm.get() >= 24.9 and self.itm.get() <= 29.2:
                self.stanje.set("Imate prekomerno telesno težo. Znebite se odvečnih kilogramov.")
            elif self.itm.get() >= 29.3:
                self.stanje.set("Ste v stanju debelosti. Poskrbite za vaše telo in s tem tudi za vaše zdravje!")
        

    def shrani(self):
        ime = filedialog.asksaveasfilename()
        if ime == "": 
            return
        with open(ime, "wt", encoding="utf8") as f:
            for i in self.sez_liste:
                f.write(i + "\n")

    def odpri(self):
        ime = filedialog.askopenfilename()
        if ime == "": 
            return
        with open(ime, encoding="utf8") as f:
            for vrstica in f:
                self.lista.insert(0, vrstica)


root = Tk()

aplikacija = dnevnik(root)

root.mainloop()
