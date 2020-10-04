from connection.conn import Conexion

class Almacen:
    def __init__(self, response):
        self.model = Conexion(response)

    def guardar_producto(self, producto):
        return self.model.insert(producto)

    def obtener_producto(self, id_producto):
        return self.model.get_by_id(id_producto)

    def obtener_productos(self, order):
        return self.model.get_all(order)

    def buscar_productos(self, data_producto):
        return self.model.get_by_column(data_producto)

    def modificar_producto(self, id_producto, data_producto):
        return self.model.update(id_producto, data_producto)

    def eliminar_producto(self, id_producto):
        return self.model.delete(id_producto)
    
    def buscar_producto_like(self, data_producto):
        return self.model.where_like(data_producto)
