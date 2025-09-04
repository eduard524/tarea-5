# Actividad 5 – Templates en Django

Incluye **herencia de templates** con `base.html` y páginas que heredan (`index.html`, `acerca.html`, `contacto.html`).
Usa **Bootstrap** (template gratuito) cargado desde CDN.

## Requisitos
- Python 3.10+
- Django (`pip install django`)

## Ejecución
```bash
cd mi_proyecto
python manage.py migrate
python manage.py runserver
```

## Rutas
- `http://127.0.0.1:8000/` → Inicio
- `http://127.0.0.1:8000/acerca/` → Acerca
- `http://127.0.0.1:8000/contacto/` → Contacto
