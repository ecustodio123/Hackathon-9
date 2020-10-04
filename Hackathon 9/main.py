from helpers.menu import Menu
from controllers.rol_controller import Roles_controller
from controllers.almacen_controller import Almacen_controller
from controllers.almacen_total_controller import Almacen_total_controller
from controllers.cajero_controller import Cajero_controller

def iniciar_app():
    try:
        print('''
        ===============================
            Minimarket - El Grupo 03
        ===============================
        ''')
        print("Bienvenido, por favor indique su cargo\n")
        menu_inicio = ["Administrador", "Cajero", "Almacen", "Salir"]
        respuesta = Menu(menu_inicio).show()
        if respuesta == 1:
            rol = Roles_controller()
            rol.inicio_admin()
            if rol.admin:
                menu_principal = ["Actualizar y/o modificar los registros", "Ver Productos", "Ver Reporte de ventas por día", "Ver reporte de ventas por mes", "Salir"]
                respuesta = Menu(menu_principal).show()
                if respuesta == 1:
                    rol = Roles_controller()
                    rol.menu()
                    if rol.salir:
                        iniciar_app()
                elif respuesta == 2:
                    almacen_total = Almacen_total_controller()
                    almacen_total.listar_productos()
                    iniciar_app()
                elif respuesta == 3:
                    cajero = Cajero_controller()
                    cajero.reporte_dia()
                    iniciar_app()
                elif respuesta == 4:
                    cajero = Cajero_controller()
                    cajero.reporte_mes()
                    iniciar_app()

        elif respuesta == 2:
            rol = Roles_controller()
            rol.inicio_cajero()
            if rol.cajero:
                cajero = Cajero_controller()
                cajero.menu()
                if cajero.salir:
                    iniciar_app()
        
        elif respuesta == 3:
            rol = Roles_controller()
            rol.inicio_almacen()
            if rol.almacen:
                almacen = Almacen_controller()
                almacen.menu()
                if almacen.salir:
                    iniciar_app()

        print("\nGracias por utilizar el sistema\n")


    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')

iniciar_app()