import mysql.connector

#OPERACIONES CRUD

def create(cursor, tabla, values):
  
    cursor.execute(f"insert into {tabla} values ({values})")

def read(cursor, parametros, tabla, where):
  
    cursor.execute(f"select {parametros} from {tabla} {where}")

    resultado = [data for (data) in cursor]
    print(resultado)
    return resultado

def delete(cursor, tabla, variable, valor):
  
    cursor.execute(f"delete from {tabla} where {variable} = {valor};") #Modificar, el primer dni debe ser la variable de tabla a modificar, el segundo el valor asignado

def update(cursor, tabla, parametro, modificacion, parametro_condicion, valor_condicion):
    
    cursor.execute(f"update {tabla} set {parametro} = {modificacion} where {parametro_condicion} = {valor_condicion};")

#REGISTRAR UN NUEVO PRODUCTO

def registrar_producto(cursor, tipo, marca, modelo, descripcion, precio, stock):
    create(cursor, "producto(tipo, marca, modelo, descripcion, precio, stock)", f"'{tipo}', '{marca}', '{modelo}', '{descripcion}', {precio}, {stock}")
    
#REGISTRAR UNA NUEVA PERSONA

def registrar_persona(cursor, dni, nombre_apellido, telefono, direccion, correo):
    create(cursor, "persona(dni, nombre_apellido, telefono, direccion, correo)", f"{dni}, '{nombre_apellido}', {telefono}, '{direccion}', '{correo}'")

#VERIFICAR SI UNA PERSONA SE ENCUENTRA REGISTRADA

def buscar_persona(cursor, dni):
    return read(cursor, "*", "persona", f"where dni = {dni}")
   
    
#VERIFICAR SI UN PRODUCTO SE ENCUENTRA REGISTRADO

def buscar_producto(cursor, marca, modelo):
    return (read(cursor, "*", "producto", f"where marca = '{marca}' AND modelo = '{modelo}'"))

#REALIZAR UN PEDIDO

def solicitar_pedido(cursor, dni, tupla_listado): #La tupla debera ingresarse como pares (IDProducto, cantidad)
    
    if len(buscar_persona(cursor, dni)) == 0:
        return 0
    else:
        for prod_cant in tupla_listado:
            cursor.execute(f"select (p.stock - ifnull(s.cantidad,0)) from producto as p left join subpedido as s on p.IDProducto = s.IDProducto where p.IDProducto = {prod_cant[0]};")
            
            if prod_cant[1] > cursor.fetchone()[0]:
                return 0
        create(cursor, 'pedido(dni)', dni)
        cursor.execute("SELECT LAST_INSERT_ID();")      #PARA OBTENER EL ULTIMO ID USO: SELECT LAST_INSERT_ID();
        IDPedido = cursor.fetchone()[0]       
        
        for prod_cant in tupla_listado:    
            create(cursor, 'subpedido(cantidad, IDPedido, IDProducto)', f"{prod_cant[1]}, {IDPedido}, {prod_cant[0]}")
        return 1

#BUSCAR UN PEDIDO
def consultar_pedido(cursor, dni):
    if len(read(cursor, "*", "pedido", f"where dni = {dni}")) == 0:
        return 0
    else:
        cursor.execute(f"select s.IDPedido, s.cantidad, prod.marca, prod.modelo, prod.precio as costo_unitario, s.cantidad*prod.precio as costo from subpedido as s left join pedido as ped on s.IDPedido = ped.IDPedido left join producto as prod on s.IDProducto = prod.IDProducto where ped.dni = {dni}")
        return cursor.fetchall()
    
#ELIMINAR UN PEDIDO
def eliminar_pedido(cursor, dni, id_pedido): #La tupla debera ingresarse como pares (IDProducto, cantidad)
    cursor.execute("select IDPedido from pedido")
    if id_pedido not in [i[0] for i in cursor.fetchall()]: 
            return 0
    if consultar_pedido(cursor, dni) == 0: #delete(cursor, tabla, variable, valor):
        return 0
    else:
        delete(cursor, "pedido", "IDPedido", id_pedido)
        delete(cursor, "subpedido", "IDPedido", id_pedido)
        return 1
    
#VER EL STOCK DISPONIBLE
def ver_stock(cursor):
    return read(cursor, "p.IDProducto, p.tipo, p.marca, p.modelo, p.descripcion, p.precio, (p.stock - ifnull(s.cantidad,0))", "producto", "as p left join subpedido as s on p.IDProducto = s.IDProducto")

#VER LISTA DE PERSONAS REGISTRADAS
def ver_personas(cursor):
    return read(cursor, "*", "persona", "")

def actualizar_persona(cursor, parametro, modificacion, dni):
    update(cursor, "persona", parametro, modificacion, "dni", dni)
    return 

def actualizar_producto(cursor, parametro, modificacion, IDProducto):
    update(cursor, "producto", parametro, modificacion, "IDProducto", IDProducto)
 

"""def actualizar_pedido(cursor):
    update(cursor, tabla, parametro, modificacion, parametro_condicion, valor_condicion)
    return """


        #FALTA:
        # Update pedidos




#CONEXIÓN A BASE DE DATOS


# cnx = mysql.connector.connect(user='root', database='db_example') #root es el usuario por defecto
# cursor = cnx.cursor()
# cursor.close()
# cnx.close()

