# 🛒 Ejercicios Prácticos: Tienda Online con PostgreSQL

## 📋 Ejercicios de Creación de Base de Datos

### Ejercicio 0: Crear la Base de Datos Completa
**Objetivo**: Practicar la creación de bases de datos, tablas, restricciones y la inserción de datos.

#### 0.1 Crear Base de Datos
```sql
-- Crear base de datos de ejemplo
-- Tu código aquí
```

#### 0.2 Crear Tabla de Categorías
```sql
-- Crear tabla de categorías con las siguientes características:
-- - id: SERIAL PRIMARY KEY
-- - nombre: VARCHAR(100) NOT NULL UNIQUE
-- - descripcion: TEXT
-- - activa: BOOLEAN DEFAULT true
-- - fecha_creacion: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

-- Tu código aquí
```

#### 0.3 Crear Tabla de Usuarios
```sql
-- Crear tabla de usuarios con las siguientes características:
-- - id: SERIAL PRIMARY KEY
-- - nombre: VARCHAR(100) NOT NULL
-- - apellido: VARCHAR(100) NOT NULL
-- - email: VARCHAR(255) NOT NULL UNIQUE
-- - password_hash: VARCHAR(255) NOT NULL
-- - fecha_nacimiento: DATE
-- - telefono: VARCHAR(20)
-- - direccion: TEXT
-- - activo: BOOLEAN DEFAULT true
-- - fecha_registro: TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- - ultimo_acceso: TIMESTAMP

-- Tu código aquí
```

#### 0.4 Crear Tabla de Productos
```sql
-- Crear tabla de productos con las siguientes características:
-- - id: SERIAL PRIMARY KEY
-- - nombre: VARCHAR(200) NOT NULL
-- - descripcion: TEXT
-- - precio: DECIMAL(10,2) NOT NULL CHECK (precio > 0)
-- - precio_oferta: DECIMAL(10,2) CHECK (precio_oferta > 0)
-- - stock: INTEGER DEFAULT 0 CHECK (stock >= 0)
-- - categoria_id: INTEGER REFERENCES categorias(id)
-- - imagen_url: VARCHAR(500)
-- - activo: BOOLEAN DEFAULT true
-- - fecha_creacion: TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- - fecha_actualizacion: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

-- Tu código aquí
```

#### 0.5 Crear Tabla de Pedidos
```sql
-- Crear tabla de pedidos con las siguientes características:
-- - id: SERIAL PRIMARY KEY
-- - usuario_id: INTEGER REFERENCES usuarios(id)
-- - fecha_pedido: TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- - estado: VARCHAR(50) DEFAULT 'pendiente' CHECK (estado IN ('pendiente', 'confirmado', 'enviado', 'entregado', 'cancelado'))
-- - total: DECIMAL(10,2) NOT NULL CHECK (total > 0)
-- - direccion_envio: TEXT
-- - notas: TEXT

-- Tu código aquí
```

#### 0.6 Crear Tabla de Detalles de Pedido
```sql
-- Crear tabla de detalles de pedido con las siguientes características:
-- - id: SERIAL PRIMARY KEY
-- - pedido_id: INTEGER REFERENCES pedidos(id)
-- - producto_id: INTEGER REFERENCES productos(id)
-- - cantidad: INTEGER NOT NULL CHECK (cantidad > 0)
-- - precio_unitario: DECIMAL(10,2) NOT NULL CHECK (precio_unitario > 0)
-- - subtotal: DECIMAL(10,2) GENERATED ALWAYS AS (cantidad * precio_unitario) STORED

-- Tu código aquí
```

#### 0.7 Insertar Datos de Ejemplo
```sql
-- Insertar 5 categorías diferentes
-- Tu código aquí

-- Insertar 5 usuarios con datos variados
-- Tu código aquí

-- Insertar 10 productos distribuidos en las categorías
-- Tu código aquí
```

**Solución:**
<details>
<summary>Ver solución completa</summary>

