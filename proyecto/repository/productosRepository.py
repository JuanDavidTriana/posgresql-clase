from typing import List, Dict, Any, Optional
from .baseRepository import BaseRepository
from models.producto import Producto

class ProductosRepository(BaseRepository):

    def create(self, producto: Producto) -> bool:
        try:

            query = """
            INSERT INTO productos (nombre, descripcion, precio, precio_oferta, stock, categoria_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            
            params = (
                    producto.nombre, 
                    producto.descripcion, 
                    producto.precio, 
                    producto.precio_oferta, 
                    producto.stock, 
                    producto.categoria_id
                )
            
            return self.execute_query(query, params)
        except Exception as e:
            raise Exception(f"Error al crear producto {e}")
        
    def find_by_id(self, producto_id: int) -> Optional[Producto]:
        try: 
            query = "SELECT * FROM productos WHERE id = %s"
            result = self.execute_query(query, (producto_id,))
            
            result = self.execute_query_one(query, (producto_id,))

            if result:
                return Producto(*result)
            
            return None
        except Exception as e:
            raise Exception(f"Error al buscar producto por ID {e}")
        
    def find_all(self) -> List[Producto]:
        try:
            query = "SELECT * FROM productos"
            results = self.execute_query(query)
            
            return [Producto(*row) for row in results]
        except Exception as e:
            raise Exception(f"Error al obtener todos los productos {e}")
        
    def update(self, producto: Producto) -> bool:
        try:
            query = """
            UPDATE productos 
            SET nombre = %s, descripcion = %s, precio = %s, precio_oferta = %s, stock = %s, categoria_id = %s
            WHERE id = %s
            """
            params = (
                producto.nombre, 
                producto.descripcion, 
                producto.precio, 
                producto.precio_oferta, 
                producto.stock, 
                producto.categoria_id,
                producto.id
            )
            
            return self.execute_query(query, params)
        except Exception as e:
            raise Exception(f"Error al actualizar producto {e}")
        
    def delete(self, producto_id: int) -> bool:
        try:
            query = "DELETE FROM productos WHERE id = %s"
            return self.execute_query(query, (producto_id,))
        except Exception as e:
            raise Exception(f"Error al eliminar producto {e}")
