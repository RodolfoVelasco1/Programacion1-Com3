#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#TP9

#EJERCICIO 4

class Agenda:

    def __init__(self):
        print("")
    
    #Lista de contactos
    def list_contact(self, all_contacts_dictionary ):
         for cont in all_contacts_dictionary:
            nombre_cont = cont["Nombre"]
            telefono_cont = cont["Telefono"]
            email_cont = cont["Email"]
            print(f"Nombre: {nombre_cont}, Telefono: {telefono_cont}, Email: {email_cont}")

    #Añadir Contacto0
    def add_contact(self, name, phone, email):
        contact = {"Nombre": name, "Telefono": phone, "Email": email}
        return contact
    
    #Buscar Contacto
    def search_contact(self,all_contacts_dictionary, name=None, phone=None,):
        print(all_contacts_dictionary)
        for cont in all_contacts_dictionary:
            if name:
                verifi_name = cont["Nombre"]
                if  verifi_name == name:
                    nombre_cont = cont["Nombre"]
                    telefono_cont = cont["Telefono"]
                    email_cont = cont["Email"]
                    return {"Nombre": nombre_cont, "Telefono": telefono_cont, "Email": email_cont}
            elif phone and isinstance(phone, int):
                 verifi_phone =cont["Telefono"]
                 if verifi_phone == phone:
                    nombre_cont = cont["Nombre"]
                    telefono_cont = cont["Telefono"]
                    email_cont = cont["Email"]
                    return {"Nombre": nombre_cont, "Telefono": telefono_cont, "Email": email_cont}
            else:
                return "Introduzca un numero o telefono, correcto o existente"

    #Editar Contacto
    def edit_contact(self, name_c=None, phone_C=None, email_C=None, name=None, phone=None):
        if name_c is None and phone_C is None and email_C is None:
            return "Tiene que ingresar al menos un dato para editar"
        elif name:
            contact = self.search_contact(name)
        elif phone:
            contact = self.search_contact(phone)
        else:
            return "Introduzca un numero o telefono, correcto o existente"

        if name_c is not None:
            contact["Nombre"] = name_c
        if phone_C is not None:
            contact["Telefono"] = phone_C
        if email_C is not None:    
            contact["Email"] = email_C
        return {"Nombre": contact["Nombre"], "Telefono": contact["Telefono"], "Email": contact["Email"]}
    

#Programa

def agenda_multyfuncional(agenda):
    all_contacts_dictionary = []
    print("\nBienvenido a su agenda MultiFuncional\n")
    while True:
        print("Porfavor, Ingrese el numero de una de las siguientes opciones \n 1-Añadir Contacto \n 2-Lista de contactos \n 3-Buscar Contacto \n 4-Editar Contacto \n 5-Cerrar agenda")
        select_option = input("\n-->  ")
        if select_option == "1":
            print("Ingrese el Nombre del contacto a añadir")
            add_name = input("\n --> ")
            print("Ingrese el Telefono del contacto a añadir")
            add_phone = int(input("\n --> "))
            print("Ingrese el Email del contacto a añadir")
            add_email = input("\n -->  ")
            if len(add_name) > 2 and len(str(add_phone)) >= 10 and len(add_email) > 7:
                new_Contact = agenda.add_contact(add_name, add_phone, add_email)
                print(new_Contact)
                all_contacts_dictionary.append(new_Contact)
                continue
        elif select_option == "2":
            resultado = agenda.list_contact(all_contacts_dictionary)
            print(resultado)
        elif select_option == "3":
            print("Buscar por nombre(Opcional)")
            search_name = input("\n --> ")
            print("Buscar por telefono(Opcional)")
            search_phone1 = (input("\n --> "))
            if search_phone1 == "" or search_phone1 == " ":
                search_phone = 1
            else:
                search_phone = int(search_phone1)
            if len(search_name) > 2 and (len(str(search_phone)) >= 10 or search_phone == 1):
                search_contact = agenda.search_contact(all_contacts_dictionary,search_name, search_phone )
                nombre_cont = search_contact["Nombre"]
                telefono_cont = search_contact["Telefono"]
                email_cont = search_contact["Email"]
                print(f"El contacto buscado tiene la siguiente informacion: Nombre: {nombre_cont}, Telefono: {telefono_cont}, Email: {email_cont}")
                continue 
        elif select_option == "4":
            print("Buscar por nombre(Opcional) para editar el contacto")
            search_name = input("\n --> ")
            print("Buscar por telefono(Opcional) para editar el contacto")
            search_phone = input("\n --> ")
            if search_phone1 == "" or search_phone1 == " ":
                search_phone = 1
            else:
                search_phone = int(search_phone1)
            print("Ingrese el nuevo Nombre del contacto(opcional)")
            edit_name = input("\n --> ")
            print("Ingrese el nuevo Telefono del contacto(opcional)")
            edit_phone = int(input("\n --> "))
            if edit_phone == "" or edit_phone == " ":
                edit_phone = None
            else:
                edit_phone = int(edit_phone)
            print("Ingrese el nuevo Email del contacto(opcional)")
            edit_email = input("\n --> ")
            if len(search_name) > 2 and len(str(search_phone)) >= 10 and len(edit_email) > 7:
                edit_contact = agenda.edit_contact(edit_name, edit_phone, edit_email, search_name, search_phone)
                nombre_cont = edit_contact["Nombre"]
                telefono_cont = edit_contact["Telefono"]
                email_cont = edit_contact["Email"]
                print(f"El contacto buscado tiene la siguiente informacion: Nombre: {nombre_cont}, Telefono: {telefono_cont}, Email: {email_cont}")
                continue
        elif select_option == "5":
            print("\nGracias por usar tu Agenda MultiFuncional\n")
            print("\nHasta la Proxima\n")
            return
        else:
            print("\nAh ocurrido un error, vuelva a intentarlo\n")
            continue





mi_agenda = Agenda()
print(agenda_multyfuncional(mi_agenda))