```sql
-- 0.1 Crear base de datos de ejemplo
CREATE DATABASE tienda_online;

-- Conectar a la base de datos
\c tienda_online;

-- 0.2 Crear tabla de categorías
CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT,
    activa BOOLEAN DEFAULT true,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 0.3 Crear tabla de usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE,
    telefono VARCHAR(20),
    direccion TEXT,
    activo BOOLEAN DEFAULT true,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultimo_acceso TIMESTAMP
);

-- 0.4 Crear tabla de productos
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL CHECK (precio > 0),
    precio_oferta DECIMAL(10,2) CHECK (precio_oferta > 0),
    stock INTEGER DEFAULT 0 CHECK (stock >= 0),
    categoria_id INTEGER REFERENCES categorias(id),
    imagen_url VARCHAR(500),
    activo BOOLEAN DEFAULT true,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 0.5 Crear tabla de pedidos
CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id),
    fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(50) DEFAULT 'pendiente' CHECK (estado IN ('pendiente', 'confirmado', 'enviado', 'entregado', 'cancelado')),
    total DECIMAL(10,2) NOT NULL CHECK (total > 0),
    direccion_envio TEXT,
    notas TEXT
);

-- 0.6 Crear tabla de detalles de pedido
CREATE TABLE pedidos_detalle (
    id SERIAL PRIMARY KEY,
    pedido_id INTEGER REFERENCES pedidos(id),
    producto_id INTEGER REFERENCES productos(id),
    cantidad INTEGER NOT NULL CHECK (cantidad > 0),
    precio_unitario DECIMAL(10,2) NOT NULL CHECK (precio_unitario > 0),
    subtotal DECIMAL(10,2) GENERATED ALWAYS AS (cantidad * precio_unitario) STORED
);

-- 0.7 Insertar datos de ejemplo
INSERT INTO categorias (nombre, descripcion) VALUES
('Electrónicos', 'Productos electrónicos y tecnología'),
('Ropa', 'Vestimenta y accesorios'),
('Hogar', 'Artículos para el hogar'),
('Deportes', 'Equipamiento deportivo'),
('Libros', 'Libros y material educativo');

INSERT INTO usuarios (nombre, apellido, email, password_hash, fecha_nacimiento, telefono) VALUES
('Juan', 'Pérez', 'juan.perez@email.com', 'hash123', '1990-05-15', '555-1234'),
('María', 'García', 'maria.garcia@email.com', 'hash456', '1985-08-22', '555-5678'),
('Carlos', 'López', 'carlos.lopez@email.com', 'hash789', '1992-03-10', '555-9012'),
('Ana', 'Martínez', 'ana.martinez@email.com', 'hash101', '1988-11-30', '555-3456'),
('Luis', 'Rodríguez', 'luis.rodriguez@email.com', 'hash112', '1995-07-18', '555-7890');

INSERT INTO productos (nombre, descripcion, precio, stock, categoria_id) VALUES
('Laptop HP Pavilion', 'Laptop de 15 pulgadas con procesador Intel i5', 899.99, 10, 1),
('Smartphone Samsung Galaxy', 'Teléfono inteligente con cámara de 48MP', 599.99, 15, 1),
('Camiseta de Algodón', 'Camiseta 100% algodón, varios colores', 24.99, 50, 2),
('Pantalón Vaquero', 'Pantalón vaquero clásico, tallas S-XXL', 49.99, 30, 2),
('Sofá de 3 Plazas', 'Sofá cómodo para sala de estar', 299.99, 5, 3),
('Mesa de Centro', 'Mesa de centro moderna y elegante', 89.99, 8, 3),
('Balón de Fútbol', 'Balón oficial de competición', 39.99, 20, 4),
('Raqueta de Tenis', 'Raqueta profesional de tenis', 129.99, 12, 4),
('El Señor de los Anillos', 'Trilogía completa en tapa dura', 45.99, 25, 5),
('Aprende SQL', 'Guía completa de SQL para principiantes', 29.99, 40, 5);
```
</details>

---

### Ejercicio 0.8: Verificar la Estructura
**Objetivo**: Verificar que todas las tablas se crearon correctamente.

```sql
-- Listar todas las tablas creadas
-- Tu código aquí

-- Mostrar la estructura de la tabla productos
-- Tu código aquí

-- Verificar las restricciones de la tabla pedidos
-- Tu código aquí

-- Contar registros en cada tabla
-- Tu código aquí
```

**Solución:**
<details>
<summary>Ver solución</summary>

```sql
-- Listar todas las tablas creadas
\dt

-- Mostrar la estructura de la tabla productos
\d productos

-- Verificar las restricciones de la tabla pedidos
SELECT conname, contype, pg_get_constraintdef(oid) 
FROM pg_constraint 
WHERE conrelid = 'pedidos'::regclass;

-- Contar registros en cada tabla
SELECT 'categorias' as tabla, COUNT(*) as total FROM categorias
UNION ALL
SELECT 'usuarios' as tabla, COUNT(*) as total FROM usuarios
UNION ALL
SELECT 'productos' as tabla, COUNT(*) as total FROM productos
UNION ALL
SELECT 'pedidos' as tabla, COUNT(*) as total FROM pedidos
UNION ALL
SELECT 'pedidos_detalle' as tabla, COUNT(*) as total FROM pedidos_detalle;
```
</details>

