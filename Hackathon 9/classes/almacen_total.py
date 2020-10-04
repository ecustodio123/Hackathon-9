from connection.conn import Conexion

class Almacen_total:
    def __init__(self):
        self.model = Conexion('almacen')

    def guardar_almacen(self, almacen):
        return self.model.insert(almacen)

    def obtener_almacen(self, id_almacen):
        return self.model.get_by_id(id_almacen)

    def obtener_almacenes(self, order):
        return self.model.get_all(order)

    def buscar_almacenes(self, data_almacen):
        return self.model.get_by_column(data_almacen)

    def modificar_almacen(self, id_almacen, data_almacen):
        return self.model.update(id_almacen, data_almacen)

    def eliminar_almacen(self, id_almacen):
        return self.model.delete(id_almacen)
    
    def buscar_almacen_like(self, data_almacen):
        return self.model.where_like(data_almacen)
