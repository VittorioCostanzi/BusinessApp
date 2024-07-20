import pytest
from interfaz import *
import pyautogui
import time
import threading
import pyperclip


entorno = Interfaz(root)

        #FALTA:
        # Eliminar personas
        # Eliminar productos
        # Update personas
        # Update pedidos
        # Update productos

#Suple la diferencia entre la ubicacion real en la pantalla y la utilizada

diff_x = root.winfo_rootx()-100
diff_y = root.winfo_rooty()-100

def test_stock():
    time.sleep(2)
    #entorno.stock()
    pyautogui.moveTo(151 + diff_x, 371 + diff_y, duration=.25)  #Clickea boton Ver Stock
    pyautogui.click() 
    items = entorno.l.get_children()
    all_values = []
    for item in items:
        item_values = entorno.l.item(item, "values")
        all_values.append(item_values)   
    assert all_values == [('1', 'Notebook', 'Lenovo', 'Thinkpad', 'Rapida y confiable', '25.50', '4'), 
                                                     ('2', 'Mouse', 'Exxo', 'Ex3', 'Con botones', '2.90', '8'), 
                                                     ('3', 'Monitor', 'HP', 'HP serie 200', '23" widescreen', '13.50', '2'), 
                                                     ('4', 'Notebook', 'Asus', 'X', 'Solida y duradera', '32.80', '6'), 
                                                     ('5', 'Mouse', 'Lenovo', 'XT30', 'Ergonomico', '3.50', '10'), 
                                                     ('6', 'Teclado', 'Lenovo', 'XT40', 'Con luces', '3.80', '14'), 
                                                     ('7', 'Notebook', 'Exxo', 'Eso', 'Muy vendida', '18.80', '10'), 
                                                     ('8', 'Monitor', 'BGH', 'B150', '23" economico', '16.20', '5')] 
    
def test_busco_persona():
    #Buscar persona
    #entorno.busco_persona()
    pyautogui.moveTo(151 + diff_x, 221 + diff_y, duration=.25)  #Clickea boton Buscar Persona
    pyautogui.click() 
    pyautogui.moveTo(250 + diff_x, 170 + diff_y, duration=.25)
    pyautogui.click() 
    #Elimina el cero
    pyautogui.hotkey("del","del")
    #Escribe
    teclear = [pyautogui.press(i) for i in '32132647']
    pyautogui.moveTo(400 + diff_x, 169 + diff_y, duration=.25)
    pyautogui.click() 
    assert entorno.persona_var.get() == 32132647
    pyautogui.moveTo(525 + diff_x, 270 + diff_y, duration=.25)
    pyautogui.click() 
    
def test_buscar_producto():
    #entorno.busco_producto()
    pyautogui.moveTo(151 + diff_x, 251 + diff_y, duration=.25)  #Clickea boton Buscar Producto
    pyautogui.click() 
    pyautogui.moveTo(251 + diff_x, 171 + diff_y, duration=.25)
    pyautogui.click() 
    teclear = [pyautogui.press(i) for i in 'Lenovo']
    pyautogui.moveTo(251 + diff_x, 201 + diff_y, duration=.25)
    pyautogui.click() 
    teclear = [pyautogui.press(i) for i in 'Thinkpad']
    pyautogui.moveTo(401 + diff_x, 170 + diff_y, duration=.25)
    pyautogui.click() 
    pyautogui.moveTo(526 + diff_x, 381 + diff_y, duration=.5)
    pyautogui.click() 
    
def test_registrar_producto():
    #entorno.registro_producto()
    pyautogui.moveTo(151 + diff_x, 191 + diff_y, duration=.25)  #Clickea boton Registrar Producto
    pyautogui.click() 
    pyautogui.moveTo(251 + diff_x, 171 + diff_y, duration=.25)
    pyautogui.click()
    teclear = [pyautogui.press(i) for i in 'Auriculares']
    pyautogui.moveTo(251 + diff_x, 201 + diff_y, duration=.25)
    pyautogui.click()
    teclear = [pyautogui.press(i) for i in 'Sony']
    pyautogui.moveTo(251 + diff_x, 231 + diff_y, duration=.25)
    pyautogui.click()
    teclear = [pyautogui.press(i) for i in 'Ch-510']
    pyautogui.moveTo(251 + diff_x, 261 + diff_y, duration=.25)
    pyautogui.click()
    teclear = [pyautogui.press(i) for i in 'Buen sonido']
    pyautogui.moveTo(251 + diff_x, 291 + diff_y, duration=.25)
    pyautogui.click()
    pyautogui.hotkey("del","del","del","del")
    teclear = [pyautogui.press(i) for i in '17.50']
    pyautogui.moveTo(251 + diff_x, 321 + diff_y, duration=.25)
    pyautogui.click()
    pyautogui.hotkey("del","del")
    teclear = [pyautogui.press(i) for i in '15']
    pyautogui.moveTo(216 + diff_x, 371 + diff_y, duration=.25)
    pyautogui.click()