---

## 🎯 Ejercicios Nivel Básico

### Ejercicio 1: Consultas SELECT Básicas
**Objetivo**: Practicar consultas SELECT simples con WHERE y ORDER BY.

```sql
-- 1.1 Seleccionar todos los usuarios activos
-- Tu código aquí

-- 1.2 Mostrar solo el nombre y email de usuarios que se registraron en 2024
-- Tu código aquí

-- 1.3 Listar productos ordenados por precio de mayor a menor
-- Tu código aquí

-- 1.4 Contar cuántos productos hay en cada categoría
-- Tu código aquí
```

**Solución:**
<details>
<summary>Ver solución</summary>

```sql
-- 1.1 Seleccionar todos los usuarios activos
SELECT * FROM usuarios WHERE activo = true;

-- 1.2 Mostrar solo el nombre y email de usuarios que se registraron en 2024
SELECT nombre, apellido, email 
FROM usuarios 
WHERE EXTRACT(YEAR FROM fecha_registro) = 2024;

-- 1.3 Listar productos ordenados por precio de mayor a menor
SELECT nombre, precio, stock 
FROM productos 
ORDER BY precio DESC;

-- 1.4 Contar cuántos productos hay en cada categoría
SELECT c.nombre as categoria, COUNT(p.id) as total_productos
FROM categorias c
LEFT JOIN productos p ON c.id = p.categoria_id
GROUP BY c.id, c.nombre;
```
</details>

---

### Ejercicio 2: Filtros y Condiciones
**Objetivo**: Practicar diferentes tipos de filtros y condiciones.

```sql
-- 2.1 Productos con precio entre $50 y $200
-- Tu código aquí

-- 2.2 Usuarios cuyo nombre empiece con 'M'
-- Tu código aquí

-- 2.3 Productos que tengan stock menor a 20
-- Tu código aquí

-- 2.4 Categorías que no tengan productos
-- Tu código aquí
```

**Solución:**
<details>
<summary>Ver solución</summary>

```sql
-- 2.1 Productos con precio entre $50 y $200
SELECT nombre, precio, stock
FROM productos
WHERE precio BETWEEN 50 AND 200
ORDER BY precio;

-- 2.2 Usuarios cuyo nombre empiece con 'M'
SELECT nombre, apellido, email
FROM usuarios
WHERE nombre LIKE 'M%';

-- 2.3 Productos que tengan stock menor a 20
SELECT nombre, precio, stock
FROM productos
WHERE stock < 20
ORDER BY stock;

-- 2.4 Categorías que no tengan productos
SELECT c.nombre, c.descripcion
FROM categorias c
LEFT JOIN productos p ON c.id = p.categoria_id
WHERE p.id IS NULL;
```
</details>

---

## 🚀 Ejercicios Nivel Intermedio

### Ejercicio 3: JOINs y Relaciones
**Objetivo**: Practicar diferentes tipos de JOINs entre tablas.

```sql
-- 3.1 Productos con su categoría y stock disponible
-- Tu código aquí

-- 3.2 Usuarios con el total de productos que han comprado
-- Tu código aquí

-- 3.3 Categorías con el producto más caro de cada una
-- Tu código aquí

-- 3.4 Productos que no pertenecen a ninguna categoría
-- Tu código aquí
```

**Solución:**
<details>
<summary>Ver solución</summary>

```sql
-- 3.1 Productos con su categoría y stock disponible
SELECT 
    p.nombre as producto,
    p.precio,
    p.stock,
    c.nombre as categoria
FROM productos p
JOIN categorias c ON p.categoria_id = c.id
WHERE p.activo = true
ORDER BY c.nombre, p.nombre;

-- 3.2 Usuarios con el total de productos que han comprado
SELECT 
    u.nombre,
    u.apellido,
    COUNT(p.id) as total_pedidos
FROM usuarios u
LEFT JOIN pedidos p ON u.id = p.usuario_id
GROUP BY u.id, u.nombre, u.apellido
ORDER BY total_pedidos DESC;

-- 3.3 Categorías con el producto más caro de cada una
SELECT 
    c.nombre as categoria,
    p.nombre as producto_mas_caro,
    p.precio as precio_maximo
FROM categorias c
JOIN productos p ON c.id = p.categoria_id
WHERE p.precio = (
    SELECT MAX(precio) 
    FROM productos p2 
    WHERE p2.categoria_id = c.id
);

-- 3.4 Productos que no pertenecen a ninguna categoría
SELECT p.nombre, p.precio
FROM productos p
LEFT JOIN categorias c ON p.categoria_id = c.id
WHERE c.id IS NULL;
```
</details>

