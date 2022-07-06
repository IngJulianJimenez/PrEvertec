"""
Ejercicio2:
Desarrollar un programa que permita cargar un numero dado de nombres de personas y sus edades respectivas. 
Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores o iguales a 21 años
"""

lst_register_user = []
lst_register_user_out = []

menu = 0
while menu != 4 :
    menu = int( input("\nEscoger una opcion:\n\t>1.Registrar Usuario\n\t>2.Visulizar\n\t "))

    if menu == 1:
        user = {}

        nombre = str(input("\t>Ingrese nombre: "))
        user['nombre'] = nombre

        edad = str(input("\t>Ingrese edad: "))
        user['edad'] = edad

        lst_register_user.append(user)

        #print ("dictionary_user =>",user)
        print ("list_register_user =>",lst_register_user)  


    if menu == 2:
        for edad in lst_register_user:
            #print (edad) 
            if edad ['edad'] >= '21':
                print (edad['nombre'], edad ['edad'])  

