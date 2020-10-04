from helpers.helper import input_data, print_table, pregunta, input_codigo, input_fecha, ingresar_dni, nombre_mes
from helpers.menu import Menu
from classes.cajero import Cajero
from controllers.almacen_total_controller import Almacen_total_controller
from controllers.almacen_controller import Almacen_controller
from classes.almacen import Almacen
from classes.almacen_total import Almacen_total

class Cajero_controller:
    def __init__(self):
        self.cajero = Cajero()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ================================
                    Ventas - Minimarket Grupo 03
                ================================
                ''')
                menu = ['Listar ventas', 'Buscar venta', "Nueva venta", "Reporte por día", "Reporte por mes", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_ventas()
                elif respuesta == 2:
                    self.buscar_venta()
                elif respuesta == 3:
                    self.insertar_venta()
                elif respuesta == 4:
                    self.reporte_dia()
                elif respuesta == 5:
                    self.reporte_mes()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_ventas(self):
        print('''
        ========================
            Lista de ventas
        ========================
        ''')
        ventas = self.cajero.obtener_ventas('id_ventas')
        print(print_table(ventas, ['ID', 'DNI', 'Producto', 'Cantidad de productos comprados', 'Precio Total', 'Fecha', 'Mes de la venta']))
        input("\nPresione una tecla para continuar...")

    def buscar_venta(self):
        print('''
        =====================
            Buscar Venta
        =====================
        ''')
        try:
            id_ventas = input_data("Ingrese el ID de la venta >> ", "int")
            venta = self.cajero.buscar_ventas({'id_ventas': id_ventas})
            print(print_table(venta, ['ID', 'DNI', 'Producto', 'Cantidad de productos comprados', 'Precio Total', 'Fecha', 'Mes de la venta']))

            if venta:
                if pregunta("¿Deseas actualizar datos de la venta?"):
                    opciones = ['Editar Venta', 'Eliminar Venta', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_venta(id_ventas)
                    elif respuesta == 2:
                        self.eliminar_venta(id_ventas)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_venta(self):
        dni = ingresar_dni()
        existe = True
        while existe:
            producto = input_data("\nIngrese el nombre del producto >> " )
            almacen_total = Almacen_total_controller()
            existe = almacen_total.verificar_producto(producto, existe)

        cantidad = True
        while cantidad:
            cantidad_comprada = input_data("\nIngrese la cantidad de productos comprados >> ", "int" )
            cantidad = almacen_total.verificar_cantidad(producto, cantidad_comprada, cantidad)

        fecha = input_fecha()
        fecha_fin = fecha.split('/')
        mes = fecha_fin[1]
        print(mes)
        mes = nombre_mes(mes)
        print(mes)

        ###############Actualizar Registros############################
        almacen_total = Almacen_total()
        producto_1 = almacen_total.buscar_almacen_like(producto)
        categoria = producto_1[5]
        precio_unitario = producto_1[3]
        precio_total = precio_unitario * cantidad_comprada

        cantidad_nueva = producto_1[4] - cantidad_comprada

        almacen_total.modificar_almacen({
            'id_almacen' : producto_1[0]
        }, {
            'cantidad' : cantidad_nueva
        })
        
        if categoria == 'frutas':
            categoria_fin = 'categoria_frutas'
        elif categoria == 'verduras':
            categoria_fin = 'categoria_verduras'
        elif categoria == 'abarrotes':
            categoria_fin = 'categoria_abarrotes'
        


        almacen = Almacen(categoria_fin)
        producto_2 =  almacen.buscar_producto_like(producto)

        almacen.modificar_producto({
            'id_producto' : producto_2[0]
        }, {
            'cantidad' : cantidad_nueva
        })
        ###############Actualizar Registros############################


        self.cajero.guardar_venta({
            'dni': dni,
            'producto' : producto,
            'cantidad_comprada' : cantidad_comprada,
            'precio_total' : precio_total,
            'fecha' : fecha,
            'mes_venta' : mes
        })
        print('''
        ==============================
            Nueva Venta agregada !
        ==============================
        ''')
        self.listar_ventas()

    def editar_venta(self, id_ventas):
        precio_total = input_data("Ingrese el nuevo precio total de la venta >> ", "float")
        fecha = input_fecha()
        fecha_fin = fecha.split('/')
        mes = fecha_fin[1]
        mes = nombre_mes(mes)

        self.cajero.modificar_venta({
            'id_ventas': id_ventas
        }, {
            'precio_total': precio_total,
            'fecha' : fecha,
            'mes_venta' : mes
        })
        print('''
        ========================
            Venta Editada !
        ========================
        ''')

    def eliminar_venta(self, id_ventas):
        self.cajero.eliminar_venta({
            'id_ventas': id_ventas
        })
        print('''
        ========================
            Venta Eliminada !
        ========================
        ''')
    
    def reporte_dia(self):
        fecha = input_fecha()
        ventas = self.cajero.ver_por_dia(fecha)
        print(print_table(ventas, ['ID', 'DNI', 'Producto', 'Cantidad de productos comprados', 'Precio Total', 'Fecha', 'Mes de la venta']))

    def reporte_mes(self):
        menu = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        respuesta = Menu(menu).show()
        if respuesta == 1:
            ventas = self.cajero.ver_por_mes('enero')
            print(print_table(ventas, ['ID', 'DNI', 'Producto', 'Cantidad de productos comprados', 'Precio Total', 'Fecha', 'Mes de la venta']))
        elif respuesta == 2:
            ventas = self.cajero.ver_por_mes('febrero')
            print(print_table(ventas, ['ID', 'DNI', 'Producto', 'Cantidad de productos comprados', 'Precio Total', 'Fecha', 'Mes de la venta']))
        elif respuesta == 3:
            ventas = self.cajero.ver_por_mes('marzo')
            print(print_table(ventas, ['ID', 'DNI', 'Producto', 'Cantidad de productos comprados', 'Precio Total', 'Fecha', 'Mes de la venta']))
        elif respuesta == 4:
            ventas = self.cajero.ver_por_mes('abril')
            print(print_table(ventas, ['ID', 'DNI', 'Producto', 'Cantidad de productos comprados', 'Precio Total', 'Fecha', 'Mes de la venta']))
        elif respuesta == 5:
            ventas = self.cajero.ver_por_mes('mayo')
            print(print_table(ventas, ['ID', 'DNI', 'Producto', 'Cantidad de productos comprados', 'Precio Total', 'Fecha', 'Mes de la venta']))
        elif respuesta == 6:
            ventas = self.cajero.ver_por_mes('junio')
            print(print_table(ventas, ['ID', 'DNI', 'Producto', 'Cantidad de productos comprados', 'Precio Total', 'Fecha', 'Mes de la venta']))
        elif respuesta == 7:
            ventas = self.cajero.ver_por_mes('julio')
            print(print_table(ventas, ['ID', 'DNI', 'Producto', 'Cantidad de productos comprados', 'Precio Total', 'Fecha', 'Mes de la venta']))
        elif respuesta == 8:
            ventas = self.cajero.ver_por_mes('agosto')
            print(print_table(ventas, ['ID', 'DNI', 'Producto', 'Cantidad de productos comprados', 'Precio Total', 'Fecha', 'Mes de la venta']))
        elif respuesta == 9:
            ventas = self.cajero.ver_por_mes('septiembre')
            print(print_table(ventas, ['ID', 'DNI', 'Producto', 'Cantidad de productos comprados', 'Precio Total', 'Fecha', 'Mes de la venta']))
        elif respuesta == 10:
            ventas = self.cajero.ver_por_mes('octubre')
            print(print_table(ventas, ['ID', 'DNI', 'Producto', 'Cantidad de productos comprados', 'Precio Total', 'Fecha', 'Mes de la venta']))
        elif respuesta == 11:
            ventas = self.cajero.ver_por_mes('noviembre')
            print(print_table(ventas, ['ID', 'DNI', 'Producto', 'Cantidad de productos comprados', 'Precio Total', 'Fecha', 'Mes de la venta']))
        elif respuesta == 12:
            ventas = self.cajero.ver_por_mes('diciembre')
            print(print_table(ventas, ['ID', 'DNI', 'Producto', 'Cantidad de productos comprados', 'Precio Total', 'Fecha', 'Mes de la venta']))
        else:
            self.salir = True