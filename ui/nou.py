from tkinter import *
import pathlib
from tkinter import filedialog as FileDialog
from tkinter.ttk import Treeview
import importar_csv

class Columna(Toplevel):
    #TODO "Transformar en una classe"
    def __init__(self, columnes):
        super().__init__()
        self.build()
        self.columna = columnes
                
    def guardar(self):
        self.destroy
        self.update
    
    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)
        self.transient()
        self.grab_set()
        self.title("Modificar columna")
        Label(frame, text="Pararra").grid(row=0,column = 0)
        input_nom = Entry(frame)
        input_nom.grid(row=1, column=0)
        btn_guardar = Button(frame, text="Guardar", command=self.guardar)
        btn_guardar.grid(row=2, column=1)  

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
                Columna()

            # Taula info
            trv = Treeview(selectmode='browse', height = 30, columns = 3)           
            trv.grid(row=30, column=0, padx=10, pady=10)
            trv['show'] = 'headings'
            
            columnes=[]         
            
            dades = importar_csv.importar_csv(ruta)
            for i,dada in enumerate(dades):
                if i > cnt.posicio():
                    if len(columnes) == 0:
                        for i in range(len(dada)):
                            columnes.append(i)
                            trv["columns"] = columnes
                            for i in columnes:
                                trv.column(i, width = 100, anchor ='c')
                            for i in columnes:
                                trv.heading(i, text =i, command=lambda : [modificar(columnes[i])])
                trv.insert("", END, values=dada)           
        lbl = Label(text="0")
        lbl.grid(column=1, row=0)
        cnt = Contador(lbl)
        btn = Button(text="Seguent", command=cnt.next).grid(column=1, row=1)
        btn2 = Button(text="Anterior", command=cnt.previous).grid(column=3, row=1)
        btn3 = Button(text="Correcte", command=mostrar_taula).grid(column=8, row=1)

def obrir():
    pass
