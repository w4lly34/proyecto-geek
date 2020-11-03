
import db
from tablas import Login
from sqlalchemy import create_engine, Column, String, Integer


def Crear_login():
    
    usuario = input("Introduce usuario a crear: ")
    contraseña = input("Introduce contraseña a crear: ")

    nuevo_login = Login(usuario, contraseña)
    db.session.add(nuevo_login)
    db.session.commit()


def Login_agenda():
    
    usuario = input("Introduce usuario: ")
    contraseña = input("Introduce contraseña: ")

    login = db.session.query(Login).filter_by(id="1")

    for row in login:
        usuario1 = row.usuario
        contraseña1 = row.contraseña

    while usuario != usuario1 or contraseña != contraseña1:
        usuario = input("Introduce usuario: ")
        contraseña = input("Introduce contraseña: ")