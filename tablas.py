import db
from sqlalchemy import create_engine, Column, String, Integer

class Tareas(db.Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True,)
    titulo = Column(String(60))
    descripcion =Column(String(500))
    estado =Column(String(30))
    responsable =Column(String(30))
    fecha_creacion =Column(String(20))

    def __init__(self, titulo, descripcion, estado, responsable, fecha_creacion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
        self.responsable = responsable
        self.fecha_creacion = fecha_creacion

    def __repr__(self):
        return f'"ID: "{self.id}, {self.descripcion}, {self.estado}, {self.responsable}, {self.fecha_creacion}\n'


db.Base.metadata.create_all(db.engine)


class Estados(db.Base):
    __tablename__= "estados"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    descripcion =Column(String(500))

    def __init__(self, nombre, descripcion):
        self.nommbre = nombre
        self.descripcion = descripcion

    def __repr__(self):
        return f'{self.id}, {self.nombre}, {self.descripcion}\n'


db.Base.metadata.create_all(db.engine)        


class Usuarios(db.Base):
    __tablename__= "usuarios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    apellidos =Column(String(60))
    email = Column(String(50))
    
    
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

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