def test_stock2():
    #entorno.stock()
    pyautogui.moveTo(151 + diff_x, 371 + diff_y, duration=.25)  #Clickea boton Ver Stock
    pyautogui.click() 
    #Hace click
    pyautogui.click()
    items = entorno.l.get_children()
    all_values = []
    for item in items:
        item_values = entorno.l.item(item, "values")
        all_values.append(item_values)   
    assert all_values == [('1', 'Notebook', 'Lenovo', 'Thinkpad', 'Rapida y confiable', '25.50', '4'), 
                                                     ('2', 'Mouse', 'Exxo', 'Ex3', 'Con botones', '2.90', '8'), 
                                                     ('3', 'Monitor', 'HP', 'HP serie 200', '23" widescreen', '13.50', '2'), 
                                                     ('4', 'Notebook', 'Asus', 'X', 'Solida y duradera', '32.80', '6'), 
                                                     ('5', 'Mouse', 'Lenovo', 'XT30', 'Ergonomico', '3.50', '10'), 
                                                     ('6', 'Teclado', 'Lenovo', 'XT40', 'Con luces', '3.80', '14'), 
                                                     ('7', 'Notebook', 'Exxo', 'Eso', 'Muy vendida', '18.80', '10'), 
                                                     ('8', 'Monitor', 'BGH', 'B150', '23" economico', '16.20', '5'),
                                                     ('9', 'Auriculares', 'Sony', 'Ch-510', 'Buen sonido', '17.50', '15')] 

    
def test_busco_pedido_sin_pedido(): 
    #entorno.busco_pedido(0)
    pyautogui.moveTo(151 + diff_x, 311 + diff_y, duration=.25)  #Clickea boton Buscar Pedido
    pyautogui.click() 
    assert entorno.show_text_bpedido.get() == ""
    pyautogui.moveTo(230 + diff_x, 170 + diff_y, duration=.25) #Se mueve al entry DNI
    pyautogui.click() 
    pyautogui.hotkey("del","del")
    teclear = [pyautogui.press(i) for i in '32132647']
    pyautogui.moveTo(370 + diff_x, 169 + diff_y, duration=.25) #Se mueve al boton buscar
    pyautogui.click() 
    assert entorno.dni_var.get() == 32132647
    assert entorno.show_text_bpedido.get() == "No tiene pedidos"
    pyautogui.moveTo(526 + diff_x, 321 + diff_y, duration=.25) #Se mueve al boton cerrar
    pyautogui.click() 

def test_elimino_pedido_sin_pedido():
    #entorno.busco_pedido(1)
    pyautogui.moveTo(151 + diff_x, 341 + diff_y, duration=.25)  #Clickea boton Eliminar Pedido
    pyautogui.click() 
    pyautogui.moveTo(150 + diff_x, 340 + diff_y, duration=.25) #Se mueve al boton eliminar pedido
    pyautogui.click() 
    assert entorno.show_text_bpedido.get() == ""
    pyautogui.moveTo(230 + diff_x, 170 + diff_y, duration=.25) #Se mueve al entry DNI
    pyautogui.click() 
    pyautogui.hotkey("del","del")
    teclear = [pyautogui.press(i) for i in '32132647']
    pyautogui.moveTo(531 + diff_x, 171 + diff_y, duration=.25) #Se mueve al entry ID
    pyautogui.click() 
    pyautogui.hotkey("del","del")
    teclear = [pyautogui.press(i) for i in '32']
    pyautogui.moveTo(671 + diff_x, 170 + diff_y, duration=.25) #Se mueve al boton eliminar
    pyautogui.click() 
    assert entorno.dni_var.get() == 32132647
    assert entorno.show_text_bpedido.get() == "Persona o pedido inexistente"
    pyautogui.moveTo(526 + diff_x, 321 + diff_y, duration=.25) #Se mueve al boton cerrar
    pyautogui.click()     
    
