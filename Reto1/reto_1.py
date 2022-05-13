#Desarrollo reto 1
#Definicon de funcion
def CDT(u,c,t):
  valorIntereses = (c*0.03*t)/12
  valorPerder = c * 0.02

  if t > 2:
    valorTotal = c + valorIntereses
    
  else:
    valorTotal = c-valorPerder

  c = str(c)
  t = str(t)
  valorTotal = str(valorTotal)
  respuesta = "Para el usuario "+ u + " La cantidad de dinero a recibir, segun el monto inicial " + c + " para un tiempo de " + t + " meses es: " + valorTotal
  return respuesta

#Codigo principal
usuario = input("Ingrese su usuario: ")
capital = int(input("Ingrese el monto del capital: "))
tiempo = int(input("Ingrese el tiempo en meses que desea guardar el capital: "))
respuesta = CDT(usuario,capital,tiempo)
print(respuesta)