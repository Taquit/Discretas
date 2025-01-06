import math
#Libreria para leer archivos
import csv
#Librerias para la grafica
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

#Funcion para suma modular
def sumod(x,y,n):
    x=int (x)
    y=int(y)
    n=int(n)
    resul=(x+y) % n
    return resul

#Funcion para resta modualr
def resmod(x,y,n):
    x = int(x)
    y = int(y)
    n = int(n)
    resul=(x-y) % n
    return resul

#Funcion para la multiplicacion modular
def multiplicacion_modular(num1, num2, modulo):
    x = int(num1)
    y = int(num2)
    n = int(modulo)
    resul=(x*y) % n
    return resul

#Funcion para exponencial modular
def expmod(x,y,n):
    x = int(x)
    y = int(y)
    n = int(n)
    resul=int(math.pow(x,y) % n)
    return resul

#Funcion de aloritmo de euclides (funcion recursiva)
def euclides(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = euclides(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

#Funcion para pedir enteros
def pedir_entero(mensaje):
    while True:
        try:
            # Intentamos convertir la entrada del usuario a un entero
            return int(input(mensaje))
        except ValueError:
            # Si ocurre un error, mostramos un mensaje y pedimos de nuevo
            print("Error: Debes introducir un número entero válido.")
# Función para resolver la ecuación ax ≡ b (mod n)
def ecuaciones(a, b, n):
    # Paso 1: Encontrar el MCD de a y n
    g, x, y = euclides(a, n)

    # Paso 2: Si el MCD no divide a b, no hay solución
    if b % g != 0:
        return "No hay solución"

    # Paso 3: Si g > 1, dividimos la ecuación por g
    a, b, n = a // g, b // g, n // g

    # Paso 4: Encontramos el inverso multiplicativo de a módulo n
    g, inv_a, _ = euclides(a, n)
    inv_a = inv_a % n  # Asegurarnos de que el inverso esté en el rango [0, n-1]

    # Paso 5: Multiplicamos ambos lados de la ecuación por el inverso de a
    x = (inv_a * b) % n

    return x

def mostrar_residuos_modulo(n):
    residuos = list(range(n))  # Los residuos serán 0, 1, ..., n-1
    angulos = np.linspace(0, 2 * np.pi, n, endpoint=False)  # Distribuir los puntos en un círculo

    # Configurar el gráfico
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')  # Para mantener la proporción de un círculo
    ax.set_xticks([])  # Quitar las marcas en el eje X
    ax.set_yticks([])  # Quitar las marcas en el eje Y

    # Graficar los residuos como puntos en un círculo
    for i, angulo in enumerate(angulos):
        x = np.cos(angulo)
        y = np.sin(angulo)
        ax.plot(x, y, 'bo')  # Dibuja puntos azules en las posiciones correspondientes
        ax.text(x * 1.1, y * 1.1, str(residuos[i]), ha='center', va='center', fontsize=12)  # Etiquetas de los residuos

    # Mostrar el gráfico
    plt.title(f"Clases de residuos módulo ", fontsize=14)
    plt.show()


#---Inico de ejecucion de codigo---
print("Desea ingresar los valor o un archivo csv\n1)Para forma manual\n2)Para archivo csv")

choose=pedir_entero("Opcion:")
if choose==1:
    print("1)Operaciones modulares basicas \n2)Ecuaciones modulares simples")
    choose=pedir_entero("Opcion:")
    if choose==1:
        print("El formato sera 'x operador y(mod n)' ")
        x=pedir_entero("x=")
        operador=input("operador=")
        y=pedir_entero("y=")
        n=pedir_entero("n=")


        match operador:
            case "+":
                suma=sumod(x,y,n)
                # Salida del resultado
                print(f"{x} * {y} (mod {n}) = {suma}")
                mostrar_residuos_modulo(n)

            case "-":
                res=resmod(x,y,n)
                print(f"{x} * {y} (mod {n}) = {res}")
                mostrar_residuos_modulo(n)

            case "*":
                mul=multiplicacion_modular(x,y,n)
                print(f"{x} * {y} (mod {n}) = {mul}")
                mostrar_residuos_modulo(n)
            case "^":
                exp=expmod(x,y,n)
                print("El resultado de la exponencial es: ", exp )
                mostrar_residuos_modulo(n)
            case _: #Caso por defecto
                print("Operador no valido.")
    else:
        print("El formato sera 'x x y(mod n)' ")
        x =pedir_entero("x=")
        y =pedir_entero("y=")
        n =pedir_entero("n=")
        resul =ecuaciones(x,y,n)
        print("El resultado es: ",  resul)
        #mostrar_residuos_modulo(n)

else:
    print("Ingrese la direccion en la que se encuentre el archivo csv y el nombre del archivo")
    ruta=str(input(":"))
    try:
        with open(ruta,mode="r" ) as archivo:
            lectura = csv.reader(archivo)
            encabezado=next(lectura)
            campos=encabezado+["Resultados"]
            with open(ruta,mode="w") as archivo_out:
                escritor=csv.writer(archivo_out)
                escritor.writerow(campos)
                for row in lectura:
                    x = row[0]  # Primera columna
                    operador = row[1]  # Segunda columna
                    y = row[2]  # Tercera columna
                    n=row [3] #Cuarta columna
                    match operador:
                        case "+":
                            resul = sumod(x, y, n)

                        case "-":
                            resul = resmod(x, y, n)

                        case "*":
                            resul = multiplicacion_modular(x, y, n)

                        case "^":
                            resul = expmod(x, y, n)
                        case _:
                            print("ERORR")


                    row.append(resul)
                    escritor.writerow(row)
                    print(f"Resultado para {x} {operador} {y} mod {n}: {resul}")
                mostrar_residuos_modulo(int(n))
    except FileNotFoundError:
        print("El archivo CSV no fue encontrado . Verifica la ruta.")
    except Exception as e:
        print(f"Error inesperado al manejar el archivo {e}")
