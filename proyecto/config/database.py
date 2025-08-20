import psycopg2

class DataBaseConfig:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="tienda_online",
            user="postgres",
            password="Admin",
            host="localhost",
            port="5432"
        )
        self.cursor = self.conn.cursor()

    def get_connection(self):
        return self.conn

    def get_cursor(self):
        return self.cursor
    
    def commit(self): #Comit para guardar cambios sean hechos en la base de datos
        self.conn.commit()

    def fetch_all(self): # Para obtener todos los resultados de una consulta
        return self.cursor.fetchall()
    
    def close(self): # Cerrar la conexión y el cursor
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()