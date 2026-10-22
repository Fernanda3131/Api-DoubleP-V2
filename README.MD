# 🌸 Double π (Double P) - Backend V2 🌸

¡Bienvenido al repositorio del Backend de **Double π**! Esta es la **segunda versión (V2)** optimizada de la plataforma web dedicada a la venta e intercambio de prendas de vestir de segunda mano, enfocada exclusivamente en los nichos de tallas **Plus Size** y **Petite**. 

*Sin límites, sin barreras, más tallas, más de ti. ✨*

---

## 🚀 Acerca de esta versión (Mejoras V2)
Esta entrega representa una reingeniería completa del ecosistema del servidor, migrando de un desarrollo inicial en Flask hacia una arquitectura empresarial robusta utilizando **Django**. 

### 🛠️ Principales Mejoras respecto a la V1:
* **Estructura Arquitectónica Limpia:** Migración completa al patrón **MVC (Modelo-Vista-Controlador)** de Django mediante controladores desacoplados en paquetes individuales por módulo corporativo.
* **Persistencia Corporativa:** Transición en el motor de base de datos hacia **Microsoft SQL Server**, garantizando integridad referencial estricta y escalabilidad.
* **Seguridad Avanzada:** Implementación de encriptación de contraseñas de última generación y protección de endpoints críticos mediante un sistema de **Decoradores de Sesión Personalizados** en el backend.
* **Gestión Eficiente de Archivos:** Carga automatizada y aislamiento de archivos multimedia (imágenes de prendas) administrados de manera nativa por el servidor.

---

## Arquitectura del Proyecto (Patrón MVC Modular)
El backend está segmentado en módulos independientes y reutilizables para facilitar el mantenimiento del código:

```text
backend/
├── api/                  # Carpeta de configuración global del proyecto
├── usuarios/             # Módulo de Autenticación, Sesiones y Roles (Modelos y Vistas separados)
│   ├── views/            # Controladores independientes (login_view, register_view)
│   └── security.py       # Interceptores / Decoradores de Seguridad (Auth)
├── publicaciones/        # Módulo de Publicaciones y Gestión de Prendas
│   └── views/            # Controladores independientes (publication_view, garment_view)
└── pagos/                # Módulo encargado de transacciones financieras y pasarelas
```

---

##  Tecnologías y Herramientas utilizadas
* **Lenguaje:** Python 3.13+
* **Framework:** Django 5.x (ORM / Seguridad Integrada)
* **Base de Datos:** Microsoft SQL Server
* **Conector BD:** `mssql-django`
* **Manejo de Imágenes:** Pillow

---

##  Configuración e Instalación Local

### 1. Clonar el repositorio y acceder a la carpeta
```bash
git clone <url-de-tu-repositorio>
cd backend
```

### 2. Levantar y activar el Entorno Virtual
```bash
# En Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# En Mac / Linux
source venv/bin/activate
```

### 3. Instalar Dependencias del proyecto
```bash
pip install -r requirements.txt
```

### 4. Configurar la Base de Datos
Asegúrate de tener una base de datos vacía creada en tu servidor local de **SQL Server** llamada `DoubleV2` y actualiza tus credenciales dentro de la sección `DATABASES` en el archivo `api/settings.py`.

### 5. Ejecutar Migraciones de la Base de Datos
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear una cuenta Administradora (Panel de Control)
```bash
python manage.py createsuperuser
```

### 7. Iniciar el Servidor de Desarrollo
```bash
python manage.py runserver
```
El servidor estará corriendo de manera local en: `http://127.0.0`

---
© 2026 **Double π** 