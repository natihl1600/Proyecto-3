#-------------< Proyecto III >-------------#
#----------< Juan David Quesada >----------#
#-----------< Natalia Hernandez >----------#
import tkinter#importar Tkinter, la libreria principal que se utilizara a lo largo del proyecto
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

#Funciones Auxiliares
def mayor(lista):
    mayor = lista[0]
    if len(lista) > 1:
        for i in lista[1:]:
            if mayor < i:
                mayor = i
        return mayor
    else:
        return mayor


def index(lista, ele):
    result = 0
    for i in lista:
        if not i == ele:
            result += 1
        else:
            break
    return result


#-~-~-~-~*Funcion Principal*-~-~-~-~#

def Prin(Nombre):#Funcion principal

    def TablaDePosiciones(Orden):
        f= open("Conductores.txt","r+")
        ListaDeConductores= f.readlines()
        ListaOrdenadaAscendente=[]
        ListaOrdenadaDescendente=[]
        ListaRGP=[]
        for i in ListaDeConductores:
            CurrentFile=open(i+".txt","r+").readlines()
            Participadas=int(CurrentFile[3])
            Ganadas= int(CurrentFile[4])
            Destacadas= int(CurrentFile[5])
            Abandonadas=int(CurrentFile[7])
            CurrentRGP= (Ganadas+Destacadas)/(Participadas-Abandonadas)
            ListaRGP+=[CurrentRGP]
        while len(ListaRGP)!=0:
            i=index(ListaRGP, mayor(ListaRGP))
            ListaOrdenadaAscendente+=[ListaDeConductores[i]]
            ListaOrdenadaDescendente=[ListaDeConductores[i]]+ListaOrdenadaDescendente
            ListaRGP= ListaRGP[0:i]+ListaRGP[i+1:]
            ListaDeConductores= ListaDeConductores[0:i]+ListaDeConductores[i+1:]
        Ventana_De_Posiciones= Toplevel()
        Ventana_De_Posiciones.title("Tabla de Posiciones")
        rows=1
        Label(Ventana_De_Posiciones,text= "Posicion").grid(row=0,column=0)
        Label(Ventana_De_Posiciones, text="Conductor").grid(row=0,column=1)
        Label(Ventana_De_Posiciones, text="Edad").grid(row=0,column=2)
        Label(Ventana_De_Posiciones, text="Nacionalidad").grid(row=0,column=3)
        Label(Ventana_De_Posiciones, text="Temporada").grid(row=0,column=4)
        Label(Ventana_De_Posiciones, text="RGP").grid(row=0,column=5)
        Label(Ventana_De_Posiciones, text="REP").grid(row=0,column=6)
        if Orden== "Descendente":
            Counter=1
            for i in ListaOrdenadaDescendente:
                File = open(i + ".txt", "r+").readlines()
                f = []
                for w in File:
                    f += [w]
                Label(Ventana_De_Posiciones,text=str(Counter)+")").grid(row=rows,column=0)
                Label(Ventana_De_Posiciones,text="\n"+i).grid(row=rows,column=1)
                Label(Ventana_De_Posiciones, text="\n"+f[0]).grid(row=rows, column=2)
                Label(Ventana_De_Posiciones, text="\n"+f[1]).grid(row=rows, column=3)
                Label(Ventana_De_Posiciones, text="\n"+f[2]).grid(row=rows, column=4)
                Label(Ventana_De_Posiciones, text=str(((int(f[4]) + int(f[5])) / (int(f[3])-int(f[6]))) * 100)[0:5]).grid(row=rows,column=5)
                Label(Ventana_De_Posiciones, text=str((int(f[4]) / int(f[3])) * 100)[:5]).grid(row=rows, column=6)
                rows+=1
                Counter+=1
        else:
            Counter= len(ListaOrdenadaAscendente)
            for i in ListaOrdenadaAscendente:
                File= open(i+".txt","r+").readlines()
                f=[]
                for w in File:
                    f+=[w]
                Label(Ventana_De_Posiciones,text= str(Counter)+")").grid(row=rows,column=0)
                Label(Ventana_De_Posiciones,text="\n"+i).grid(row=rows,column=1)
                Label(Ventana_De_Posiciones,text= "\n"+f[0]).grid(row=rows,column=2)
                Label(Ventana_De_Posiciones, text="\n"+f[1]).grid(row=rows, column=3)
                Label(Ventana_De_Posiciones, text="\n"+f[2]).grid(row=rows, column=4)
                Label(Ventana_De_Posiciones, text=str(((int(f[4])+int(f[5]))/(int(f[3])-int(f[6])))*100)[:5]).grid(row=rows, column=5)
                Label(Ventana_De_Posiciones,text= str((int(f[4])/int(f[3]))*100)[:5]).grid(row=rows,column=6)
                Counter-=1
                rows+=1

        def OrdenarAscendente():
            Ventana_De_Posiciones.destroy()
            TablaDePosiciones("Ascendente")
        def OrdenarDescendente():
            Ventana_De_Posiciones.destroy()
            TablaDePosiciones("Descendente")

        Button(Ventana_De_Posiciones, text="Ordenar de Manera Ascendente", command=OrdenarAscendente).grid(row=rows + 1, column=0)
        Button(Ventana_De_Posiciones, text="Ordenar de Manera Descendente", command=OrdenarDescendente).grid(row=rows + 1, column=1)
        Button(Ventana_De_Posiciones,text= "Ver Datos de los Conductores",command=VerTodosLosConductores).grid(row=rows+2,column=0)
    def VerTodosLosConductores():
        f=open("Conductores.txt","r+")
        VentanaJederConductor= Toplevel()
        VentanaJederConductor.title("Conductores")
        ComboBoxJederConductor= ttk.Combobox(VentanaJederConductor,state="readonly",values=f.readlines())
        Label(VentanaJederConductor,text="Seleccione Conductor").grid(row=0,column=0)
        ComboBoxJederConductor.grid(row=0,column=1)
        Button(VentanaJederConductor,text="Ver Datos",command= lambda: Piloto(ComboBoxJederConductor.get())).grid(row=1,column=0)
    def About():#Funcion para mostrar datos de los autores
        Nosotros= Toplevel()     #Crear ventana
        Nosotros.title("About")#y ponerle titulo



        Nosotros.minsize(800,800) #Definir Tamanho
        Nosotros.maxsize(800, 800)#de la ventana



        canvas= Canvas(Nosotros,width= 800, height= 800, bg="White")#Crear un canvas
        canvas.place(x=0,y=0)                                       #y colocarlo dentro de la ventana



        canvas.create_line(400,0,400,800,fill="Black",dash=(1,1))#Crear una linea saparadora para el canvas



        Label(Nosotros, text="Natalia",bg="white").place(x=0, y=0)#Lado de la ventana de Natalia



        Label(Nosotros, text="Juan David",bg="white").place(x=401, y=0)#Lado de la ventana de JD



        Nosotros.mainloop()

    def Piloto(Nombre2):  # Crear una funcion para poder ver los datos de un piloto particular

        Pilot = Toplevel()  # Crear una ventana donde se mostraran los datos
        Pilot.title(str(Nombre2))  # y ponerle como titulo el nombre del piloto

        Label(Pilot, text="Edad:").grid(row=0, column=0)  # Definir donde se mostrara la edad
        Label(Pilot, text="Nacionalidad:").grid(row=1, column=0)  # Definir donde se mostrara la Nacionalidad
        Label(Pilot, text="Temporada:").grid(row=2, column=0)  # Definir donde se mostrara la temporada
        Label(Pilot, text="Competencias Participadas:").grid(row=3,column=0)  # Definir donde se mostraran las Competencias en las cuales haya participado
        Label(Pilot, text="Competencias Ganadas:").grid(row=0,column=4)
        Label(Pilot, text="Competencias Destacadas:").grid(row=1,column=4)  # Definir donde se mostraran las competencias en las cuales haya quedado en Top 3
        Label(Pilot, text="Competencias Fallidas:").grid(row=2,column=4)
        Label(Pilot, text="Competencias Abandonadas:").grid(row=3,column=4)
        Label(Pilot, text="Movimiento Especial:").grid(row=4, column=4)
        Label(Pilot, text=" | ").grid(row=0, column=3)
        Label(Pilot, text=" | ").grid(row=1, column=3)
        Label(Pilot, text=" | ").grid(row=2, column=3)
        Label(Pilot, text=" | ").grid(row=3, column=3)
        Label(Pilot, text=" | ").grid(row=4, column=3)

        rows = 0  # Definir una variable para hacer mas facil el ordenamiento por filas de los datos
        f = open(Nombre2 + ".txt", "r")  # Abrir el archivo de texto hecho especificamente para este piloto
        for i in f.readlines():  # Comenzar el ciclo con el cual se ordenaran los datos
            if rows < 4:  # En este caso, los datos se ordenaran en dos columnas de 3 filas cada una, por lo que se debe especificar el caso en el que todavia no se haya llegado al final de la primer columna
                Label(Pilot, text="\n" + i).grid(row=rows, column=1)
                rows += 1
            else:  # Resetear las filas una vez se llega a la tercera
                Label(Pilot, text="\n" + i).grid(row=rows - 4, column=5)
                rows += 1
        f.close()  # Cerrar el archivo, pues ya no se usara mas

    def VerConductores(Nombre1):#Funcion para ver todos los conductores de la escuderia



        Conduc= Toplevel()#Crear una ventana para mostrar los nombres de los conductores creados hasta el momento
        Conduc.title("Pilotos")#Ponerle Titulo a la ventana
        f = open("Conductores" + Nombre1 + ".txt", "r+")#Abrir el archivo de texto de los conductores para poder leerlo
        Combobox_Pilotos= ttk.Combobox(master= Conduc,state= "readonly",values= f.readlines())
        Combobox_Pilotos.grid(row=0,column=0)
        Button(Conduc, text= "Ver datos",command= lambda: Piloto(Combobox_Pilotos.get())).grid(row=0,column=1)
        f.close()

    def Nuevo_Piloto():
            NuevoPiloto=Toplevel()
            NuevoPiloto.title("Crear Nuevo Piloto")
            Label(NuevoPiloto, text="Nombre:").grid(row=0, column=0)
            Label(NuevoPiloto, text="Edad:").grid(row=1, column=0)
            Label(NuevoPiloto, text="Nacionalidad:").grid(row=2, column=0)
            Label(NuevoPiloto, text="Temporada:").grid(row=3, column=0)
            Label(NuevoPiloto, text="Competencias Participadas:").grid(row=4, column=0)
            Label(NuevoPiloto, text="Competencias Ganadas:").grid(row=5, column=0)
            Label(NuevoPiloto, text= "Competencias Destacadas").grid(row=6,column=0)
            Label(NuevoPiloto, text="Competencias Fallidas:").grid(row=7, column=0)
            Label(NuevoPiloto, text="Competencias Abandonadas:").grid(row=8, column=0)
            Label(NuevoPiloto, text="Movimiento Especial:").grid(row=9,column=0)
            Entry_Nombre = Entry(NuevoPiloto,width=30)
            Entry_Nombre.grid(row=0, column=1)
            Entry_Edad = Entry(NuevoPiloto,width=3)
            Entry_Edad.grid(row=1, column=1)
            Entry_Nacionalidad = Entry(NuevoPiloto,width=10)
            Entry_Nacionalidad.grid(row=2, column=1)
            Entry_Temporada = Entry(NuevoPiloto,width=3)
            Entry_Temporada.grid(row=3, column=1)
            Entry_Competencias_Participadas = Entry(NuevoPiloto,width=3)
            Entry_Competencias_Participadas.grid(row=4, column=1)
            Entry_Ganadas= Entry(NuevoPiloto,width=3)
            Entry_Ganadas.grid(row=5, column=1)
            Entry_Destacadas = Entry(NuevoPiloto,width=3)
            Entry_Destacadas.grid(row=6, column=1)
            Entry_Fallidas = Entry(NuevoPiloto,width=3)
            Entry_Fallidas.grid(row=7, column=1)
            Entry_Abandonadas = Entry(NuevoPiloto, width=3)
            Entry_Abandonadas.grid(row=8, column=1)
            Entry_Especial = Entry(NuevoPiloto,width=10)
            Entry_Especial.grid(row=9, column=1)


            def CrearPiloto(Nombre2):
                f = open("Conductores"+Nombre2+".txt", "a+")
                f.write(Entry_Nombre.get() + "\n")
                f.close()
                f= open("Conductores.txt","a+")
                f.write(Entry_Nombre.get()+"\n")
                f.close()
                f=open(Entry_Nombre.get()+"\n.txt","a+")
                f.write(Entry_Edad.get()+"\n")
                f.write(Entry_Nacionalidad.get() + "\n")
                f.write(Entry_Temporada.get() + "\n")
                f.write(Entry_Competencias_Participadas.get() + "\n")
                f.write(Entry_Ganadas.get()+"\n")
                f.write(Entry_Destacadas.get() + "\n")
                f.write(Entry_Fallidas.get() + "\n")
                f.write(Entry_Abandonadas.get() + "\n")
                f.write(Entry_Especial.get() + "\n")
                NuevoPiloto.destroy()
            Button(NuevoPiloto,text="Crear Nuevo",command=lambda:CrearPiloto(Nombre)).grid(row=10,column=0)
            NuevoPiloto.mainloop()


    def realConductores():#Funcion para poder llamar a los conductores sin argumentos, util para botones
        VerConductores(Nombre)

    def Test():
            bruh= Toplevel()
            bruh.title("REEEEEEEEEEEE")
            bruh.mainloop()

    def VentanaParaNuevaEscuderia():#Crear una funcion para poder crear una nueva escuderia
        Ventana_Escuderia= Toplevel()#Crear ventana
        Ventana_Escuderia.title("Crear Nueva Escuderia")#Ponerle titulo
        Label(Ventana_Escuderia, text= "Ingresar Nombre de Nueva Escuderia:").grid(row= 0, column= 0)#Dar la opcion de ponerle nombre a la nueva escuderia
        entry=Entry(Ventana_Escuderia,width=30,bg="white",fg="black")#Dar un lugar para poder escribir el nombre de la escuderia
        entry.grid(row=0,column=1)#Posicionar el lugar para poner el nombre
        Label(Ventana_Escuderia, text= "Logo:").grid(row=1, column = 0)
        EntryLogo= Entry(Ventana_Escuderia, width= 10)
        EntryLogo.grid(row=1, column = 1)
        def NuevaEscuderia(Nombre):#Funcion donde se lleva a cabo la creacion en si de la escuderia
            f= open("Escuderias.txt","r+")#Abrir el archivo de texto donde se guarda el nombre de cada escuderia
            for i in f.readlines():
                if Nombre +"\n"== i:#Poner un limitante para que no existan dos escuderias con el mismo nombre
                    messagebox.showinfo("Error", "Esa escuderia ya existe")
                    return
            f = open(Nombre + "\n.txt", "a+")#Si pasa por el caso limitante, se crea un archivo de texto con el nombre de la nueva escuderia
            f.write(EntryLogo.get())
            f.close()#Se cierra una vez creado
            f= open("Escuderias.txt","a+")#Se abre el archivo donde se almacenan los nombres de las escuderias, esta vez apara anadir la nueva escuderia
            f.write(Nombre+"\n")#Se escribe en el archivo la nueva escuderia
            f.close()#Se vuelve a cerrar el archivo
            #E: Nombre de una nueva Escuderia
            #S:--
            #R: Que sea un nuevo nombre
            #Uso:Escribir la escuderia nueva en la lista de escuderias y asignarle un archivo propio
        def CrearNuevaEscuderia():#Funcion para poder crear la nueva escuderia sin argumentos
            NuevaEscuderia(entry.get())#Crear la escuderia nueva con los datos del entry
            Ventana_Escuderia.destroy()#Cerrar la ventana que se crea para anadir escuderias
            Ventana_inicio.destroy()#se resetea la ventana principal para que aparezca la nueva ventana en el menu
            Prin(Nombre)#Se llama de nuevo a la funcion, para mostrar la ventan updateada
            #E:--
            #S:--
            #R:--
            #Uso: Poder usar el comando "NuevaEscuderia" en un boton
        BotonEscuderia= Button(Ventana_Escuderia,text= "Crear Nueva Escuderia",command= CrearNuevaEscuderia)
        BotonEscuderia.grid(row=2,column=0)
    #E:--
    #S:--
    #R:--
    #Uso: Permite crear una nueva Escuderia
    def VerAutomovil(NombreDeEscuderia):
        def Automovil(NombreDelAutomovil):
            Ventana_Info_Carro= Toplevel()
            Ventana_Info_Carro.title(NombreDelAutomovil)
            Label(Ventana_Info_Carro, text= "Marca:").grid(row=0,column=0)
            Label(Ventana_Info_Carro, text="Modelo:").grid(row=1, column=0)
            Label(Ventana_Info_Carro, text="Pais de Fabricacion:").grid(row=2, column=0)
            Label(Ventana_Info_Carro, text="Anho de la temporada:").grid(row=3, column=0)
            Label(Ventana_Info_Carro, text="Cantidad de Baterias:").grid(row=4, column=0)
            Label(Ventana_Info_Carro, text="Peso del carro:").grid(row=1, column=4)
            Label(Ventana_Info_Carro, text="Tension normal de baterias:").grid(row=0, column=4)
            Label(Ventana_Info_Carro, text="Estado:").grid(row=2, column=4)
            Label(Ventana_Info_Carro, text="Consumo de los motores:").grid(row=3, column=4)
            Label(Ventana_Info_Carro, text="Sensores:").grid(row=4, column=4)
            Label(Ventana_Info_Carro, text="Pilas por bateria:").grid(row=5, column=0)
            Label(Ventana_Info_Carro, text="Eficiencia:").grid(row=5, column=4)
            Label(Ventana_Info_Carro, text=" | ").grid(row=0, column=3)
            Label(Ventana_Info_Carro, text=" | ").grid(row=1, column=3)
            Label(Ventana_Info_Carro, text=" | ").grid(row=2, column=3)
            Label(Ventana_Info_Carro, text=" | ").grid(row=3, column=3)
            Label(Ventana_Info_Carro, text=" | ").grid(row=4, column=3)
            Label(Ventana_Info_Carro, text=" | ").grid(row=5, column=3)
            f = open(NombreDelAutomovil +".txt", "r+")
            rows=0
            for i in f.readlines():
                if  not rows>5 and not rows==1:
                    Label(Ventana_Info_Carro,text= "\n"+i).grid(row=rows,column=1)
                    rows+=1
                elif rows==1:
                    Label(Ventana_Info_Carro,text= "\n"+NombreDelAutomovil).grid(row=rows,column= 1)
                    Label(Ventana_Info_Carro,text="\n"+i).grid(row=rows+1,column=1)
                    rows+=2
                else:
                    Label(Ventana_Info_Carro,text="\n"+i).grid(row=rows-6,column=5)
                    rows+=1

        VerAuto = Toplevel()
        ComboAuto = ttk.Combobox(master=VerAuto,state= "readonly",values=open("Automoviles" + NombreDeEscuderia + ".txt", "r+").readlines())
        ComboAuto.grid(row=0, column=1)
        Label(VerAuto, text="Seleccione Auto").grid(row=0, column=0)
        Button(VerAuto, text="Ver Datos", command=lambda: Automovil(ComboAuto.get())).grid(row=1,column=0)
    def NuevoAutomovil(escuderia):
        VentanaDeNuevoAutomovil= Toplevel()
        Label(VentanaDeNuevoAutomovil,text="Marca:").grid(row=0,column=0)
        Label(VentanaDeNuevoAutomovil, text="Modelo:").grid(row=1, column=0)
        Label(VentanaDeNuevoAutomovil, text="Pais de Fabricacion:").grid(row=2, column=0)
        Label(VentanaDeNuevoAutomovil, text="Anho de la temporada:").grid(row=3, column=0)
        Label(VentanaDeNuevoAutomovil, text="Cantidad de baterias:").grid(row=4, column=0)
        Label(VentanaDeNuevoAutomovil, text="Pilas por bateria:").grid(row=5, column=0)
        Label(VentanaDeNuevoAutomovil, text="Tension normal de las baterias:").grid(row=6, column=0)
        Label(VentanaDeNuevoAutomovil, text="Peso del Carro:").grid(row=7, column=0)
        Label(VentanaDeNuevoAutomovil, text="Estado:").grid(row=8, column=0)
        Label(VentanaDeNuevoAutomovil, text="Consumo de los motores:").grid(row=9, column=0)
        Label(VentanaDeNuevoAutomovil, text="Sensores:").grid(row=10, column=0)
        Label(VentanaDeNuevoAutomovil, text= "Imagen:").grid(row= 11 , column=0)
        EntryMarca= Entry(VentanaDeNuevoAutomovil,width=10)
        EntryMarca.grid(row=0,column=1)
        EntryModelo= Entry(VentanaDeNuevoAutomovil, width= 7)
        EntryModelo.grid(row=1, column=1)
        EntryPaisDeFabricacion= Entry(VentanaDeNuevoAutomovil, width= 10)
        EntryPaisDeFabricacion.grid(row=2,column= 1)
        EntryAnhoDeLaTemporada= Entry(VentanaDeNuevoAutomovil,width=5)
        EntryAnhoDeLaTemporada.grid(row= 3, column =1)
        EntryCantidadDeBaterias= Entry(VentanaDeNuevoAutomovil,width=4)
        EntryCantidadDeBaterias.grid(row= 4, column =1 )
        EntryPilasPorBateria= Entry(VentanaDeNuevoAutomovil, width = 4)
        EntryPilasPorBateria.grid(row= 5, column = 1)
        EntryTensionNormalDeLasBaterias= Entry(VentanaDeNuevoAutomovil, width = 4)
        EntryTensionNormalDeLasBaterias.grid(row = 6,column = 1)
        EntryPesoDelCarro= Entry(VentanaDeNuevoAutomovil,width = 4)
        EntryPesoDelCarro.grid(row = 7, column=1)
        EntryEstado= Entry(VentanaDeNuevoAutomovil, width= 9)
        EntryEstado.grid(row= 8,column = 1)
        EntryConsumoDeLosMotores= Entry(VentanaDeNuevoAutomovil, width= 5)
        EntryConsumoDeLosMotores.grid(row =9 , column= 1)
        EntrySensores= Entry(VentanaDeNuevoAutomovil, width= 10)
        EntrySensores.grid(row = 10, column= 1)
        EntryImagen= Entry(VentanaDeNuevoAutomovil, width= 10)
        EntryImagen.grid(row = 11, column=1)
        def AnhadirAutomovil():
            f= open("Automoviles"+escuderia+".txt","a+")
            f.write(EntryModelo.get()+"\n")
            f.close()
            AutoTexto= open(EntryModelo.get()+"\n.txt","w+")
            AutoTexto.write(EntryMarca.get()+"\n")
            AutoTexto.write(EntryPaisDeFabricacion.get()+"\n")
            AutoTexto.write(EntryAnhoDeLaTemporada.get()+"\n")
            AutoTexto.write(EntryCantidadDeBaterias.get()+"\n")
            AutoTexto.write(EntryPilasPorBateria.get() + "\n")
            AutoTexto.write(EntryTensionNormalDeLasBaterias.get() + "\n")
            AutoTexto.write(EntryPesoDelCarro.get() + "\n")
            AutoTexto.write(EntryEstado.get() + "\n")
            AutoTexto.write(EntryConsumoDeLosMotores.get() + "\n")
            AutoTexto.write(EntrySensores.get() + "\n")
            AutoTexto.write(EntryImagen.get() + "\n")
            AutoTexto.close()
            VentanaDeNuevoAutomovil.destroy()
        Button(VentanaDeNuevoAutomovil, text= "Anhadir Nuevo Automovil",command=AnhadirAutomovil).grid(row= 12,column=0)


    Ventana_inicio= Tk()#Crear una ventana principal de tkinter para realizar la mayoria del trabajo
    Ventana_inicio.title(Nombre)#Definir el titulo de la ventana principal
    Ventana_inicio.minsize(500,500)#Definir el tamano de la ventana
    Ventana_inicio.maxsize(500,500)
    canvas_inicio= Canvas(Ventana_inicio,width= 500, height= 500, bg= "White")#Crear un canvas para hacer mas facil el trabajo
    canvas_inicio.place(x=0, y=0)#Posicionar el canvas
    img = PhotoImage(file="1.gif")
    canvas_inicio.create_image(0, 0, anchor=NW, image=img)
    MenuEscuderia= Menu(master= Ventana_inicio)#Crear el menu con las diferentes opciones de las escuderias
    Ventana_inicio.config(menu=MenuEscuderia)
    SubEscuderia= Menu(MenuEscuderia)
    MenuEscuderia.add_cascade(label="Escuderias",menu= SubEscuderia)
    def CambiarDeEscuderia(Nombre3):
        Ventana_inicio.destroy()
        Prin(Nombre3)
    def Cambiar_De_Escuderia():
        Nueva_Ventana= Toplevel()
        Nueva_Ventana.title("Cambiar de Escuderia")
        OpcionesEscuderias= ttk.Combobox(Nueva_Ventana,state= "readonly", values= open("Escuderias.txt","r+").readlines())
        Button(Nueva_Ventana,text="Cambiar de Escuderia", command= lambda: CambiarDeEscuderia(OpcionesEscuderias.get())).grid(row=1,column=0)
        Label(master= Nueva_Ventana, text= "Seleccione Escuderia").grid(row=0, column = 0)
        OpcionesEscuderias.grid(row= 0, column = 1)

    def BorrarEscuderia():
        VentanaSeguro = Toplevel()
        VentanaSeguro.title("Esta Seguro?")

        def Si():
            ListaNuevaDeEscuderias = []
            for i in open("Escuderias.txt", "r+").readlines():
                if i != Nombre:
                    ListaNuevaDeEscuderias += [i]
            f = open("Escuderias.txt", "w+")
            f.close()
            f = open("Escuderias.txt", "a+")
            for i in ListaNuevaDeEscuderias:
                f.write(i)
            f.close()
            VentanaSeguro.destroy()
            Ventana_inicio.destroy()
            Prin(open("Escuderias.txt","r+").readlines()[0])

        def No():
            VentanaSeguro.destroy()

        Button(VentanaSeguro, text="Si", command=Si).grid(row=0, column=0)
        Button(VentanaSeguro, text="No", command=No).grid(row=1, column=0)

    SubEscuderia.add_command(label= "Cambiar de escuderia", command= Cambiar_De_Escuderia)
    SubEscuderia.add_command(label= "Crear Nueva Escuderia",command= VentanaParaNuevaEscuderia)
    SubModif= Menu(MenuEscuderia)
    SubModif.add_command(label= "Borrar Escuderia Actual",command= BorrarEscuderia)
    SubModif.add_command(label= "Automoviles",command= lambda:VerAutomovil(Nombre))
    SubModif.add_command(label= "Ver Conductores",command= realConductores)
    SubModif.add_command(label="Anhadir un nuevo Conductor",command=Nuevo_Piloto)
    SubModif.add_command(label="Anhadir un nuevo Automovil",command= lambda:NuevoAutomovil(Nombre))
    MenuEscuderia.add_cascade(label="Opciones",menu= SubModif)
    SubAbout = Menu(MenuEscuderia)
    SubAbout.add_command(label="About", command=About)
    MenuEscuderia.add_cascade(label= "About", menu=SubAbout)
    SubTabla= Menu(MenuEscuderia)
    SubTabla.add_command(label= "Tabla de Posiciones",command= lambda:TablaDePosiciones("Descendente"))
    MenuEscuderia.add_cascade(label="Tabla De Posiciones",menu= SubTabla)
    ArchivoDeEscuderia= open(Nombre+".txt","a+")
    ArchivoDeEscuderia.close()
    Pos=20
    Label(canvas_inicio,text="Patrocinadores:").place(x=0,y=0)
    for i in open(Nombre+".txt","r+").readlines()[:-1]:
            Label(canvas_inicio,text=i).place(x=0,y=Pos)
            Pos+=20
    def AnhadirPatrocinador():
        VentanaNuevoPatrocinador= Toplevel()
        VentanaNuevoPatrocinador.title("Nuevo Patrocinador")
        Label(VentanaNuevoPatrocinador,text= "Nuevo Patrocinador").grid(row=0,column=0)
        EntryPatrocinador=Entry(VentanaNuevoPatrocinador,width=15)
        EntryPatrocinador.grid(row=0,column=1)

        def Anhadir():
            ListaNueva= []
            for i in open(Nombre+".txt","r+").readlines():
                ListaNueva+=[i]
            ListaNueva= ListaNueva[:-1]+[EntryPatrocinador.get()+"\n"]+[ListaNueva[-1]]
            f=open(Nombre+".txt","w+")
            f.close()
            f= open(Nombre+".txt","a+")
            for w in ListaNueva:
                f.write(w)
            f.close()
            VentanaNuevoPatrocinador.destroy()
            Ventana_inicio.destroy()
            Prin(Nombre)
        Button(VentanaNuevoPatrocinador, text= "Anhadir",command= Anhadir).grid(row=1,column=0)
    def BorrarPatrocinador():
        VentanaBorrarPatrocinador= Toplevel()
        VentanaBorrarPatrocinador.title("Borrar Patrocinador")
        Label(VentanaBorrarPatrocinador,text="Seleccione Patrocinador a remover").grid(row=0,column=0)
        ComboPatrocinadores= ttk.Combobox(VentanaBorrarPatrocinador,state="readonly",values= open(Nombre+".txt","r+").readlines()[:-1])
        ComboPatrocinadores.grid(row=1,column=0)
        def Borrar():
            ListaNuevaDePatrocinadores=[]
            for i in open(Nombre+".txt","r+").readlines():
                if i!=ComboPatrocinadores.get():
                    ListaNuevaDePatrocinadores+=[i]
            f=open(Nombre+".txt","w+")
            f.close()
            f=open(Nombre+".txt","a+")
            for i in ListaNuevaDePatrocinadores:
                f.write(i)
            f.close()
            VentanaBorrarPatrocinador.destroy()
            Ventana_inicio.destroy()
            Prin(Nombre)
        Button(VentanaBorrarPatrocinador,text="Borrar",command=Borrar).grid(row=1,column=1)

    def CambiarLogo():
        VentanaNuevoLogo= Toplevel()
        VentanaNuevoLogo.title("Nuevo Logo")
        Label(VentanaNuevoLogo, text= "Nombre de la imagen del nuevo logo:").grid(row=0,column=0)
        EntryNuevoLogo= Entry(VentanaNuevoLogo, width= 10)
        EntryNuevoLogo.grid(row=1, column=0)
        def Cambiar():
            ListaPatro=[]
            for i in open(Nombre+".txt","r+").readlines()[:-1]:
                ListaPatro+=[i]
            ListaPatro+=[EntryNuevoLogo.get()]
            f= open(Nombre+".txt","w+")
            f.close()
            f= open(Nombre+".txt","a+")
            for i in ListaPatro:
                f.write(i)
            f.close()
            VentanaNuevoLogo.destroy()
            Ventana_inicio.destroy()
            Prin(Nombre)
        Button(VentanaNuevoLogo, text="Cambiar",command= Cambiar).grid(row=2,column=0)
    Button(canvas_inicio, text="Cambiar Logo",command= CambiarLogo).place(x=300,y= 400)
    Button(canvas_inicio, text= "Anhadir patrocinador",command=AnhadirPatrocinador).place(x=0, y=Pos)
    Button(canvas_inicio,text="Borrar Patrocinador",command=BorrarPatrocinador).place(x=175,y=Pos)
    SelfImage = PhotoImage(file=open(Nombre+".txt","r+").readlines()[-1])
    canvas_inicio.create_image(0, 200, anchor=NW, image=SelfImage)
    Ventana_inicio.mainloop()
    #E:--
    #S:--
    #R:--
    #Uso: Funcion principal en la que se basa el proyecto

Prin(open("Escuderias.txt","r+").readlines()[0])
