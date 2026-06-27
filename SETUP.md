# Optometría — Estructura inicial del proyecto

Estructura base del MVP: backend (FastAPI + SQLAlchemy 2.0 + SQLite) y
frontend (Next.js + TypeScript + TailwindCSS + shadcn/ui), conectados
entre sí.

En esta fase **no** hay CRUDs, PDFs, IA, wizard ni pantallas completas.
Solo estructura, dependencias, conexión y modelos (`User`, `Patient`,
`Consultation`, `Document`).

---

## Estructura

```
optometria/
├── backend/
│   ├── app/
│   │   ├── main.py            # App FastAPI + CORS + endpoint /health
│   │   ├── core/
│   │   │   ├── config.py      # Settings (.env)
│   │   │   └── security.py    # bcrypt + JWT (utilidades, sin endpoints aún)
│   │   ├── db/
│   │   │   ├── base.py        # Base declarativa SQLAlchemy 2.0
│   │   │   └── session.py     # Engine + get_db()
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── patient.py
│   │   │   ├── consultation.py
│   │   │   └── document.py
│   │   ├── schemas/            # (vacío, para Pydantic schemas de los CRUD)
│   │   └── api/routes/         # (vacío, para los endpoints de los CRUD)
│   ├── alembic/                # Migraciones
│   ├── requirements.txt
│   └── .env.example
│
└── frontend/
    ├── app/
    │   ├── layout.tsx
    │   ├── page.tsx             # Página de verificación de conexión
    │   └── globals.css          # Tema blanco / azul oscuro (ver docs/UX.md)
    ├── components/ui/           # Carpeta para componentes shadcn/ui
    ├── lib/
    │   ├── api.ts                # Cliente de conexión al backend
    │   └── utils.ts               # Helper cn() de shadcn/ui
    ├── components.json           # Configuración shadcn/ui
    ├── package.json
    └── .env.local.example
```

---

## Cómo ejecutar localmente

### 1. Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env             # Ya viene copiado en este entregable

# Generar la migración inicial y aplicarla
alembic revision --autogenerate -m "inicial: users, patients, consultations, documents"
alembic upgrade head

uvicorn app.main:app --reload --port 8000
```

Verificar en el navegador: `http://localhost:8000/health`

### 2. Frontend

```bash
cd frontend
npm install
cp .env.local.example .env.local   # Ya viene copiado en este entregable
npm run dev
```

Abrir `http://localhost:3000`. Debe mostrar el estado de conexión con
el backend (`api: ok`, `base_de_datos: conectada`).

### 3. Agregar componentes shadcn/ui (cuando se empiecen a construir pantallas)

```bash
cd frontend
npx shadcn@latest add button input card
```

---

## Notas importantes

- La base de datos es SQLite (`optometria.db`), pero todos los modelos
  evitan características exclusivas de SQLite para poder migrar a
  PostgreSQL sin cambios de código (ver `docs/BASE_DATOS.md`).
- `app/core/security.py` ya incluye las funciones de hashing (bcrypt) y
  JWT, pero **todavía no hay endpoints de login/registro** — eso
  corresponde a la Fase 1 (Autenticación) según `GUIA_DESARROLLO.md`.
- No se han creado los CRUD ni las rutas de la API (carpeta
  `app/api/routes/` está vacía intencionalmente).
- El frontend solo tiene una página de verificación de conexión, no
  pantallas del producto.
