
import db
from tablas import Tareas, Estados, Usuarios
from sqlalchemy import create_engine, Column, String, Integer, inspect
from colorama import init , Fore, Style





def Lista_tareas():
   
    print("\n----LISTA DE TAREAS----")
    tareas = db.session.query(Tareas).all()
    
    for tarea in tareas:
        print(Fore.RED+"\nID:"+Fore.RESET, tarea.id,Fore.RED+"TAREAS:"+Fore.RESET, tarea.titulo, Fore.RED+"DESCRIPCION:"+Fore.RESET, tarea.descripcion, Fore.RED+"ESTADO:"+Fore.RESET, tarea.responsable, Fore.RED+"FECHA:"+Fore.RESET, tarea.fecha_creacion, Fore.RED+"USUARIO:"+Fore.RESET, tarea.usuarios_nombre, Fore.RED+"ESTADO:"+Fore.RESET, tarea.estado_nombre)


def Nueva_tarea():
    

    titulo = input("Introduce el titulo de la tarea: ")
    descripcion = input("Introduce descripcion de la tarea: ")
    responsable = input("Introduce el nombre del responsable: ")
    fecha_creacion = input("Introduce la fecha de hoy: ")
    usuario_nombre = input("Introduce el usuario")
    estado_nombre = input("Introduce el estado de la tarea: ")

    nueva_tarea = Tareas(titulo, descripcion, responsable, fecha_creacion, usuario_nombre, estado_nombre)
    db.session.add(nueva_tarea)
    db.session.commit()


def Editar_tarea_titulo():

    titulo_antiguo = input("Escribe titulo que quieres cambiar: ")
    titulo_editar = input("Escribe el nuevo titulo de la nueva tarea: ")

    titulo = db.session.query(Tareas).filter(Tareas.titulo==titulo_antiguo).first()
    titulo.titulo = titulo_editar
    db.session.commit()


def Editar_tarea_descripcion():
    
    id_tarea = input("Escribe la 'ID' de la descripcion que quieres cambiar: ")
    descripcion_editar = input("Escribe la nueva descripcion de la tarea: ")

    descripcion = db.session.query(Tareas).filter(Tareas.id==id_tarea).first()
    descripcion.descripcion = descripcion_editar
    db.session.commit()


def Editar_tarea_responsable():
    
    responsable_antiguo = input("Escribe responsable que quieres cambiar: ")
    responsable_editar = input("Escribe la nueva responsable de la tarea: ")

    responsable = db.session.query(Tareas).filter(Tareas.responsable==responsable_antiguo).first()
    responsable.responsable = responsable_editar
    db.session.commit()


def Editar_tarea_estado():
    
    nombreid = input("\nEscribe la " +Fore.GREEN+Style.BRIGHT+"'ID'"+Fore.RESET+Style.RESET_ALL+ " de la tarea a cambiar : ")
    nombreNU = input("Escribe el nuevo estado de la tarea : ")
    
    tareas = db.session.query(Tareas).filter_by(id=nombreid).first()
    tareas.estado = nombreNU
    
    db.session.commit()


def Editar_fecha_creacion():

    id_tarea = input("Escribe la 'ID' de la fecha de creacion que quieres cambiar: ")
    fecha_editar = input("Escribe la nueva fecha de la tarea: ")

    fecha = db.session.query(Tareas).filter(Tareas.id==id_tarea).first()
    fecha.fecha_creacion = fecha_editar
    db.session.commit()


def Borrar_tarea():
    
    tarea_borrar = input("Escribe el nombre de la tarea a BORRAR: ")
    borrar_tarea = db.session.query(Tareas).filter_by(titulo=tarea_borrar).first()
    db.session.delete(borrar_tarea)
    db.session.commit()
    print("----Tarea BORRADA----")


def Buscar_tarea():
    pass