def test_registro_persona():
    #entorno.registro_persona()
    pyautogui.moveTo(151 + diff_x, 161 + diff_y, duration=.25)  #Clickea boton Registrar Persona
    pyautogui.click() 
    pyautogui.moveTo(281 + diff_x, 171 + diff_y, duration=.25)
    pyautogui.click()
    pyautogui.hotkey("del","del")
    teclear = [pyautogui.press(i) for i in '32541895']
    pyautogui.moveTo(281 + diff_x, 201 + diff_y, duration=.25)
    pyautogui.click()
    teclear = [pyautogui.press(i) for i in 'Marcos Perez']
    pyautogui.moveTo(281 + diff_x, 231 + diff_y, duration=.25)
    pyautogui.click()
    pyautogui.hotkey("del","del")
    teclear = [pyautogui.press(i) for i in '2215486958']
    pyautogui.moveTo(281 + diff_x, 261 + diff_y, duration=.25)
    pyautogui.click()
    teclear = [pyautogui.press(i) for i in 'Av.13 1243 2B']
    pyautogui.moveTo(281 + diff_x, 291 + diff_y, duration=.25)
    pyautogui.click()
    teclear = [pyautogui.press(i) for i in 'MP_86']
    pyperclip.copy("@")
    pyautogui.hotkey("ctrl", "v")
    teclear = [pyautogui.press(i) for i in 'gmail.com']
    pyautogui.moveTo(281 + diff_x, 321 + diff_y, duration=.25)

    pyautogui.moveTo(216 + diff_x, 371 + diff_y, duration=.25)
    pyautogui.click()
    
def test_ver_personas():
    #entorno.ver_personas()
    pyautogui.moveTo(151 + diff_x, 401 + diff_y, duration=.25)  #Clickea boton Ver Personas
    pyautogui.click() 
    items = entorno.l.get_children()
    all_values = []
    for item in items:
        item_values = entorno.l.item(item, "values")
        all_values.append(item_values)   
    assert all_values == [('32132647' ,"Pedro Sanchez",'2364251426', "Av. Del Carmen 502","Pepitojohnson@eso.com"),
                          ('32541895' ,"Marcos Perez",'2215486958', "Av.13 1243 2B","MP_86@gmail.com")]

def test_generar_pedido():
    #entorno.generar_pedido()
    pyautogui.moveTo(151 + diff_x, 281 + diff_y, duration=.25)  #Clickea boton Generar Pedido
    pyautogui.click() 
    pyautogui.moveTo(211 + diff_x, 171 + diff_y, duration=.25) #Se mueve al entry dni
    pyautogui.click()
    pyautogui.hotkey("del","del")
    teclear = [pyautogui.press(i) for i in '32541895']
    pyautogui.moveTo(391 + diff_x, 171 + diff_y, duration=.25) #Se mueve al combobox tipo
    pyautogui.click()
    pyautogui.moveTo(401 + diff_x, 211 + diff_y, duration=.25) #Toca la opcion
    pyautogui.click()
    pyautogui.moveTo(190 + diff_x, 241 + diff_y, duration=.25) #Selecciona el objeto en el treeview
    pyautogui.click()
    pyautogui.moveTo(711 + diff_x, 351 + diff_y, duration=.25) #Se mueve al entry cantidad
    pyautogui.click()
    pyautogui.hotkey("del","del")
    teclear = [pyautogui.press(i) for i in '2']
    pyautogui.moveTo(851 + diff_x, 349 + diff_y, duration=.25) #Presiona boton para sumar al pedido
    pyautogui.click()
    
    pyautogui.moveTo(391 + diff_x, 171 + diff_y, duration=.25) #Se mueve al combobox tipo
    pyautogui.click()
    pyautogui.moveTo(401 + diff_x, 230 + diff_y, duration=.25) #Toca la opcion
    pyautogui.click()
    
    pyautogui.moveTo(601 + diff_x, 171 + diff_y, duration=.25) #Se mueve al combobox marca
    pyautogui.click()
    pyautogui.moveTo(601 + diff_x, 230 + diff_y, duration=.25) #Toca la opcion
    pyautogui.click()
    
    pyautogui.moveTo(190 + diff_x, 241 + diff_y, duration=.25) #Selecciona el objeto en el treeview
    pyautogui.click()
    pyautogui.moveTo(711 + diff_x, 351 + diff_y, duration=.25) #Se mueve al entry cantidad
    pyautogui.click()
    pyautogui.hotkey("del","del")
    teclear = [pyautogui.press(i) for i in '7']
    pyautogui.moveTo(851 + diff_x, 349 + diff_y, duration=.25) #Presiona boton para sumar al pedido
    pyautogui.click()
    
    
    pyautogui.moveTo(391 + diff_x, 171 + diff_y, duration=.25) #Se mueve al combobox tipo
    pyautogui.click()
    pyautogui.moveTo(401 + diff_x, 201 + diff_y, duration=.25) #Toca la opcion
    pyautogui.click()
    pyautogui.moveTo(601 + diff_x, 171 + diff_y, duration=.25) #Se mueve al combobox marca
    pyautogui.click()
    pyautogui.moveTo(601 + diff_x, 220 + diff_y, duration=.25) #Toca la opcion
    pyautogui.click()    
    pyautogui.moveTo(190 + diff_x, 261 + diff_y, duration=.25) #Selecciona el objeto en el treeview
    pyautogui.click()
    pyautogui.moveTo(711 + diff_x, 351 + diff_y, duration=.25) #Se mueve al entry cantidad
    pyautogui.click()
    pyautogui.hotkey("del","del")
    teclear = [pyautogui.press(i) for i in '1']
    pyautogui.moveTo(851 + diff_x, 349 + diff_y, duration=.25) #Presiona boton para sumar al pedido
    pyautogui.click()
    pyautogui.moveTo(746 + diff_x, 526 + diff_y, duration=.25) #Presiona boton para generar el pedido
    pyautogui.click()

