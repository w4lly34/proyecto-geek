import db
from tablas import Estados





def Nuevo_estado():
    nombre = input("Introduce el nombre del estado: ")
    descripcion = input("Introduce la descripcion del estado: ")
    
    nuevo_estado = Estados(nombre, descripcion)
    db.session.add(nuevo_estado)
   
    db.session.commit()

def Editar_nombre_estado():
    nombre_antiguo = input("Escribe el nombre del estado que quieres cambiar: ")
    nombre_editar = input("Escribe el nuevo nombre del estado: ")

    nombre = db.session.query(Estados).filter(Estados.nombre==nombre_antiguo).first()
    nombre.nombre = nombre_editar

    db.session.commit()

def Editar_descripcion_estado():
    id_descripcion = input("Escribe la 'ID' de la descripcion que quieres cambiar: ")
    descripcion_editar = input("Escribe la nueva descripcion del estado: ")

    descripcion = db.session.query(Estados).filter(Estados.id==id_descripcion).first()
    descripcion.descripcion = descripcion_editar
    
    db.session.commit()

