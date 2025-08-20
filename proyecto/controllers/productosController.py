from repository.productosRepository import ProductosRepository  
from models.producto import Producto

class ProductosController:

    def __init__(self):
        self.productos_repo = ProductosRepository()

    def crear_producto(self, producto: Producto) -> bool:
        try:
            return self.productos_repo.create(producto)
        except Exception as e:
            raise Exception(f"Error al crear producto: {e}")
        
    def obtener_producto_por_id(self, producto_id: int) -> Producto:
        try:
            return self.productos_repo.find_by_id(producto_id)
        except Exception as e:
            raise Exception(f"Error al obtener producto por ID: {e}")
        
    def obtener_todos_los_productos(self) -> list:
        try:
            return self.productos_repo.find_all()
        except Exception as e:
            raise Exception(f"Error al obtener todos los productos: {e}")
        
    def actualizar_producto(self, producto: Producto) -> bool:
        try:
            return self.productos_repo.update(producto)
        except Exception as e:
            raise Exception(f"Error al actualizar producto: {e}")
        
    def eliminar_producto(self, producto_id: int) -> bool:
        try:
            return self.productos_repo.delete(producto_id)
        except Exception as e:
            raise Exception(f"Error al eliminar producto: {e}")