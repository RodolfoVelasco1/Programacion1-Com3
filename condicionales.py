fecha = input("Ingrese el día (lunes, martes, etc): ") + ", " + input("Ingrese el número de día: ") + "/" + input("Ingrese el número de més: ")
fecha = fecha.lower()
print(fecha)


dia_sem = fecha[0 : fecha.find(",")]
dia = int(fecha[fecha.find(" ")+1 : fecha.find("/")])
mes = int(fecha[fecha.find("/")+1 :])
if (dia_sem != "lunes" and dia_sem != "martes" and dia_sem != "miercoles" and dia_sem != "jueves" and dia_sem != "viernes" and dia_sem != "sabado" and dia_sem != "domingo" and dia_sem != "miércoles" and dia_sem != "sábado"):
    print("Error en día")
elif (dia > 31 or dia <= 0):
    print("Error en número de día")
elif (mes > 12 or dia <= 0):
    print("Error en número de mes")
else:
    print("Fecha Ingresada Correctamente")   
    if (dia_sem == "lunes" or dia_sem == "martes" or dia_sem == "miercoles" or dia_sem == "miércoles"):
        examen = input("¿Se tomó examen hoy? s/n: ")
        if (examen == "s"):
            aprobados = int(input("Ingrese el número de alumnos que aprobó: "))
            desaprobados = int(input("Ingrese el número de alumnos que desaprobó: "))
            total_alumnos = aprobados + desaprobados
            porcentaje_aprobados = aprobados * 100 / total_alumnos  
            print(f"El porcentaje de alumnos aprobados es de: {porcentaje_aprobados}%")
        else:
            print("Hoy no se tomó examen.")
    elif (dia_sem == "jueves"):
        asistencia = int(input("Ingrese el porcentaje de alumnos que asistieron: "))
        if (asistencia > 50):
            print("Asistió la mayoría.")
        else:
            print("No asistió la mayoría.")
    elif (dia_sem == "viernes" and dia == 1 and mes == 1 or dia_sem == "viernes" and dia == 1 and mes == 7):
        print("Comienzo de nuevo ciclo.")
        cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
        arancel = int(input("Ingrese el costo del arancel: "))
        ingreso = cantidad_alumnos * arancel
        print(f"El ingreso total es de ${ingreso}")
    elif (dia_sem == "viernes" and dia != 1 and mes != 1 or dia_sem == "viernes" and dia != 1 and mes != 7):
        print("Hoy hay clases con normalidad.")
    else:
        print("En este día no se dictan clases.")
