'''
Virtual wallet 
Autores: Causarano Daniela, More Julieta
Fecha: 2024
Version 1.0

''' 
import os 
import colorama
import getpass #para que no se muestre la contraseña mientras estas escribiendo.
import datetime
from datetime import date
import json
Usuario= ""
Clave= ""

def limpiarpantalla():
    '''
    Función limpiarpantalla()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere
    Retorno: no tiene
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def verificar_persona():
    '''
    Función verificar_persona()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere
    Retorno: si retorna, bool (True si la verificación es exitosa, False en caso contrario)

    '''
    global Usuario, Clave
    i=3
    while i > 0:
        usu=input(("Ingrese usuario: ").rjust(65," "))
        clave1=getpass.getpass(("Ingrese contraseña: ").rjust(68," "))

        if usu==Usuario and clave1==Clave:
            return True
        else:
            i-=1
            print(("Usuario y/o contraseña inválidos".rjust(80," ")))
            print((f"Le quedan {i} intentos").rjust(68," "))
            if i == 0:
                print(("Ha superado el máximo de intentos permitidos. Salga e intentelo de nuevo").rjust(120," "))
                return False
def menu():
    '''
    Función menu()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere
    Retorno: si retorna, la opción seleccionada por el usuario

    '''
    limpiarpantalla()
    print(colorama.Fore.GREEN + "VIRTUAL WALLET".center(45))
    print(colorama.Fore.RESET + "="*45)
    print(colorama.Fore.LIGHTMAGENTA_EX + "1-"+ colorama.Fore.RESET +  "perfil".capitalize())
    print(colorama.Fore.LIGHTMAGENTA_EX + "2-" + colorama.Fore.RESET + "ingresar dinero a cuenta".capitalize())
    print(colorama.Fore.LIGHTMAGENTA_EX + "3-" + colorama.Fore.RESET + "transferir dinero".capitalize().ljust(40," ") )
    print(colorama.Fore.LIGHTMAGENTA_EX + "4-" + colorama.Fore.RESET + "saldo disponible".capitalize() )
    print(colorama.Fore.LIGHTMAGENTA_EX + "5-" + colorama.Fore.RESET + "agenda de facturas".capitalize() )
    print(colorama.Fore.LIGHTMAGENTA_EX + "6-" + colorama.Fore.RESET + "imprimir resumen de cuenta".capitalize() )
    print(colorama.Fore.LIGHTMAGENTA_EX + "7-" + colorama.Fore.RESET + "salir".capitalize() )
    print(colorama.Fore.RESET + "="*45)
    try:
        op=int(input(colorama.Fore.LIGHTYELLOW_EX + "Seleccione una opción: " + colorama.Fore.RESET))
    except ValueError:
        op=0 #lo inicializamos con 0 para asegurarnos de que siempre tenga un valor asignado 
        print("¡ERROR!")
    return op

def cargar_datosUsuCla():
    '''
    Función cargar_datosUsuCla()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere 
    Retorno: sí retorna, lista vacía

    '''
    try:
        with open("usuario y clave.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def guardar_datosUsu(Usuario):
    '''
    Función guardar_datosUsuCla(usuario)
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: sí requiere (1)
    Retorno: no

    '''
    with open("usuario y clave.json","w") as file:
        json.dump(Usuario, file, indent=4)
        return
    
def guardar_datosCla(Clave):
    '''
    Función guardar_datosCla(clave)
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: sí requiere (1)
    Retorno: no

    '''
    with open("usuario y clave.json","w") as file:
        json.dump(Clave, file, indent=4)
        return

def perfil():
    '''
    Función Perfil()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere 
    Retorno: no

    '''
    limpiarpantalla()
    print()
    print(colorama.Fore.RED + "¡ATENCIÓN! Debe registrarse para poder acceder al menú")
    print()
    print()

    nomCom=(input("Ingresa tu nombre completo: ").title())
    mail=input("Ingresa tu correo electrónico: ")
    nTel=int(input("Ingresa tu número de celular: "))
    configuracion= {
        "Nombre": nomCom,
        "Correo electrónico": mail,
        "Celular": nTel
    }
    limpiarpantalla()
    print(f"""
¡Bienvenido/a!
Nombre: {nomCom}\nCorreo: {mail}\nCelular: {nTel}""")
    print()
    print()
    print()
    rta=int(input("""
1- Configuración
2- Ver Datos de Transferencia
3- Salir 
""" ))
    while True:
        if rta == 1:
            rta2=(input("""
Elija la opción que desea modificar: 
    A) Nombre Completo
    B) Correo Electrónico
    C) Número de Celular
    D) Usuario
    E) Contraseña
    """).upper())
            
            match rta2:
                case "A":
                   nomCom=input("Ingrese el nuevo nombre completo: ")
                   print("¡Nombre completo modificado correctamente!") 
                   configuracion["Nombre"]=nomCom
                   break
                case "B":
                    mail=input("Ingrese el nuevo correo electrónico: ")
                    print("¡Correo electrónico modificado correctamente!")
                    configuracion["Correo electrónico"]=mail
                    break
                case "C":
                    nroTel=int(input("Ingrese el nuevo número de celular: "))
                    print("¡Número de celular modificado correctamente!") 
                    configuracion["Celular"]=nroTel
                    break
                case "D":
                    try:
                        global Usuario
                        Usuario=(input("Ingrese el nuevo usuario: "))
                        print("Usuario modificado con éxito!!")
                        guardar_datosUsu(Usuario)
                    except ValueError:
                        print("""
                              ERROR!
                              Ingrese letras o números""")
                    break
                case "E":
                    try:
                        global Clave
                        Clave=int(input("Ingrese la nueva contraseña: "))
                        print("Contraseña modificada con éxito!!")
                        guardar_datosCla(Clave)
                    except ValueError:
                        print("""
                              ERROR!
                              Ingrese letras o números""")
                    break
                case _: 
                    print("Opción no válida.")
        elif rta == 2:
            limpiarpantalla()
            print(colorama.Fore.BLUE + "CBU: 0040888777532") 
            print(colorama.Fore.BLUE + "Alias: PATO.CONEJO.PERRO")
            input(colorama.Fore.RED + "Presione enter para continuar")
        elif rta == 3:
            break
     
    return
# ver como hacer para que acepte el usuario y clave que la persona cambio, al ingresar al programa.

    

def cargar_datosSaldo():
    '''
    Función cargar_datosSaldo()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere 
    Retorno: sí retorna, lista vacía

    '''
    try:
        with open("saldo.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def guardar_datosSaldo(saldo):
    '''
    Función guardar_datosSaldo(saldo)
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: sí requiere
    Retorno: no

    '''
    with open("saldo.json","w") as file:
        json.dump(saldo, file, indent=4)
        return

Saldo=[] # lo inicializamos afuera de la función para que no se pierdan los datos y pop funcione correctamente

def ingresar_dinero(dinero1):
    '''
    Función ingresar_dinero()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: si requiere (1)
    Retorno: no retorna nada

    '''
    
    global saldo
    
    try:
        dinero1 = float(input("Ingrese la cantidad de dinero a depositar: "))
        if dinero1 <= 0:
            print("El monto debe ser mayor a 0")
            print("Vuelva a intentar")
        elif dinero1 != 0: #Esto era un if aparte. lo puse dentro como un elif
            saldo.append(dinero1)
            print(f"Cantidad: ${dinero1} ")
            while True:
                resp=input("¿Es correcto? s/n: ")
                if resp.lower() == "s":
                    print("Dinero Despositado con éxito!!")
                    break
                elif resp.lower() == "n":
                    saldo.pop()
                    dinero1=float(input("Vuelva a ingresar la cantidad de dinero a depositar: "))
                    saldo.append(dinero1)
                    print("Dinero depositado con éxito")
            guardar_datosSaldo(saldo)
            return
    except ValueError: #esto estaba más arriba, lo puse a la misma altura del try
        print("Entrada no válida. Por favor ingrese números.")
        return
    
def cargar_datosContactos():
    '''
    Función cargar_datosContactos()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere 
    Retorno: sí retorna, lista vacía

    '''
    try:
        with open("contactos.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def guardar_datosContactos(lista_contactos):
    '''
    Función guardar_datosContactos()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere 
    Retorno: no 

    '''
    with open("contactos.json","w") as file:
        json.dump(lista_contactos,file,indent=4)
        return lista_contactos



        



def ingresarContacto (): #CREE ESTA FUNCIÓN PARA QUE NO QUEDE MUY LARGA LA FUNCIÓN OPCIONES CONTACTO
    nom=input("Ingrese el nombre de su contacto: ")
    dni=int(input("Ingrese el DNI de su contacto: "))
    alias=input("Ingrese el alias de su contacto:  ")
    cbu=int(input("Ingrese el CBU de su contacto: "))
    contacto={
        "Nombre": nom,
        "Alias": alias,
        "CBU": cbu,
        "DNI": dni,
    }
    lista_contactos.append(contacto)
    print ("Contacto creado con éxito!!")
    print (f"Usted realizará una transferencia a {contacto["Nombre"]}")
    guardar_datosContactos(lista_contactos)
    return lista_contactos
#PROBLEMA. guarda el contacto en el momento, pero después si cierro la consola, se pisa lo anterior

def opcionesContactos():
    print ("CONTACTOS PARA TRANSFERENCIAS")
    print ("1, para agregar un nuevo contacto")
    print ("2, para buscar/modificar un contacto existente")
    print ("3, para borrar contacto")
    print ("4, ver contactos guardados")
    opcion=input("Indique la opción elegida: ")
    if opcion=="1":
        ingresarContacto() 
        return True
    elif opcion=="2":
        dni=int(input("Ingrese el N° de DNI del contacto: "))#PROBLEMA.cuando cierro la terminal y pongo el dni no entra al for. si sigo ejecutando y pongo un número recién ingresado sí
        for i in range (len(lista_contactos)):
            if lista_contactos[i]["DNI"]==dni:
                for c, v in lista_contactos[i].items():
                    print (lista_contactos[i])
                    resp=input("¿Los datos son correctos? s/n: ")
                    if resp.lower() == "s":
                        print (f"Usted realizará una transferencia a {lista_contactos[i]["Nombre"]}")
                        return True
                    elif resp.lower() == "n":
                        rta=int(input("""Elija qué quiere modificar:
                        1) NOMBRE
                        2) ALIAS 
                        3) CBU 
                        4) DNI 
                        """))
                        if rta == 1:
                            nom=input("Ingrese el nombre")
                            lista_contactos[i]["Nombre"]=nom
                            print("Nombre modificado con exito!")
                            break
                        elif rta== 2:
                            alias=input("Ingrese el alias de su contacto:  ")
                            lista_contactos["Alias"]=alias
                            print("Contacto modificado con exito!")
                            break
                        elif rta == 3:
                            cbu=input("Ingrese el CBU de su contacto: ")
                            lista_contactos[i]["CBU"]=cbu
                            print("Contacto modificado con exito!")
                            break
                        elif rta == 4:
                            dni=int(input("Ingrese el DNI de su contacto: "))
                            lista_contactos[i]["DNI"]=dni
                            print("Contacto modificado con exito!")
                            break
                        else:
                            print("Opción no válida. Inténtelo de nuevo")
                    guardar_datosContactos(lista_contactos)
                    return 
            else:
                print ("DNI no encontrado. Regrese al Menú")
            return False
    elif opcion=="3":
        dni=int(input("Ingrese el N° de DNI del contacto: "))
        for i in range (len(lista_contactos)):
            if lista_contactos[i]["DNI"]==dni:
                for c, v in lista_contactos[i].items():
                    print (lista_contactos[i])
                    resp=input("¿Desea borrar el contacto? s/n")
                    if resp.lower() == "s":
                        lista_contactos.remove(lista_contactos[i])
                        print ("Contacto borrado")
                        guardar_datosContactos(lista_contactos)
                        return False
                    elif resp.lower() == "n":
                        print ("Regrese al Menú")
                        return False
            else:
                print ("DNI no encontrado. Regrese al Menú") #PROBLEMA.continúa a la opción de ingresar dinero dentro del menú cuando no debería   
                return False        
    elif opcion=="4":
        cargar_datosContactos ()
        print (lista_contactos)
    else: 
        print ("Opción incorrecta")   
        return 
    
def transferir_dinero(dinero1):
    '''
    Función transferir_dinero()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: si requiere (4)
    Retorno: si retorna, contactos

    '''
    global saldo
    try:
        dinero1=float(input("Indique la cantidad de dinero que desea transferir: "))
        if dinero1 <=0: 
            print("Debe ingresar una cantidad mayor a $0")
            print ("Vuelva a intentar")
        elif dinero1!=0:
            print(f"Usted ingresó ${dinero1}")
            dinero1=dinero1*-1 #para convertir dinero en negativo y reste en el saldo
            saldo.append(dinero1)
            while True:
                resp=input("¿Es correcto? s/n: ")
                if resp.lower() == "s":
                    print("Transferencia realizada con éxito!!")
                    break
                elif resp.lower() == "n":
                    saldo.pop()
                    dinero1=float(input("Ingrese nuevamente el dinero a transferir: "))
                    dinero1=dinero1*-1
                    saldo.append(dinero1)
                    print("Transferencia realizada con éxito!!")
            guardar_datosSaldo(saldo)
            return
    except ValueError:
        print("Entrada no válida. Por favor ingrese números.")
        return



def guardar_serv (lista_pagos):
    with open ('agendadepagos.json','w') as file:
        json.dump(lista_pagos,file,indent=4)
        return lista_pagos

def cargar_serv ():
    with open ("agendadepagos.json","r") as file:
        return json.load(file)

    
#agenda de facturas
def agendar_pagos ():
    print ("AGENDA DE FACTURAS")
    print ("1 - Agendar servicios/impuestos a pagar: ")
    print ("2 - Ver servicios/impuestos: ")
    opc=int(input("Seleccione la opción deseada: "))
    limpiarpantalla()
    if opc==1:
        print ("Agendar servicios/impuestos a pagar: ")
        nom_serv=input("Ingrese el nombre del servicio: ")
        fecha_venc=input("Ingrese la fecha de vencimiento de su factura (ejemplo: 2024-02-20): ")
        dias_ven=date.fromisoformat(fecha_venc)-hoy
        servicios={
            "SERVICIO/IMPUESTO": nom_serv,
            "FECHA DE VENCIMIENTO": fecha_venc,
            "DIAS RESTANTES PARA PAGAR": dias_ven.days
        }
        lista_pagos.append(servicios)
        print ("Factura ingresada con éxito! ")
        guardar_serv (lista_pagos) 
        return lista_pagos
    elif opc==2:
        print ("Servicios/impuestos a pagar: ")
        cargar_serv()
        print (lista_pagos)
    else:
        print ("Opción no válida")
    return 

def ver_saldo():
    '''
    Función ver_saldo()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere 
    Retorno: no retorna

    '''
    limpiarpantalla()
    global saldo
    total_saldo=sum(saldo)
    print(f"Saldo actual: ${total_saldo:.2f}")
    return

#programa principal
colorama.init()
saldo=cargar_datosSaldo()
dinero1=0 #declaré acá la variable porque dentro de la opción 2,
# cuando ingresaba una letra, no iba al except. 
lista_contactos=cargar_datosContactos()
lista_pagos=[]
zona=datetime.timezone(datetime.timedelta(hours=-3))
hoy = datetime.date.today()


if verificar_persona() == True:
    perfil()
   
while True:
        op = menu()
        if op == 1:
            print("Perfil")
            print("-" * 24)
            perfil()
            input(colorama.Fore.RED + "Presione enter para continuar")
        elif op == 2:
            print("Ingresar dinero a cuenta")
            print("-" * 24)
            ingresar_dinero(dinero1)
            input(colorama.Fore.RED + "Presione enter para continuar")
        elif op == 3:
            print("Transferir dinero")
            print("-" * 24)
            opcionesContactos()
            input(colorama.Fore.RED + "Presione enter para continuar"+ colorama.Fore.RESET)
            limpiarpantalla()
            while True:
                transferir_dinero(dinero1)
                break
            input(colorama.Fore.RED + "Presione enter para continuar")

        elif op == 4:
            print("Ver saldo disponible")
            print("-" * 24)
            ver_saldo()
            input(colorama.Fore.RED + "Presione enter para continuar")
        elif op == 5:
            print("Agenda de Facturas")
            print("-" * 24)
            agendar_pagos()
            input(colorama.Fore.RED + "Presione enter para continuar")
        elif op == 6:
            print("Imprimir resumen de cuenta")
            print("-" * 24)
            input(colorama.Fore.RED + "Presione enter para continuar")
        elif op == 7:
            break
        else:
            print("Por favor ingrese una opción válida.")
            input(colorama.Fore.RED + "Presione enter para continuar")