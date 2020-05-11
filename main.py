from tkinter import *
from tkinter import ttk

import calculator

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)#heredamos el init de Tk para incializar nuestro init de MainApp pasándole la instancia self porque es de la clase y no de instancia
        self.title("Calculadora")#nuestra inicialización propia de nuestra instancia
        self.geometry("272x300")#nuestra inicialización propia de nuestra instancia
        self.pack_propagate(0)#para que los contenidos se adecuen a la ventana y no al revés

        c = calculator.Controlator(self)#self es el padre de calculator que es la ventana principal (MainApp(Tk))
        c.pack(side=TOP, fill = BOTH)



    def start(self):
        self.mainloop()


if __name__=="__main__":
    app = MainApp()
    app.start()



