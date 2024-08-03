<h1 align="center"> BusinessApp </h1>

## Descripción del Proyecto 
El proyecto consiste en la creación de una aplicación para comercios, con una interfaz grafica simple. Se centra en la administración de las ventas por medio de la gestión de una base de datos que registra clientes, productos y pedidos. 

## Características 
<ul>
    <li>La aplicación se comunica a través de métodos CRUD con una base de datos de tipo relacional utilizando la librería mysql</li>
    <li>Consta de una interfaz gráfica simple desarrollada utilizando la libreria Tkinter</li>
    <li>Se realizaron tests unitarios utilizando la libreria pytest</li>
    <li>Se testeo el funcionamiento de la interfaz grafica utilizando la libreria pyautogui</li>
</ul>

## Estado del proyecto 
:heavy_check_mark:Lanzamiento de la versión inicial

## Pre-requisitos 📋
<br>El proyecto fue desarrollado en lenguaje Python, por lo cual primero deberá tenerlo instalado. [Python](https://www.python.org/downloads/)<br>

<br>Luego deberá instalar las librerías correspondientes, para ello podra optar por instalarlas manualmente (las mismas se encuentran en el archivo requirements.txt) o abrir la consola en la ubicacion del proyecto y correr el siguiente comando
``` 
pip install -r requirements.txt
```
<br>Para poder ejecutar el proyecto deberá correr un servidor MySQL. Para probar la aplicación puede crear un servidor local utilizando Wampserver o algun otro servicio para ejecutar servidores.<br>

## 📁 Acceso al proyecto y ejecución 🛠️
<br>Para poder acceder al codigo, clone el repositorio de GitHub ejecutando la siguiente linea en consola<br>
``` 
git clone https://github.com/VittorioCostanzi/BusinessApp.git
```

<br>En caso de querer probar la aplicación se puede utilizar una base de datos de ejemplo proporcionada en el codigo. <br>
En el siguiente fragmento del script interfaz.py deberá utilizar la base de datos 'db_example'<br>
```
bbdd = "base_de_datos"

create_db(bbdd)

cnx = mysql.connector.connect(user='root', database=bbdd) #root es el usuario por defecto
cursor = cnx.cursor()
```

<br>Para modificar los datos de acceso al servidor podra modificar el siguiente fragmento del script create_database.py con los datos del servidor a utilizar<br>
```
def create_db(db_name):
    db = mysql.connector.connect(
            #host="localhost",
            user="root",
            password="",
        )
```

<br>Una vez iniciado el servidor, para iniciar la app ejecute el script interfaz.py 

```
python interfaz.py
```

## 🧪 Testeo de la Aplicación
Para garantizar el correcto funcionamiento de la aplicación, se realizaron diferentes tipos de tests
Para ejecutar los tests, asegúrese de que el servidor MySQL esté corriendo y que las dependencias estén instaladas<br>
### Tests Unitarios
Los tests unitarios se realizaron utilizando la librería pytest. Para ejecutarlos, puede utilizar el siguiente comando en la consola, ubicado en el directorio del proyecto
```
coverage run -m pytest -v "test_main.py"
```
<br>Se podra visualizar la cobertura de los tests ejecutando la siguiente linea en consola 
```
coverage report "test_main.py"
```
### Tests de la Interfaz Gráfica
> [!CAUTION]
> Cuando corra el test de la interfaz grafica, asegurese de tener instaladas todas las dependencias y la base de datos funcionando.
> Utilice la base de datos 'db_example' para realizar el testeo de la interfaz gráfica.
> Como verificación adicional, corra la aplicación previo al testeo y asegurese que funcione. De lo contrario podria tener problemas dado que la metodología utilizada para testear la interfaz gráfica controla el teclado y el mouse mientras se ejecuta el test.

El funcionamiento de la interfaz gráfica se testeó utilizando la librería pyautogui. Estos tests aseguran que los componentes de la interfaz respondan correctamente a las acciones del usuario, por lo cual la verificación es visual. Para ejecutarlos, puede utilizar el siguiente comando en la consola, ubicado en el directorio del proyecto. 
```
python "test_interfaz_auto.py"
```