def test_busco_pedido_con_pedido():
    #entorno.busco_pedido(0)
    pyautogui.moveTo(151 + diff_x, 311 + diff_y, duration=.25)  #Clickea boton Buscar Pedido
    pyautogui.click() 
    pyautogui.moveTo(230 + diff_x, 170 + diff_y, duration=.25)
    pyautogui.click() 
    pyautogui.hotkey("del","del")
    teclear = [pyautogui.press(i) for i in '32541895']
    pyautogui.moveTo(370 + diff_x, 169 + diff_y, duration=.25)
    pyautogui.click() 
    assert entorno.dni_var.get() == 32541895
    assert entorno.show_text_bpedido.get() == ""
    pyautogui.moveTo(525 + diff_x, 320 + diff_y, duration=.25)
    pyautogui.click() 

def test_elimino_pedido_con_pedido():
    #entorno.busco_pedido(1)
    pyautogui.moveTo(151 + diff_x, 341 + diff_y, duration=.25)  #Clickea boton Eliminar Pedido
    pyautogui.click() 
    pyautogui.moveTo(230 + diff_x, 170 + diff_y, duration=.25) #Se mueve al entry DNI
    pyautogui.click() 
    pyautogui.hotkey("del","del")
    teclear = [pyautogui.press(i) for i in '32541895']
    pyautogui.moveTo(531 + diff_x, 171 + diff_y, duration=.25) #Se mueve al entry ID
    pyautogui.click() 
    pyautogui.hotkey("del","del")
    teclear = [pyautogui.press(i) for i in '1']
    pyautogui.moveTo(671 + diff_x, 170 + diff_y, duration=.25) #Se mueve al boton eliminar
    pyautogui.click() 
    assert entorno.dni_var.get() == 32541895
    assert entorno.show_text_bpedido.get() == "Eliminado"
    pyautogui.moveTo(526 + diff_x, 320 + diff_y, duration=.25)
    pyautogui.click() 
    
def test_busco_pedido_con_pedido_verificacion():
    #entorno.busco_pedido(0)
    pyautogui.moveTo(151 + diff_x, 311 + diff_y, duration=.25)  #Clickea boton Buscar Pedido
    pyautogui.click() 
    pyautogui.moveTo(230 + diff_x, 170 + diff_y, duration=.25)
    pyautogui.click() 
    pyautogui.hotkey("del","del")
    teclear = [pyautogui.press(i) for i in '32541895']
    pyautogui.moveTo(370 + diff_x, 169 + diff_y, duration=.25)
    pyautogui.click() 
    assert entorno.dni_var.get() == 32541895
    assert entorno.show_text_bpedido.get() == "No tiene pedidos"
    pyautogui.moveTo(525 + diff_x, 320 + diff_y, duration=.25)
    pyautogui.click()
    
