from models.producto import Producto

class IProductoRepository:
    def crear_producto(self, producto: Producto):
        raise NotImplementedError

#Implementación del repositorio de productos
class ProductoRepositoryPosgresSQL(IProductoRepository):

    def crear(self, producto: Producto):
        print("Creating product in PostgreSQL")

    def actualizar(self, producto: Producto):
        print("Creating product in PostgreSQL")

class ProductoRepositoryMongo(IProductoRepository):

    def crear(self, producto: Producto):
        print("Creating product in MongoDB")

    def actualizar(self, producto: Producto):
        print("Creating product in MongoDB")

class AdminControllers:
    def __init__(self, Producto_Repo: IProductoRepository):
        self.producto_repo = Producto_Repo

    def regristrar_producto(self, prodcto: Producto):
        return self.producto_repo.crear(prodcto)
    

producto1 = Producto(1, "Producto 1", "Descripción del producto 1", 100.0, 80.0, 10, 1)

repo_posgres = ProductoRepositoryMongo()

admin_pg = AdminControllers(repo_posgres)

admin_pg.regristrar_producto(producto1)