# Optometría — Estructura inicial del proyecto

Estructura base del MVP: backend (FastAPI + SQLAlchemy 2.0 + SQLite) y
frontend (Next.js + TypeScript + TailwindCSS + shadcn/ui), conectados
entre sí.

En esta fase **no** hay CRUDs, PDFs, IA, wizard ni pantallas completas.
Solo estructura, dependencias, conexión y modelos (`User`, `Patient`,
`Consultation`, `Document`).

---

# Estado verificado

Se comprobó correctamente que:

- ✅ FastAPI inicia correctamente.
- ✅ SQLite se conecta correctamente.
- ✅ Los modelos SQLAlchemy funcionan correctamente.
- ✅ El endpoint `/health` responde.
- ✅ La documentación automática (`/docs`) funciona.
- ✅ El frontend inicia correctamente.
- ✅ El frontend se comunica correctamente con el backend.
- ✅ La pantalla temporal muestra el estado real de la API y la base de datos.

---

## Estructura

```
optometria/
├── backend/
│   ├── app/
│   │   ├── main.py             # App FastAPI + CORS + endpoint /health
│   │   ├── core/
│   │   │   ├── config.py       # Settings (.env)
│   │   │   └── security.py     # bcrypt + JWT (utilidades, sin endpoints aún)
│   │   ├── db/
│   │   │   ├── base.py         # Base declarativa SQLAlchemy 2.0
│   │   │   └── session.py      # Engine + get_db()
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── patient.py
│   │   │   ├── consultation.py
│   │   │   └── document.py
│   │   ├── schemas/            # Vacío (Pydantic Schemas)
│   │   └── api/
│   │       └── routes/         # Vacío (Endpoints futuros)
│   ├── alembic/
│   ├── requirements.txt
│   └── .env.example
│
└── frontend/
    ├── app/
    │   ├── layout.tsx
    │   ├── page.tsx            # Página temporal de prueba
    │   └── globals.css
    ├── components/
    │   └── ui/
    ├── lib/
    │   ├── api.ts
    │   └── utils.ts
    ├── components.json
    ├── package.json
    └── .env.local.example
```

---

# Cómo ejecutar localmente

## 1. Backend

```bash
cd backend

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt

cp .env.example .env
```

Las migraciones están configuradas con Alembic.

Si se desea crear la migración inicial:

```bash
alembic revision --autogenerate -m "inicial"
alembic upgrade head
```

Durante esta fase del proyecto, el backend también puede crear
automáticamente las tablas mediante:

```python
Base.metadata.create_all(bind=engine)
```

por lo que es posible iniciar el proyecto sin generar migraciones.

Iniciar el servidor:

```bash
python -m uvicorn app.main:app --reload
```

Abrir:

```
http://localhost:8000/health
```

Debe responder algo similar a:

```json
{
    "api": "ok",
    "base_de_datos": "conectada"
}
```

También puede verificarse la documentación automática en:

```
http://localhost:8000/docs
```

---

## 2. Frontend

```bash
cd frontend

npm install

cp .env.local.example .env.local

npm run dev
```

Abrir:

```
http://localhost:3000
```

La pantalla temporal debe mostrar algo similar a:

```
Optometría — Estructura inicial

Estado del backend:
ok

BD:
conectada
```

---

## 3. Componentes de shadcn/ui

Cuando comiencen las pantallas reales:

```bash
cd frontend

npx shadcn@latest add button input card
```

---

# Compatibilidad

El proyecto fue probado utilizando:

- Python 3.9.12
- FastAPI 0.115
- SQLAlchemy 2.0
- Next.js 14
- SQLite

Debido a que el entorno utiliza Python 3.9, **no debe utilizarse** la
sintaxis introducida en Python 3.10.

Incorrecto:

```python
fecha: date | None
nombre: str | None
list[str]
```

Correcto:

```python
from typing import List, Optional

fecha: Optional[date]
nombre: Optional[str]
List[str]
```

---

# Notas importantes

- La base de datos utilizada durante el desarrollo es SQLite (`optometria.db`).
- Los modelos fueron diseñados para facilitar una futura migración a PostgreSQL.
- `app/core/security.py` ya contiene las funciones para hashing (bcrypt) y JWT, pero todavía **no existen endpoints de autenticación**.
- Las carpetas `app/api/routes/` y `app/schemas/` permanecen vacías intencionalmente hasta comenzar la implementación de los CRUD.
- El frontend únicamente contiene una pantalla de verificación de conexión; las pantallas del producto aún no han sido desarrolladas.

---

# Próxima fase

Implementar:

1. Autenticación JWT.
2. CRUD de Pacientes.
3. CRUD de Consultas.
4. CRUD de Documentos.

Posteriormente:

- Generación de PDFs.
- Wizard de consulta.
- Integración con IA.
- Frontend completo.
- Despliegue.