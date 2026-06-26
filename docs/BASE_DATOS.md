# Base de Datos

## Objetivo

La base de datos debe ser simple, fácil de mantener y preparada para crecer.

Inicialmente será utilizada por una única doctora utilizando SQLite.

Toda la estructura debe permitir migrar posteriormente a PostgreSQL sin modificar el código de la aplicación.

---

# Modelo General

users
│
└──── consultations
         │
         └──── patients
                │
                └──── documents

---

# Tabla: users

Representa los usuarios del sistema.

En el MVP únicamente existirá una doctora.

Campos:

id
nombre
email
password_hash
titulo_profesional
registro_medico
created_at
updated_at

---

# Tabla: patients

Contiene la información permanente del paciente.

Estos datos NO pertenecen a una consulta específica.

Campos

id

nombre_completo

tipo_documento

documento

fecha_nacimiento

edad

sexo

estado_civil

direccion

ciudad

telefono

correo

eps

entidad

numero_carnet

ocupacion

remitido_por

acompanante

telefono_acompanante

origen_enfermedad

created_at

updated_at

---

# Tabla: consultations

Cada registro representa una consulta médica.

Campos generales

id

patient_id

user_id

tipo_consulta

Valores permitidos

primera_vez

control

estado

en_progreso

finalizada

fecha_consulta

created_at

updated_at

---

# Sección: Anamnesis

anamnesis

---

# Antecedentes

Solo aplican para consultas de Primera Vez.

antecedentes_oculares

antecedentes_farmacologicos

antecedentes_generales

---

# Lensometría y Agudeza Visual

clase_lentes

vl_od_avsc
vl_od_cc
vl_od_ph

vl_oi_avsc
vl_oi_cc
vl_oi_ph

vp_od_avsc
vp_od_cc
vp_od_ph

vp_oi_avsc
vp_oi_cc
vp_oi_ph

---

# Queratometría

queratometria_od

queratometria_oi

---

# Retinoscopía

retinoscopia_od_formula

retinoscopia_od_v

retinoscopia_oi_formula

retinoscopia_oi_v

retinoscopia_observaciones

---

# Subjetivo

subjetivo_od_formula

subjetivo_od_v

subjetivo_od_extra

subjetivo_oi_formula

subjetivo_oi_v

subjetivo_oi_extra

adicion_od

adicion_oi

---

# Estado Motor

cover_test_vl

cover_test_vp

hirschberg

angulo_kappa_od

angulo_kappa_oi

vision_color

estereopsis

distancia_pupilar

---

# Cierre

diagnosticos

Tipo:

JSON Array

Ejemplo

[
"Astigmatismo miópico compuesto",
"Presbicia"
]

conducta

observaciones

---

# Tabla: documents

Cada documento generado queda registrado.

Campos

id

consultation_id

tipo

Valores posibles

historia_clinica

certificado

orden

remision

formula

texto_personalizado

incluir_encabezado

incluir_firma

pdf_path

created_at

---

# Relaciones

Un usuario

↓

Tiene muchos pacientes

Un paciente

↓

Tiene muchas consultas

Una consulta

↓

Puede generar muchos documentos

---

# Reglas

Nunca eliminar pacientes físicamente.

Nunca eliminar consultas.

Si algún registro deja de utilizarse, marcarlo como inactivo.

Todo debe quedar trazable.

---

# Consideraciones futuras

Aunque el MVP utiliza SQLite, todas las tablas deben ser compatibles con PostgreSQL.

No utilizar características exclusivas de SQLite.

Mantener nombres claros y consistentes.

Todos los modelos deben implementarse utilizando SQLAlchemy 2.0.