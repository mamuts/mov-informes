from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter.ttk import Treeview
import importar_csv
import pathlib

ruta = ""  # La utilizaremos para almacenar la ruta del fichero


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor d'informes de moviments bancaris")
        self.build()

    def nou_projecte(self):
        frame = Frame(self)
        NouProjecteWindow(frame)

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


class NouProjecteWindow(Frame):
    def __init__(self, frame):
        super().__init__()
        self.build(frame)

    def build(self, frame):
        global ruta
        home = pathlib.Path().resolve()
        ruta = FileDialog.askopenfilename(
               initialdir=home,
                    filetypes=(("Arxius csv", "*.csv"),
                               ("Qualsevol fitxer", "*.*")),
                               title="Escull un fitxer de moviments a importar")

        if ruta != "":          
            
            frame.pack(padx=2, pady=0)
            lbl = Label(frame, text="0")
            lbl.grid(column=0, row=0)

            class Contador:
                def __init__(self, lbl:Label, init=0):
                    self.c = init
                    self.lbl:Label = lbl

                def next(self):
                    self.c = self.c + 1
                    self.lbl["text"] = importar_csv.config_csv(ruta, self.c)[0]
                
                def position(self):
                     print(importar_csv.config_csv(ruta, self.c)[1])
                     return importar_csv.config_csv(ruta, self.c)[1]

            cnt = Contador(lbl)

            def mostrar_taula():
                frame2 = Frame(self, width=480, height=320)
                frame2.pack()
                 #Taula info
                trv = Treeview(frame2, selectmode ='browse')
                trv.pack(expand=YES, fill=BOTH)
                # Using treeview widget
                trv.grid(row=1,column=1,padx=20,pady=20)
                for i in range(0,7):
                    trv.heading("#0", text=i)

                # Defining heading
                trv['show'] = 'headings'
                trv.insert("", END, text="README.txt", values=("850 bytes", "18:30"))
                trv.pack()
                

            btn = Button(frame, text="Seguent", command=cnt.next)
            btn2 = Button(frame, text="Correcte", command=mostrar_taula)
            btn.grid(column=1, row=1)
            btn2.grid(column=2, row=1)

            
            
            # number of columns
            #trv["columns"] = ("1", "2", "3","4","5")

            

            # width of columns and alignment
            #trv.column("1", width = 120, anchor ='c')
            #trv.column("2", width = 500, anchor ='c')
            #trv.column("3", width = 100, anchor ='c')
            #trv.column("4", width = 100, anchor ='c')
            #trv.column("5", width = 200, anchor ='c')
            # Headings
            # respective columns
            #trv.heading("1", text ="Data")
            #trv.heading("2", text ="concepte")
            #trv.heading("3", text ="Valor")
            #trv.heading("4", text ="Saldo")
            #trv.heading("5", text ="Ref1")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