---

### Ejercicio 4: Agregaciones y GROUP BY
**Objetivo**: Practicar funciones de agregación y agrupación.

```sql
-- 4.1 Precio promedio por categoría
-- Tu código aquí

-- 4.2 Total de stock por categoría
-- Tu código aquí

-- 4.3 Usuarios con mayor gasto total
-- Tu código aquí

-- 4.4 Productos con stock crítico (menos de 10 unidades)
-- Tu código aquí
```

**Solución:**
<details>
<summary>Ver solución</summary>

```sql
-- 4.1 Precio promedio por categoría
SELECT 
    c.nombre as categoria,
    ROUND(AVG(p.precio), 2) as precio_promedio,
    COUNT(p.id) as total_productos
FROM categorias c
LEFT JOIN productos p ON c.id = p.categoria_id
GROUP BY c.id, c.nombre
ORDER BY precio_promedio DESC;

-- 4.2 Total de stock por categoría
SELECT 
    c.nombre as categoria,
    SUM(p.stock) as stock_total,
    COUNT(p.id) as productos_con_stock
FROM categorias c
LEFT JOIN productos p ON c.id = p.categoria_id
GROUP BY c.id, c.nombre
ORDER BY stock_total DESC;

-- 4.3 Usuarios con mayor gasto total
SELECT 
    u.nombre,
    u.apellido,
    u.email,
    COALESCE(SUM(p.total), 0) as gasto_total
FROM usuarios u
LEFT JOIN pedidos p ON u.id = p.usuario_id
GROUP BY u.id, u.nombre, u.apellido, u.email
ORDER BY gasto_total DESC;

-- 4.4 Productos con stock crítico (menos de 10 unidades)
SELECT 
    p.nombre,
    p.stock,
    c.nombre as categoria
FROM productos p
JOIN categorias c ON p.categoria_id = c.id
WHERE p.stock < 10
ORDER BY p.stock;
```
</details>

---

## 🎯 Ejercicios Nivel Avanzado

### Ejercicio 5: Subconsultas y EXISTS
**Objetivo**: Practicar subconsultas y operadores EXISTS.

```sql
-- 5.1 Productos más caros que el promedio de su categoría
-- Tu código aquí

-- 5.2 Categorías que tienen al menos 3 productos
-- Tu código aquí

-- 5.3 Usuarios que no han hecho ningún pedido
-- Tu código aquí

-- 5.4 Productos con precio superior al 80% de los productos de su categoría
-- Tu código aquí
```

**Solución:**
<details>
<summary>Ver solución</summary>

```sql
-- 5.1 Productos más caros que el promedio de su categoría
SELECT 
    p.nombre,
    p.precio,
    c.nombre as categoria
FROM productos p
JOIN categorias c ON p.categoria_id = c.id
WHERE p.precio > (
    SELECT AVG(precio) 
    FROM productos p2 
    WHERE p2.categoria_id = p.categoria_id
);

-- 5.2 Categorías que tienen al menos 3 productos
SELECT 
    c.nombre,
    COUNT(p.id) as total_productos
FROM categorias c
JOIN productos p ON c.id = p.categoria_id
GROUP BY c.id, c.nombre
HAVING COUNT(p.id) >= 3;

-- 5.3 Usuarios que no han hecho ningún pedido
SELECT 
    u.nombre,
    u.apellido,
    u.email
FROM usuarios u
WHERE NOT EXISTS (
    SELECT 1 FROM pedidos p WHERE p.usuario_id = u.id
);

-- 5.4 Productos con precio superior al 80% de los productos de su categoría
SELECT 
    p.nombre,
    p.precio,
    c.nombre as categoria
FROM productos p
JOIN categorias c ON p.categoria_id = c.id
WHERE p.precio > (
    SELECT PERCENTILE_CONT(0.8) WITHIN GROUP (ORDER BY precio)
    FROM productos p2 
    WHERE p2.categoria_id = p.categoria_id
);
```
</details>

