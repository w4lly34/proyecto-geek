import db
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Usuarios(db.Base):
    __tablename__= "usuarios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    apellidos =Column(String(60))
    email = Column(String(50))
    usuarios = relationship("Tareas", uselist = False)
    
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

db.Base.metadata.create_all(db.engine)


class Estados(db.Base):
    __tablename__= "estados"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    descripcion =Column(String(500))
    estado = relationship("Tareas")

    def __init__(self, nombre, descripcion):
        self.nommbre = nombre
        self.descripcion = descripcion

    def __repr__(self):
        return f'{self.id}, {self.nombre}, {self.descripcion}\n'


db.Base.metadata.create_all(db.engine)        


class Tareas(db.Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True,)
    titulo = Column(String(60))
    descripcion =Column(String(500))   
    responsable =Column(String(50))
    fecha_creacion =Column(String(20))
    usuarios_nombre =Column(String(40), ForeignKey("usuarios.nombre"))
    estado_nombre =Column(String(30), ForeignKey("estados.nombre"))

   
   
    def __init__(self, titulo, descripcion, responsable, fecha_creacion, usuarios_nombre, estado_nombre):
        self.titulo = titulo
        self.descripcion = descripcion
        self.responsable = responsable
        self.fecha_creacion = fecha_creacion
        self.usuarios_nombre = usuarios_nombre
        self.estado_nombre = estado_nombre


    def __repr__(self):
        return f'"ID: "{self.id}, {self.descripcion}, {self.responsable}, {self.fecha_creacion}, {self.usuarios_nombre}, {self.estado_nombre}\n'


db.Base.metadata.create_all(db.engine)



class Login(db.Base):
    __tablename__= "login"

    id = Column(Integer, primary_key=True)
    usuario = Column(String(50))
    contraseña = Column(String(50))
    
    
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

    def __repr__(self):
        return f'{self.id}, {self.usuario}, {self.contraseña}\n'

db.Base.metadata.create_all(db.engine)






