class Pepidos:
    def __init__(self, id, usuario_id, fecha_pedido, estado, total, direccion_envio,nota):
        self.id = id
        self.usuario_id = usuario_id
        self.fecha_pedido = fecha_pedido
        self.estado = estado
        self.total = total
        self.direccion_envio = direccion_envio
        self.nota = nota

    def to_dict(self):
        return {
            'id': self.id,
            'usuario_id': self.usuario_id,
            'fecha_pedido': self.fecha_pedido,
            'estado': self.estado,
            'total': self.total,
            'direccion_envio': self.direccion_envio,
            'nota': self.nota
        }
