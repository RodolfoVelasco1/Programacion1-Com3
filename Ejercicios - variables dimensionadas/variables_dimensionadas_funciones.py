#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#Ejercicio 1

def add_passenger(passengers):
    name = input("Ingrese el nombre del pasajero: ")
    id_number = input("Ingrese el DNI del pasajero: ")
    city = input("Ingrese la ciudad a la que viaja el pasajero: ")
    passengers.append((name, id_number, city))

def add_cities(cities):
    city = input("Ingrese una ciudad: ")
    country = input("Ingrese el país donde se encuentra dicha ciudad: ")
    cities.append((city, country))

def search_city(passengers):
    id_passenger = input("Ingrese el número de DNI del pasajero: ")
    for name, id_number, city in passengers:
        if (id_passenger == id_number):
            print("El pasajero " + name + " viaja a " + city)

def city_passengers(passengers):
    destination = input("Ingrese la ciudad de destino: ")
    counter = 0
    for name, id_number, city in passengers:
        if (city == destination):
            counter = counter + 1
    print(str(counter) + " pasajeros viajan a esa ciudad.")

def search_country(passengers, cities):
    id_passenger = input("Ingrese el número de DNI del pasajero: ")
    for name, id_number, city in passengers:
        if (id_passenger == id_number):
            id_passenger = city
            for city, country in cities:
                if(id_passenger == city):
                    print("El pasajero " + name + " viaja a " + country)
def country_passengers(passengers, cities):
    destination = input("Ingrese el país de destino: ")
    counter = 0
    for city, country in cities:
        if (country == destination):
            destination = city
            for name, id_number, city in passengers:
                if (destination == city):
                    counter = counter + 1
    print(str(counter) + " pasajeros viajan a ese país.")

#EJERCICIO 2

def get_address(sales_list):
    address = set()  
    for client, day, money, street in sales_list:
        address.add(street)
    return list(address)  

#EJERCICIO 3

def show(partners_):
    for i, value in partners_.items():
        print("-----------------------------")
        print("socio",i)
        for key_, val in value.items():
            print(key_+": "+val) 

def amount(partners_):
    con = 0          
    for i in partners_:
        con+=1
    return con     

def notify_payment(numberso_,partners_):
    print(partners_[numberso_]["cuota al dia"])
    partners_[numberso_]["cuota al dia"] = "si"
    print("se actualizo el pago de socio " + partners_[numberso_]["nombre"])
    return partners_

def Changedate(partners_):
    for key, value in partners_.items():
        if (value["ingreso"] == "17/03/2009"):
            partners_[key]["ingreso"] = "14/03/2018"
            print("Se cambio la feca de ingreso de " + value["nombre"] + " de 17/03/2009 al 14/03/2018")

def deletpartner(partners_,name_):
    for key, value in partners_.items():
        if ((value["nombre"]).lower() == name_):
            del partners_[key]
            return partners_
    print("No se encontro el nombre")
    return partners_        

def addpartners(partners_):
    aux = len(partners_) + 1
    name = input("ingresar nombre: ").title()
    date = input("ingresar fecha formato(dd/mm/aaaa): ")
    
    partners_[aux] = {"nombre":name, "ingreso":date,"cuota al dia":"si"}
    return partners_