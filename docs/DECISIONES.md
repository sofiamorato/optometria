# Decisiones del Proyecto

Este documento registra todas las decisiones funcionales y técnicas aprobadas.

Si existe una contradicción entre una implementación y este documento, prevalece este documento.

---

# DECISIÓN 001

## Título

Objetivo del proyecto

## Decisión

Desarrollar una aplicación sencilla para una clínica de optometría.

No desarrollar un software médico empresarial.

---

# DECISIÓN 002

## Usuario principal

### Decisión

El MVP será utilizado por una única optómetra.

Toda la experiencia debe diseñarse pensando en ella.

No diseñar pensando inicialmente en múltiples usuarios.

---

# DECISIÓN 003

## Tipo de aplicación

### Decisión

Aplicación web.

Backend FastAPI.

Frontend Next.js.

Base de datos SQLite.

Preparada para migrar posteriormente a PostgreSQL.

---

# DECISIÓN 004

## Flujo de consulta

### Decisión

La consulta siempre se realiza mediante un asistente paso a paso.

Nunca mediante un formulario gigante.

---

# DECISIÓN 005

## Inicio de una consulta

### Decisión

Toda consulta nueva comienza mostrando un resumen de la consulta anterior.

Ese resumen sirve únicamente como referencia.

Nunca copiar información automáticamente.

---

# DECISIÓN 006

## Tipo de consulta

### Decisión

Si el paciente ya tiene consultas anteriores, el sistema sugerirá automáticamente **"Control"**.

La doctora puede cambiarlo manualmente por **"Primera Vez"**.

---

# DECISIÓN 007

## Lensometría

### Decisión

Lensometría y Agudeza Visual permanecen unificadas.

No separar estas pantallas.

Debe respetarse exactamente la estructura de la historia clínica física.

---

# DECISIÓN 008

## Retinoscopía

### Decisión

Las observaciones se escriben en una columna adicional.

---

# DECISIÓN 009

## Inteligencia Artificial

### Decisión

La IA es completamente opcional.

El sistema debe funcionar normalmente sin utilizar IA.

---

# DECISIÓN 010

## Funciones permitidas para la IA

### La IA puede

* Mejorar redacción.
* Organizar texto.
* Ayudar mediante dictado.
* Generar documentos utilizando datos existentes.

### La IA nunca puede

* Diagnosticar.
* Inventar información.
* Completar datos médicos.
* Modificar diagnósticos.

---

# DECISIÓN 011

## Guardado

### Decisión

Toda la información se guarda automáticamente.

No existe botón **Guardar**.

Mostrar únicamente:

**Guardado ✓**

---

# DECISIÓN 012

## PDF

### Decisión

Los documentos deben conservar exactamente el formato utilizado actualmente por la clínica.

La aplicación debe adaptarse al documento.

Nunca modificar el documento.

---

# DECISIÓN 013

## Documentos

### Decisión

Los documentos se generan uno por uno.

No generar varios simultáneamente.

---

# DECISIÓN 014

## Pantalla final

### Decisión

Después de finalizar una consulta aparecerán únicamente cinco opciones:

* Historia Clínica
* Certificado
* Orden
* Remisión
* Fórmula

---

# DECISIÓN 015

## Personalización

### Decisión

Antes de generar un documento la doctora puede:

* Editar texto personalizado.
* Elegir si desea incluir encabezado.
* Elegir si desea incluir firma.

---

# DECISIÓN 016

## UX

### Decisión

Siempre priorizar:

* Simplicidad.
* Letras grandes.
* Botones grandes.
* Muy pocos botones.
* Una acción principal por pantalla.

Nunca implementar:

* Dashboards.
* Sidebars.
* Menús complejos.
* Configuraciones innecesarias.

---

# DECISIÓN 017

## Código

### Decisión

Siempre escribir código limpio.

Separar frontend y backend.

Utilizar componentes reutilizables.

Mantener nombres claros.

Documentar únicamente lo necesario.

---

# DECISIÓN 018

## Eliminación de registros

### Decisión

Nunca eliminar físicamente los registros de la base de datos.

En particular:

* Pacientes
* Consultas
* Documentos

Cuando sea necesario desactivar un registro, utilizar inactivación lógica mediante el campo `is_active`.

El historial clínico debe conservarse siempre.

---

# DECISIÓN 019

## Infraestructura

### Decisión

La infraestructura base del proyecto se considera finalizada y estable.

Incluye:

* Configuración de FastAPI.
* Configuración de SQLAlchemy.
* Configuración de Alembic.
* Configuración de Next.js.
* Modelos de datos.
* Conexión entre frontend y backend.
* Endpoint `/health`.
* Configuración de CORS.
* Configuración de autenticación (utilidades JWT y bcrypt).

Las siguientes fases deben construirse sobre esta infraestructura.

No reemplazar tecnologías ni reorganizar la arquitectura salvo que exista una razón técnica importante previamente aprobada.

---

# Cómo agregar nuevas decisiones

Cada nueva decisión debe agregarse al final del documento utilizando el mismo formato.

Nunca modificar decisiones anteriores.

Si una decisión cambia, agregar una nueva indicando explícitamente que reemplaza a la anterior.
