# Prompt Maestro

Este proyecto consiste en desarrollar una aplicación web para una clínica de optometría.

Antes de escribir cualquier línea de código debes leer completamente:

- README.md
- CLAUDE.md
- ESTADO.md
- docs/PROYECTO.md
- docs/BASE_DATOS.md
- docs/UX.md
- docs/DECISIONES.md

La carpeta "formatos" contiene los documentos oficiales de la clínica.

Todos los PDFs deben replicarse exactamente.

Nunca modificar la estructura de los documentos.

---

## Objetivo

Construir una aplicación extremadamente sencilla para una optómetra con poca experiencia utilizando tecnología.

La aplicación debe sentirse como diligenciar una historia clínica en papel.

---

## Stack Tecnológico

Frontend

- Next.js
- TypeScript
- TailwindCSS
- shadcn/ui

Backend

- FastAPI
- SQLAlchemy 2.0
- SQLite

Autenticación

- JWT
- bcrypt

PDF

- HTML + CSS
- Playwright

IA (Opcional)

- OpenAI API

---

## Flujo

Login

↓

Buscar Paciente

↓

Perfil del Paciente

↓

Resumen Última Consulta

↓

Nueva Consulta

↓

Finalizar

↓

Generar Documento

---

## Reglas

- Nunca implementar funcionalidades no solicitadas.
- Siempre mantener el código limpio.
- Trabajar por etapas.
- Explicar decisiones importantes.
- Priorizar simplicidad sobre complejidad.

Si existe alguna contradicción entre este prompt y los archivos de `docs`, prevalece la documentación del proyecto.