def test_actualizar_persona_incorrecto():
    #entorno.actualizar_persona()
    pyautogui.moveTo(151 + diff_x, 431 + diff_y, duration=.25)  #Clickea boton Actualizar Persona
    pyautogui.click() 
    pyautogui.moveTo(201 + diff_x, 171 + diff_y, duration=.25) #Se mueve al entry DNI
    pyautogui.click() 
    pyautogui.hotkey("del","del")
    teclear = [pyautogui.press(i) for i in '40245144']
    pyautogui.moveTo(471 + diff_x, 171 + diff_y, duration=.25) #Se mueve al combobox
    pyautogui.click() 
    pyautogui.moveTo(500 + diff_x, 201 + diff_y, duration=.25) #Clickea opcion en el combobox
    pyautogui.click() 
    pyautogui.moveTo(701 + diff_x, 171 + diff_y, duration=.25) #Clickea entry nuevo valor
    pyautogui.click() 
    teclear = [pyautogui.press(i) for i in 'Roman Garcia']
    pyautogui.moveTo(851 + diff_x, 170 + diff_y, duration=.25) #Clickea boton actualizar
    pyautogui.click() 
    
    pyautogui.moveTo(526 + diff_x, 321 + diff_y, duration=.25) #Se mueve al boton cerrar
    pyautogui.click() 
    
def test_actualizar_persona_correcto():
    #entorno.actualizar_persona()
    pyautogui.moveTo(151 + diff_x, 431 + diff_y, duration=.25)  #Clickea boton Actualizar Persona
    pyautogui.click() 
    pyautogui.moveTo(201 + diff_x, 171 + diff_y, duration=.25) #Se mueve al entry DNI
    pyautogui.click() 
    pyautogui.hotkey("del","del")
    teclear = [pyautogui.press(i) for i in '32541895']
    pyautogui.moveTo(471 + diff_x, 171 + diff_y, duration=.25) #Se mueve al combobox
    pyautogui.click() 
    pyautogui.moveTo(500 + diff_x, 201 + diff_y, duration=.25) #Clickea opcion en el combobox
    pyautogui.click() 
    pyautogui.moveTo(701 + diff_x, 171 + diff_y, duration=.25) #Clickea entry nuevo valor
    pyautogui.click() 
    teclear = [pyautogui.press(i) for i in 'Juan Perez']
    pyautogui.moveTo(851 + diff_x, 170 + diff_y, duration=.25) #Clickea boton actualizar
    pyautogui.click() 
    
    pyautogui.moveTo(526 + diff_x, 321 + diff_y, duration=.25) #Se mueve al boton cerrar
    pyautogui.click()
    
def test_actualizar_objeto():
    #entorno.actualizar_producto()
    pyautogui.moveTo(151 + diff_x, 461 + diff_y, duration=.25)  #Clickea boton Actualizar Producto
    pyautogui.click() 
    pyautogui.moveTo(231 + diff_x, 171 + diff_y, duration=.25) #Se mueve al combobox marca
    pyautogui.click()
    pyautogui.moveTo(251 + diff_x, 201 + diff_y, duration=.25) #Selecciona opcion
    pyautogui.click()
    pyautogui.moveTo(231 + diff_x, 201 + diff_y, duration=.25) #Se mueve al combobox modelo
    pyautogui.click()
    pyautogui.moveTo(251 + diff_x, 231 + diff_y, duration=.25) #Selecciona opcion
    pyautogui.click()
    pyautogui.moveTo(541 + diff_x, 171 + diff_y, duration=.25) #Se mueve al combobox parametro
    pyautogui.click()
    pyautogui.moveTo(571 + diff_x, 251 + diff_y, duration=.25) #Selecciona opcion
    pyautogui.click()
    pyautogui.moveTo(793 + diff_x, 171 + diff_y, duration=.25) #Se mueve al entry nuevo valor
    pyautogui.click()
    teclear = [pyautogui.press(i) for i in 'Excelente calidad']
    pyautogui.moveTo(851 + diff_x, 200 + diff_y, duration=.25) #Clickea boton actualizar
    pyautogui.click()
    
    pyautogui.moveTo(526 + diff_x, 321 + diff_y, duration=.25) #Se mueve al boton cerrar
    pyautogui.click()
    
def test_salir():
    pyautogui.moveTo(151 + diff_x, 511 + diff_y, duration=.25)
    pyautogui.click() 
    
    
def run_testing():
    #pytest.main(['--cov=CRUD', '--cov=interfaz', '--cov-report=term', '--cov-report=html', '-v'])
    pytest.main(['-v', 'test_interfaz_auto.py'])

    
if __name__ == '__main__':
    # Crear la aplicación Tkinter en el hilo principal
    entorno

    # Iniciar las pruebas de GUI en otro hilo separado
    test_thread = threading.Thread(target=run_testing)
    test_thread.start()

    # Iniciar el bucle principal de Tkinter
    root.mainloop()

    # Esperar a que el hilo de las pruebas termine antes de salir completamente
    test_thread.join()