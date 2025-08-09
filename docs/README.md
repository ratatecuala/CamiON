# CamiON 🚛

**Plataforma B2B** para flotas medianas (5–20 camiones) que **optimiza rutas** y reduce **costos operacionales** (combustible, TAG, horas extra) sin instalar hardware ni integrar sistemas complejos.

---

## ✨ ¿Qué hace CamiON?
- Carga pedidos desde **Excel** o copia/pega direcciones.
- Calcula rutas optimizadas (VRP, **OR-Tools**).
- Envía instrucciones por **WhatsApp** (Twilio API).
- Mide **ahorro en CLP**, km y horas.
- Panel simple con estado y reporte semanal.

> **MVP**: mostrar ahorro real en ≤ 30 días.

---

## 🧱 Arquitectura (MVP)
- **Backend**: Python + Flask (`/optimizar`).
- **Optimización**: Google OR-Tools (modelo VRP).
- **Frontend**: base para React (web).
- **Datos**: Excel de ejemplo (`backend/sample_pedidos.xlsx`).

CamiON/
├─ backend/
│ ├─ app.py
│ ├─ routes/optimize.py
│ ├─ requirements.txt
│ └─ sample_pedidos.xlsx
├─ frontend/
│ └─ public/index.html
├─ docs/
│ ├─ API_Specs.md
│ ├─ MVP_Description.md
│ └─ IA_Future_Plan.md
└─ .gitignore

yaml
Copiar
Editar

---

## ▶️ Cómo ejecutar el backend (local)
```bash
cd backend
python -m venv .venv && source .venv/bin/activate   # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py   # abre en http://localhost:8000/salud
Probar el endpoint /optimizar
bash
Copiar
Editar
curl -X POST http://localhost:8000/optimizar -H "Content-Type: application/json" -d '{
  "orders": [
    {"id": 1, "address": "Av. Providencia 125, Santiago"},
    {"id": 2, "address": "Los Olivos 475, Ñuñoa"},
    {"id": 3, "address": "Las Violetas 739, Macul"}
  ],
  "depot": "Av. Apoquindo 3500, Las Condes",
  "vehicle_count": 1
}'
Respuesta (ejemplo)

json
Copiar
Editar
{
  "deposito": "Av. Apoquindo 3500, Las Condes",
  "ruta": [
    {"parada": 1, "id": 1, "direccion": "Av. Providencia 125, Santiago"},
    {"parada": 2, "id": 2, "direccion": "Los Olivos 475, Ñuñoa"},
    {"parada": 3, "id": 3, "direccion": "Las Violetas 739, Macul"}
  ],
  "resumen": {"total_km": 35, "ahorro_estimado_clp": 72400, "horas_ahorradas": 2}
}
Nota: routes/optimize.py trae un resultado de ejemplo. El desarrollador debe reemplazarlo por el modelo VRP real con OR-Tools.

📈 KPIs que medimos
% de reducción de km vs. baseline.

Ahorro CLP por combustible/TAG/horas extra.

Tiempo de planificación (antes vs. después).

Entregas puntuales.

🗺️ Roadmap
Fase 1 (MVP)

Carga Excel → Optimizar → WhatsApp → Panel → Reporte.

Fase 2 (IA, avanzada)

IA (GPT/DeepSeek) para explicar reportes, leer planillas/emails y generar mensajes.

Reglas duras + validación humana para evitar errores de IA.

Fase 3

Integraciones (GPS/ERP), mantenimiento predictivo, módulos premium.

⚙️ Requisitos técnicos
Python 3.10+

pip, venv

(Opcional) Cuenta Twilio/WhatsApp Business para enviar rutas.

🔒 Seguridad
Este repo incluye .gitignore para evitar subir:

bash
Copiar
Editar
.venv/, __pycache__/, *.pyc, node_modules/, .env, .DS_Store
Guarda tokens/credenciales en un archivo .env (no se sube).

📄 Licencia
Privado: no uses licencia (solo tú ves el código).

Público: si quieres permitir uso libre con atribución, usa MIT License.

🤝 Contacto
Proyecto: CamiON

Enfoque: flotas medianas de Chile/LatAm

Objetivo: ahorro medible en ≤ 30 días

Si quieres colaborar (desarrollo/ventas), abre un Issue o contáctanos por email.
