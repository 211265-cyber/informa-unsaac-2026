# Guía de gestión de INFORMA UNSAAC en Jira

Documento interno del equipo. Estado de carga confirmado el 29 de octubre de 2026. Fechas en America/Lima.

## 1. Acceso y estado confirmado

[Abrir el tablero INFORMA, número 2](https://unsaac-team-v2a056y1.atlassian.net/jira/software/projects/INFORMA/boards/2?filter=&groupBy=none).

El proyecto y las épicas **INFORMA-1** e **INFORMA-2** están creados. Las **16 tareas** están creadas y confirmadas, todas en estado **Por hacer**. C01-C08 pertenecen a INFORMA-1 y V01-V08 a INFORMA-2. Las tablas siguientes relacionan sus ID locales con las claves reales.

La verificación de la lista se conserva en jira_verificacion_filas.json: contiene un encabezado y 18 actividades, correspondientes a dos épicas y 16 tareas. Se contrastaron responsables, vencimientos y estado. Las épicas están sin responsable por ser agrupaciones; las tareas sí tienen persona asignada. La captura del proyecto se conserva en jira_proyecto_creado.png.

Están registrados como campos de Jira la épica principal, el responsable y el vencimiento. El **inicio propuesto, el revisor y las dependencias se conservaron en la descripción**. No se configuró un campo Inicio ni se crearon vínculos nativos de bloqueo entre tareas. Las claves de predecesoras del CSV facilitan esa mejora posterior; no acreditan vínculos ya creados.

Las invitaciones a los integrantes 211265 y 204800 fueron enviadas. Su captura se conserva en jira_invitaciones.png; acredita el envío, no su aceptación. La asignación de una tarjeta tampoco demuestra por sí sola que se haya ejecutado.

Archivos de trabajo:

- BACKLOG_JIRA.csv: 16 filas con claves, responsables, vencimientos y estado confirmados; conserva inicio, revisor, criterios y dependencias del plan.
- BACKLOG_JIRA.json: detalle estructurado del plan y un bloque Jira que distingue campos confirmados y datos de descripción.
- jira_claves_confirmadas.json: mapeo comprobado de ID locales y claves reales.
- jira_invitaciones.png: copia de la captura de invitaciones.
- jira_verificacion_filas.json y jira_proyecto_creado.png: verificación de la lista y captura del proyecto.

Los ID C01-C08 y V01-V08 identifican el plan local; las claves INFORMA corresponden a Jira. No deducir nuevas claves por secuencia ni volver a cargar estas 16 tareas.

## 2. Organización del trabajo

| Fase | ID locales | Épica confirmada | Fechas planificadas |
|---|---|---|---|
| Cierre de primera entrega | C01-C08 | INFORMA-1 | 29 y 30 de octubre de 2026 |
| Validación posterior | V01-V08 | INFORMA-2 | Del 2 al 20 de noviembre de 2026 |

La primera entrega y exposición corresponde al 30 de octubre. La ventana de noviembre es una propuesta de validación, no una fecha oficial de segunda parcial, autorización de instalación ni compromiso de terceros.

| Integrante | Código | Responsabilidad principal |
|---|---|---|
| Flavio Antony Cabeza Huillca | 211265 | Problema, encuesta, necesidad, revisión cruzada y presentación |
| George Ivanok Muñoz Castillo | 204800 | Requisitos, terminales, CMS, ubicaciones y validación técnica |
| Lucian Neptalí Fernández Baca Castro | 184197 | Presupuesto, riesgos, balance preliminar y consolidación |

El revisor comprueba criterios y evidencia; no es un cargo formal ni reemplaza al responsable. Confirmar disponibilidad y aceptación de la distribución antes de comprometer trabajo adicional.

## 3. Gestionar las tarjetas creadas desde la interfaz

1. Abrir la clave de la tabla o buscar el ID local en el tablero. Confirmar que se trabaja sobre la tarjeta existente.
2. Revisar el título, descripción y épica principal. Mantener los criterios completos y conservar la distinción entre datos de campo y de descripción.
3. En **Responsable / Assignee**, comprobar la cuenta guardada. Si un integrante no puede entrar, revisar primero aceptación de invitación y acceso al proyecto; no crear otra cuenta ni duplicar la tarjeta como solución.
4. En **Vencimiento / Due date**, revisar la fecha guardada. El CSV la expresa como YYYY-MM-DD; la interfaz puede pedir otro formato.
5. Consultar el inicio y revisor dentro de la descripción. Si cambia el plan, actualizar la descripción y el registro local. No afirmar que existe un campo Inicio o un campo Revisor configurado.
6. Mantener **Por hacer** hasta que el responsable inicie. Antes de mover a En curso, comprobar condiciones de entrada y dependencias.
7. Registrar resultado, versión, evidencia, bloqueo y siguiente acción. Solicitar la revisión indicada antes de pasar a Listo.
8. Si se acuerda cambiar responsable, vencimiento o alcance, guardar el cambio en Jira y conciliar el CSV/JSON. Una fecha programada no acredita ejecución.

Para una actividad nueva, seleccionar **Crear / Create**, confirmar INFORMA y el tipo Tarea, completar título y descripción, elegir una épica existente y guardar. Copiar exclusivamente la clave devuelta por Jira al registro local. Esta instrucción es para ampliaciones futuras; las 16 tareas actuales ya existen. [Atlassian, crear un elemento de trabajo](https://support.atlassian.com/jira-software-cloud/docs/create-a-work-item-and-a-subtask).

El CSV es un registro de coordinación, no una afirmación de campos personalizados o de importación automática. Los códigos universitarios no equivalen a identificadores de cuenta de Jira.

## 4. Fechas, revisión y secuencia

### Cierre del 29 y 30 de octubre

| ID | Clave confirmada | Responsable asignado | Revisor en descripción | Inicio propuesto | Vencimiento guardado | HP del plan | Depende de |
|---|---|---|---|---|---|---:|---|
| C01 | [INFORMA-3](https://unsaac-team-v2a056y1.atlassian.net/browse/INFORMA-3) | Flavio | George | 29/10 | 29/10 | 1,5 | Sin dependencia |
| C02 | [INFORMA-4](https://unsaac-team-v2a056y1.atlassian.net/browse/INFORMA-4) | George | Flavio | 29/10 | 29/10 | 2 | C01 |
| C03 | [INFORMA-5](https://unsaac-team-v2a056y1.atlassian.net/browse/INFORMA-5) | George | Lucian | 29/10 | 30/10 | 2,5 | C02 |
| C04 | [INFORMA-6](https://unsaac-team-v2a056y1.atlassian.net/browse/INFORMA-6) | Lucian | George | 29/10 | 30/10 | 2,5 | C02 |
| C05 | [INFORMA-7](https://unsaac-team-v2a056y1.atlassian.net/browse/INFORMA-7) | Lucian | Flavio | 30/10 | 30/10 | 2 | C03, C04 |
| C06 | [INFORMA-8](https://unsaac-team-v2a056y1.atlassian.net/browse/INFORMA-8) | Lucian | George | 29/10 | 30/10 | 1,5 | C02 |
| C07 | [INFORMA-9](https://unsaac-team-v2a056y1.atlassian.net/browse/INFORMA-9) | Flavio | George | 30/10 | 30/10 | 3 | C01, C02, C03, C04, C05, C06 |
| C08 | [INFORMA-10](https://unsaac-team-v2a056y1.atlassian.net/browse/INFORMA-10) | Flavio | Lucian | 30/10 | 30/10 | 3 | C07 |
| Total | | | | | | 18,0 | |

La secuencia dentro del mismo día importa: C01 precede a C02; después pueden avanzar C03 y C04 en paralelo. C05 necesita ambas; C07 requiere la integración de C01-C06; C08 necesita C07. Una fecha igual no elimina esa dependencia.

La agrupación por responsable principal es Flavio 7,5 HP, George 4,5 HP y Lucian 6 HP. Son 18 HP agregadas que incluyen revisión por actividad; no son horas trabajadas ni acreditan capacidad disponible. Distribuir la revisión dentro de ese esfuerzo sin duplicarla. Las HP se mantienen como estimación del plan; no se afirma que se haya configurado seguimiento de tiempo en Jira.

### Validación posterior propuesta

| ID | Clave confirmada | Responsable asignado | Revisor en descripción | Inicio propuesto | Vencimiento guardado | Depende de |
|---|---|---|---|---|---|---|
| V01 | [INFORMA-11](https://unsaac-team-v2a056y1.atlassian.net/browse/INFORMA-11) | Flavio | Lucian | 02/11 | 03/11 | C08 |
| V02 | [INFORMA-12](https://unsaac-team-v2a056y1.atlassian.net/browse/INFORMA-12) | Flavio | George | 03/11 | 06/11 | V01 |
| V03 | [INFORMA-13](https://unsaac-team-v2a056y1.atlassian.net/browse/INFORMA-13) | George | Flavio | 04/11 | 06/11 | V01 |
| V04 | [INFORMA-14](https://unsaac-team-v2a056y1.atlassian.net/browse/INFORMA-14) | George | Flavio | 09/11 | 12/11 | V02, V03 |
| V05 | [INFORMA-15](https://unsaac-team-v2a056y1.atlassian.net/browse/INFORMA-15) | George | Lucian | 09/11 | 13/11 | V03 |
| V06 | [INFORMA-16](https://unsaac-team-v2a056y1.atlassian.net/browse/INFORMA-16) | Lucian | George | 16/11 | 18/11 | V04, V05 |
| V07 | [INFORMA-17](https://unsaac-team-v2a056y1.atlassian.net/browse/INFORMA-17) | Lucian | Flavio | 18/11 | 19/11 | V02, V04, V05, V06 |
| V08 | [INFORMA-18](https://unsaac-team-v2a056y1.atlassian.net/browse/INFORMA-18) | Flavio | Lucian | 20/11 | 20/11 | V07 |

Todas las fechas son de 2026. Las horas de V01-V08 están pendientes de estimar y no se reemplazan por cero. Que sus vencimientos estén registrados en Jira no convierte la propuesta en una consigna docente o compromiso de respuesta externa.

Si falta acceso, equipo, especialista u oferta, registrar el bloqueo y reprogramar sucesoras. V02 sólo puede avanzar una vez obtenida la condición de acceso de V01, aunque compartan el 3 de noviembre.

## 5. Mejorar las dependencias y fechas como funciones nativas

Actualmente las dependencias se consultan en la descripción. Para convertirlas en vínculos nativos, cuando el equipo lo acuerde:

1. Abrir la tarea sucesora y elegir la opción de vincular elementos relacionados.
2. Seleccionar **is blocked by / está bloqueada por**.
3. Usar las claves comprobadas de la columna de predecesoras del CSV. Por ejemplo, **C02 = INFORMA-4** estará bloqueada por **C01 = INFORMA-3**.
4. Comprobar que en la predecesora aparece la relación recíproca blocks / bloquea.
5. Repetir para las dependencias del plan y actualizar el registro indicando qué enlaces se crearon realmente.
6. Si la opción no está disponible, conservar las relaciones en la descripción y consultar al administrador sobre permisos o configuración.

Tener una misma épica no establece dependencia. Crear un vínculo tampoco garantiza que Jira impida mover una tarjeta; respetar las condiciones de inicio. [Atlassian, vincular elementos de trabajo](https://support.atlassian.com/jira-software-cloud/docs/link-issues/).

Para incorporar Inicio como campo nativo, comprobar primero si el proyecto lo ofrece y acordar su uso. Sólo después de guardarlo y verificarlo, registrar la fecha como campo confirmado. No cambiar retroactivamente una fecha de inicio propuesta por una fecha de ejecución inexistente.

## 6. Actualizar estado con evidencia

- **Por hacer:** no hay ejecución iniciada o falta condición de entrada.
- **En curso:** el responsable comenzó y puede mostrar avance verificable.
- **Listo:** se cumplieron criterios, el revisor comprobó evidencia y la versión puede localizarse.

Si el tablero utiliza otros nombres, mantener su equivalencia sin inventar estados. Un bloqueo necesita causa, responsable de resolverlo, siguiente acción y fecha de revisión. Usar una marca de impedimento si está habilitada.

Comentario de seguimiento sugerido:

- Resultado comprobado:
- Evidencia o versión:
- Criterios pendientes:
- Bloqueo y responsable de resolverlo:
- Siguiente acción y fecha propuesta:
- Revisor y resultado de revisión:

Una publicación comercial no es una cotización recibida; una solicitud no es autorización; redactar una prueba no demuestra haberla ejecutado. C08 puede quedar listo para entregar sin afirmar una entrega efectuada, que exige constancia propia.

## 7. Comprobar el avance antes de informarlo

1. Abrir las claves de las tarjetas y comprobar que no hay duplicados.
2. Contrastar responsable, vencimiento, épica y estado con CSV/JSON.
3. Verificar acceso de los integrantes sin declarar aceptadas invitaciones pendientes.
4. Consultar inicio, revisor y dependencia en la descripción mientras no existan campos o vínculos nativos.
5. Abrir evidencia y revisión de cada tarjeta Listo.
6. Mantener las validaciones como trabajo pendiente mientras no se ejecuten.
7. Registrar la fecha de cada nueva conciliación del tablero.

Las 16 tarjetas creadas permiten coordinar el plan; su existencia no acredita instalación, aprobación institucional, validación cumplida ni calificación de la rúbrica.
