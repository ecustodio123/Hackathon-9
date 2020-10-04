from connection.conn import Conexion

class Rol:
    def __init__(self):
        self.model = Conexion('roles')

    def guardar_rol(self, rol):
        return self.model.insert(rol)

    def obtener_rol(self, id_libro):
        return self.model.get_by_id(id_libro)

    def obtener_roles(self, order):
        return self.model.get_all(order)

    def buscar_roles(self, data_rol):
        return self.model.get_by_column(data_rol)

    def modificar_rol(self, id_rol, data_rol):
        return self.model.update(id_rol, data_rol)

    def eliminar_rol(self, id_rol):
        return self.model.delete(id_rol)
    
    def buscar_rol_like(self, data_rol):
        return self.model.where_like(data_rol)

    def buscar_usuario(self, data):
        return self.model.where_name(data)
