# Sistema de Historia Clínica para Optometría

## Objetivo

Desarrollar una aplicación web para digitalizar el proceso de atención de una clínica de optometría.

El objetivo NO es cambiar la forma de trabajar de la doctora.

El sistema debe adaptarse completamente al flujo actual del consultorio.

La aplicación está pensada inicialmente para una sola usuaria (la doctora), pero debe permitir escalar a múltiples usuarios en el futuro.

---

# Principios del Proyecto

Todo el proyecto debe seguir estas reglas.

## 1. Simplicidad

El sistema debe ser extremadamente sencillo.

La doctora no tiene experiencia utilizando software médico complejo.

Nunca agregar funcionalidades innecesarias.

---

## 2. La consulta nunca empieza desde cero

Antes de iniciar una consulta nueva siempre debe mostrarse un resumen de la consulta anterior.

El resumen sirve únicamente como referencia.

Nunca copiar automáticamente información clínica.

La doctora siempre debe confirmar toda la información.

---

## 3. La IA es opcional

El sistema debe funcionar completamente aunque la IA esté deshabilitada.

La IA solamente sirve como asistente.

Nunca debe ser un requisito para trabajar.

---

## 4. Los documentos actuales son la fuente oficial

Todos los PDFs ubicados en la carpeta "formatos" son la referencia oficial del proyecto.

La aplicación debe adaptarse a esos documentos.

Nunca modificar los documentos para adaptarlos a la aplicación.

---

# Flujo General

Login

↓

Buscar paciente

↓

Crear paciente (si no existe)

↓

Perfil del paciente

↓

Resumen última consulta

↓

Nueva consulta

↓

Finalizar consulta

↓

Generar documento

---

# Gestión de Pacientes

Cada paciente tiene información administrativa permanente.

Nombre

Documento

Fecha de nacimiento

Edad

Sexo

Estado civil

Dirección

Ciudad

Teléfono

Correo

EPS

Entidad

Carnet

Ocupación

Remitido por

Acompañante

Teléfono del acompañante

Origen de la enfermedad

Estos datos permanecen guardados para futuras consultas.

No todos aparecen en los documentos PDF.

---

# Tipos de Consulta

El sistema maneja únicamente dos tipos.

## Primera Vez

Incluye antecedentes.

## Control

No incluye antecedentes.

Cuando el paciente ya tiene consultas anteriores el sistema debe sugerir automáticamente "Control".

La doctora puede cambiarlo manualmente.

---

# Flujo de la Consulta

La consulta se realiza mediante un asistente paso a paso.

Cada pantalla muestra únicamente una sección.

El usuario nunca debe sentirse perdido.

---

## Paso 1

Encabezado

Tipo de consulta

Datos del paciente

Fecha

---

## Paso 2

Anamnesis

Motivo de consulta

Antecedentes (solo Primera Vez)

Antecedentes oculares

Antecedentes farmacológicos

Antecedentes generales

---

## Paso 3

Lensometría y Agudeza Visual

Se mantienen unificadas exactamente como aparecen en la historia clínica física.

---

## Paso 4

Queratometría

OD

OI

---

## Paso 5

Retinoscopía

OD

OI

Observaciones debajo de la tabla.

---

## Paso 6

Subjetivo

OD

OI

Adición

---

## Paso 7

Estado Motor

Cover Test

Hirschberg

Ángulo Kappa

Visión del Color

Estereopsis

Distancia Pupilar

---

## Paso 8

Diagnóstico

Lista numerada.

Botón:

Mejorar redacción.

Botón:

Dictado por voz (opcional).

---

## Paso 9

Conducta

Texto libre.

Botón:

Mejorar redacción.

Botón:

Dictado.

---

## Paso 10

Observaciones

Texto libre.

Botón:

Mejorar redacción.

Botón:

Dictado.

---

## Paso 11

Finalizar

La consulta queda guardada.

El usuario decide qué documento generar.

---

# Generación de Documentos

El sistema puede generar:

Historia Clínica

Certificado

Orden

Remisión

Fórmula

Todos los documentos utilizan exactamente el formato oficial de la clínica.

---

# Personalización del Documento

Antes de generar un documento debe aparecer una pantalla sencilla donde la doctora puede:

Elegir el tipo de documento.

Escribir texto personalizado.

Decidir si desea incluir encabezado.

Decidir si desea incluir firma.

Generar PDF.

---

# Inteligencia Artificial

La IA únicamente puede:

Mejorar redacción.

Organizar texto.

Generar documentos utilizando información existente.

Ayudar mediante dictado por voz.

Nunca puede:

Inventar datos.

Modificar diagnósticos.

Completar información médica automáticamente.

---

# Guardado

Toda la información debe guardarse automáticamente.

No debe existir un botón "Guardar".

Debe mostrarse únicamente un indicador discreto:

Guardado ✓

---

# Objetivo Final

La aplicación debe sentirse como diligenciar una historia clínica en papel.

El usuario nunca debe pensar que está utilizando un software complicado.