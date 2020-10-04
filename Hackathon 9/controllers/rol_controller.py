from helpers.helper import input_data, print_table, pregunta, input_codigo, input_fecha, cargo
from helpers.menu import Menu
from classes.rol import Rol
import getpass

class Roles_controller:
    def __init__(self):
        self.rol = Rol()
        self.admin = False
        self.cajero = False
        self.almacen = False
        self.salir = False
    
    def inicio_admin(self):
        while True:
            try:
                usuario = input_data("\nIntroduzca su usuario >> ")
                contrasena = getpass.getpass("\nIntroduzca su contraseña >> ")
                # contrasena = input_data("\nIntroduzca su contraseña >> ")
                usuario_verificado = self.rol.buscar_usuario(usuario)
                if not usuario_verificado:
                    print('\nEl Usuario elegido no existe !')
                elif contrasena != usuario_verificado[2]:
                    print("\nHa introducido mal la contraseña. Intentelo nuevamente")
                elif "admin" != usuario_verificado[3]:
                    print("\nUsted no tiene permiso de administrador")
                elif contrasena == usuario_verificado[2]:
                    print(f'''
        ======================================
                Bienvenido {usuario_verificado[1]}
        ======================================
                    ''')
                    self.admin = True
                    break
            except Exception as e:
                print(f'{str(e)}')
    
    def inicio_cajero(self):
        while True:
            try:
                usuario = input_data("\nIntroduzca su usuario >> ")
                contrasena = getpass.getpass("\nIntroduzca su contraseña >> ")
                # contrasena = input_data("\nIntroduzca su contraseña >> ")
                usuario_verificado = self.rol.buscar_usuario(usuario)
                if not usuario_verificado:
                    print('\nEl Usuario elegido no existe !')
                elif contrasena != usuario_verificado[2]:
                    print("\nHa introducido mal la contraseña. Intentelo nuevamente")
                elif "cajero" != usuario_verificado[3]:
                    print("\nUsted no tiene permiso de cajero")
                elif contrasena == usuario_verificado[2]:
                    print(f'''
        ======================================
                Bienvenido {usuario_verificado[1]}
        ======================================
                    ''')
                    self.cajero = True
                    break
            except Exception as e:
                print(f'{str(e)}')
    
    def inicio_almacen(self):
        while True:
            try:
                usuario = input_data("\nIntroduzca su usuario >> ")
                contrasena = getpass.getpass("\nIntroduzca su contraseña >> ")
                # contrasena = input_data("\nIntroduzca su contraseña >> ")
                usuario_verificado = self.rol.buscar_usuario(usuario)
                if not usuario_verificado:
                    print('\nEl Usuario elegido no existe !')
                elif contrasena != usuario_verificado[2]:
                    print("\nHa introducido mal la contraseña. Intentelo nuevamente")
                elif "almacen" != usuario_verificado[3]:
                    print("\nUsted no tiene permiso de almacen")
                elif contrasena == usuario_verificado[2]:
                    print(f'''
        ======================================
                Bienvenido {usuario_verificado[1]}
        ======================================
                    ''')
                    self.almacen = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def menu(self):
        while True:
            try:
                print('''
                =================
                    Registros
                =================
                ''')
                menu = ['Listar Registros', 'Buscar Registro', "Nuevo Registro", "Salir"]
                respuesta = Menu(menu).show()

                if respuesta == 1:
                    self.listar_registros()
                elif respuesta == 2:
                    self.buscar_registro()
                elif respuesta == 3:
                    self.insertar_registro()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')
    
    def listar_registros(self):
        print('''
        ==========================
            Lista de Registros
        ==========================
        ''')
        roles = self.rol.obtener_roles('id_rol')
        print(print_table(roles, ['ID', 'Nombre', 'contraseña', 'Cargo accedido']))
        input("\nPresione una tecla para continuar...")

    def insertar_registro(self):
        nombre = input_data("Ingrese el nombre de la persona que está registrando>> " )
        contrasena = input_data("Ingrese la contraseña dada para el usuario que está creando >> ")
        contrasena2 = input_data("Vuelva a introducir la contraseña >> ")
        if (contrasena != contrasena2):
            print("\nLas contraseñas no coinciden, por favor verificar bien")
            return
        cargo_final = cargo("¿Deseas darle cargo de administrador, cajero o almacen")
        # print(cargo_final)
        self.rol.guardar_rol({
            'nombre' : nombre,
            'contrasena' : contrasena,
            'cargo' : cargo_final
        })
        print('''
        =================================
            Nuevo registro agregado !
        =================================
        ''')
        self.listar_registros()

    def buscar_registro(self):
        print('''
        =======================
            Buscar Registro
        =======================
        ''')
        try:
            id_rol = input_data("Ingrese el ID del registro que está buscando >> ", "int")
            rol = self.rol.obtener_rol({'id_rol' : id_rol})
            print(print_table(rol, ['ID', 'Nombre', 'contraseña', 'Cargo accedido']))

            if rol:
                if pregunta("¿Deseas dar mantenimiento al Registro?"):
                    opciones = ['Editar Registro', 'Eliminar Registro', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_registro(id_rol)
                    elif respuesta == 2:
                        self.eliminar_registro(id_rol)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def editar_registro(self, id_rol):
        nombre = input_data("Ingrese el nombre de la persona que está registrando>> " )
        contrasena = input_data("Ingrese la contraseña dada para el usuario que está creando >> ")
        contrasena2 = input_data("Vuelva a introducir la contraseña >> ")
        if (contrasena != contrasena2):
            print("\nLas contraseñas no coinciden, por favor verificar bien")
        cargo_final = cargo("¿Deseas darle cargo de administrador, cajero o almacen?")
        print(cargo_final)
        self.rol.modificar_rol({
            'id_rol' : id_rol
        }, {
            'nombre' : nombre,
            'contrasena' : contrasena,
            'cargo' : cargo_final
        })
        print('''
        ========================
            Registro Editado !
        ========================
        ''')     

    def eliminar_registro(self, id_rol):
        self.rol.eliminar_rol({
            'id_rol' : id_rol
        })
        print('''
        ============================
            Registro Eliminado !
        ============================
        ''')




    