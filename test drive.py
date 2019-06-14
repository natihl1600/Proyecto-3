import tkinter
import tkinter as tk
from tkinter import *
import os
from tkinter import messagebox
from threading import Thread
import time
from WiFiClient import NodeMCU
import tkinter.scrolledtext as tkscrolled



def nombre(): #detecta nombre seleccionado por el cliente
    return '--'

def escuderia(): #detecta escudería seleccionada por el cliente
    return '--'

#            _____________________
#___________/Counter para batería
counter = 100 #valor en el que empieza la batería
def counter_label(label):
    counter = 100
    def count():
        global counter
        if counter > 0: #llega a cero y no disminuye más
            counter -= 1 #descuenta un uno porcierto 
            label.config(text = str(counter))
            label.after(10000, count) #lo disminuye cada diez segundos
        else:
            counter += 0
    count()


#            _____________________
#___________/Ventana Test
def test_drive():
    global Veloci
    global prueba
    global escuderia
    global nombre
#            _____________________
#___________/Crear ventana //se crea la pantalla
    ventana = Tk()
    ventana.title("Test Drive") #título de la misma
    ventana.minsize(800, 400) #tamaño de la pantalla
    ventana.resizable(width=NO, height=NO) #no se puede ajustar su tamaño
    canvas = Canvas(ventana, width=800, height=400, bg='Pink') #color de la pantalla principal
    canvas.place(x=0, y=0) #ubicación

#            _____________________
#___________/Velocidad // funcion para aumentar o disminuir la velocidad en la pantalla de test drive
    velocidades = 0
    def velocidad(velo):
        global Veloci
        velocidades = 0
        def vel():
            global velocidades
            if Veloci:
                velocidades += 1
                velo.config(text=str(velocidades)+'kpm')
                velo.after(velocidad(velo))

        vel()
#           ______________________
#__________/Cargar imágenes // función para cargar imágenes a la pantalla del test drive
    def cargarimagen(carro):
        ruta= os.path.join('imagenes', carro) #ubicacion de a imagen (folder, nombre)
        imagen = PhotoImage(file=ruta)
        return imagen
    
    logo = cargarimagen("logo.png")
    logo1 = canvas.create_image(480,50, image=logo, anchor = NW)

    carro = cargarimagen("vistapiloto.png")
    carro1 = canvas.create_image(-90, 22, image=carro, anchor = NW)

    canvas.create_rectangle(0, 0, 800, 150, fill= "skyblue")


#           ______________________
#__________/Textos // textos incluídos a la ventana del test drive
    Test_Drive = Label(canvas, text = "TEST DRIVE", font=('Times New Roman', 20), bg='red', fg='black')
    Test_Drive.place(x=585, y=10)
    NombrePiloto = Label(canvas, text = nombre(), font = ('Arial', 15), bg = 'black', fg = 'white')
    NombrePiloto.place(x=585,y = 55)
    NombreEscuderia = Label(canvas, text = escuderia(), font = ('Arial', 15), bg = 'black', fg = 'white')
    NombreEscuderia.place(x=625, y=95)
    piloto = Label(canvas, text = 'Piloto:', font = ('Arial', 15), fg = 'black', bg = 'skyblue')
    piloto.place(x=500,y = 55)
    escuderia = Label(canvas, text = 'Escudería:', font = ('Arial', 15), fg = 'black', bg = 'skyblue')
    escuderia.place(x=500,y = 95)
    label = Label(canvas, fg = 'black', font = ('Arial', 15), bg = 'skyblue')#.place(x=100, y=100)
    label.place(x=105, y=110)
    velo = Label(canvas, fg = 'black', font = ('Arial', 15), bg = 'grey')
    velo.place(x=375, y=177)
    bateria = Label(canvas, text = 'Batería: ', font = ("Arial", 15), fg = 'black', bg = "skyblue")
    bateria.place(x=20, y=110)
    #label.pack()
    counter_label(label)
    #cuadros que reflejan la información enviada por el cliente en otras palabras da un status de cómo está la sitauación al mandar 
    #mensajes al nodeMCU
    SentCarScrolledTxt = tkscrolled.ScrolledText(canvas, height=5, width=5)
    SentCarScrolledTxt.place(x=-400,y=200)
    RevCarScrolledTxt = tkscrolled.ScrolledText(canvas, height=5, width=5)
    RevCarScrolledTxt.place(x=-410,y=200)

