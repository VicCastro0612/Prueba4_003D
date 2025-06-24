diccionario = [
    "estudiantes" == []
]

def lista_de_nombres(diccionario_a_iterar):
    lista_nombres = []
    if len(diccionario_a_iterar["usuarios"]) != 0:
        for i in diccionario_a_iterar:
            lista_nombres.append(i["nombre"])
    return lista_nombres

def ingrese_nombre(mensaje):
        while True:
            lista_nombres = lista_de_nombres(diccionario["usuarios"])
            print(lista_nombres)


            nombre = input("Ingrese el nombre del usuario: ")
            if nombre in lista_nombres:
                print("El usuario ya se encuentra registrado, ingrese otro nombre.")
            else:
                return nombre
        

def ingrese_sexo(mensaje):
    while True:
        sexo = input(mensaje)
        if (sexo != "M") and (sexo != "F"):
            print("Solamente puede ingresar M o F. Intentelo de nuevo.")
        else:
            return sexo
        
def buscar_usuario(lista,nombre):
    if len(lista_nombres) == 0:
        print("No hay usuarios registrados.")
    else:
        nombre = input("Ingrese el usuario que busca: ")
        if nombre in lista_nombres:
            i = 0
            while i < len(diccionario["usuarios"]):
                if nombre == diccionario["usuarios"][i]["nombre"]:
                    indice = i
                    break
            else:
                i += 1
        else:
            print("No se ha encontrado el usuario.")

def eliminar_usuario(lista,nombre):
    if len(lista) == 0:
        print("No hay usuarios registrados.")
    else:
        if nombre in lista:
            indice = 


def opciones():
    while True:
        try:
            print("Menú principal")
            print("[1] - Ingresar usuarios")
            print("[2] - Buscar usuario")
            print("[3] - Eliminar usuario")
            print("[4] - Salir")

            opcion = int(input("Ingrese opción (1-4): "))
        except ValueError:
            print("Porfavor, ingrese una opcion del 1 al 4. Intentelo de nuevo.")


while True:
    
    opcion = opciones()

    if opcion == 1:

        lista_nombres = lista_de_nombres(diccionario["usuarios"])
        print(lista_nombres)
        nombre = ingrese_nombre("Ingrese el nombre del usuario: ")
        sexo = ingrese_sexo("Ingrese el sexo del usuario (F/M): ")
        contrasena = input("Ingrese contraseña: ")

        usuario = {
            "nombre":nombre,
            "sexo":sexo,
            "contrasena":contrasena
        }

        diccionario["usuarios"].append(usuario)
    
    elif opcion == 2:
        
        lista_nombres = lista_de_nombres(diccionario["usuarios"])
        i = 0
        print(diccionario["usuarios"][i]["nombre"])
        print(len(diccionario["usuarios"]))

        indice = buscar_usuario(lista_nombres)
        print(f"El sexo del usuario es: {diccionario['usuarios'][indice]["sexo"]} y la contraseña es: {diccionario['usuarios'][indice][contrasena]}")
        buscar_usuario(lista_nombres,nombre)


    elif opcion == 3:
        #me quede corto de tiempo :c

    elif opcion == 4:
        print("Programa terminado.")
        break

    else:
        print("Debe ingresar una opción valida.")