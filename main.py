from typing import Optional
import pandas as pd
from pandasql import sqldf
from fastapi import FastAPI,Query

#cargando los datos finales
data=pd.read_csv("datfinal.csv")

app= FastAPI()

@app.get("/")
def index():
    """funcion que retorna la informacion en la pagina de inicio"""

    return f"Bienvenido a la aplicación para realizar consultas sobre los servicios de streaming \n ir a 'url-actual'/docs para la interfaz intereactiva"




@app.get("/get_max_duration")
def get_max_duration(year:Optional[str]=Query("'%'"),
                     platform:Optional[str]=Query("'%'"),
                     duration_type:Optional[str]=Query("'%'")):
    """la funcion recibe como parametros opcionales año,plataforma o tipo de duracion y retorna
        la pelicula con mayor duracion
        ACLARACION:min o season van entre comillas"""
    
    if platform=="netflix":
        platform="'n%'"
    elif platform=="amazon":
        platform="'a%'"
    elif platform=="hulu":
        platform="'h%'"
    elif platform=="disney":
        platform="'d%'"

    query=f"SELECT title,MAX(duration_int),duration_type FROM data WHERE id LIKE {platform} AND release_year LIKE {year} AND duration_type LIKE {duration_type}"
    
    result=sqldf(query)
    final_result=f"La pelicula de mayor duracion es {result.iloc[0,0]} con una duracion de {result.iloc[0,1]} {result.iloc[0,2]}"
    return final_result

@app.get("/get_score_count")
def get_score_count(platform:str,score:float,year:int):
    """la funcion recibe plataforma de streaming,año y puntaje del cual se busca
        la cantidad de peliculas con un puntaje mayor al indicado"""
    if platform=="netflix":
        platform="'n%'"
    elif platform=="amazon":
        platform="'a%'"
    elif platform=="hulu":
        platform="'h%'"
    elif platform=="disney":
        platform="'d%'"
    
    query=f"SELECT score,COUNT(*) AS cantidad_de_peliculas FROM data WHERE id LIKE {platform} AND release_year={year} AND score >{score}"
    response=sqldf(query)
    finalresponse=f"la cantidad de peliculas con un score mayor a {score} es {response.iloc[0,1]}"
    
    return finalresponse

@app.get("/get_count_platform")
def get_count_platform(platform:str):
    if platform=="netflix":
        platform="'n%'"
    elif platform=="amazon":
        platform="'a%'"
    elif platform=="hulu":
        platform="'h%'"
    elif platform=="disney":
        platform="'d%'"

    query=f"SELECT COUNT(*) AS cantidad_de_peliculas FROM data WHERE id LIKE {platform}"
    response=sqldf(query)

    return f"El servicio de streaming contiene {response.iloc[0,0]} títulos"

@app.get("/get_actor")
def get_actor(platform:str,year:int):
    """la funcion devuelve la cantidad de veces que aparece un actor segun la plataforma
       y año indicados en la query"""
    if platform=="netflix":
        platform="'n%'"
    elif platform=="amazon":
        platform="'a%'"
    elif platform=="hulu":
        platform="'h%'"
    elif platform=="disney":
        platform="'d%'"
    
    query=f"SELECT casting FROM data WHERE id LIKE {platform} AND release_year={year}"
    platform=sqldf(query)
    dfactor=platform.casting.str.split(",")
    dic={}
    for x in range(dfactor.shape[0]):
        if dfactor.iloc[x]==None:
            pass
        else:
            for actor in dfactor.iloc[x]:
                actorws=actor.strip()
                if actorws in dic:
                    dic[actorws] +=1
                else:
                    dic[actorws]=1
    try:
        finalresponse=f"El actor que mas veces se repite es {max(dic, key=dic.get)} con apariciones en {dic[max(dic, key=dic.get)]} titulos"
    except:
        finalresponse="error en la base de datos"
    
    return finalresponse
    
    
