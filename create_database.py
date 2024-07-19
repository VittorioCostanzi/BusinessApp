import mysql.connector

def create_db(db_name):
    db = mysql.connector.connect(
            #host="localhost",
            user="root",
            password="",
            #database="mydatabase"
        )
    cursor= db.cursor()
    if db_name == 'db_example':
        query = f"""  
                        drop database if exists {db_name};
                        create database {db_name};
                        
                        use {db_name};
                        
                        create table if not exists persona(
                            dni int unsigned not null,
                            nombre_apellido varchar(50) not null,
                            telefono bigint,
                            direccion varchar(50) not null,
                            correo varchar(50),
                            primary key(dni)
                        );

                        create table if not exists producto(
                            IDProducto int unsigned auto_increment not null,
                            tipo varchar(50) not null,
                            marca varchar(50) not null,
                            modelo varchar(50) not null,
                            descripcion text,
                            precio decimal(6,2),
                            stock int unsigned not null,
                            primary key(IDProducto)
                        );

                        create table if not exists pedido(
                            IDPedido int unsigned auto_increment not null,
                            dni int unsigned not null,
                            primary key(IDPedido),
                            foreign key(dni) references persona(dni)
                        );

                        create table if not exists subpedido(
                            IDSubpedido int unsigned auto_increment not null,
                            cantidad int unsigned not null,
                            IDPedido int unsigned not null,
                            IDProducto int unsigned not null,
                            primary key(IDSubpedido),
                            foreign key(IDPedido) references pedido(IDPedido),
                            foreign key(IDProducto) references producto(IDProducto)
                        );


                        insert into persona(dni, nombre_apellido, telefono, direccion, correo) values (32132647 ,"Pedro Sanchez",2364251426, "Av. Del Carmen 502","Pepitojohnson@eso.com");

                        insert into producto(tipo, marca, modelo, descripcion, precio, stock) values('Notebook', 'Lenovo', 'Thinkpad', 'Rapida y confiable', 25.5, 4);
                        insert into producto(tipo, marca, modelo, descripcion, precio, stock) values('Mouse', 'Exxo', 'Ex3', 'Con botones', 2.9, 8);
                        insert into producto(tipo, marca, modelo, descripcion, precio, stock) values('Monitor', 'HP', 'HP serie 200', '23" widescreen', 13.5, 2);
                        insert into producto(tipo, marca, modelo, descripcion, precio, stock) values('Notebook', 'Asus', 'X', 'Solida y duradera', 32.8, 6);
                        insert into producto(tipo, marca, modelo, descripcion, precio, stock) values('Mouse', 'Lenovo', 'XT30', 'Ergonomico', 3.5, 10);
                        insert into producto(tipo, marca, modelo, descripcion, precio, stock) values('Teclado', 'Lenovo', 'XT40', 'Con luces', 3.8, 14);
                        insert into producto(tipo, marca, modelo, descripcion, precio, stock) values('Notebook', 'Exxo', 'Eso', 'Muy vendida', 18.8, 10);
                        insert into producto(tipo, marca, modelo, descripcion, precio, stock) values('Monitor', 'BGH', 'B150', '23" economico', 16.2, 5);
                         """
    else:
        query = f"""  
                        create database if not exists {db_name};
                        
                        use {db_name};
                        
                        create table if not exists persona(
                            dni int unsigned not null,
                            nombre_apellido varchar(50) not null,
                            telefono bigint,
                            direccion varchar(50) not null,
                            correo varchar(50),
                            primary key(dni)
                        );

                        create table if not exists producto(
                            IDProducto int unsigned auto_increment not null,
                            tipo varchar(50) not null,
                            marca varchar(50) not null,
                            modelo varchar(50) not null,
                            descripcion text,
                            precio decimal(6,2),
                            stock int unsigned not null,
                            primary key(IDProducto)
                        );

                        create table if not exists pedido(
                            IDPedido int unsigned auto_increment not null,
                            dni int unsigned not null,
                            primary key(IDPedido),
                            foreign key(dni) references persona(dni)
                        );

                        create table if not exists subpedido(
                            IDSubpedido int unsigned auto_increment not null,
                            cantidad int unsigned not null,
                            IDPedido int unsigned not null,
                            IDProducto int unsigned not null,
                            primary key(IDSubpedido),
                            foreign key(IDPedido) references pedido(IDPedido),
                            foreign key(IDProducto) references producto(IDProducto)
                        );
                         """
    for result in cursor.execute(query, multi=True): 
        pass
    db.commit()
    cursor.close()
    db.close()
    return 1
    