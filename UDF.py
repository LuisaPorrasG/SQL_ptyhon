import sqlite3 #importo la libreria de conexión o referencia de sqlite
import pandas as pd #importo pandas para usar los datos y darles un formato
#extensión de Pandas     para manipulación y análisis de datos para el lenguaje de programación Python

#FORMA 1
square = lambda n: n*n #lamda es como si fuera una funcion flecha , 
                          #entonces mi codigo seria square = (funcion con argumento n me devuelva n*n)
#print(square(10))
conn = sqlite3.connect("Northwind.db") #realizo la conexion de la base de datos

conn.create_function("cuadrado_square", 1, square) #registro de la funcion square, como la voy a registrar en SQL 
                                                   #puedo ponerle otro nombre
                                                   #(nombre de como lo llamo en sql, numero de argumentos que pido,
                                                   # funcion de python que voy a usar para ejecutar)
cursor = conn.cursor() #la funcion cursos me va almacenar los datos de mi consulta
cursor.execute(
    #aquí puedo escribir el codigo de sql de consultas que voy a usar
    '''
     
    SELECT * FROM Products;
    '''
)                    
results= cursor.fetchall() #resultados va almacenar lo que la función cursor recibio de mi consulta, fetchall me devuelve un listado en duplas
results_dt = pd.DataFrame(results) #resultado de datadrame
#print(results)--> me devuelve los datos como una lista 
cursor.close() #buena practica cerrar el cursor de la consulta
conn.close() #cierro la conexion a la base de datos, de esta forma los recursos que esta usando el computador se detiene y se se vuelve optimo de trabajar
conn.commit() #guardo la información de la base de datos, como un delete u update

print(results_dt) #me devuelve los datos visualmente más bonitos