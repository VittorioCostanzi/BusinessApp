from tkinter import *
from tkinter import ttk
import mysql.connector
from CRUD import *
from create_database import create_db

create_db('db_example')

cnx = mysql.connector.connect(user='root', database='db_example') #root es el usuario por defecto
cursor = cnx.cursor()

class Interfaz:

    def __init__(self, root):

        root.title("Database")
        root.geometry("900x460+100+100")
        
        self.persona_var = IntVar()
        self.dni_var = IntVar()
        self.show_text_bpedido = StringVar()
        
        ttk.Label(root, text="Elija una opcion").place(x=70, y=30)
        equis = 50

        #FALTA:
        # Update pedidos
        # Update productos
        
        #Done Done
        Button1 = ttk.Button(root, text="Registrar Persona", command=self.registro_persona, width=20)
        Button1.place(x=equis, y=60)
        #Done Done
        Button2 = ttk.Button(root, text="Registrar Producto", command=self.registro_producto, width=20)
        Button2.place(x=equis, y=90)
        #Done Done
        Button3 = ttk.Button(root, text="Buscar Persona", command=self.busco_persona, width=20)
        Button3.place(x=equis, y=120)
        #Done Done
        Button4 = ttk.Button(root, text="Buscar Producto", command=self.busco_producto, width=20)
        Button4.place(x=equis, y=150)
        #Done Done
        Button5 = ttk.Button(root, text="Generar Pedido", command=self.generar_pedido, width=20)
        Button5.place(x=equis, y=180)
        #Done Done
        Button6 = ttk.Button(root, text="Consultar Pedido", command=lambda:self.busco_pedido(0), width=20)
        Button6.place(x=equis, y=210)
        #Done Done
        Button7 = ttk.Button(root, text="Eliminar Pedido", command=lambda:self.busco_pedido(1), width=20)
        Button7.place(x=equis, y=240)
        #Done Done
        Button8 = ttk.Button(root, text="Ver Stock", command=self.stock, width=20)
        Button8.place(x=equis, y=270)
        #Done Done
        Button9 = ttk.Button(root, text="Ver Personas", command=self.ver_personas, width=20)
        Button9.place(x=equis, y=300)
        #Done Done
        Button10 = ttk.Button(root, text="Actualizar Persona", command=self.actualizar_persona, width=20)
        Button10.place(x=equis, y=330)
        #Done Done
        Button11 = ttk.Button(root, text="Actualizar Producto", command=self.actualizar_producto, width=20)
        Button11.place(x=equis, y=360)
                
        #Done Done
        Button13 = ttk.Button(root, text="Salir", command=self.salir, width=20)
        Button13.place(x=equis, y=410)
       
        x_treeview=200
        y_treeview=60
        width_treeview=650
        height_treeview= 325
    
        self.l = ttk.Treeview(root)
        self.l.place(x=x_treeview, y=y_treeview, width=width_treeview, height=height_treeview)  # Posicionar el Treeview
        
        s = ttk.Scrollbar(root, orient=VERTICAL, command=self.l.yview)
        s.place(x=x_treeview+width_treeview, y=y_treeview, height=height_treeview)  # Posicionar la Scrollbar
        self.l['yscrollcommand'] = s.set
    
    def actualizar_producto(self):
        self.variable_var = StringVar()
        
        ventana9 = Toplevel()
        ventana9.title("Actualizar Producto")
        ventana9.geometry("800x210+150+150")
        ventana9.focus()
        ventana9.grab_set()

        width_treeview=750
        height_treeview= 80
        x_treeview= 20
        y_treeview=80
        self.l_ventana9 = ttk.Treeview(ventana9)
        self.l_ventana9.place(x=x_treeview, y=y_treeview, width=width_treeview, height=height_treeview)  # Posicionar el Treeview
        self.l_ventana9['columns'] = ('ID Producto','Tipo','Marca','Modelo','Descripcion', 'Precio', 'Stock')
        self.l_ventana9.column('#0', width=0, stretch=NO)
        
        s_ventana5 = ttk.Scrollbar(ventana9, orient=VERTICAL, command=self.l.yview)
        s_ventana5.place(x=x_treeview+width_treeview, y=y_treeview, height=height_treeview)  # Posicionar la Scrollbar
        self.l_ventana9['yscrollcommand'] = s_ventana5.set
        
        for colum in self.l_ventana9['columns']:
            width = 100
            self.l_ventana9.column(colum, width=width, anchor='center')
            self.l_ventana9.heading(colum, text=colum)
        
        ttk.Label(ventana9, text="Marca").place(x=20, y=20)
        marca = ttk.Combobox(ventana9, state="readonly", values=read(cursor, "marca", "producto", "group by marca"))
        marca.place(x=80, y=20) 
        ttk.Label(ventana9, text="Modelo").place(x=20, y=50)
        modelo = ttk.Combobox(ventana9, state="readonly", values="")
        modelo.place(x=80, y=50) 
        texto = ttk.Label(ventana9, textvariable=self.show_text_bpedido)
        texto.place(x=230, y=50)
        texto.config(foreground='red')
        
        def parametros_combobox(event=None):
            if marca.get() == "":
                modelo['values'] = ""
            else: 
                modelo['values'] =read(cursor, "modelo", "producto", f"where marca = '{marca.get()}'")
        
        marca.bind("<<ComboboxSelected>>", parametros_combobox)
        
        ttk.Label(ventana9, text="Parametro a modificar").place(x=260, y=20)
        parametro = ttk.Combobox(ventana9, state="readonly", values=('Tipo','Marca','Modelo','Descripcion', 'Precio', 'Stock'))
        parametro.place(x=390, y=20) 
                
        def parametros_combobox2(event=None):
            if parametro.get() == 'Stock':
                self.show_text_bpedido.set("El stock se suma o se resta, use '-' para disminuir el stock")
        parametro.bind("<<ComboboxSelected>>", parametros_combobox2)

        ttk.Label(ventana9, text="Nuevo valor").place(x=570, y=20)
        self.buscar_persona_entry = ttk.Entry(ventana9, justify=LEFT, width=20, textvariable=self.variable_var).place(x=643, y=20)
        def str_int():
            try:
                valor = int(self.variable_var.get())
            except:
                valor = str(self.variable_var.get())
            return valor
        def funcion():
            self.l_ventana9.delete(*self.l_ventana9.get_children())  # Limpiar cualquier dato anterior en el Treeview
            if parametro.get() == "Tipo":
                parametro_modificado = "tipo"
            elif parametro.get() == "Marca":
                parametro_modificado = "marca"
            elif parametro.get() == "Modelo":
                parametro_modificado = "modelo"
            elif parametro.get() == "Descripcion":
                parametro_modificado = "descripcion"
            elif parametro.get() == "Precio":
                parametro_modificado = "precio"
            elif parametro.get() == "Stock":
                parametro_modificado = "stock"
            
            if parametro_modificado == "stock":
                if (int(read(cursor, 'stock', 'Producto', f'where (marca = "{marca.get()}") and (modelo = "{modelo.get()}")')[0][0]) + str_int()) > 0 :          
                    actualizacion = int(read(cursor, 'stock', 'Producto', f'where (marca = "{marca.get()}") and (modelo = "{modelo.get()}")')[0][0]) + str_int()
                    actualizar_producto(cursor, parametro_modificado, actualizacion, read(cursor, 'IDProducto', 'Producto', f'where (marca = "{marca.get()}") and (modelo = "{modelo.get()}")')[0][0])
                else: 
                    return self.show_text_bpedido.set("Stock insuficiente")
            elif type(str_int()) == str:
                actualizar_producto(cursor, parametro_modificado, f"'{str_int()}'", read(cursor, 'IDProducto', 'Producto', f'where (marca = "{marca.get()}") and (modelo = "{modelo.get()}")')[0][0])
            else:
                 actualizar_producto(cursor, parametro_modificado, str_int(), read(cursor, 'IDProducto', 'Producto', f'where (marca = "{marca.get()}") and (modelo = "{modelo.get()}")')[0][0])
            if parametro_modificado == 'marca':
                producto = buscar_producto(cursor, str_int(), modelo.get())
            elif parametro_modificado == 'modelo':
                producto = buscar_producto(cursor, marca.get(), str_int())
            else: 
                producto = buscar_producto(cursor, marca.get(), modelo.get())
            if len(producto) != 0:
                self.show_text_bpedido.set("")
                for item in producto:
                    self.l_ventana9.insert("",END,values=item)
            else:
                self.show_text_bpedido.set("No se encontró el producto")   
            marca['values'] =read(cursor, "marca", "producto", "group by marca")    
            modelo['values'] = ""

        boton_eliminar_pedido = ttk.Button(
            ventana9,
            text="Actualizar", 
            command=funcion
        )
        boton_eliminar_pedido.place(x=700, y=49, width=70)
        
        boton_cerrar_pedido = ttk.Button(
            ventana9,
            text="Cerrar", 
            command=lambda:(self.dni_var.set(0), self.show_text_bpedido.set(""), ventana9.destroy())
        )
        boton_cerrar_pedido.place(x=375, y=170)
    
    def actualizar_persona(self):
        self.variable_var = StringVar()
        ventana8 = Toplevel()
        ventana8.title("Actualizar Persona")
        ventana8.geometry("800x210+150+150")
        ventana8.focus()
        ventana8.grab_set()

        width_treeview=750
        height_treeview= 80
        x_treeview= 20
        y_treeview=80
        self.l_ventana8 = ttk.Treeview(ventana8)
        self.l_ventana8.place(x=x_treeview, y=y_treeview, width=width_treeview, height=height_treeview)  # Posicionar el Treeview
        self.l_ventana8['columns'] = ('DNI','Nombre y Apellido','Telefono','Direccion','Correo')
        self.l_ventana8.column('#0', width=0, stretch=NO)
        
        s_ventana5 = ttk.Scrollbar(ventana8, orient=VERTICAL, command=self.l.yview)
        s_ventana5.place(x=x_treeview+width_treeview, y=y_treeview, height=height_treeview)  # Posicionar la Scrollbar
        self.l_ventana8['yscrollcommand'] = s_ventana5.set
        
        for colum in self.l_ventana8['columns']:
            width = 100
            self.l_ventana8.column(colum, width=width, anchor='center')
            self.l_ventana8.heading(colum, text=colum)
        
        ttk.Label(ventana8, text="DNI").place(x=20, y=20)
        self.buscar_persona_entry = ttk.Entry(ventana8, justify=LEFT, width=20, textvariable=self.dni_var).place(x=50, y=20)
        texto = ttk.Label(ventana8, textvariable=self.show_text_bpedido)
        texto.place(x=25, y=50)
        texto.config(foreground='red')
        
        
        ttk.Label(ventana8, text="Parametro a modificar").place(x=190, y=20)
        parametro = ttk.Combobox(ventana8, state="readonly", values=("Nombre y Apellido", "Telefono", "Direccion", "Correo"))
        parametro.place(x=320, y=20) 
    
        ttk.Label(ventana8, text="Nuevo valor").place(x=475, y=20)
        self.buscar_persona_entry = ttk.Entry(ventana8, justify=LEFT, width=20, textvariable=self.variable_var).place(x=550, y=20)
        def str_int():
            try:
                valor = int(self.variable_var.get())
            except:
                valor = str(self.variable_var.get())
            return valor
        def funcion():
            self.l_ventana8.delete(*self.l_ventana8.get_children())  # Limpiar cualquier dato anterior en el Treeview
            if parametro.get() == "Nombre y Apellido":
                parametro_modificado = "nombre_apellido"
            elif parametro.get() == "Telefono":
                parametro_modificado = "telefono"
            elif parametro.get() == "Direccion":
                parametro_modificado = "direccion"
            elif parametro.get() == "Correo":
                parametro_modificado = "correo"
                
            if type(str_int()) == str:
                actualizar_persona(cursor, parametro_modificado, f"'{str_int()}'", self.dni_var.get())
            else:
                actualizar_persona(cursor, parametro_modificado, str_int(), self.dni_var.get())
            persona = buscar_persona(cursor, self.dni_var.get())
            if len(persona) != 0:
                self.show_text_bpedido.set("")
                for item in persona:
                    self.l_ventana8.insert("",END,values=item)
            else:
                self.show_text_bpedido.set("DNI No registrado")       

        boton_eliminar_pedido = ttk.Button(
            ventana8,
            text="Actualizar", 
            command=funcion
        )
        boton_eliminar_pedido.place(x=700, y=19, width=70)
        
        boton_cerrar_pedido = ttk.Button(
            ventana8,
            text="Cerrar", 
            command=lambda:(self.dni_var.set(0), self.show_text_bpedido.set(""), ventana8.destroy())
        )
        boton_cerrar_pedido.place(x=375, y=170)

         
    def generar_pedido(self):
                
        ventana7 = Toplevel()
        ventana7.title("Generar Pedido")
        ventana7.geometry("800x420+150+150")
        ventana7.focus()
        ventana7.grab_set()
        
        self.cantidad_var = IntVar()
        self.dni_genped_var = IntVar()
        
        ttk.Label(ventana7, text="DNI ").place(x=20, y=20) 
        self.dni_generar = ttk.Entry(ventana7, justify=LEFT, width=20, textvariable=self.dni_genped_var).place(x=60, y=20)  
        
        
        ttk.Label(ventana7, text="Tipo ").place(x=200, y=20)  
        tipo = ttk.Combobox(ventana7, state="readonly", values=['']+read(cursor, "tipo", "producto", "group by tipo"))
        tipo.place(x=240, y=20) 
        
        ttk.Label(ventana7, text="Marca ").place(x=400, y=20)
        marca = ttk.Combobox(ventana7, state="readonly", values=['']+read(cursor, "marca", "producto", "group by marca"))
        marca.place(x=450, y=20)  
        
        def insertar_tipo(event=None):
            self.l_ventana71.delete(*self.l_ventana71.get_children())
            if marca.get() == "":
                #seleccion = read(cursor, "*", "producto", f"where tipo = '{tipo.get()}'")
                seleccion = read(cursor, "p.IDProducto, p.tipo, p.marca, p.modelo, p.descripcion, p.precio, (p.stock - ifnull(s.cantidad,0))", "producto", f"as p left join subpedido as s on p.IDProducto = s.IDProducto where p.tipo = '{tipo.get()}'")
            elif tipo.get() == "":
                seleccion = read(cursor, "p.IDProducto, p.tipo, p.marca, p.modelo, p.descripcion, p.precio, (p.stock - ifnull(s.cantidad,0))", "producto", f"as p left join subpedido as s on p.IDProducto = s.IDProducto where marca = '{marca.get()}'")
            else:
                #seleccion = read(cursor, "*", "producto", f"where marca = '{marca.get()}' and tipo = '{tipo.get()}'")
                seleccion = read(cursor, "p.IDProducto, p.tipo, p.marca, p.modelo, p.descripcion, p.precio, (p.stock - ifnull(s.cantidad,0))", "producto", f"as p left join subpedido as s on p.IDProducto = s.IDProducto where p.marca = '{marca.get()}' and p.tipo = '{tipo.get()}' ")
            for tipo_item in seleccion:
                self.l_ventana71.insert("",END,values=tipo_item)
                
        tipo.bind("<<ComboboxSelected>>", insertar_tipo)

        def insertar_marca(event=None):
            self.l_ventana71.delete(*self.l_ventana71.get_children())
            if tipo.get() == "":
                #seleccion = read(cursor, "*", "producto", f"where marca = '{marca.get()}'")
                seleccion = read(cursor, "p.IDProducto, p.tipo, p.marca, p.modelo, p.descripcion, p.precio, (p.stock - ifnull(s.cantidad,0))", "producto", f"as p left join subpedido as s on p.IDProducto = s.IDProducto where marca = '{marca.get()}'")
            elif marca.get() == "":
                seleccion = read(cursor, "p.IDProducto, p.tipo, p.marca, p.modelo, p.descripcion, p.precio, (p.stock - ifnull(s.cantidad,0))", "producto", f"as p left join subpedido as s on p.IDProducto = s.IDProducto where p.tipo = '{tipo.get()}'")
            else:
                #seleccion = read(cursor, "*", "producto", f"where marca = '{marca.get()}' and tipo = '{tipo.get()}'")
                seleccion = read(cursor, "p.IDProducto, p.tipo, p.marca, p.modelo, p.descripcion, p.precio, (p.stock - ifnull(s.cantidad,0))", "producto", f"as p left join subpedido as s on p.IDProducto = s.IDProducto where marca = '{marca.get()}' and tipo = '{tipo.get()}'")
                
            for tipo_item in seleccion:
                self.l_ventana71.insert("",END,values=tipo_item)
                
        marca.bind("<<ComboboxSelected>>", insertar_marca)
        
        def seleccion():
            
            item_all = self.l_ventana71.selection()
            lista = [i for i in (self.l_ventana71.item(item_all[0], "values"))]
            lista[6]=self.cantidad_var.get()
            self.l_ventana72.insert("",END,values=lista)
            self.l_ventana71.delete(*self.l_ventana71.get_children())
            self.cantidad_var.set(0)
        
        width_treeview1=750
        height_treeview1= 120
        x_treeview1= 20
        y_treeview1=60
        self.l_ventana71 = ttk.Treeview(ventana7)
        self.l_ventana71.place(x=x_treeview1, y=y_treeview1, width=width_treeview1, height=height_treeview1)  # Posicionar el Treeview
        self.l_ventana71.column('#0', width=0, stretch=NO)
        self.l_ventana71['columns'] = ('ID Producto','Tipo','Marca','Modelo','Descripcion','Precio', 'Stock')
        s_ventana71 = ttk.Scrollbar(ventana7, orient=VERTICAL, command=self.l.yview)
        s_ventana71.place(x=x_treeview1+width_treeview1, y=y_treeview1, height=height_treeview1)  # Posicionar la Scrollbar
        self.l_ventana71['yscrollcommand'] = s_ventana71.set
        
        for colum in self.l_ventana71['columns']:
            width = 100
            self.l_ventana71.column(colum, width=width, anchor='center')
            self.l_ventana71.heading(colum, text=colum)

        ttk.Label(ventana7, text="Cantidad ").place(x=500, y=200)
        self.buscar_persona_entry = ttk.Entry(ventana7, justify=LEFT, width=20, textvariable=self.cantidad_var).place(x=560, y=200)         
        
        boton_agregar = ttk.Button(
            ventana7,
            text="Agregar", 
            command = seleccion
        )
        boton_agregar.place(x=700, y=198, width=70)
        
        width_treeview2=750
        height_treeview2= 120
        x_treeview2= 20
        y_treeview2=240
        self.l_ventana72 = ttk.Treeview(ventana7)
        self.l_ventana72.place(x=x_treeview2, y=y_treeview2, width=width_treeview2, height=height_treeview2)  # Posicionar el Treeview
        self.l_ventana72.column('#0', width=0, stretch=NO)
        self.l_ventana72['columns'] = ('ID Producto','Tipo','Marca','Modelo','Descripcion','Precio', 'Cantidad')
        l_ventana72 = ttk.Scrollbar(ventana7, orient=VERTICAL, command=self.l.yview)
        l_ventana72.place(x=x_treeview2+width_treeview2, y=y_treeview2, height=height_treeview2)  # Posicionar la Scrollbar
        self.l_ventana72['yscrollcommand'] = l_ventana72.set
        
        for colum in self.l_ventana72['columns']:
            width = 100
            self.l_ventana72.column(colum, width=width, anchor='center')
            self.l_ventana72.heading(colum, text=colum)
        
        def seleccion2():
            items = self.l_ventana72.get_children()
            all_values = []
            for item in items:
                item_values = self.l_ventana72.item(item, "values")
                all_values.append(item_values)
            print(all_values)
            solicitar_pedido(cursor, self.dni_genped_var.get(), [(i[0], int(i[6])) for i in all_values])
            print(consultar_pedido(cursor, 32132647))
        
        boton_borrar_pedido = ttk.Button(
            ventana7,
            text="Borrar", 
            command=lambda:(self.l_ventana72.delete(*self.l_ventana72.get_children()))
        )
        boton_borrar_pedido.place(x=510, y=375)
            
        boton_generar_pedido = ttk.Button(
            ventana7,
            text="Generar Pedido", 
            command= lambda:(seleccion2(), self.l_ventana72.delete(*self.l_ventana72.get_children()), ventana7.destroy())
        )
        boton_generar_pedido.place(x=595, y=375)
        
        boton_cerrar_pedido = ttk.Button(
            ventana7,
            text="Cerrar", 
            command=ventana7.destroy
        )
        boton_cerrar_pedido.place(x=695, y=375)
        
        
    def busco_pedido(self, eso):
        
        self.IDPedido_var = IntVar()
        
        ventana5 = Toplevel()
        ventana5.title("Editar Pedido")
        ventana5.geometry("800x210+150+150")
        ventana5.focus()
        ventana5.grab_set()

        width_treeview=750
        height_treeview= 100
        x_treeview= 20
        y_treeview=60
        self.l_ventana5 = ttk.Treeview(ventana5)
        self.l_ventana5.place(x=x_treeview, y=y_treeview, width=width_treeview, height=height_treeview)  # Posicionar el Treeview
        self.l_ventana5['columns'] = ('ID Pedido','Cantidad','Marca','Modelo','Costo Unidad','Costo')
        self.l_ventana5.column('#0', width=0, stretch=NO)
        
        s_ventana5 = ttk.Scrollbar(ventana5, orient=VERTICAL, command=self.l.yview)
        s_ventana5.place(x=x_treeview+width_treeview, y=y_treeview, height=height_treeview)  # Posicionar la Scrollbar
        self.l_ventana5['yscrollcommand'] = s_ventana5.set
        
        for colum in self.l_ventana5['columns']:
            width = 100
            self.l_ventana5.column(colum, width=width, anchor='center')
            self.l_ventana5.heading(colum, text=colum)
        
        ttk.Label(ventana5, text="DNI").place(x=20, y=20)
        self.buscar_persona_entry = ttk.Entry(ventana5, justify=LEFT, width=20, textvariable=self.dni_var).place(x=80, y=20)
        texto = ttk.Label(ventana5, textvariable=self.show_text_bpedido)
        texto.config(foreground='red')
        if eso == 0:
            texto.place(x=300, y=20)
        def funcion():
            self.l_ventana5.delete(*self.l_ventana5.get_children())  # Limpiar cualquier dato anterior en el Treeview
            pedido = consultar_pedido(cursor, self.dni_var.get())
            if pedido != 0:
                self.show_text_bpedido.set("")
                for item in pedido:
                    self.l_ventana5.insert("",END,values=item)
            else:
                self.show_text_bpedido.set("No tiene pedidos")
            
        def eliminar():
            self.l_ventana5.delete(*self.l_ventana5.get_children())  # Limpiar cualquier dato anterior en el Treeview
            eliminado = eliminar_pedido(cursor, self.dni_var.get(), self.IDPedido_var.get())
            if eliminado != 0:
                self.show_text_bpedido.set("Eliminado")
            else:
                self.show_text_bpedido.set("Persona o pedido inexistente")
            
            
        
        boton_buscar_pedido = ttk.Button(
            ventana5,
            text="Buscar", 
            command=funcion
        )
        boton_buscar_pedido.place(x=220, y=19, width=70)
        boton_cerrar_pedido = ttk.Button(
            ventana5,
            text="Cerrar", 
            command=lambda:(self.dni_var.set(0), self.IDPedido_var.set(0), self.show_text_bpedido.set(""), ventana5.destroy())
        )
        boton_cerrar_pedido.place(x=375, y=170)
        if eso == 1:
            texto.place(x=600, y=20)
            ttk.Label(ventana5, text="ID Pedido").place(x=300, y=20)
            self.buscar_persona_entry = ttk.Entry(ventana5, justify=LEFT, width=20, textvariable=self.IDPedido_var).place(x=380, y=20)
            boton_eliminar_pedido = ttk.Button(
                ventana5,
                text="Eliminar", 
                command=eliminar
            )
            boton_eliminar_pedido.place(x=520, y=19, width=70)
        
    def busco_persona(self):
        #self.persona_var = IntVar()
        self.show_text_bpersona = StringVar()
        
        ventana3 = Toplevel()
        ventana3.title("Buscar Persona")
        ventana3.geometry("800x150+150+150")
        #ventana3.config(width=800, height=150)
        ventana3.focus()
        ventana3.grab_set()
        
        width_treeview=760
        height_treeview= 50
        x_treeview = 20
        y_treeview = 60
        self.l_ventana3 = ttk.Treeview(ventana3)
        self.l_ventana3.place(x=x_treeview, y=y_treeview, width=width_treeview, height=height_treeview)  # Posicionar el Treeview
        self.l_ventana3.column('#0', width=0, stretch=NO)
        self.l_ventana3['columns'] = ('DNI','Nombre y Apellido', 'Telefono', 'Direccion','Correo')
        self.l_ventana3.column('#0', width=0, stretch=NO)
        
        s_ventana3 = ttk.Scrollbar(ventana3, orient=VERTICAL, command=self.l.yview)
        s_ventana3.place(x=x_treeview+width_treeview, y=y_treeview, height=height_treeview)  # Posicionar la Scrollbar
        self.l_ventana3['yscrollcommand'] = s_ventana3.set
        
        for colum in self.l_ventana3['columns']:
            if colum == 'DNI':
                width = 40
            elif colum != 'Correo':
                width = 75
            else:
                width = 200
            self.l_ventana3.column(colum, width=width, anchor='center')
            self.l_ventana3.heading(colum, text=colum)
        
        ttk.Label(ventana3, text="DNI: ").place(x=20, y=20)
        self.buscar_persona_entry = ttk.Entry(ventana3, justify=LEFT, width=20, textvariable=self.persona_var).place(x=100, y=20)
        texto = ttk.Label(ventana3, textvariable=self.show_text_bpersona)
        texto.config(foreground='red')
        texto.place(x=310, y=20)
        def funcion():
            self.l_ventana3.delete(*self.l_ventana3.get_children())  # Limpiar cualquier dato anterior en el Treeview
            persona = buscar_persona(cursor, self.persona_var.get())
            if len(persona)==1:
                self.show_text_bpersona.set("")
            else:
                self.show_text_bpersona.set("No se encontro en el registro")
            for item in persona:
                self.l_ventana3.insert("",END,values=item)
        
        
        boton_buscar_persona = ttk.Button(
            ventana3,
            text="Buscar", 
            command=funcion
        )
        boton_buscar_persona.place(x=250, y=19, width=50)
        boton_cerrar_persona = ttk.Button(
            ventana3,
            text="Cerrar", 
            command=ventana3.destroy
        )
        boton_cerrar_persona.place(x=375, y=120)

    
    def busco_producto(self):
        self.producto_var_marca = StringVar()
        self.producto_var_modelo = StringVar()
        self.show_text = StringVar()
        
        ventana4 = Toplevel()
        ventana4.title("Buscar Producto")
        ventana4.geometry("800x270+150+150")
        ventana4.focus()
        ventana4.grab_set()

        width_treeview=760
        height_treeview= 120
        x_treeview = 20
        y_treeview = 90
        self.l_ventana4 = ttk.Treeview(ventana4)
        self.l_ventana4.place(x=x_treeview, y=y_treeview, width=width_treeview, height=height_treeview)  # Posicionar el Treeview
        self.l_ventana4.column('#0', width=0, stretch=NO)
        self.l_ventana4['columns'] = ('ID', 'Tipo', 'Marca', 'Modelo', 'Descripcion', 'Precio')
        self.l_ventana4.column('#0', width=0, stretch=NO)
        
        s_ventana4 = ttk.Scrollbar(ventana4, orient=VERTICAL, command=self.l.yview)
        s_ventana4.place(x=x_treeview+width_treeview, y=y_treeview, height=height_treeview)  # Posicionar la Scrollbar
        self.l_ventana4['yscrollcommand'] = s_ventana4.set
        
        for colum in self.l_ventana4['columns']:
            if colum == 'ID':
                width = 40
            elif colum != 'Descripcion':
                width = 75
            else:
                width = 200
            self.l_ventana4.column(colum, width=width, anchor='center')
            self.l_ventana4.heading(colum, text=colum)
        
        ttk.Label(ventana4, text="Marca: ").place(x=20, y=20)
        self.buscar_producto_entry = ttk.Entry(ventana4, justify=LEFT, width=20, textvariable=self.producto_var_marca).place(x=100, y=20)
        ttk.Label(ventana4, text="Modelo: ").place(x=20, y=50)
        self.buscar_producto_entry = ttk.Entry(ventana4, justify=LEFT, width=20, textvariable=self.producto_var_modelo).place(x=100, y=50)
        texto = ttk.Label(ventana4, textvariable=self.show_text)
        texto.config(foreground='red')
        texto.place(x=310, y=20)
        def funcion():
            self.l_ventana4.delete(*self.l_ventana4.get_children())  # Limpiar cualquier dato anterior en el Treeview
            producto = buscar_producto(cursor, self.producto_var_marca.get(), self.producto_var_modelo.get())
            if len(producto) == 1:
                self.show_text.set("")
            else:
                self.show_text.set("No se encontraron productos que coincidan")
            for item in producto:
                    self.l_ventana4.insert("",END,values=item)
        
        boton_buscar_producto = ttk.Button(
            ventana4,
            text="Buscar", 
            command=lambda:(funcion(), self.producto_var_marca.set(""), self.producto_var_modelo.set(""))
        )
        boton_buscar_producto.place(x=250, y=19, width=50)
        boton_cerrar_persona = ttk.Button(
            ventana4,
            text="Cerrar", 
            command=ventana4.destroy
        )
        boton_cerrar_persona.place(x=375, y=230)
        
    def registro_persona(self):
        self.dni_var = IntVar()
        self.nombre_apellido_var = StringVar()
        self.telefono_var = IntVar()
        self.direccion_var = StringVar()
        self.correo_var = StringVar()
        
        # Crear una ventana secundaria.
        ventana6 = Toplevel()
        ventana6.title("Registrar Producto")
        ventana6.geometry("300x270+150+150")
        ventana6.focus()
        ventana6.grab_set()
        
        
        ttk.Label(ventana6, text="DNI: ").place(x=20, y=20)
        self.entry_tipo = ttk.Entry(ventana6, justify=LEFT, width=20, textvariable=self.dni_var).place(x=130, y=20)
        ttk.Label(ventana6, text="Nombre y Apellido: ").place(x=20, y=50)
        self.entry_marca = ttk.Entry(ventana6, justify=LEFT, width=20, textvariable=self.nombre_apellido_var).place(x=130, y=50)
        ttk.Label(ventana6, text="Telefono: ").place(x=20, y=80)
        self.entry_modelo = ttk.Entry(ventana6, justify=LEFT, width=20, textvariable=self.telefono_var).place(x=130, y=80)
        ttk.Label(ventana6, text="Direccion: ").place(x=20, y=110)
        self.entry_descripcion = ttk.Entry(ventana6, justify=LEFT, width=20, textvariable=self.direccion_var).place(x=130, y=110)
        ttk.Label(ventana6, text="Correo: ").place(x=20, y=140)
        self.entry_precio = ttk.Entry(ventana6, justify=LEFT, width=20, textvariable=self.correo_var).place(x=130, y=140)
     
        def registrar():
            #registrar_producto(cursor, tipo, marca, modelo, descripcion, precio, stock)
            registrar_persona(cursor,self.dni_var.get(), self.nombre_apellido_var.get(), self.telefono_var.get(), self.direccion_var.get(), self.correo_var.get())
            ventana6.destroy()
            
        boton_registrar = ttk.Button(
            ventana6,
            text="Registrar", 
            command=lambda:(registrar(), self.dni_var.set(0), self.nombre_apellido_var.set(""), self.telefono_var.set(0), self.direccion_var.set(""), self.correo_var.set(""))
        )
        boton_registrar.place(x=65, y=220)
        boton_cerrar = ttk.Button(
            ventana6,
            text="Cerrar", 
            command=ventana6.destroy
        )
        boton_cerrar.place(x=160, y=220)
    
    def registro_producto(self):
        self.tipo_var = StringVar()
        self.marca_var = StringVar()
        self.modelo_var = StringVar()
        self.descripcio_var = StringVar()
        self.precio_var = DoubleVar()
        self.stock_var = IntVar()
        
        # Crear una ventana secundaria.
        ventana_secundaria = Toplevel()
        ventana_secundaria.title("Registrar Producto")
        ventana_secundaria.geometry("300x270+150+150")
        ventana_secundaria.focus()
        ventana_secundaria.grab_set()
        
        ttk.Label(ventana_secundaria, text="Tipo: ").place(x=20, y=20)
        self.entry_tipo = ttk.Entry(ventana_secundaria, justify=LEFT, width=20, textvariable=self.tipo_var).place(x=100, y=20)
        ttk.Label(ventana_secundaria, text="Marca: ").place(x=20, y=50)
        self.entry_marca = ttk.Entry(ventana_secundaria, justify=LEFT, width=20, textvariable=self.marca_var).place(x=100, y=50)
        ttk.Label(ventana_secundaria, text="Modelo: ").place(x=20, y=80)
        self.entry_modelo = ttk.Entry(ventana_secundaria, justify=LEFT, width=20, textvariable=self.modelo_var).place(x=100, y=80)
        ttk.Label(ventana_secundaria, text="Descripcion: ").place(x=20, y=110)
        self.entry_descripcion = ttk.Entry(ventana_secundaria, justify=LEFT, width=20, textvariable=self.descripcio_var).place(x=100, y=110)
        ttk.Label(ventana_secundaria, text="Precio: ").place(x=20, y=140)
        self.entry_precio = ttk.Entry(ventana_secundaria, justify=LEFT, width=20, textvariable=self.precio_var).place(x=100, y=140)
        ttk.Label(ventana_secundaria, text="Stock: ").place(x=20, y=170)
        self.entry_stock = ttk.Entry(ventana_secundaria, justify=LEFT, width=20, textvariable=self.stock_var).place(x=100, y=170)
        
        def registrar():
            #registrar_producto(cursor, tipo, marca, modelo, descripcion, precio, stock)
            registrar_producto(cursor,self.tipo_var.get(), self.marca_var.get(), self.modelo_var.get(), self.descripcio_var.get(), self.precio_var.get(), self.stock_var.get())
            ventana_secundaria.destroy()
            
        boton_registrar = ttk.Button(
            ventana_secundaria,
            text="Registrar", 
            command=registrar
        )
        boton_registrar.place(x=65, y=220)
        boton_cerrar = ttk.Button(
            ventana_secundaria,
            text="Cerrar", 
            command=ventana_secundaria.destroy
        )
        boton_cerrar.place(x=160, y=220)
 
        
    def stock(self):
        self.l.delete(*self.l.get_children())  # Limpiar cualquier dato anterior en el Treeview

        self.l['columns'] = ('ID','Tipo', 'Marca', 'Modelo', 'Descripcion', 'Precio', 'Cantidad')  
        self.l.column('#0', width=0, stretch=NO)
        for colum in self.l['columns']:
            if colum == 'ID' or colum == 'Cantidad':
                width = 40
            elif colum != 'Descripcion':
                width = 75
            else:
                width = 125
            self.l.column(colum, width=width, anchor='center')
            self.l.heading(colum, text=colum)
        stock = ver_stock(cursor)
      
        for stock_item in stock:
                self.l.insert("",END,values=stock_item)
    
    def ver_personas(self):
        self.l.delete(*self.l.get_children())  # Limpiar cualquier dato anterior en el Treeview

        self.l['columns'] = ('DNI','Nombre y Apellido', 'Telefono', 'Direccion', 'Correo')  
        self.l.column('#0', width=0, stretch=NO)
        for colum in self.l['columns']:
            if colum == 'DNI':
                width = 40
            elif colum == 'Correo':
                width = 150
            elif colum == 'Direccion':
                width = 100
            else:
                width = 75
            self.l.column(colum, width=width, anchor='center')
            self.l.heading(colum, text=colum)
        stock = ver_personas(cursor)
      
        for stock_item in stock:
                self.l.insert("",END,values=stock_item)
                        
    def salir(self):
        cursor.close()
        cnx.close()
        root.destroy()
        return 1
        

root = Tk()
Interfaz(root)
if __name__ == "__main__":
    root.mainloop()

