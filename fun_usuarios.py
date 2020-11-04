import db
from tablas import Tareas, Estados, Usuarios
from sqlalchemy import create_engine, Column, String, Integer
from colorama import init , Fore, Style


def Nuevo_usuario():
    nombre = input("Introduce el nombre del usuario: ")
    apellidos = input("Introduce los apellidos del usuario: ")
    email = input("Introduce el email del usuario: ")

    nuevo_usuario = Usuarios(nombre, apellidos, email)
    db.session.add(nuevo_usuario)
    db.session.commit() 


def Editar_nombre_usuario():
    nombre_antiguo = input("Escribe el nombre del usuario que quieres cambiar: ")
    nombre_editar = input("Escribe el nuevo nombre del usuario: ")

    nombre = db.session.query(Usuarios).filter(Usuarios.nombre==nombre_antiguo).first()
    nombre.nombre = nombre_editar

    db.session.commit()

def Editar_apellidos_usuario():
    apellidosid = input("\nEscribe la " +Fore.GREEN+Style.BRIGHT+"'ID'"+Fore.RESET+Style.RESET_ALL+ " de los apellidos a cambiar: ")
    apellidosNU = input("Escribe los nuevos apeliidos del usuario : ")
    
    usuario = db.session.query(Usuarios).filter_by(id=apellidosid).first()
    usuario.apellidos = apellidosNU
    
    db.session.commit()

def Editar_email_usuario():
    emailid = input("\nEscribe la " +Fore.GREEN+Style.BRIGHT+"'ID'"+Fore.RESET+Style.RESET_ALL+ " del email a cambiar: ")
    emailNU = input("Escribe el nuevo email del usuario : ")
    
    usuario = db.session.query(Usuarios).filter_by(id=emailid).first()
    usuario.email = emailNU
    
    db.session.commit()

def Buscar_usario_nombre():
    nombre_buscar= input("Escribe el nombre del usuario: ")
    usuario = db.session.query(Usuarios).filter(Usuarios.nombre == nombre_buscar).all

def Lista_usuarios():

    print("\n----LISTA DE USUARIOS----")
    usuarios = db.session.query(Usuarios).all()
    
    for usuario in usuarios:
        print(Fore.RED+"\nID:"+Fore.RESET, usuario.id,Fore.RED+"NOMBRE:"+Fore.RESET, usuario.nombre, Fore.RED+"APELLIDOS:"+Fore.RESET, usuario.apellidos, Fore.RED+"EMAIL:"+Fore.RESET, usuario.email)


    
    

