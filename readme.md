# Sistema de Gestión de Habitaciones

Este proyecto es una aplicación de consola para gestionar habitaciones y clientes en un hotel. Incluye dos roles: Administrador y Encargado, con diferentes funcionalidades.

## Requisitos

- Python 3.8 o superior
- MySQL (instalado y configurado)
- Entorno virtual de Python

## Instalación

Sigue los pasos a continuación para ejecutar este proyecto:

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

### 2. Crear un entorno virtual
```bash
python -m venv env
```

### 3. Activar el entorno virtual
- En Windows:
  ```bash
  .\env\Scripts\activate
  ```
- En macOS/Linux:
  ```bash
  source env/bin/activate
  ```

### 4. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 5. Configurar la base de datos
1. Crea una base de datos en MySQL llamada `hotel`:
   ```sql
   CREATE DATABASE hotel;
   ```
2. Configura las credenciales de conexión en los controladores (`AdminController`, `LoginController`, etc.) dentro del archivo `config`:
   ```python
   self.config = {
       'user': 'tu-usuario-mysql',
       'password': 'tu-password',
       'host': 'localhost',
       'database': 'hotel',
   }
   ```

### 6. Crear las tablas necesarias
1. Ejecuta los scripts de creación de tablas si es necesario. Puedes incluir un archivo Python específico para ello:
   ```bash
   python create_tables.py
   ```

### 7. Ejecutar la aplicación
```bash
python app.py
```

---

## Funcionalidades

### Rol Administrador
- Crear usuarios encargados.

### Rol Encargado
- Registrar habitaciones.
- Asignar clientes a habitaciones.
- Ver asignaciones de clientes.
- Ver habitaciones activas/inactivas.

---

## Notas

1. Asegúrate de tener instalado MySQL y de que esté en ejecución.
2. Configura correctamente las credenciales en los archivos de configuración.
3. Si faltan dependencias en `requirements.txt`, actualiza el archivo ejecutando:
   ```bash
   pip freeze > requirements.txt
   ```

## Contribuciones

Si quieres contribuir, envía un pull request o abre un issue.

## Licencia

Este proyecto está bajo la Licencia MIT.

