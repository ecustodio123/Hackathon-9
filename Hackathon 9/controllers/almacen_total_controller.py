from helpers.helper import input_data, print_table, pregunta, input_codigo, input_fecha
from helpers.menu import Menu
from classes.almacen_total import Almacen_total

class Almacen_total_controller():
    def __init__(self):
        self.almacen_total = Almacen_total()
        self.salir = False

    def listar_productos(self):
        print('''
        ========================
            Lista de Productos
        ========================
        ''')
        productos = self.almacen_total.obtener_almacenes('categoria')
        print(print_table(productos, ['ID', 'Código del producto', 'Nombre', 'Precio por unidad', 'Cantidad', 'Categoria']))
        print("\nUsted solo puede ver los productos\n")
        input("\nPresione una tecla para continuar...")

    def verificar_producto(self, producto, existe):
        ##################ALMACEN#####################
        producto = self.almacen_total.buscar_almacen_like(producto)
        if producto == None:
            print("\nEl producto no existe")
            return True
        else:
            return False    

    def verificar_cantidad(self, producto, cantidad_comprada, cantidad):
        producto = self.almacen_total.buscar_almacen_like(producto)
        if cantidad_comprada > producto[4]:
            print(f"\nNo tenemos suficientes {producto[2]} en stock, solo tenemos {producto[4]}")
            return True
        else:
            return False
