# Sistema de gestión de usuarios (Python)

Aplicación de consola en Python para administrar usuarios con operaciones **CRUD** (crear, consultar, actualizar y eliminar). Los datos se guardan en un archivo JSON, así que persisten entre ejecuciones.

Proyecto académico desarrollado como parte de mi formación en Tecnología en Desarrollo de Software (ETITC).

## Funcionalidades

- **Crear** usuarios con nombre, edad y ciudad.
- **Consultar** la lista completa de usuarios registrados.
- **Buscar** un usuario por nombre (sin distinguir mayúsculas de minúsculas).
- **Editar** el nombre, la edad o la ciudad de un usuario.
- **Eliminar** usuarios, con confirmación previa.
- **Persistencia** en `usuarios.json`: se carga automáticamente al iniciar y se guarda tras cada cambio.
- **Validación de datos**: el nombre y la ciudad solo aceptan letras, la edad debe estar entre 1 y 120, y las opciones de menú no permiten entradas inválidas.
- **Manejo de errores** con `try/except`, para que el programa no se cierre si se escribe texto donde se espera un número.

## Tecnologías

- Python 3
- Módulo estándar `json`

No requiere instalar librerías externas.

## Cómo ejecutarlo

1. Clona el repositorio:

   ```bash
   git clone https://github.com/DCuestaas/python-user-manager.git
   cd python-user-manager
   ```

2. Ejecuta el programa:

   ```bash
   python main.py
   ```

## Uso

Al iniciar verás este menú:

```
1. Agregar usuario
2. Mostrar usuarios
3. Cargar usuarios
4. Buscar usuario
5. Salir
```

Desde **Buscar usuario** puedes editar o eliminar el registro encontrado.

## Qué practiqué en este proyecto

- Uso de funciones para organizar el código y evitar repetir lógica.
- Ciclos `while` para repetir la petición hasta recibir datos válidos.
- Lectura y escritura de archivos JSON.
- Manejo de excepciones (`ValueError`, `FileNotFoundError`).
- Diseño de menús interactivos en consola.

## Posibles mejoras

- Migrar el almacenamiento de JSON a una base de datos (por ejemplo SQLite).
- Añadir pruebas automáticas.
- Crear una interfaz gráfica.

## Autor

Diego Alejandro Cuesta Soler, estudiante de Tecnología en Desarrollo de Software.
