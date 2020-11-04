#PROYECTO: LISTA DE TAREAS CLI CON PYTHON + SQLALCHEMY
import db
from fun_tareas import  Nueva_tarea, Lista_tareas, Borrar_tarea, Editar_tarea_titulo, Editar_tarea_descripcion, Editar_tarea_responsable, Editar_tarea_estado, Editar_fecha_creacion
from fun_login import Crear_login , Login_agenda
from fun_usuarios import Nuevo_usuario, Editar_nombre_usuario,Editar_apellidos_usuario, Editar_email_usuario, Lista_usuarios
from fun_menus import Menu_de_opciones,  Menu_tareas, Menu_usuario, Menu_estado, Menu_login
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

#-------------TAREAS-------------------------

    #[2]Menu tareas
    elif opciones == "2":
        Menu_tareas()
        opciones_editar = input("Elige una opcion: ")
        
        #Editar titulo
        if opciones_editar == "1":
            Nueva_tarea()
        
        #Editar titulo
        if opciones_editar == "2":
            Editar_tarea_titulo()
        
        #Editar descripcion
        elif opciones_editar == "3":
            Editar_tarea_descripcion()
       
        #Editar responsable
        elif opciones_editar == "4":
            Editar_tarea_responsable()
        
        #Editar fecha
        elif opciones_editar == "5":
            Editar_fecha_creacion()

        else:
            print("ELECCION INCORRECTA")

#--------------USUARIOS----------------------------- 
    
    #[3]Menu usuario
    elif opciones == "3":
        Menu_usuario()
        opciones = input("Elige una opcion: ")
        
        #Nuevo usuario
        if opciones == "1":
            Nuevo_usuario()
        
        #Editar nombre usuario
        if opciones == "2":
            Editar_nombre_usuario()
        
        #Editar apellidos usuario
        elif opciones == "3":
            Editar_apellidos_usuario()
       
        #Editar email usuario
        elif opciones == "4":
            Editar_email_usuario()
        
        #Buscar usuario por nombre
        elif opciones == "5":
            pass
        
        #Lista de usuarios
        elif opciones == "6":
            Lista_usuarios()

        
        else:
            print("ELECCION INCORRECTA")    

#--------------ESTADOS-------------------------   
       
    
    #[4]Menu estados
    elif opciones == "4":
        Menu_estado()
        print("funciona")
    
    #[5]Menu login
    elif opciones == "5":
        Menu_login()
        print("funciona")
    
    #[S]Salir
    elif opciones == "S":
        print("Agenda Cerrada")
        salir=False
    
    else:
        print("OPCION INCORRECTA")