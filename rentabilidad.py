import sqlite3
import pandas as pd #libreria para visualización de datos mas estetica
import matplotlib.pyplot as plt #libreria para graficas de datos
#CONSULATA PARA OBTENER LOS 10 PRODUCTOS MAS RENTABLES
conn= sqlite3.connect("Northwind.db")
query = (
    '''
    SELECT ProductName, SUM(price * Quantity) as Revenue
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
    '''
)

top_products = pd.read_sql_query(query, conn) #es como si fura un cursor pero es una función de pandas ya definida
#print(top_products)
top_products.plot(x = "ProductName", y = "Revenue", kind= "bar", figsize=(10,5), legend=False) #configuración del diagrama

plt.title("10 Productos Más Rentables")
plt.xlabel("Products")#nombre del eje x
plt.ylabel("Revenue") #nombre del eje y 
plt.xticks(rotation=90) #rota carios nombres del eje x para que no se amontonen
plt.show()

#OBTENIENDO LOS 10 EMPPLEADOS MAS RENTABLES

query2 =(
    '''
    SELECT FirstName || " "  || LastName as Employee, COUNT(*) as Total
    FROM Orders as o
    JOIN Employees e
    ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY  Total DESC    
    LIMIT 10
    '''
)

top_employees = pd.read_sql_query(query2, conn)
top_employees.plot(x= "Employee", y= "Total", kind="bar", figsize=(10,5), legend=False) #creo un grafico
plt.title("10 Empleados más efectivos")
plt.xlabel("empleados")
plt.ylabel("Total Vendido")
plt.xticks(rotation = 45)
plt.show()
