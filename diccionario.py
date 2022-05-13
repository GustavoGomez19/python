notas = {}
notas ["nombre"]= input("Ingrese su nombre: ")
notas ["apellido"]= input("Ingrese su apellido: ")
notas ["cedula"]= int(input("Ingrese su nímero de cedula: "))
notas ["reto1"]= float(input("ingrese la nota del reto 1:"))
notas ["reto2"]= float(input("ingrese la nota del reto 2:"))
notas ["reto3"]= float(input("ingrese la nota del reto 3:"))
notas ["reto4"]= float(input("ingrese la nota del reto 4:"))
notas ["reto5"]= float(input("ingrese la nota del reto 5:"))
notas ["notaFinal"]= (notas["reto1"]+notas["reto2"]+notas["reto3"]+notas["reto4"]+notas["reto5"])/5
print("El promedio de la nota final es: ",notas["notaFinal"])