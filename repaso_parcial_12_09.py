#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

print("¡Bienvenidos a \"Delicias de casa\"!")
print("Las mejores viandas con los sabores más caseros.")
food_amount = 0
drink_amount = 0
money = 0
order = "-"

while (food_amount <= 0):   #Ciclo while: se ingresa la cantidad de viandas. Si el número es menor o igual a 0, el ciclo se repite hasta que se ingrese un número válido.
    food_amount = int(input("Ingrese cuántas viandas va a pedir: "))
    if(food_amount <= 0):
        print("Error. Ingrese un número mayor o igual a 1.")

print("Nuestro menú:")  #Se imprime todo el menú junto a su precio.
print("1. Pizza muzzarella individual + Botella de agua. $1500")
print("2. Hamburguesa de carne + Botella de agua. $2000")
print("3. Milanesa de pollo con papas fritas + Botella de agua. $2000")
print("4. Spaghetti con salsa bolognesa + Botella de agua. $2500")
print("5. Calabaza rellena con queso, pimientos y cebolla + Botella de agua. $2500")
print("0. No deseo ordenar comida. Salir.")

for i in range(food_amount): #Por cada vianda, el usuario ingresará qué platillo desea seleccionar.
    print("Ingrese el número de opción que desea seleccionar.")
    food_option = int(input(f"Vianda #{i+1}: "))
    if (food_option == 0): #Si al usuario no le gusta el menú, selecciona cero. Si ingresar 0, el break terminará con el ciclo.
        break
    elif(food_option == 1):  #Por cada opción elegida, guardamos su pedido como string en la variable "order" y sumamos los precios en la variable "money".
        order = order + " Pizza muzzarella individual  + Botella de agua -"
        money = money + 1500
    elif(food_option == 2):
        order = order + " Hamburguesa de carne  + Botella de agua -"
        money = money + 2000
    elif(food_option == 3):
        order = order + " Milanesa de pollo con papas fritas  + Botella de agua -"
        money = money + 2000
    elif(food_option == 4):
        order = order + " Spaghetti con salsa bolognesa  + Botella de agua -"
        money = money + 2500
    elif(food_option == 5):
        order = order + " Calabaza rellena con queso, pimientos y cebolla  + Botella de agua -"
        money = money + 2500
    else:   #Si la opción ingresada no es válida, se le pedirá al usuario que ingrese un número válido.
        print("Error. Ingrese un número válido.")

if (food_option == 0):  #Si el usuario decidió salir del menú sin ordenar, le mostramos un mensaje de despedida.
    print("Lamentamos que no le gustaran nuestras opciones.")
    print("Esperamos que vuelva pronto.")
else: #Si el usuario hizo un pedido, le agradeceremos, le mostraremos su pedido en pantalla y el precio del pedido.
    print("Gracias por pedir en nuestro local.")
    print(f"Su pedido: {order}")
    print(f"El costo de total de su pedido es de ${money}")
    
