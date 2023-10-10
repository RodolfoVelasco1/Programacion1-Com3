#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

from variables_dimensionadas_funciones import *

#Ejercicio 1

passengers = []
cities = []
while (True):
    print("Lista de opciones:")
    print("1. Agregar pasajeros.")
    print("2. Agregar ciudades.")
    print("3. Buscar ciudad por DNI.")
    print("4. Ver la cantidad de pasajeros por ciudad.")    
    print("5. Ver país de destino por DNI.")
    print("6. Ver la cantidad de pasajeros por país.")    
    print("7. Salir.")   
    answer = int(input("Ingrese el número de opción deseada: "))

    if (answer == 1):
        add_passenger(passengers)
    elif (answer == 2):
        add_cities(cities)
    elif (answer == 3):
        search_city(passengers)
    elif (answer == 4):
        city_passengers(passengers)
    elif (answer == 5):
        search_country(passengers, cities)
    elif (answer == 6):
        country_passengers(passengers, cities)
    elif (answer == 7):
        print("Programa Finalizado.")
        print("Adiós. Vuelva pronto.")
        break
    else:
        print("Respuesta incorrecta. Vuelva a intentarlo.") 

#EJERCICIO 2

sales_list = [("Andrés Calamaro", 2, 3490, "Calle 1 - 267"), ("Julieta Venegas", 2, 8245, "Calle 2 - 678"), ("Gustavo Cerati", 3, 25976, "Calle 3 - 123"), ("Charly García", 3, 59953, "Calle 4 - 745"), ("Fito Paez", 4, 250, "Calle 5 - 345"), ("Charly García", 4, 2943, "Calle 4 - 745"), ("Andrés Calamaro", 5, 3490, "Calle 1 - 267"), ("Federico Moura", 5, 26345, "Calle 6 - 123")]
print("Lista con información de cada venta:")
print(sales_list)
address = get_address(sales_list)
print("Lista con direcciones de los clientes:")
print(address)

#EJERCICIO 3

#Socio n°1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
#Socio n°2, Bárbara Molina, ingresó: 17/03/2009, cuota al día
#Socio n°3, Lautaro Campos, ingresó: 17/03/2009, cuota al día

partners = {"1":{"nombre":"Amanda Núñez","ingreso":"17/03/2009","cuota al dia":"si"},
          "2":{"nombre":"Bárbara Molina", "ingreso":"17/03/2009","cuota al dia":"si"},
          "3":{"nombre":"Lautaro Campos", "ingreso":"17/03/2009","cuota al dia":"si"},
}  

while (True):
    print("1. Mostrar ")
    print("2. Ver cantidad de socios")
    print("3. Notificar pago")
    print("4. Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018")
    print("5. Eliminar un socio")
    print("0. salir del menu")
    option = int(input("Ingrese el número de opción deseado: "))
    if(option == 1):
        show(partners)
        print("-----------------------------")
    
    elif(option == 2):
        print("Cantidad de socios:",amount(partners))
        print("-----------------------------")
    
    elif(option == 3):
        numberso = input("Ingresar numero de socio para notificar el pago: ")
        partners = notify_payment(numberso,partners)
        print("-----------------------------")
    elif(option == 4):
        Changedate(partners)
        print("-----------------------------")
    elif(option == 5):
        name = (input("Ingresar nombre y apellido del socio a eliminar: ")).lower()    
        partners = deletpartner(partners, name)
        print("-----------------------------")
    elif(option == 6):
        partners = addpartners(partners)
        print("-----------------------------")
    elif(option == 0):
        print("Adiós, vuelva pronto. ")
        break    
