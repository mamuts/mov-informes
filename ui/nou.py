from tkinter import *
import pathlib
from tkinter import filedialog as FileDialog
from tkinter.ttk import Treeview
import importar_csv

def nou(self):
    NouFinestra(self)

class NouFinestra(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=BOTH, expand=YES)
        self.config(bg="blue")
        ruta = ""  # La utilizaremos para almacenar la ruta del fichero
        home = pathlib.Path().resolve()

        ruta = FileDialog.askopenfilename(
            initialdir=home, 
            filetypes=(("Arxius csv", "*.csv"),
                        ("Qualsevol fitxer", "*.*")),
            title="Escull un fitxer de moviments a importar")
        
        if ruta != "":
            class Contador:

                def __init__(self, init=0):
                    self.c = init

                def next(self):
                    self.c = self.c + 1
                    return self.c

                def previous(self):
                    if self.c > 0:
                        self.c = self.c -1
                        return self.c

                def posicio(self):
                    return self.c

                def camps_linia(self):
                    camps = len(importar_csv.config_csv(ruta, self.c))
                    print(camps) 
                    return camps
                
            def mostrar_taula(linia, tot):
   
                # Taula info
                trv = Treeview(self, selectmode='browse', columns = 3)           
                trv.grid(row=30, column=0, padx=10, pady=10)
                trv['show'] = 'headings'
                cols = []
                columnes = []
                if tot == True:
                    dades = importar_csv.importar_csv(ruta, linia)
                else:
                    dades = importar_csv.config_csv(ruta, linia)
                
                for i in range(0, cnt.camps_linia()):
                        col = Columna(i,i)
                        columnes.append(col)
                        cols.append(col.id_columna())
                trv["columns"] = cols
                for columna in columnes:
                    trv.column(columna.id_columna(), width = 100, anchor ='c')  
                    trv.heading(columna.id_columna(), text =columna.get_nom_columna())
                trv.insert("", END, values=dades)
            
            cnt = Contador()
            mostrar_taula(0, False)            
            Button(self, text="Seguent", command= lambda : mostrar_taula(cnt.next(), False)).grid(column=1, row=1)
            Button(self, text="Anterior", command=lambda : mostrar_taula(cnt.previous(), False)).grid(column=3, row=1)
            Button(self, text="Correcte", command=lambda : mostrar_taula(cnt.posicio(), True)).grid(column=8, row=1)
        
    def borrar(self):
        self.pack_forget()
        self.destroy()
        print("Frame borrado")

class Columna():

    """
        Classe per emmagatzemar informació de columnes
    """
    
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom

    def mod_columna(self, nom):
        self.nom = nom
    
    def id_columna(self):
        return self.id

    def get_nom_columna(self):
        return self.nom
    

