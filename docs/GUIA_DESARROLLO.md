# Guía de Desarrollo

## Objetivo

Mantener un desarrollo ordenado y consistente.

---

# Estado actual

## ✅ Fase 0 — Infraestructura (COMPLETADA)

Backend

- ✅ Configuración de FastAPI
- ✅ Configuración de SQLAlchemy
- ✅ Configuración de Alembic
- ✅ Base de datos SQLite
- ✅ Modelos (User, Patient, Consultation, Document)
- ✅ Configuración JWT y bcrypt (utilidades, sin endpoints)
- ✅ Endpoint `/health`
- ✅ CORS
- ✅ Estructura del proyecto

Frontend

- ✅ Configuración de Next.js
- ✅ TypeScript
- ✅ Tailwind CSS
- ✅ shadcn/ui configurado
- ✅ Cliente para conexión con backend
- ✅ Página temporal de verificación de conexión

Verificación realizada:

- ✅ Backend ejecuta correctamente.
- ✅ Base de datos responde correctamente.
- ✅ Frontend se conecta exitosamente al backend.

---

# Fase 1 (EN DESARROLLO)

Backend

1. Autenticación (JWT)
2. CRUD Usuarios (si es necesario para el MVP)
3. CRUD Pacientes
4. CRUD Consultas
5. CRUD Documentos

**No modificar la infraestructura existente salvo que sea estrictamente necesario para implementar estas funcionalidades.**

---

# Fase 2

Frontend

- Login
- Buscar Pacientes
- Nuevo Paciente
- Perfil Paciente
- CRUD de pacientes

---

# Fase 3

Wizard de Consulta

1. Encabezado
2. Anamnesis
3. Lensometría y Agudeza Visual
4. Queratometría
5. Retinoscopía
6. Subjetivo
7. Estado Motor
8. Diagnóstico
9. Conducta
10. Observaciones
11. Finalizar

---

# Fase 4

Generación de PDFs

- Historia Clínica
- Control
- Certificados
- Órdenes
- Remisiones
- Fórmulas

---

# Fase 5

Integración IA

- Dictado
- Mejorar redacción
- Organización de texto
- Generación de documentos usando datos existentes

La IA nunca debe inventar información clínica.

---

# Regla Principal

No avanzar a la siguiente fase hasta que la anterior funcione correctamente.

Antes de comenzar una nueva fase, verificar que el backend y el frontend continúan funcionando correctamente.