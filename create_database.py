import mysql.connector

def create_db(db_name):
    db = mysql.connector.connect(
            #host="localhost",
            user="root",
            password="",
        )
    cursor= db.cursor()
    lista = []
    if db_name == 'db_example':
        query1 = f"drop database if exists {db_name};"
        lista.append(query1)
        query2 = f"create database {db_name};"
        lista.append(query2)
    else: 
        query3 = f"create database if not exists {db_name};"
        lista.append(query3)
            
    query4 = f"use {db_name};"
    lista.append(query4)
    query5 = f"""create table if not exists persona(
                        dni int unsigned not null,
                        nombre_apellido varchar(50) not null,
                        telefono bigint,
                        direccion varchar(50) not null,
                        correo varchar(50),
                        primary key(dni)
                    )"""
    lista.append(query5)
    query6 = f""" create table if not exists producto(
                        IDProducto int unsigned auto_increment not null,
                        tipo varchar(50) not null,
                        marca varchar(50) not null,
                        modelo varchar(50) not null,
                        descripcion text,
                        precio decimal(6,2) unsigned,
                        stock int unsigned not null,
                        primary key(IDProducto)
                    );"""
    lista.append(query6)
    query7 = f"""create table if not exists pedido(
                        IDPedido int unsigned auto_increment not null,
                        dni int unsigned not null,
                        primary key(IDPedido),
                        foreign key(dni) references persona(dni)
                    );"""
    lista.append(query7)
    query8 = f"""create table if not exists subpedido(
                        IDSubpedido int unsigned auto_increment not null,
                        cantidad int unsigned not null,
                        IDPedido int unsigned not null,
                        IDProducto int unsigned not null,
                        primary key(IDSubpedido),
                        foreign key(IDPedido) references pedido(IDPedido),
                        foreign key(IDProducto) references producto(IDProducto)
                    );"""
    lista.append(query8)
    for i in lista:
        cursor.execute(i)
        db.commit()
    
    if db_name == 'db_example':
        objetos = [
            ('Notebook', 'Lenovo', 'Thinkpad', 'Rapida y confiable', 25.5, 4),
            ('Mouse', 'Exxo', 'Ex3', 'Con botones', 2.9, 8),
            ('Monitor', 'HP', 'HP serie 200', '23" widescreen', 13.5, 2),
            ('Notebook', 'Asus', 'X', 'Solida y duradera', 32.8, 6),
            ('Mouse', 'Lenovo', 'XT30', 'Ergonomico', 3.5, 10),
            ('Teclado', 'Lenovo', 'XT40', 'Con luces', 3.8, 14),
            ('Notebook', 'Exxo', 'Eso', 'Muy vendida', 18.8, 10),
            ('Monitor', 'BGH', 'B150', '23" economico', 16.2, 5)
        ]
        for i in objetos:
            cursor.execute(f"""insert into producto(tipo, marca, modelo, descripcion, precio, stock) values{i};""")
            db.commit()
        cursor.execute(f"""insert into persona(dni, nombre_apellido, telefono, direccion, correo) values (32132647 ,"Pedro Sanchez",2364251426, "Av. Del Carmen 502","Pepitojohnson@eso.com");""")
        db.commit()
    cursor.close()
    db.close()
    return 1
    