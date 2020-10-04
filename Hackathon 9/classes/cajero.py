from connection.conn import Conexion

class Cajero:
    def __init__(self):
        self.model = Conexion('ventas')

    def guardar_venta(self, venta):
        return self.model.insert(venta)

    def obtener_venta(self, id_venta):
        return self.model.get_by_id(id_venta)

    def obtener_ventas(self, order):
        return self.model.get_all(order)

    def buscar_ventas(self, data_venta):
        return self.model.get_by_column(data_venta)

    def modificar_venta(self, id_venta, data_venta):
        return self.model.update(id_venta, data_venta)

    def eliminar_venta(self, id_ventas):
        return self.model.delete(id_ventas)
    
    def ver_por_dia(self, fecha):
        return self.model.where_dia(fecha)
    
    def ver_por_mes(self, mes):
        return self.model.where_mes(mes)
