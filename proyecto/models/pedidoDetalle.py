class DetallePedido:

    def __init__(self, id, pedido_id, producto_id, cantidad, precio_unitario,subtotal):
        self.id = id
        self.pedido_id = pedido_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = subtotal

    def to_dict(self):
        return {
            'id': self.id,
            'pedido_id': self.pedido_id,
            'producto_id': self.producto_id,
            'cantidad': self.cantidad,
            'precio_unitario': self.precio_unitario,
            'subtotal': self.subtotal
        }
