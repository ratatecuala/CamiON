# CamiON

**CamiON** es una plataforma B2B para optimizar rutas y reducir costos operacionales en flotas medianas (5–20 camiones) en Latinoamérica.

## Estructura del proyecto
- `backend/`: API Flask con endpoint `/optimizar`.
- `frontend/`: base para la interfaz (React u otro framework).
- `docs/`: documentación del proyecto.

## Cómo ejecutar el backend
```bash
cd backend
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Abrir en: `http://localhost:8000/salud`
