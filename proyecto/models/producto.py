class Productos:
    def __init__(self, id, nombre, descripcion, precio, precio_oferta,stock,categoria_id,img_url):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.precio_oferta = precio_oferta
        self.stock = stock
        self.categoria_id = categoria_id
        self.img_url = img_url
