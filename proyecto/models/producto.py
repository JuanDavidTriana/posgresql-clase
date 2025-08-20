class Producto:
    def __init__(self, id, nombre, descripcion, precio, precio_oferta,stock,categoria_id):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.precio_oferta = precio_oferta
        self.stock = stock
        self.categoria_id = categoria_id

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'precio_oferta': self.precio_oferta,
            'stock': self.stock,
            'categoria_id': self.categoria_id,
        }
