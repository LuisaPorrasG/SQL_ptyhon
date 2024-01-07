import sqlite3
import pandas as pd
square = lambda n : n*n #funcion lamba como funcion flecha
 
#metodo 2 de uso de conexion a base de datos

with sqlite3.connect ("Northwind.db") as conn:
    conn.create_function ("square", 1, square)
    cursor = conn.cursor()
    cursor.execute('SELECT *, square(Price) FROM Products WHERE Price >0') #hago uso de la funcion square que habia definido
    results = cursor.fetchall() # igual me devuelve los datos de una manera primitiva, es decir como datos separados por  ,
    results_df= pd.DataFrame(results)#conviero a data frame de manera masa estetica
    
    print(results_df)
    
    #con el with la ventaja es qe la conexion se cierra automaticamente
    