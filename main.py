#PROYECTO: LISTA DE TAREAS CLI CON PYTHON + SQLALCHEMY
import db
from fun_tareas import  Nueva_tarea, Lista_tareas, Borrar_tarea, Editar_tarea_titulo, Editar_tarea_descripcion, Editar_tarea_responsable, Editar_tarea_estado, Editar_fecha_creacion
from fun_login import Crear_login , Login_agenda
from fun_menus import Menu_de_opciones,  Menu_editar
from tablas import Tareas, Estados, Usuarios, Login
from colorama import init , Fore, Style


#Login_agenda()

salir = True
 
while salir:
     
    Menu_de_opciones()
    opciones=input("Elige una Opcion: ").upper()
    
    #[1]Lista de tareas
    if opciones == "1":
        Lista_tareas()

    #[2]Nueva tarea:   
    elif opciones == "2":
        Nueva_tarea()
        print("funciona")
     
    
    #[4]Editar tarea
    elif opciones == "4":
        Menu_editar()
        opciones_editar = input("Elige una opcion: ")
        
        if opciones_editar == "1":
            Editar_tarea_titulo()
        
        elif opciones_editar == "2":
            Editar_tarea_descripcion()
        
        elif opciones_editar == "3":
            Editar_tarea_estado()
        
        elif opciones_editar == "4":
            Editar_tarea_responsable()
        
        elif opciones_editar == "5":
            Editar_fecha_creacion()

        else:
            print("ELECCION INCORRECTA")

        
            
    
    #[5]Borrar tarea
    elif opciones == "5":
        Borrar_tarea()
        print("funciona")
    
    #[6]Buscar usuario
    elif opciones == "6":
        print("funciona")
    
    #[7]Crear usuario y contraseña
    elif opciones == "7":
        Crear_login()
        print("funciona")
    
    #[S]Salir
    elif opciones == "S":
        print("Agenda Cerrada")
        salir=False
    
    else:
        print("OPCION INCORRECTA")