---

### Ejercicio 6: Funciones de Ventana y CTEs
**Objetivo**: Practicar funciones de ventana y Common Table Expressions.

```sql
-- 6.1 Ranking de productos por precio dentro de cada categoría
-- Tu código aquí

-- 6.2 Productos con mayor diferencia de precio respecto al promedio de su categoría
-- Tu código aquí

-- 6.3 Usuarios con su posición en ranking de gasto total
-- Tu código aquí

-- 6.4 Categorías con productos ordenados por stock usando CTE
-- Tu código aquí
```

**Solución:**
<details>
<summary>Ver solución</summary>

```sql
-- 6.1 Ranking de productos por precio dentro de cada categoría
SELECT 
    p.nombre,
    p.precio,
    c.nombre as categoria,
    ROW_NUMBER() OVER (PARTITION BY c.id ORDER BY p.precio DESC) as ranking_precio
FROM productos p
JOIN categorias c ON p.categoria_id = c.id
ORDER BY c.nombre, ranking_precio;

-- 6.2 Productos con mayor diferencia de precio respecto al promedio de su categoría
SELECT 
    p.nombre,
    p.precio,
    c.nombre as categoria,
    ROUND(p.precio - AVG(p.precio) OVER (PARTITION BY c.id), 2) as diferencia_promedio
FROM productos p
JOIN categorias c ON p.categoria_id = c.id
ORDER BY diferencia_promedio DESC;

-- 6.3 Usuarios con su posición en ranking de gasto total
SELECT 
    u.nombre,
    u.apellido,
    COALESCE(SUM(p.total), 0) as gasto_total,
    RANK() OVER (ORDER BY COALESCE(SUM(p.total), 0) DESC) as ranking_gasto
FROM usuarios u
LEFT JOIN pedidos p ON u.id = p.usuario_id
GROUP BY u.id, u.nombre, u.apellido;

-- 6.4 Categorías con productos ordenados por stock usando CTE
WITH productos_ordenados AS (
    SELECT 
        p.nombre,
        p.stock,
        c.nombre as categoria,
        ROW_NUMBER() OVER (PARTITION BY c.id ORDER BY p.stock DESC) as ranking_stock
    FROM productos p
    JOIN categorias c ON p.categoria_id = c.id
)
SELECT 
    categoria,
    nombre as producto,
    stock,
    ranking_stock
FROM productos_ordenados
ORDER BY categoria, ranking_stock;
```
</details>

---

## 🔧 Ejercicios de Modificación de Datos

### Ejercicio 7: INSERT, UPDATE, DELETE
**Objetivo**: Practicar operaciones de modificación de datos.

```sql
-- 7.1 Insertar una nueva categoría 'Juguetes'
-- Tu código aquí

-- 7.2 Actualizar el precio de todos los productos de electrónicos (aumentar 10%)
-- Tu código aquí

-- 7.3 Desactivar productos con stock 0
-- Tu código aquí

-- 7.4 Eliminar categorías que no tienen productos
-- Tu código aquí
```

**Solución:**
<details>
<summary>Ver solución</summary>

```sql
-- 7.1 Insertar una nueva categoría 'Juguetes'
INSERT INTO categorias (nombre, descripcion) 
VALUES ('Juguetes', 'Juguetes y entretenimiento para todas las edades');

-- 7.2 Actualizar el precio de todos los productos de electrónicos (aumentar 10%)
UPDATE productos 
SET precio = precio * 1.10,
    fecha_actualizacion = CURRENT_TIMESTAMP
WHERE categoria_id = (SELECT id FROM categorias WHERE nombre = 'Electrónicos');

-- 7.3 Desactivar productos con stock 0
UPDATE productos 
SET activo = false,
    fecha_actualizacion = CURRENT_TIMESTAMP
WHERE stock = 0;

-- 7.4 Eliminar categorías que no tienen productos
DELETE FROM categorias 
WHERE id NOT IN (
    SELECT DISTINCT categoria_id 
    FROM productos 
    WHERE categoria_id IS NOT NULL
);
```
</details>

---

## 📊 Ejercicios de Análisis de Datos

### Ejercicio 8: Análisis Complejo
**Objetivo**: Combinar múltiples conceptos en consultas complejas.

