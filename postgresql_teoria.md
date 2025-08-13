# 🐘 PostgreSQL: Teoría Completa

## 📖 Índice
1. [¿Qué es PostgreSQL?](#qué-es-postgresql)
2. [Arquitectura de PostgreSQL](#arquitectura-de-postgresql)
3. [Tipos de Datos](#tipos-de-datos)
4. [Creación de Bases de Datos](#creación-de-bases-de-datos)
5. [Tablas y Restricciones](#tablas-y-restricciones)
6. [Normalización](#normalización)
7. [Índices](#índices)
8. [Transacciones](#transacciones)
9. [Procedimientos Almacenados](#procedimientos-almacenados)
10. [Triggers](#triggers)
11. [Vistas](#vistas)
12. [Seguridad](#seguridad)

---

## 🎯 ¿Qué es PostgreSQL?

**PostgreSQL** es un sistema de gestión de bases de datos relacional (RDBMS) de código abierto, desarrollado por la Universidad de California en Berkeley. Es conocido por su robustez, escalabilidad y cumplimiento de estándares SQL.

### ✨ Características Principales
- **ACID Compliance**: Garantiza Atomicidad, Consistencia, Aislamiento y Durabilidad
- **Extensible**: Permite crear tipos de datos personalizados
- **Multiplataforma**: Funciona en Windows, Linux, macOS
- **Concurrencia**: Maneja múltiples usuarios simultáneamente
- **Integridad**: Validación de datos y restricciones avanzadas

---

## 🏗️ Arquitectura de PostgreSQL

### Componentes Principales

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Cliente       │    │   Servidor      │    │   Almacenamiento│
│   (psql, pgAdmin)│◄──►│   PostgreSQL    │◄──►│   Disco        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Procesos del Servidor
1. **Postmaster**: Proceso principal que gestiona conexiones
2. **Backend Processes**: Un proceso por cada conexión de cliente
3. **Background Processes**: Procesos de mantenimiento automático

---

## 📊 Tipos de Datos

### Tipos Numéricos
```sql
-- Enteros
SMALLINT     -- 2 bytes, -32,768 a 32,767
INTEGER      -- 4 bytes, -2,147,483,648 a 2,147,483,647
BIGINT       -- 8 bytes, -9,223,372,036,854,775,808 a 9,223,372,036,854,775,807

-- Decimales
DECIMAL(p,s) -- Precisión p, escala s
NUMERIC(p,s) -- Sinónimo de DECIMAL
REAL         -- 6 dígitos decimales
DOUBLE PRECISION -- 15 dígitos decimales

-- Serial (Auto-incremento)
SERIAL       -- INTEGER con auto-incremento
BIGSERIAL    -- BIGINT con auto-incremento
```

### Tipos de Texto
```sql
CHAR(n)      -- Caracteres de longitud fija n
VARCHAR(n)   -- Caracteres de longitud variable hasta n
TEXT         -- Longitud ilimitada
```

### Tipos de Fecha y Hora
```sql
DATE         -- Solo fecha (YYYY-MM-DD)
TIME         -- Solo hora (HH:MM:SS)
TIMESTAMP    -- Fecha y hora
TIMESTAMPTZ  -- Fecha y hora con zona horaria
INTERVAL     -- Intervalo de tiempo
```

### Tipos Booleanos y Especiales
```sql
BOOLEAN      -- true/false
UUID         -- Identificador único universal
JSON         -- Datos JSON
JSONB        -- JSON binario (más eficiente)
ARRAY        -- Arrays de cualquier tipo
```

---

## 🗄️ Creación de Bases de Datos

### Comandos Básicos
```sql
-- Conectar a PostgreSQL
psql -U username -d database_name

-- Crear base de datos
CREATE DATABASE nombre_base_datos;

-- Listar bases de datos
\l

-- Conectar a una base de datos
\c nombre_base_datos

-- Listar tablas
\dt

-- Salir
\q
```

### Usuarios y Permisos
```sql
-- Crear usuario
CREATE USER nombre_usuario WITH PASSWORD 'password';

-- Otorgar permisos
GRANT ALL PRIVILEGES ON DATABASE nombre_base_datos TO nombre_usuario;

-- Revocar permisos
REVOKE ALL PRIVILEGES ON DATABASE nombre_base_datos FROM nombre_usuario;
```

---

## 📋 Tablas y Restricciones

### Creación de Tablas
```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT true
);
```

### Tipos de Restricciones
```sql
-- PRIMARY KEY: Identificador único
id INTEGER PRIMARY KEY

-- FOREIGN KEY: Referencia a otra tabla
usuario_id INTEGER REFERENCES usuarios(id)

-- NOT NULL: Campo obligatorio
nombre VARCHAR(100) NOT NULL

-- UNIQUE: Valor único
email VARCHAR(255) UNIQUE

-- CHECK: Validación personalizada
edad INTEGER CHECK (edad >= 18)

-- DEFAULT: Valor por defecto
fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
```

### Explicación Detallada de NOT NULL y CURRENT_TIMESTAMP

#### NOT NULL
La restricción `NOT NULL` asegura que una columna **nunca pueda contener valores nulos (NULL)**. Esto significa que:
- **Es obligatorio** proporcionar un valor al insertar registros
- **Previene errores** de lógica de negocio
- **Mejora la integridad** de los datos

**Ejemplo práctico:**
```sql
-- ❌ Esto FALLARÁ porque 'nombre' es NOT NULL
INSERT INTO usuarios (email, fecha_registro) 
VALUES ('juan@email.com', CURRENT_TIMESTAMP);

-- ✅ Esto FUNCIONARÁ porque proporcionamos todos los campos NOT NULL
INSERT INTO usuarios (nombre, email, fecha_registro) 
VALUES ('Juan Pérez', 'juan@email.com', CURRENT_TIMESTAMP);
```

#### CURRENT_TIMESTAMP
`CURRENT_TIMESTAMP` es una función que devuelve la **fecha y hora actual del servidor** en el momento de la inserción:
- **Se ejecuta automáticamente** al insertar un registro
- **No requiere intervención** del usuario
- **Es consistente** para todos los registros insertados en el mismo momento

**Ejemplo práctico:**
```sql
-- La tabla se crea con DEFAULT CURRENT_TIMESTAMP
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultima_actividad TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Al insertar, fecha_registro se llena automáticamente
INSERT INTO usuarios (nombre, email) 
VALUES ('María García', 'maria@email.com');

-- Resultado: fecha_registro = '2024-01-15 14:30:25' (fecha/hora actual)
```

#### Combinación NOT NULL + DEFAULT CURRENT_TIMESTAMP
Cuando combinas ambas restricciones:
```sql
fecha_registro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
```

**Esto significa:**
1. **NOT NULL**: El campo nunca puede ser NULL
2. **DEFAULT CURRENT_TIMESTAMP**: Si no se proporciona valor, se usa la fecha/hora actual
3. **Comportamiento**: Siempre tendrás un valor válido de fecha/hora

**Casos de uso comunes:**
```sql
-- Campos de auditoría
fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
fecha_modificacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
usuario_creacion VARCHAR(100) NOT NULL,
usuario_modificacion VARCHAR(100) NOT NULL

-- Campos de estado
fecha_registro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
fecha_ultimo_acceso TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
activo BOOLEAN NOT NULL DEFAULT true
```

### Ejemplo Completo
```sql
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL CHECK (precio > 0),
    stock INTEGER DEFAULT 0 CHECK (stock >= 0),
    categoria_id INTEGER REFERENCES categorias(id),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT true
);
```


---

## 📈 Índices

### ¿Qué son los Índices?
Los índices son estructuras de datos que mejoran la velocidad de recuperación de datos, pero ralentizan las operaciones de inserción, actualización y eliminación.

### Tipos de Índices
```sql
-- Índice único
CREATE UNIQUE INDEX idx_email ON usuarios(email);

-- Índice compuesto
CREATE INDEX idx_nombre_apellido ON usuarios(nombre, apellido);

-- Índice parcial
CREATE INDEX idx_usuarios_activos ON usuarios(id) WHERE activo = true;

-- Índice con orden
CREATE INDEX idx_fecha_desc ON productos(fecha_creacion DESC);
```

### Cuándo Usar Índices
- **SÍ**: Columnas usadas en WHERE, JOIN, ORDER BY
- **NO**: Tablas pequeñas, columnas con baja selectividad
- **CONSIDERAR**: Balance entre velocidad de lectura y escritura

---

## 💼 Transacciones

### Propiedades ACID
- **Atomicidad**: Todas las operaciones se ejecutan o ninguna
- **Consistencia**: La base de datos permanece en un estado válido
- **Aislamiento**: Las transacciones no interfieren entre sí
- **Durabilidad**: Los cambios son permanentes

### Control de Transacciones
```sql
-- Iniciar transacción
BEGIN;

-- Operaciones SQL
INSERT INTO usuarios (nombre, email) VALUES ('Juan', 'juan@email.com');
UPDATE productos SET stock = stock - 1 WHERE id = 1;

-- Confirmar transacción
COMMIT;

-- O cancelar
ROLLBACK;
```

### Niveles de Aislamiento
```sql
-- Leer datos no confirmados (más rápido, menos seguro)
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;

-- Leer datos confirmados (por defecto)
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- Lectura repetible
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- Serializable (más lento, más seguro)
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

---



## 📚 Conclusión

PostgreSQL es un sistema de bases de datos robusto y avanzado que ofrece:
- Cumplimiento completo de estándares SQL
- Características avanzadas como JSON, arrays y tipos personalizados
- Excelente rendimiento y escalabilidad
- Comunidad activa y documentación extensa
- Gratuito y de código abierto

Para continuar aprendiendo, practica con los ejemplos en `ejemplos_sql.sql` y resuelve los ejercicios en `ejercicios.md`.

---

**¡Sigue practicando y explorando las capacidades de PostgreSQL! 🎉**
