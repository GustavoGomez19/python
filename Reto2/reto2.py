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
  if d["edad"]>18:
    diccionario["atraccion"]="x-treme"
  if d["edad"]>=15 and d["edad"]<=18:
    diccionario["atraccion"]="Carros chocones"
  if d["edad"]>=7 and d["edad"]<15:
    diccionario["atraccion"]="Sillas voladoras"
  if d["edad"]<7:
    diccionario["atraccion"]="N/A"
  if d["apto"]:
    diccionario["apto"]=True
  diccionario["apto"]=d["apto"]
  if d["primer_ingreso"]:
    diccionario["primer_ingreso"]=True
  diccionario["primer_ingreso"]=d["primer_ingreso"]


  return diccionario

#Codigo ppal
dic1={"id_cliente":1,"nombre":"Johana Fernandez","edad":20,"primer_ingreso":True,"apto":True,}
print(cliente(dic1))