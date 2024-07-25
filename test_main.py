import pytest
import mysql.connector
from CRUD import (read, create, delete, update, solicitar_pedido, ver_stock, registrar_persona, 
                  registrar_producto, buscar_persona, buscar_producto, consultar_pedido, eliminar_pedido, 
                  ver_personas, actualizar_persona, actualizar_producto)
from create_database import create_db

#Comando para testear: pytest "test_archivo.py" 
#Comando para evaluar la cobertura: coverage run -m pytest -v "test_main.py"
#Comando para ver el informe de la cobertura: coverage report -m  
#Comando para generar el informe de cobertura en html: coverage html 

def test_create_db_example():
    cnx = mysql.connector.connect(user='root')
    cnx.cursor().execute("drop database if exists db_example")
    cnx.close()
    assert create_db('db_example') == 1
    
@pytest.fixture(scope='module')
def connection():
    cnx = mysql.connector.connect(user='root', database='db_example')
    yield cnx
    cnx.close()
    
    
class TestDatabase_operations:
    @pytest.fixture(autouse=True)
    def cursor_use(self,connection):
        self.cursor = connection.cursor()
        connection.start_transaction()
        yield 
        connection.commit()
        self.cursor.close()

        
    @pytest.mark.parametrize("test_input1, test_input2, expected",
                            [("persona(dni, nombre_apellido, telefono, direccion, correo)", "320124230 ,'Mario Luis', 12332423, 'algo 123', 'algo@algo.com'", None),
                             ("non_exist(eso)", "pescado",0)])
    def test_create(self, test_input1, test_input2, expected):
        assert create(self.cursor, test_input1, test_input2) == expected
        
    @pytest.mark.parametrize("test_input1, test_input2, test_input3, expected",
                            [("*", "persona","",(320124230, 'Mario Luis', 12332423, 'algo 123', 'algo@algo.com'))])  
    def test_read(self, test_input1, test_input2, test_input3, expected):
        assert read(self.cursor, test_input1, test_input2, test_input3)[-1] == expected

    @pytest.mark.parametrize("test_input1, test_input2, test_input3, test_input4, test_input5, expected", 
                            [("persona", "telefono", "12332432", "dni", 32132647, None)])
    def test_update(self, test_input1, test_input2, test_input3, test_input4, test_input5, expected):
        assert update(self.cursor, test_input1, test_input2, test_input3, test_input4, test_input5) == expected
 
    @pytest.mark.parametrize("test_input1, test_input2, test_input3, expected",
                            [("persona", "dni", "320124230", None)])  
    def test_delete(self,test_input1, test_input2, test_input3, expected):
        assert delete(self.cursor, test_input1, test_input2, test_input3) == expected
        
    def test_solicitar_pedido(self):
        assert solicitar_pedido(self.cursor, 32132647, ((1,5),(6,2),(7,1))) == 0     #Se pide mas que el stock disponible
        assert solicitar_pedido(self.cursor, 32132632, ((2,3),(6,2),(7,1))) == 0     #Test DNI faltante
        assert solicitar_pedido(self.cursor, 32132647, ((2,3),(6,2),(7,1))) == 1     #Test que verifica 
        self.cursor.execute("select IDPedido from pedido")
        ID = self.cursor.fetchall()[-1][0]
        print(ID)
        eliminar_pedido(self.cursor, 32132647, ID)

    def test_ver_stock(self):
        assert str(ver_stock(self.cursor)[0]) == "(1, 'Notebook', 'Lenovo', 'Thinkpad', 'Rapida y confiable', Decimal('25.50'), 4)"

    def test_registrar_persona(self): 
        assert registrar_persona(self.cursor, 43234932, 'Tomas Perez', 243439289, 'Juarez 325', 'Tomip.25@hotmail.com') == None
        delete(self.cursor, "persona", "dni", 43234932)

        
    def test_registrar_producto(self): 
        assert registrar_producto(self.cursor, 'Gabinete', 'Gamermax', 'Infinity Black', 'Robusto para placas grandes', 10.2, 15) == None 
        self.cursor.execute("SELECT LAST_INSERT_ID();")      #PARA OBTENER EL ULTIMO ID USO: SELECT LAST_INSERT_ID();
        IDProducto = self.cursor.fetchone()[0]
        delete(self.cursor, "producto", "IDProducto", IDProducto)
        
    def test_buscar_persona(self):
        assert buscar_persona(self.cursor, 32452432) == []
        assert buscar_persona(self.cursor, 32132647) == [(32132647, 'Pedro Sanchez', 12332432, 'Av. Del Carmen 502','Pepitojohnson@eso.com')]

    def test_buscar_producto(self):
        assert str(buscar_producto(self.cursor, 'Lenovo', 'Thinkpad')) == "[(1, 'Notebook', 'Lenovo', 'Thinkpad', 'Rapida y confiable', Decimal('25.50'), 4)]"
        assert buscar_producto(self.cursor, 'HP', 'HP serie 201') == []
        
    def test_consultar_pedido(self):
        solicitar_pedido(self.cursor, 32132647, ((2,3),(6,2),(7,1)))
        self.cursor.execute("select IDPedido from pedido")
        ID = self.cursor.fetchall()[-1][0]
        assert consultar_pedido(self.cursor, 39482394) == 0
        assert str(consultar_pedido(self.cursor, 32132647)) == "[(2, 1, 'Exxo', 'Eso', Decimal('18.80'), Decimal('18.80')), (2, 2, 'Lenovo', 'XT40', Decimal('3.80'), Decimal('7.60')), (2, 3, 'Exxo', 'Ex3', Decimal('2.90'), Decimal('8.70'))]"
        eliminar_pedido(self.cursor, 32132647, ID)
    
    def test_eliminar_pedido(self):
        dni = 32132647
        pedido = ((4, 1),(6, 2))
        solicitar_pedido(self.cursor, dni, pedido)
        self.cursor.execute("select IDPedido from pedido")
        ID = self.cursor.fetchall()[-1][0]
        assert eliminar_pedido(self.cursor, 32132647, 1345) == 0
        assert eliminar_pedido(self.cursor, 65432562, ID) == 0
        assert eliminar_pedido(self.cursor, 32132647, ID) == 1
        
    def test_ver_personas(self):
        registrar_persona(self.cursor, 43234932, 'Tomas Perez', 243439289, 'Juarez 325', 'Tomip.25@hotmail.com')
        assert ver_personas(self.cursor) == [(32132647 ,"Pedro Sanchez",12332432, "Av. Del Carmen 502","Pepitojohnson@eso.com"),
                     (43234932, 'Tomas Perez', 243439289, 'Juarez 325', 'Tomip.25@hotmail.com')]
        
    def test_actualizar_persona(self):
        actualizar_persona(self.cursor, "telefono", 22314521, 32132647)
        assert buscar_persona(self.cursor, 32132647)[0][2] == 22314521

    
    def test_actualizar_producto(self):
        actualizar_producto(self.cursor, "descripcion", "'La mejor del mercado'", 4) #SI ES STR VA CON DOBLE COMILLA
        assert buscar_producto(self.cursor, "Asus", "X")[0][4] == "La mejor del mercado"