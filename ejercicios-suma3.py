'''
It is my first programming proyect in life, I hope you like it.
It is a simple game, you will catch easy


corrections and improves:
    -translate to english
    -order the ranking
    -add sustraction, division and multiplication
'''


import os
import random
import time
#import pathlib


def high_score(file_data):
    if os.path.exists("tabla.txt") == False:
        print("no existia un carajo el archivo")
        file_data = open("tabla.txt","w")
        file_data.write("Nombre                    Tiempo(segundos)" + "\n")
        
    else:
        file_data = open("tabla.txt","r")
        file_data.close()


# esto de aqui abajo no me sale, o me borra el archivo anterior o no me corre el prog
'''
def crear_archivo():
    if 'text.txt'.exists():
        print("existe el archivo")
        print(pathlib.Path('text.txt'))
        input("esto esta para demorar: ")
        clasificacion = open('tabla.txt','r+')
        #clasificacion.write("nombre                    tiempo(segundos)" + "\n")
    else:
        clasificacion = open('tabla.txt','w')
        clasificacion.write("nombre                    tiempo(segundos)" + "\n")
'''

def menu():
    print('''
                       Juego de hacer cuentas
    1) Jugar
    2) Tabla clasificacion 

    0) Salir                
    ''')




def ejercicios():
    continuar = True
    input("presione cualquier tecla, recuerde se le evaluara el tiempo")
    start = time.time()
    aciertos = 0
    vidas = 3
    while continuar:
        os.system("cls")
        a = random.randint(0,999)
        b = random.randint(0,999)
        resultado = a + b
        print(f'aciertos: {aciertos}        vidas: {vidas}')

        print('''
        Calcula esto perrito malvado

        ''')
        print (f'{a}  +  {b}   =   ')
        print("")
        respuesta = int(input("el resultado es: "))
        # aca tengo que hacer algo por si me responden vacio me salta error, desp pongo un except
        if respuesta == resultado or respuesta == 0:
            #la respuesta '0' es para testeo, cuando se termine deberia borrarse
            print("tu respuesta es correcta")
            aciertos += 1
        else:
            print(f'tu respuesta es incorrecta, la respuesta correcta es {a + b}')
            print("")
            vidas -= 1 

        if aciertos == 3:
            end = time.time()
            tiempo_total = round(end - start, 2)
            print("Has ganado!!")
            print(f'has tardado {tiempo_total} segundos y has tenido {3 - vidas} errores')
            tabla(tiempo_total)
            continuar = False

        elif vidas == 0:
            print("se te acabaron las vidas, sigue intentando y mejorando")
            continuar = False
        else:
            pass
            
        
        input("presiona 'enter' para continuar")
            
        

def tabla(tiempo_total):

    clasificacion = open('tabla.txt','a')
    nombre = input("inserte su nombre: ")
    if 20 > len(nombre) > 0:
        spaces = " " * (20 - len(nombre))
        a = str(f'{str(nombre)}   {spaces}       {str(tiempo_total)}   \n')
        #clasificacion.write(  str(nombre), '  ',' '*(15-len(nombre)), str(tiempo_total),  "\n"  )   
        clasificacion.write(a)
        clasificacion.close()
    
        ranking()

    else:
        clasificacion.close()
        print("ingrse un nombre valido chinguenguencha")
        tabla(tiempo_total)
    #practica con el archivos-practica.py


def ranking():
    os.system('cls')
    clasi = open('tabla.txt','r')
    x = clasi.read()
    print(x)
    input("presiona 'enter' para continuar")
    clasi.close()


def main():
    file_data = 0
    high_score(file_data)
    continuar = True
    while continuar:
        os.system('cls')
        menu()
        x = int(input("inserte una opcion: "))
        if x == 1 :
            ejercicios()
        elif x == 2:
            ranking()
        elif x == 0:
            continuar = False
            print("saliendo...")
        else:
            print("no se te entendio nada, paquero")
        input("presiona 'enter' para continuar")

main()






