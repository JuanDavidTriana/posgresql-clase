import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="tienda_online",
    user="postgres",
    password="Admin",
    port="5432"
    )

cursor = conn.cursor()

#CREATE

def crear_usuario(nombre,apellido,email,password_hash, fecha_nacimiento,telefono,direccion):
    try:
        query = """
        INSERT INTO usuarios (nombre, apellido, email, password_hash, fecha_nacimiento, telefono, direccion) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nombre, apellido, email, password_hash, fecha_nacimiento, telefono, direccion))
        conn.commit()
        print("Usuario creado exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al crear el usuario: {e}")
        conn.rollback()

#crear_usuario("Duvan","Salas","DuvanSalas@gmail.com","$2b$12$KIXQJfFz8eG1Z5Z5Z5Z5eO","1999-12-01", "1234567890","Calle Falsa 123" )

#READ
def leer_usuarios():
    try:
        query = "SELECT * FROM usuarios;"
        cursor.execute(query)
        for fila in cursor.fetchall():
            print(fila)

    except psycopg2.Error as e:
        print("Error al consultar los usuarios")

leer_usuarios()

#UDPATE
def actulizar_objeto_usuario(id, objeto, nuevo_valor):
    try:
        query = f"UPDATE usuarios SET {objeto} = %s WHERE id = %s"
        cursor.execute(query, (nuevo_valor, id))
        conn.commit()
        print("Objeto actualizado exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al actualizar el objeto: {e}")
        conn.rollback()

#actulizar_objeto_usuario(1, "telefono", "0987654321")

#DELETE
def eliminar_usuario(id):
    try:
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
        conn.commit()
        print("Usuario eliminado")
    except psycopg2.Error as e:
        print(f"Error al eliminar el usuario: {e}")
        conn.rollback()

#eliminar_usuario(1)