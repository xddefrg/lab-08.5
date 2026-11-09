# ClassroomHub

Sitio web educativo hecho con Django. Muestra una página principal, una lista de recursos de aprendizaje y una página informativa. Los recursos son datos de ejemplo definidos en `pages/views.py`.

## Versiones

- Python 3.13
- Django 6.1.3

## Preparar el entorno

```bash
python -m venv .venv
```

Activar el entorno:

- Linux/macOS: `source .venv/bin/activate`
- Windows (PowerShell): `.venv\Scripts\Activate.ps1`

Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```

## Ejecutar

```bash
python manage.py check
python manage.py runserver
```

## Rutas públicas

| Ruta | Descripción |
| --- | --- |
| `/` | Página principal con bienvenida |
| `/resources/` | Lista de recursos con su disponibilidad |
| `/about/` | Propósito del proyecto |

Cualquier otra dirección responde con 404.

## Pruebas

```bash
python manage.py test pages
```

## Funcionalidades que aún no incluye

- Modelos, base de datos ni migraciones propias.
- Crear, editar o eliminar recursos.
- Autenticación de usuarios.
- Archivos estáticos separados (los estilos están dentro de `base.html`).
- Configuración para producción.
