# fesinit :
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

##todo el json
import json
#nose
# Abre el archivo JSON en modo lectura con el parametro "r"
with open('platillos.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)
    
class User(BaseModel):
    name: str
    lastname: str
    age: int

users_list = [User(name = "Alex",lastname="Maturano",age=20),
         User(name ="Nicol",lastname="Zelaya",age=20),
         User(name ="Bernardino",lastname="Vedia",age=20),
         User(name ="Max",lastname="Rodas",age=19)]




@app.get("/")
async def root():
    return "helllo FastAPI"

@app.get("/users")
async def users():
    return users_list

@app.get("/user/{usuario}")
async def user(usuario:str):
    return buscarUsuario(usuario)
    
@app.get("/user/")
async def user(usuario:str):
    return buscarUsuario(usuario)


def buscarUsuario(usuario:str):
    suser = filter(lambda user: user.name == usuario, users_list)
    return list(suser)[0]
    
    
@app.get("/platillos/{platoB}")
async def platillos(platoB:str):
    resultados = []
    for dato in datos:
        if platoB.lower() in dato['nombre'].lower()   and platoB[0].lower()==dato['nombre'][0].lower():  # Ignorar mayúsculas/minúsculas
            resultados.append(dato)
    if resultados==None:
        return "No se encontro nada"
    else:
        return resultados
    