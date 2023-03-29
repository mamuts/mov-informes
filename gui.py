from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter.ttk import Treeview
import importar_csv
import pathlib

ruta = ""  # La utilizaremos para almacenar la ruta del fichero

class CenterWidgetMixin:
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)
        self.geometry(f"{w}x{h}+{x}+{y}")

class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title("Gestor d'informes de moviments bancaris")
        self.build()

    def nou_projecte(self):
        self.update()

        home = pathlib.Path().resolve()
        ruta = FileDialog.askopenfilename(
               initialdir=home,
                    filetypes=(("Arxius csv", "*.csv"),
                               ("Qualsevol fitxer", "*.*")),
                               title="Escull un fitxer de moviments a importar")

        if ruta != "":

            class Contador:
                def __init__(self, lbl:Label, init=0):
                    self.c = init
                    self.lbl:Label = lbl

                def next(self):
                    self.c = self.c + 1
                    self.lbl["text"] = importar_csv.config_csv(ruta, self.c)[0]
                
                def camps_linia(self):
                     return importar_csv.config_csv(ruta, self.c)[1]

            def mostrar_taula():
                #Taula info
                trv = Treeview(selectmode ='browse')
                # Using treeview widget
                trv.grid(row=1,column=1,padx=20,pady=20)
                
                # Defining heading
                trv['show'] = 'headings'
                # TODO "Abocar totes les dades"
                dades = importar_csv.importar_csv(ruta)
                for dada in dades:                   
                    trv.insert("", END, values=dada)

                # number of columns
                trv["columns"] = ("1", "2", "3","4","5")          

                # width of columns and alignment
                trv.column("1", width = 120, anchor ='c')
                trv.column("2", width = 500, anchor ='c')
                trv.column("3", width = 100, anchor ='c')
                trv.column("4", width = 100, anchor ='c')
                trv.column("5", width = 200, anchor ='c')
                # Headings
                # respective columns
                trv.heading("1", text ="Data")
                trv.heading("2", text ="concepte")
                trv.heading("3", text ="Valor")
                trv.heading("4", text ="Saldo")
                trv.heading("5", text ="Ref1")        

            
            lbl = Label(text="0")
            lbl.grid(column=1, row=0)
            cnt = Contador(lbl)
            btn = Button(text="Seguent", command=cnt.next)
            btn2 = Button(text="Correcte", command=mostrar_taula)
            btn.grid(column=1, row=1)
            btn2.grid(column=2, row=1)

            
    def build(self):
        menubar = Menu(self)
        self.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nou", command=self.nou_projecte)
        filemenu.add_command(label="Abrir")
        filemenu.add_command(label="Guardar")
        filemenu.add_command(label="Cerrar")
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.quit)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cortar")
        editmenu.add_command(label="Copiar")
        editmenu.add_command(label="Pegar")

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Ayuda")
        helpmenu.add_separator()
        helpmenu.add_command(label="Acerca de...")

        menubar.add_cascade(label="Archivo", menu=filemenu)
        menubar.add_cascade(label="Editar", menu=editmenu)
        menubar.add_cascade(label="Ayuda", menu=helpmenu)


class NouProjecteWindow(MainWindow):
    def __init__(self):
        super().__init__()
        self.build()

    def build(self):
        global ruta
        
class Nueva(Toplevel):
    def __init__(self):
        self.frame = Frame()
        self.pack()
        self.config(bg="lightblue") 
        self.mostrar_campos()

    def mostrar_campos(self):
        self.master.title("Nueva ventana")
        self.nombre = self.Label(self, text="Nombre y apellidos: ")
        self.nombre.pack(side="left")
        self.nombre = self.Entry(self)
        self.nombre.pack(side="left")

        self.lenguaje = self.Label(self, text="Lenguaje de programación preferido: ")
        self.lenguaje.pack(side="left")
        self.lenguaje = self.Entry(self)
        self.lenguaje.pack(side="left")

        self.button_guardar = self.Button(self, text="Guardar", fg="green", command=self.actualizar_datos)
        self.button_guardar.pack(side="left")

        self.button_cancelar = self.Button(self, text="Cancelar", fg="red", command=self.master.destroy)
        self.button_cancelar.pack(side="left")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
