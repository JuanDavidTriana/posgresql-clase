from config.database import DataBaseConfig


class AdminControllers:
    def __init__(self):
        self.db = DataBaseConfig()

    #Gestión de productos
    def crear_producto(self, nombre, descripcion, precio, precio_oferta, stock, categoria_id):
        query = """
        INSERT INTO productos (nombre, descripcion, precio, precio_oferta, stock, categoria_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.db.get_cursor().execute(query, (nombre, descripcion, precio, precio_oferta, stock, categoria_id))
        self.db.commit()    
