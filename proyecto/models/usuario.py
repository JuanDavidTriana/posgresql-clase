class Usurios:
    def __init__(self, id, nombre, apellido, email, password_hash, fecha_nacimiento, telefono, direccion):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password_hash = password_hash
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.direccion = direccion

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'password_hash': self.password_hash,
            'fecha_nacimiento': self.fecha_nacimiento,
            'telefono': self.telefono,
            'direccion': self.direccion
        }
