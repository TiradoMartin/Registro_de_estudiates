#Universidad Tecnologica de Santiago (UTESA).
#Segundo parcial de programacion 2.
#Profesor: Neldo Oltega.
#Alumno: Mrtin Antonio Tirado .
#.


##Importar modulos y libreria

from tkinter import *

##definición de variables

Windows=Tk()
TxtNombre=0
TxtMatricula=0
TxtCurso=0
sexo=IntVar()

##Inicio del programa##


Windows.geometry("700x700")#Cambia el tamaño de la ventana
Windows.config(bg="light blue")#Define el color de la ventana


titulo = Label(Windows,text="Progranación 2",fg="blue",font=("Arial",24))#Esta dos linea muestran el titulo
titulo.pack(side=TOP,padx=10,pady=10)
Windows.title("Programación2")




fondo = PhotoImage(file="fondo.png")#Este block de codigo muestra el logo de utesa
Fondo = Label(Windows,image = fondo).place(x=0,y=0)
logoimg = PhotoImage(file="utesa.png")#Este block de codigo muestra el logo de utesa
etiquetalogo = Label(Windows,image = logoimg)
etiquetalogo.pack(side=TOP,padx=5,pady=5)

autor = Label(Windows,text=" Alumno: Martin Antonio Tirado M.\n\n Prof: Neldo oltega")#Estas dos lineas  muestran el nombre del alumno y el profesor 
autor.pack(side=TOP,padx=10,pady=10)






#Formulario
Nombre= Label(Windows,text="Nombre",fg="blue",font=("Calibri (Body)",8)).pack(side=TOP,padx=10,pady=10)#Esta dos linea muestran el titulo
entradaN=StringVar()
TxtNombre=Entry(Windows,textvariable=entradaN).pack(side=TOP,padx=50,pady=10)


Matricula= Label(Windows,text="Matricula",fg="blue",font=("Calibri (Body)",8)).pack(side=TOP,padx=10,pady=10)
entradaM=StringVar()
TxtMatricula=Entry(Windows,textvariable=entradaM).pack(side=TOP,padx=10,pady=10)

entrada=StringVar()


Curso= Label(Windows,text="Sección",fg="blue",font=("Calibri (Body)",8)).pack(side=TOP,padx=10,pady=10)#Esta dos linea muestran el titulo
entradaC=StringVar()
TxtCurso=Entry(Windows,textvariable=entradaC).pack(side=TOP,padx=10,pady=10)




##listbox salida 
lista = Listbox(Windows)
lista.place(height=160, width=300,x=200,y=510)


#TxtSexo=Entry(Windows,textvariable=entrada).place(x=100,y=350)

Sexo= Label(Windows,text="seleccione masculino(M)o femenino(F)",fg="blue",font=("Calibri (Body)",8)).place(x=250,y=450)

#ESTADO= Label(Windows,text="seleccione masculino(M)o femenino(F)",fg="blue",font=("Calibri (Body)",8)).place(x=200,y=350)

# Boton de selecion
SexoF=Radiobutton(Windows,text="(F)",value=1,variable=sexo).place(x=300,y=480)
SexoM=Radiobutton(Windows,text="(M)",value=2,variable=sexo).place(x=350,y=480)


#Definir Clases y Metodos#
class Formulario():#Esta clase es la que hace la  accion de cerrar la ventana
    def __init__(self):
        pass
    @staticmethod
    def Cerrar():
        Windows.withdraw()


    
    @staticmethod
    def escribir():
        #print("Has elegido añadir un registro a la agenda")
        nombrem = entradaN.get()
        nombre=str(nombrem)
        matriculam = entradaM.get()
        matricula=str(matriculam)
        cursom=entradaC.get()
        curso=str(cursom)
        
        if sexo.get()==1:
            genero="Femenino"
        else:
             genero="Masculino"
        agenda = open("Data/db.csv")
        for n in range(1,40):
            linea = agenda.readline()
            lineapartida = linea.split(",")
    ##        print(lineapartida[0])
            if lineapartida[0] != "":
                memoria = lineapartida[0]
    ##    print("El numero máximo es",memoria)
        agenda.close()
        memonum = int(memoria)
        posicion = 0
        posicion = memonum + 1
        postr = str(posicion)
      #  print("Se ha guardado en la agenda el contacto: ",nombre,"con el número de teléfono",telefono)
        agenda = open("Data/db.csv",'a')
        agenda.write(postr)
        agenda.write(",")
        agenda.write(nombre)
        agenda.write(",")
        agenda.write(matricula)
        agenda.write(",")
        agenda.write(curso)
        agenda.write(",")
        agenda.write(genero)
        agenda.write(",")
        agenda.write("\n")
        agenda.close()
       # print(genero,"D",SexoM)



    @staticmethod  
    def listar():
        agenda = open("Data/db.csv")
        numero = 0
        for i in range(1,30):
            lectura = agenda.readline()
    ##        print(lectura.replace(",","\t\t"))
            lista.insert(END,lectura.replace(",","   "))
            numero = numero + 1
        agenda.close()
        
Registro=Formulario()
          


Boton=Button(Windows,text="Guardar",command=lambda:Registro.escribir()) #Esta lineas muestran  el boton y llaman la class para cerrar la ventana
Boton.pack(side=LEFT,padx=10,pady=10)

Boton2=Button(Windows,text=" Salir  ",command=lambda:Registro.Cerrar()) #Esta lineas muestran  el boton y llaman la class para cerrar la ventana
Boton2.pack(side=RIGHT,padx=10,pady=10)

Boton3=Button(Windows,text=" Ver registro  ",command=lambda:Registro.listar()) #Esta lineas muestran  el boton y llaman la class para cerrar la ventana
Boton3.pack(side=RIGHT,padx=10,pady=10)


Windows.mainloop()#es el evento principal de la ventana

