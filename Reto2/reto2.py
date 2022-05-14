#Clase 11/05/2022
#Temas: Desarrollo reto 2 - Diccionarios
#En los diccionarios se definen con las llave {}, los elementos vienen en parejas, el primer elemento es la llave y el segundo es el elemento asociado van separados por (:)
#No se pueden duplicar las llaves, pero si los elementos asociados
#Para acceder a un allave del diccionario se usan los [] y el nombre de la llave, ya sea para modificar su elemento asociado.
#Para crear una nueva llave se llama el diccionario seguido de los [] y se agrega la nueva llave con su valor asociado
#dicc1={
#  "marca": "Ford",
#  "modelo": "Mustang",
#  "annio": 1964
#}
#print(dicc1)
#dicc1["color"]="rojo"
#print(dicc1)

def cliente(d):
  
  diccionario={}
  diccionario["nombre"]=d["nombre"]
  diccionario["edad"]=d["edad"]

#Atracciones
  if d["edad"]>18:
    diccionario["atraccion"]="x-treme"
    diccionario["apto"]=True
    diccionario["primer_ingreso"]=d["primer_ingreso"]

  if d["edad"]>=15 and d["edad"]<=18:
    diccionario["atraccion"]="Carroschocones"
    diccionario["apto"]=True
    diccionario["primer_ingreso"]=d["primer_ingreso"]

  if d["edad"]>=7 and d["edad"]<=15:
    diccionario["atraccion"]="Sillas voladoras"
    diccionario["apto"]=True
    diccionario["primer_ingreso"]=d["primer_ingreso"]

#Precio entradas
  if d["edad"]>18 and d["primer_ingreso"]==True:
    diccionario["total_boleta"]=20000*.95

  if d["edad"]>18 and d["primer_ingreso"]==False:
    diccionario["total_boleta"]=20000

  if d["edad"]>=15 and d["edad"]<=18 and d["primer_ingreso"]==True:
    diccionario["total_boleta"]=5000*.93

  if d["edad"]>=15 and d["edad"]<=18 and d["primer_ingreso"]==False:
    diccionario["total_boleta"]=5000

  if d["edad"]>=7 and d["edad"]<=15 and d["primer_ingreso"]==True:
    diccionario["total_boleta"]=10000*.95

  if d["edad"]>=7 and d["edad"]<=15 and d["primer_ingreso"]==False:
    diccionario["total_boleta"]=10000

  if d["edad"]<7:
    diccionario["atraccion"]="N/A"
    diccionario["apto"]=False
    diccionario["primer_ingreso"]=True
    diccionario["total_boleta"]="N/A"



  return diccionario

#Codigo ppal
dic1={"id_cliente":1,"nombre":"Johana Fernandez","edad":20,"primer_ingreso":True}
dic2={"id_cliente":1,"nombre":"Johana Fernandez","edad":20,"primer_ingreso":False}
dic3={"id_cliente":2,"nombre":"Gloria Suarez","edad":3,"primer_ingreso":True}
dic4={"id_cliente":3,"nombre":"Tatiana Suarez","edad":17,"primer_ingreso":True}
dic5={"id_cliente":3,"nombre":"Tatiana Suarez","edad":17,"primer_ingreso":False}
dic6={"id_cliente":4,"nombre":"Tatiana Ruiz","edad":8,"primer_ingreso":True}
dic7={"id_cliente":4,"nombre":"Tatiana Ruiz","edad":8,"primer_ingreso":False}

print(cliente(dic1))
print(cliente(dic2))
print(cliente(dic3))
print(cliente(dic4))
print(cliente(dic5))
print(cliente(dic6))
print(cliente(dic7))