```sql
-- 8.1 Dashboard de ventas por categoría con porcentajes
-- Tu código aquí

-- 8.2 Análisis de usuarios por edad y actividad
-- Tu código aquí

-- 8.3 Productos con mejor rendimiento de stock
-- Tu código aquí

-- 8.4 Recomendaciones de productos basadas en categorías populares
-- Tu código aquí
```

**Solución:**
<details>
<summary>Ver solución</summary>

```sql
-- 8.1 Dashboard de ventas por categoría con porcentajes
WITH ventas_categoria AS (
    SELECT 
        c.nombre as categoria,
        COUNT(p.id) as total_productos,
        SUM(p.stock) as stock_total,
        AVG(p.precio) as precio_promedio
    FROM categorias c
    LEFT JOIN productos p ON c.id = p.categoria_id
    GROUP BY c.id, c.nombre
)
SELECT 
    categoria,
    total_productos,
    stock_total,
    ROUND(precio_promedio, 2) as precio_promedio,
    ROUND(
        (total_productos::DECIMAL / SUM(total_productos) OVER()) * 100, 2
    ) as porcentaje_productos
FROM ventas_categoria
ORDER BY total_productos DESC;

-- 8.2 Análisis de usuarios por edad y actividad
SELECT 
    CASE 
        WHEN EXTRACT(YEAR FROM AGE(fecha_nacimiento)) < 25 THEN '18-24'
        WHEN EXTRACT(YEAR FROM AGE(fecha_nacimiento)) < 35 THEN '25-34'
        WHEN EXTRACT(YEAR FROM AGE(fecha_nacimiento)) < 45 THEN '35-44'
        ELSE '45+'
    END as grupo_edad,
    COUNT(*) as total_usuarios,
    ROUND(AVG(EXTRACT(YEAR FROM AGE(fecha_nacimiento))), 1) as edad_promedio
FROM usuarios
WHERE fecha_nacimiento IS NOT NULL
GROUP BY grupo_edad
ORDER BY grupo_edad;

-- 8.3 Productos con mejor rendimiento de stock
SELECT 
    p.nombre,
    p.stock,
    p.precio,
    c.nombre as categoria,
    ROUND((p.precio * p.stock), 2) as valor_inventario,
    ROW_NUMBER() OVER (PARTITION BY c.id ORDER BY (p.precio * p.stock) DESC) as ranking_valor
FROM productos p
JOIN categorias c ON p.categoria_id = c.id
WHERE p.activo = true
ORDER BY c.nombre, ranking_valor;

-- 8.4 Recomendaciones de productos basadas en categorías populares
WITH categorias_populares AS (
    SELECT 
        c.id,
        c.nombre,
        COUNT(p.id) as total_productos,
        RANK() OVER (ORDER BY COUNT(p.id) DESC) as ranking_popularidad
    FROM categorias c
    JOIN productos p ON c.id = p.categoria_id
    GROUP BY c.id, c.nombre
)
SELECT 
    cp.nombre as categoria,
    p.nombre as producto_recomendado,
    p.precio,
    p.stock
FROM categorias_populares cp
JOIN productos p ON cp.id = p.categoria_id
WHERE cp.ranking_popularidad <= 3
  AND p.activo = true
  AND p.stock > 0
ORDER BY cp.ranking_popularidad, p.precio;
```
</details>

---

## 🎉 ¡Felicidades!

Has completado todos los ejercicios de PostgreSQL para la tienda online. Estos ejercicios cubren:

✅ **Nivel Básico**: SELECT, WHERE, ORDER BY, JOINs simples  
✅ **Nivel Intermedio**: Agregaciones, GROUP BY, subconsultas  
✅ **Nivel Avanzado**: Funciones de ventana, CTEs, análisis complejo  
✅ **Modificación de Datos**: INSERT, UPDATE, DELETE  
✅ **Análisis de Datos**: Consultas complejas y dashboards  

### 💡 Consejos para Continuar Aprendiendo:

1. **Practica regularmente** con estos ejercicios
2. **Modifica las consultas** para explorar diferentes resultados
3. **Crea tus propios ejercicios** basados en casos reales
4. **Usa EXPLAIN ANALYZE** para optimizar consultas
5. **Experimenta con índices** para mejorar el rendimiento

### 🔗 Recursos Adicionales:

- [Documentación oficial de PostgreSQL](https://www.postgresql.org/docs/)
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/)
- [SQLZoo](https://sqlzoo.net/) - Ejercicios interactivos de SQL

**¡Sigue practicando y explorando las capacidades de PostgreSQL! 🚀**
