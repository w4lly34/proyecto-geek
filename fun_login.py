import db
from tablas import Login



def Crear_login():
    
    usuario = input("Introduce usuario a crear: ")
    contraseña = input("Introduce contraseña a crear: ")

    nuevo_login = Login(usuario, contraseña)
    db.session.add(nuevo_login)
    db.session.commit()


def Editar_usuario():
   
    usuario_antiguo = input("Escribe el usuario a cambiar: ")
    usuario_editar = input("Escribe el nuevo usuario: ")

    nombre = db.session.query(Login).filter(Login.usuario==usuario_antiguo).first()
    nombre.usuario = usuario_editar

    db.session.commit()


def Editar_contraseña():
    
    contraseña_antiguo = input("Escribe el contraseña a cambiar: ")
    contraseña_editar = input("Escribe el contraseña usuario: ")

    nombre = db.session.query(Login).filter(Login.contraseña==contraseña_antiguo).first()
    nombre.contraseña = contraseña_editar

    db.session.commit()



def Login_agenda():
   
    salir=True
    while salir:
         
        try:
            nick = input("Introduce usuario: ")
            nick1 = db.session.query(Login).filter_by(usuario=nick).first()
            nickr = nick1.usuario
            print("correcto")
            salir=False
        except:
            print("Incorrecto")

    salir=True
    while salir:    
        
        try:
            passw = input("Introduce contraseña: ")
            passw1 = db.session.query(Login).filter_by(contraseña=passw).first()
            passwr = passw1.contraseña
            print("correcto")
            salir=False
        except:
            print("Incorrecto")
            
            





    

       

      
    


    
    
    
    

    
