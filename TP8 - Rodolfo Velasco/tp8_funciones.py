#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#EJERCICIO 1

def counting_digits(number):
    counter = 0
    number = str(number)
    if (len(number) <= 1):
        counter = counter + 1
        return counter
    else:
        counter = counter + 1
        return counter + counting_digits(int(number[:-1]))


#EJERCICIO 2

def power(n,b):
    if(n==b):
        return True
    elif((n%b)!=0):
        return False
    else:
        return power((n/b),b)


#EJERCICIO 3

def find_in (body_, sample_, start_, answer_list_):
    aux = body_.find(sample_,start_)
    if aux != -1:
      answer_list_.append(aux)
      find_in(body_,sample_,(aux + len(sample_)),answer_list_)
    return answer_list_


#EJERCICIO 4

def odd(number):
    if number==1:
        return "impar"
    elif(even(number-1)=="par"):
        return "impar"
    else:
        return even(number)    

def even(number):
    if (number==1):
        return odd(number)
    elif (odd(number-1)=="impar"):
        return "par"
    else:
        return odd(number)  


#EJERCICIO 5

def max_list(list, pos = 0, max = 0):
   if pos > len(list) - 1:
      print(f"El mayor numero de la lista es: {max}")
   else:
      if list[pos] > max: max_list(list, pos + 1, list[pos])
      else: max_list(list, pos + 1, max)


#EJERCICIO 6

def repeat(list, length, new_list = [], count = 0, pos = 0):
   if pos > len(list) - 1:
      print(f"Nuevo Arreglo: {new_list}")
   else:
      if count < length:
         new_list.append(list[pos])
         repeat(list, length, new_list, count + 1, pos)
      else:
         repeat(list, length, new_list, 0, pos + 1)


#EJERCICIO 7

def sumatory(number, count):
   if count == 1: return number + 2
   else:
      return number + count * sumatory(number, count - 1)


#EJERCICIO 8

def pascal(n, k):
    if (n==k):
        return 1
    elif(n==0):
        return 1
    else:
        return pascal(n-1,k-1)+pascal(n,k-1)


#EJERCICIO 9

def combinations(lista, k, aux=""):
    if k == 0:
        print(aux)
        return

    for character in lista:
        combinations(lista, k - 1, aux + character)


#EJERCICIO 10

def sheet_measurements(n, h = 841, w = 1189):
   if n == 0: 
      return (h, w)
   else: 
      aux = w
      w = h
      h = aux
      return sheet_measurements(n - 1, round(h / 2), w)







