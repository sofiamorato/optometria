# Sistema de Historia Clínica para Optometría

## Descripción

Este proyecto consiste en desarrollar una aplicación web para digitalizar el flujo de trabajo de una clínica de optometría.

El objetivo NO es cambiar la forma de trabajar de la doctora, sino adaptar la tecnología a su proceso actual.

La aplicación está diseñada para una única optómetra con poca experiencia utilizando computadores, por lo que la simplicidad es el principio más importante del proyecto.

---

## Objetivos

El sistema debe permitir:

- Gestionar pacientes.
- Realizar consultas de Primera Vez y Control.
- Consultar el historial clínico.
- Generar historias clínicas en PDF.
- Generar certificados, órdenes, remisiones y fórmulas.
- Utilizar Inteligencia Artificial únicamente como apoyo para redactar.

---

## Tecnologías

### Frontend

- Next.js
- TypeScript
- TailwindCSS
- shadcn/ui

### Backend

- FastAPI
- SQLAlchemy
- Pydantic

### Base de datos

SQLite (MVP)

Preparado para PostgreSQL en el futuro.

---

## Documentación

Toda la documentación del proyecto se encuentra en la carpeta:

docs/

---

## Formatos

Todos los documentos originales de la clínica se encuentran en:

formatos/

Estos documentos son la fuente oficial del proyecto.

La aplicación debe adaptarse a estos formatos.

Nunca modificar los formatos para adaptarlos a la aplicación.

---

## Desarrollo

Antes de comenzar a desarrollar leer:

1. CLAUDE.md
2. ESTADO.md
3. docs/

---

## Filosofía

La aplicación debe sentirse como diligenciar una historia clínica en papel.

La tecnología debe adaptarse a la doctora.

Nunca la doctora al software.

---

## Ejecución local

Ver [`SETUP.md`](./SETUP.md) para la guía paso a paso de instalación y
ejecución del backend y el frontend, además del detalle de la estructura
de carpetas creada para el MVP.
