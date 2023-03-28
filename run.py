import sys
import gui

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            pass
        except:
            print("Error en carregar l'arxiu")
    else:
        app = gui.MainWindow()
        app.mainloop()
