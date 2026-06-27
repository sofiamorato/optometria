# Instrucciones para cualquier IA

## Antes de escribir una sola línea de código

Leer completamente, en este orden:

1. README.md
2. ESTADO.md
3. docs/PROYECTO.md
4. docs/BASE_DATOS.md
5. docs/UX.md
6. docs/DECISIONES.md

No comenzar a programar hasta haber leído todos los documentos.

Si alguno entra en conflicto con otro, detenerse y preguntar antes de continuar.

Después de leerlos, continuar únicamente con la siguiente tarea pendiente indicada en **ESTADO.md**.

---

# Objetivo del proyecto

Desarrollar una aplicación web para una clínica de optometría.

El objetivo principal es **digitalizar el proceso actual**, conservando exactamente la forma de trabajo de la doctora.

No rediseñar el producto.

No cambiar decisiones ya aprobadas.

Si alguna mejora implica modificar el flujo de trabajo actual, debe proponerse primero y esperar aprobación.

---

# Usuario final

La aplicación será utilizada principalmente por una optómetra con muy poca experiencia utilizando tecnología.

Todas las decisiones deben priorizar:

* simplicidad
* rapidez
* claridad
* facilidad de aprendizaje

Siempre pensar en reducir el número de clics y minimizar la carga cognitiva del usuario.

---

# Principios de UX

Siempre:

* Letras grandes.
* Botones grandes.
* Muy pocos botones por pantalla.
* Una acción principal por pantalla.
* Guardado automático cuando sea posible.
* Navegación paso a paso.
* Interfaces limpias.

Nunca:

* Dashboards complejos.
* Sidebars con muchas opciones.
* Formularios gigantes.
* Pantallas saturadas.
* Configuraciones innecesarias.

---

# Historia clínica

La carpeta **formatos/** contiene los formatos oficiales utilizados actualmente por la clínica.

Es la fuente de verdad para la estructura de las consultas.

Nunca:

* modificar su estructura;
* inventar campos;
* eliminar información existente.

Si existe alguna duda sobre un campo, preguntar antes de implementarlo.

---

# Base de datos

La estructura oficial se encuentra en:

docs/BASE_DATOS.md

Todos los modelos deben mantenerse sincronizados con ese documento.

---

# Inteligencia Artificial

La IA únicamente puede ayudar en tareas de apoyo.

Puede:

* mejorar redacción;
* transcribir dictado;
* organizar texto;
* generar documentos utilizando datos existentes;
* resumir información ya registrada.

Nunca puede:

* inventar información clínica;
* completar campos automáticamente;
* diagnosticar;
* sugerir diagnósticos;
* modificar información médica sin intervención del profesional.

Toda decisión clínica pertenece exclusivamente a la doctora.

---

# Desarrollo

Trabajar siempre por etapas.

No implementar funcionalidades futuras.

No adelantarse a la siguiente fase.

Implementar únicamente la tarea actualmente pendiente.

Antes de comenzar una nueva etapa, explicar brevemente qué se va a implementar.

---

# Calidad del código

Mantener siempre:

* código limpio;
* nombres descriptivos;
* archivos pequeños;
* buena organización;
* comentarios solo cuando aporten valor;
* consistencia con la arquitectura existente.

No duplicar código.

No agregar dependencias sin justificar su necesidad.

---

# Compatibilidad

El entorno de desarrollo utiliza actualmente:

* Python 3.9.12

Por lo tanto, no utilizar características exclusivas de Python 3.10 o superior.

Utilizar:

* Optional[T]
* List[T]

No utilizar:

* T | None
* list[T]

salvo que el proyecto sea actualizado oficialmente a una versión más reciente de Python.

---

# Comunicación

Cuando se proponga una decisión importante:

1. Explicar brevemente el motivo.
2. Esperar aprobación si modifica el diseño o el flujo del sistema.
3. Luego implementar.

No realizar cambios grandes sin antes explicarlos.

---

# Prioridad

La prioridad siempre será:

1. Correctitud funcional.
2. Simplicidad para la doctora.
3. Mantenibilidad del código.
4. Estética.

Nunca sacrificar la simplicidad del usuario por una solución técnicamente más sofisticada.
