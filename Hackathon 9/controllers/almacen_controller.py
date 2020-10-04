from helpers.helper import input_data, print_table, pregunta, input_codigo, input_fecha
from helpers.menu import Menu
from classes.almacen import Almacen
from classes.almacen_total import Almacen_total

class Almacen_controller():
    def __init__(self):
        print("Por favor indique la categoría del producto :")
        menu = ["Frutas", "Verduras", "Abarrotes"]
        respuesta = Menu(menu).show()
        if respuesta == 1:
            response = 'categoria_frutas'
            categoria = 'frutas'
        elif respuesta == 2:
            response = 'categoria_verduras'
            categoria = 'verduras'
        elif respuesta == 3:
            response = 'categoria_abarrotes'
            categoria = 'abarrotes'
        self.almacen = Almacen(response)
        self.almacen_total = Almacen_total()
        self.categoria = categoria
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ================================
                      Almacen del minimarket
                ================================
                ''')
                menu = ['Listar Productos', 'Agregar un nuevo producto', 'Buscar Producto',"Salir"]
                respuesta = Menu(menu).show()

                if respuesta == 1:
                    self.listar_productos()
                elif respuesta == 2:
                    self.insertar_producto()
                elif respuesta == 3:
                    self.buscar_producto()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')
    
    def listar_productos(self):
        print('''
        ========================
            Lista de Productos
        ========================
        ''')
        productos = self.almacen.obtener_productos('id_producto')
        print(print_table(productos, ['ID', 'Código del producto', 'Nombre', 'Precio por unidad', 'Cantidad']))
        input("\nPresione una tecla para continuar...")

    def insertar_producto(self):
        codigo = input_codigo()
        producto = input_data("Ingrese el nombre del producto >> " )
        precio_por_unidad = input_data("Ingrese el precio del producto >> ", "float")
        cantidad = input_data("Ingrese la cantidad de productos en stock >> ", "int")
        self.almacen.guardar_producto({
            'codigo' : codigo,
            'producto' : producto,
            'precio_por_unidad' : precio_por_unidad,
            'cantidad' : cantidad
        })
        print('''
        ==============================
            Nuevo Producto agregado !
        ==============================
        ''')
        #Ingreso a la tbala almacen
        self.almacen_total.guardar_almacen({
            'codigo' : codigo,
            'producto' : producto,
            'precio_por_unidad' : precio_por_unidad,
            'cantidad' : cantidad,
            'categoria' :  self.categoria
        })
        self.listar_productos()

    def buscar_producto(self):
        print('''
        =====================
            Buscar Producto
        =====================
        ''')
        try:
            id_producto = input_data("Ingrese el ID del Producto >> ", "int")
            producto = self.almacen.obtener_producto({'id_producto' : id_producto})
            print(print_table(producto, ['ID', 'Código del producto', 'Nombre', 'Precio por unidad', 'Cantidad']))

            if producto:
                if pregunta("¿Deseas dar mantenimiento al producto?"):
                    opciones = ['Editar producto', 'Eliminar producto', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_producto(id_producto, producto)
                    elif respuesta == 2:
                        self.eliminar_producto(id_producto, producto)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def editar_producto(self, id_producto, producto):
        producto_nuevo = input_data("Ingrese el nuevo nombre del producto >> " )
        precio_por_unidad = input_data("Ingrese el nuevo precio del producto >> ", "float")
        cantidad = input_data("Ingrese la nueva cantidad de productos en stock >> ", "int")

        self.almacen.modificar_producto({
            'id_producto' : id_producto
        }, {
            'producto' : producto_nuevo,
            'precio_por_unidad' : precio_por_unidad,
            'cantidad' : cantidad
        })

        ##################ALMACEN#####################
        producto = self.almacen_total.buscar_almacen_like(producto[2])

        self.almacen_total.modificar_almacen({
            'id_almacen' : producto[0]
        }, {
            'producto' : producto_nuevo,
            'precio_por_unidad' : precio_por_unidad,
            'cantidad' : cantidad
        })
        ##################ALMACEN#####################

        print('''
        ========================
            Producto Editado !
        ========================
        ''')     

    def eliminar_producto(self, id_producto, producto):
        self.almacen.eliminar_producto({
            'id_producto' : id_producto
        })
        producto = self.almacen_total.buscar_almacen_like(producto[2])
        self.almacen_total.eliminar_almacen({
            'id_almacen' : producto[0]
        })
        print('''
        ========================
            Producto Eliminado !
        ========================
        ''')