#           ______________________
#__________/Funcion del NodeMCU // funciones para recibir un mensaje y mandarlo al nodeMCU
    myCar = NodeMCU()
    myCar.start()
    
    def get_log():
        """
        Hilo que actualiza los Text cada vez que se agrega un nuevo mensaje al log de myCar
        """
        indice = 0
        # Variable del carro que mantiene el hilo de escribir.
        while(myCar.loop):
            while(indice < len(myCar.log)):
                mnsSend = "[{0}] cmd: {1}\n".format(indice,myCar.log[indice][0])
                SentCarScrolledTxt.insert(END,mnsSend)
                SentCarScrolledTxt.see("end")
                mnsRecv = "[{0}] result: {1}\n".format(indice,myCar.log[indice][1])
                RevCarScrolledTxt.insert(END, mnsRecv)
                RevCarScrolledTxt.see('end')
                indice+=1
            time.sleep(0.200)
    p = Thread(target=get_log)
    p.start()
    #funciones específicas ya con su propio código para que el cliente solo tenga que estripar un botón y la función se ejecute
    def Circle(event):
        if myCar.send('circle' + ';'):
            myCar.send('circle' + ';')
        else:
            messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')")

    def Mov_Especial(event):
        if myCar.send('Movimiento especial1' + ';'):
            myCar.send('Movimiento especial1' + ';')
        else:
            messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')")

    def Mov_Especial2(event):
        if myCar.send('Movimiento especial2' + ';'):
            myCar.send('Movimiento especial2' + ';')
        else:
            messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')")

    def ZigZag(event):
        if myCar.send('zigzag' + ';'):
           myCar.send('zigzag' + ';')
        else:
            messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')")

    def Infinite(event):
        if myCar.send('infinite' + ';'):
           myCar.send('infinite' + ';')
        else:
            messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')")

    def Especial(event):
        if myCar.send('especial' + ';'):
           myCar.send('especial' + ';')
        else:
            messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')")

    def Recto(event):
        if myCar.send('Recto' + ';'):
           myCar.send('Recto' + ';')
        else:
            messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')")
    def Izquierda(event):
        if myCar.send('Izquierda' + ';'):
           myCar.send('Izquierda' + ';')
        else:
            messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')")
    def Derecha(event):
        if myCar.send('Derecha' + ';'):
           myCar.send('Derecha' + ';')
        else:
            messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')")



    def sendShowID():
        """
        Ejemplo como capturar un ID de un mensaje específico.
        """
        mns = str(E_Command.get())
        if(len(mns)>0 and mns[-1] == ";"):
            E_Command.delete(0, 'end')
            mnsID = myCar.send(mns)
            messagebox.showinfo("Mensaje pendiente", "Intentando enviar mensaje, ID obtenido: {0}\n\
    La respuesta definitiva se obtine en un máximo de {1}s".format(mnsID, myCar.timeoutLimit))
        else:
            messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')")
    def read():
        """
        Ejemplo de como leer un mensaje enviado con un ID específico
        """
        mnsID = str(E_read.get())
        if(len(mnsID)>0 and ":" in mnsID):
            mns = myCar.readById(mnsID)
            if(mns != ""):
                messagebox.showinfo("Resultado Obtenido", "El mensaje con ID:{0}, obtuvo de respuesta:\n{1}".format(mnsID, mns))
                E_read.delete(0, 'end')
            else:
                messagebox.showerror("Error de ID", "No se obtuvo respuesta\n\
    El mensaje no ha sido procesado o el ID es invalido\n\
    Asegurese que el ID: {0} sea correcto".format(mnsID))
        else:
            messagebox.showwarning("Error en formato", "Recuerde ingresar el separador (':')")
    #ventana.bind('<Return>', Circle) #Vinculando tecla Enter a la función send

#           ______________________
#__________/Botones

    #Botones relacionados con las funciones de comandos enseñados anteriormente la función de estos botones es que ya tienen el comando
    #dentro de ellos por lo que con tan solo presionarlos ya se enviará el mensaje

    Btn_ConnectControl2 = Button(canvas,text='Circle',command=lambda:Circle(None),fg='black',bg='red', font=('Agency FB',15))
    Btn_ConnectControl2.place(x=10,y=10)

    Btn_ConnectControl3 = Button(canvas,text='Movimiento Especial1',command=lambda:Mov_Especial(None),fg='black',bg='red', font=('Agency FB',15))
    Btn_ConnectControl3.place(x=55,y=10)

    Btn_ConnectControl4 = Button(canvas,text='Movimiento Especial2',command=lambda:Mov_Especial2(None),fg='black',bg='red', font=('Agency FB',15))
    Btn_ConnectControl4.place(x=185,y=10)

    Btn_ConnectControl5 = Button(canvas,text='ZigZag',command=lambda:ZigZag(None),fg='black',bg='red', font=('Agency FB',15))
    Btn_ConnectControl5.place(x=10,y=60)

    Btn_ConnectControl6 = Button(canvas,text='Infinite',command=lambda:Infinite(None),fg='black',bg='red', font=('Agency FB',15))
    Btn_ConnectControl6.place(x=55,y=60)

    Btn_ConnectControl7 = Button(canvas,text='Especial',command=lambda:Especial(None),fg='black',bg='red', font=('Agency FB',15))
    Btn_ConnectControl7.place(x=104,y=60)

    Btn_ConnectControl8 = Button(canvas,text='Recto',command=lambda:Recto(None),fg='black',bg='red', font=('Agency FB',15))
    Btn_ConnectControl8.place(x=380,y=110)

    Btn_ConnectControl9 = Button(canvas,text='Izquierda',command=lambda:Izquierda(None),fg='black',bg='red', font=('Agency FB',15))
    Btn_ConnectControl9.place(x=50,y=250)

    Btn_ConnectControl10 = Button(canvas,text='Derecha',command=lambda:Derecha(None),fg='black',bg='red', font=('Agency FB',15))
    Btn_ConnectControl10.place(x=680,y=250)


    Veloci = Button(canvas, text='PWM', command=lambda:velocidad(velo), fg="black", bg="grey", font=('Arial', 10))
    Veloci.place(x=380, y=177)
      
    ventana.mainloop()
    
test_drive()


