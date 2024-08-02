:construction: Repositorio en construcción :construction:

<h1 align="center"> BusinessApp </h1>

<h2 align="center"> Descripción del Proyecto </h2>
El proyecto consiste en la creación de una aplicación para comercios, con una interfaz grafica simple. Se centra en la administración de las ventas por medio de la gestión de una base de datos que registra clientes, productos y pedidos. 

<h2 align="center"> Características </h2>
- La aplicación se comunica a través de métodos CRUD con una base de datos de tipo relacional utilizando la librería mysql
- Consta de una interfaz gráfica simple desarrollada utilizando la libreria Tkinter
- Se realizaron tests unitarios utilizando la libreria pytest
- Se testeo el funcionamiento de la interfaz grafica utilizando la libreria pyautogui

<h2 align="center"> Estado del proyecto </h2>
:heavy_check_mark:Lanzamiento de la versión inicial

<h2 align="center"></h2>

<h2 align="center">📁 Acceso al proyecto y ejecución 🛠️</h2>

Para poder ejecutar el proyecto deberá correr un servidor MySQL
Para probar la aplicación puede crear un servidor local utilizando Wampserver o algun otro servicio para ejecutar servidores
Para poder acceder al codigo, clone el repositorio de GitHub ejecutando la siguiente linea en consola
```
git clone https://github.com/VittorioCostanzi/BusinessApp.git
```
En caso de querer probar la aplicación se puede utilizar una base de datos de ejemplo proporcionada en el codigo. 
En el siguiente fragmento del script interfaz.py deberá utilizar la base de datos 'db_example'
```
bbdd = "db_example"
```
Para modificar los datos de acceso al servidor podra modificar el siguiente fragmento del script create_database.py con los datos del servidor a utilizar
```
def create_db(db_name):
    db = mysql.connector.connect(
            #host="localhost",
            user="root",
            password="",
        )
```
Una vez iniciado el servidor, para iniciar la app ejecute el script interfaz.py 


