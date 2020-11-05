#PROYECTO: LISTA DE TAREAS CLI CON PYTHON + SQLALCHEMY
import db
from fun_tareas import  Nueva_tarea, Lista_tareas, Borrar_tarea, Editar_tarea_titulo, Editar_tarea_descripcion, Editar_tarea_responsable, Editar_tarea_estado, Editar_fecha_creacion
from fun_login import Crear_login, Login_agenda, Editar_usuario, Editar_contraseña
from fun_usuarios import Nuevo_usuario, Editar_nombre_usuario,Editar_apellidos_usuario, Editar_email_usuario, Lista_usuarios, Buscar_usario_nombre
from fun_estados import Nuevo_estado, Editar_nombre_estado, Editar_descripcion_estado
from fun_menus import Menu_de_opciones,  Menu_tareas, Menu_usuario, Menu_estado, Menu_login
from tablas import Tareas, Estados, Usuarios, Login
from colorama import init , Fore, Style


Login_agenda()

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
        elif opciones_editar == "2":
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
        elif opciones == "2":
            Editar_nombre_usuario()
        
        #Editar apellidos usuario
        elif opciones == "3":
            Editar_apellidos_usuario()
       
        #Editar email usuario
        elif opciones == "4":
            Editar_email_usuario()
        
        #Buscar usuario por nombre
        elif opciones == "5":
            Buscar_usario_nombre()
        
        #Lista de usuarios
        elif opciones == "6":
            Lista_usuarios()
   
        else:
            print("ELECCION INCORRECTA")    

#--------------ESTADOS-------------------------   
         
    #[4]Menu estados
    elif opciones == "4":
        Menu_estado()
        opciones = input("Elige una opcion: ")
        
        #Nuevo estado
        if opciones == "1":
            Nuevo_estado()
        
        #Editar nombre estado
        elif opciones == "2":
            Editar_nombre_estado()
        
        #Editar descripcion estado
        elif opciones == "3":
            Editar_descripcion_estado()

        else:
            print("ELECCION INCORRECTA")                
    
#----------LOGIN----------------
    
    #[5]Menu login
    elif opciones == "5":
        Menu_login()
        opciones = input("Elige una opcion: ")
        
        #Crear login
        if opciones == "1":
            Crear_login()
        
        #Editar usuario
        elif opciones == "2":
            Editar_usuario()
        
        #Editar contraseña
        elif opciones == "3":
            Editar_contraseña()
    
    #[S]Salir
    elif opciones == "S":
        print("Agenda Cerrada")
        salir=False
    
    else:
        print("OPCION INCORRECTA")