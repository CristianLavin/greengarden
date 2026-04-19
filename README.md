# GreenGarden

GreenGarden es un proyecto web desarrollado con Django que simula una tienda orientada a productos de jardineria. La aplicacion permite mostrar un catalogo de plantas y maceteros, registrar usuarios, iniciar sesion y gestionar un carrito de compras usando sesiones.

## Descripcion General

El proyecto esta organizado como una aplicacion Django tradicional:

- `greengarden/`: configuracion principal del proyecto.
- `paginaweb/`: app donde se concentra la logica de negocio.
- `paginaweb/templates/`: plantillas HTML de la interfaz.
- `paginaweb/templates/static/`: archivos estaticos como CSS, JS e imagenes.
- `db.sqlite3`: base de datos local usada en desarrollo.

La pagina presenta una experiencia simple de ecommerce para una tienda de jardin. El usuario puede recorrer el catalogo, revisar productos, registrarse, iniciar sesion y agregar articulos al carrito.

## Caracteristicas Principales

- Catalogo de productos dividido por categorias como plantas y maceteros.
- Vista general de tienda con listado dinamico de productos almacenados en la base de datos.
- Registro de usuarios mediante formulario.
- Inicio de sesion con manejo de sesion en Django.
- Carrito de compras administrado con sesiones.
- Operaciones para agregar, restar, eliminar y limpiar productos del carrito.
- Paginas de confirmacion para registro, compra y despacho.
- Panel de administracion de Django con modelos registrados.
- Uso de SQLite para facilitar pruebas y ejecucion local.

## Tecnologias Utilizadas

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap
- JavaScript

## Funcionalidades Del Sistema

### 1. Catalogo y tienda

La ruta principal del proyecto muestra la tienda y carga todos los productos desde el modelo `Producto`. Cada producto incluye:

- `nombre`
- `categoria`
- `precio`
- `imagen`

Esto permite administrar el catalogo desde base de datos y reutilizarlo en distintas vistas.

### 2. Registro de usuarios

El sistema incluye un formulario de registro basado en el modelo `Usuario`. Los datos que se solicitan son:

- nombre completo
- nombre de usuario
- correo electronico
- contrasena

Cuando el formulario es valido, se crea el usuario y se redirige a una pagina de confirmacion.

### 3. Inicio de sesion

El inicio de sesion se maneja con una logica propia basada en el modelo `Usuario` y el uso de sesiones. Una vez autenticado, el usuario puede acceder a vistas personalizadas como:

- `index2.html`
- `plantas2.html`
- `maceteros2.html`
- `carrito.html`

### 4. Carrito de compras

El carrito se implementa en la clase `Carrito`, almacenando la informacion en `request.session`. Entre las acciones disponibles se encuentran:

- agregar un producto
- restar una unidad
- eliminar un producto completo
- limpiar el carrito
- llevar un contador de productos en sesion

### 5. Vistas y navegacion

El proyecto incluye paginas para distintos flujos del usuario:

- inicio
- catalogo de plantas
- catalogo de maceteros
- login
- registro
- carrito
- despacho
- confirmaciones

## Modelos Principales

### `Usuario`

Modelo de usuario personalizado que almacena:

- `nombre_completo`
- `username`
- `correo_electronico`
- `password`
- `is_active`
- `is_admin`
- `is_staff`

### `Producto`

Modelo que representa los articulos disponibles en la tienda:

- `nombre`
- `categoria`
- `precio`
- `imagen`

## Estructura Basica Del Proyecto

```text
greengarden/
|-- greengarden/
|   |-- settings.py
|   |-- urls.py
|-- paginaweb/
|   |-- models.py
|   |-- views.py
|   |-- urls.py
|   |-- forms.py
|   |-- Carrito.py
|   |-- templates/
|-- static_root/
|-- db.sqlite3
|-- manage.py
```

## Instalacion y Ejecucion

### 1. Clonar o abrir el proyecto

Ubicate en la carpeta raiz del proyecto:

```bash
cd d:\greengarden
```

### 2. Crear y activar un entorno virtual

En Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

Como no se incluye un `requirements.txt`, instala Django manualmente:

```bash
pip install django
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Ejecutar el servidor

```bash
python manage.py runserver
```
## Rutas Relevantes

- `/` -> tienda principal
- `/index.html` -> pagina de inicio publica
- `/plantas.html` -> catalogo publico de plantas
- `/maceteros.html` -> catalogo publico de maceteros
- `/login.html` -> formulario de acceso
- `/registro.html` -> formulario de registro
- `/carrito.html` -> carrito del usuario
- `/admin/` -> panel de administracion

## Objetivo Del Proyecto

Este proyecto puede servir como:

- practica academica con Django
- base para una tienda online sencilla
- ejemplo de uso de sesiones para carrito de compras
- punto de partida para mejorar autenticacion, pagos y gestion de pedidos

## Posibles Mejoras

- agregar un archivo `requirements.txt`
- usar el sistema de autenticacion nativo de Django de forma completa
- cifrar y validar mejor las contrasenas en el flujo de login
- incorporar busqueda y filtros de productos
- agregar pruebas automatizadas
- mejorar la gestion de imagenes y medios
- implementar historial de pedidos

## Autor

Proyecto GreenGarden, orientado a la gestion de una tienda web de jardineria construida con Django.
