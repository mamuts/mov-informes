from tkinter import *
import pathlib
from tkinter import filedialog as FileDialog
from tkinter.ttk import Treeview
import importar_csv


def nou():
    
    ruta = ""  # La utilizaremos para almacenar la ruta del fichero
    home = pathlib.Path().resolve()

    ruta = FileDialog.askopenfilename(
        initialdir=home,
        filetypes=(("Arxius csv", "*.csv"),
                    ("Qualsevol fitxer", "*.*")),
        title="Escull un fitxer de moviments a importar")

    if ruta != "":
        class Contador:

            def __init__(self, lbl: Label, init=0):
                self.c = init
                self.lbl: Label = lbl

            def next(self):
                self.c = self.c + 1
                self.lbl["text"] = importar_csv.config_csv(ruta, self.c)[0]

            def previous(self):
                if self.c > 0:
                    self.c = self.c -1
                    self.lbl["text"] = importar_csv.config_csv(ruta, self.c)[0]

            def posicio(self):
                return self.c

            def camps_linia(self):
                return importar_csv.config_csv(ruta, self.c)[1]

        def mostrar_taula():

            def modificar():
                #TODO "Crear finestra per seleccionar el nom de la columna"
                trv.heading("1", text ="Rata")

            # Taula info
            trv = Treeview(selectmode='browse', height = 30, columns = 3)           
            trv.grid(row=30, column=0, padx=10, pady=10)
            trv['show'] = 'headings'
            
            dades = importar_csv.importar_csv(ruta)
            for i,dada in enumerate(dades):
                if i > cnt.posicio():
                    trv.insert("", END, values=dada)

            trv["columns"] = ("1","2","3","4","5","6","7","8")          

            trv.column("1", width = 120, anchor ='c')
            trv.column("2", width = 500, anchor ='c')
            trv.column("3", width = 100, anchor ='c')
            trv.column("4", width = 100, anchor ='c')
            trv.column("5", width = 200, anchor ='c')
            trv.column("6", width = 100, anchor ='c')
            trv.column("7", width = 100, anchor ='c')
            trv.column("8", width = 200, anchor ='c')
            # Headings
            # respective columns
            trv.heading("1", text ="Data", command=modificar)
            trv.heading("2", text ="concepte")
            trv.heading("3", text ="Valor")
            trv.heading("4", text ="Saldo")
            trv.heading("5", text ="Ref1")
            trv.heading("6", text ="Valor")
            trv.heading("7", text ="Saldo")
            trv.heading("8", text ="Ref1")        


        lbl = Label(text="0")
        lbl.grid(column=1, row=0)
        cnt = Contador(lbl)
        btn = Button(text="Seguent", command=cnt.next).grid(column=1, row=1)
        btn2 = Button(text="Anterior", command=cnt.previous).grid(column=3, row=1)
        btn3 = Button(text="Correcte", command=mostrar_taula).grid(column=8, row=1)
