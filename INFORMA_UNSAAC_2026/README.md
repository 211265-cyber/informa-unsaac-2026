# INFORMA UNSAAC: proyecto integral 2026

Proyecto LaTeX completo del servicio de información institucional de la EPIIS, con tres terminales táctiles, gestión central de contenidos, red local, videovigilancia de los equipos, respaldo y evaluación de generación solar. Esta versión desarrolla formulación, diseño, evaluación de alternativas, ejecución, transferencia, operación y cierre.

## Archivos

- `main.tex`: entrada principal del mismo proyecto.
- `main.pdf`: informe compilado con XeLaTeX.
- `estilo.tex`, `portada.tex` y `contenido.tex`: presentación, carátula, índices y resumen.
- `01_formulacion.tex`: problema y árbol de problemas, origen, finalidad pública con sustento normativo y de acreditación, estadísticas e insumos, árbol de objetivos, objetivos, matriz de marco lógico, población, fuentes de información, ficha técnica de la encuesta y alternativas.
- `08_mercado_tecnologico.tex`: cuadro comparativo de cuatro tótems con imagen, configuración, precio y enlaces; matriz de cumplimiento; fuentes de precio y catálogos de PERÚ COMPRAS; CMS.
- `02_tecnica.tex`: arquitectura, origen y emisores de la información, requisitos, datos, planos y diseño energético.
- `10_comparacion_energia.tex`: cuadro comparativo de cuatro módulos FV con imagen, ficha, precio y enlaces; conjunto energético elegido y compatibilidad.
- `11_especificaciones.tex`: especificaciones técnicas ET-01 a ET-10 sin marca, decisiones de dimensionamiento, cálculo del servidor, metrado de red, videovigilancia, protecciones, caídas de tensión, cuadro de cargas y mantenimiento por equipo.
- `12_seleccion_mercado.tex`: cuadros comparativos de inversores, baterías, red, videovigilancia y alojamiento, con la opción elegida y su razón.
- `03_presupuesto.tex`: precios publicados partida por partida, estimaciones propias, inversión, operación, reposición, sensibilidad, costos a cinco años con gráfico generado en LaTeX, valor actual de costos al 8 % e índice de costo-efectividad por estudiante.
- `04_gestion.tex`: entregables, responsabilidades, viabilidad, riesgos y coordinación.
- `07_ejecucion_operacion.tex`: EDT, programación con diagrama de Gantt, adquisiciones, pruebas, transferencia, operación y evaluación.
- `09_conclusiones.tex`, `05_referencias.tex` y `06_anexos.tex`: conclusiones, bibliografía normativa, técnica y comercial, encuesta, documentación exigible por especificación y procedencia de las características de cada marca.
- `imagenes/`, `escudo_UNSAAC.png` y `procedencia_imagenes.json`: imágenes y registro de procedencia. Las ocho imágenes `mercado_*.jpg` son fotografías referenciales de producto; el registro conserva página de origen, URL de la imagen, fecha de consulta, huellas SHA-256 y el tratamiento aplicado.
- `gestion/evidencia/`: modelo económico reproducible y serie regional NASA POWER.
- `gestion/REVISION_CRITICA.md`: evaluación interna del documento.
- `validacion.json`: comprobaciones de la entrega.

## Compilación

Conservar toda la estructura y compilar `main.tex` con XeLaTeX. Las referencias y los índices requieren más de una pasada; latexmk automatiza las repeticiones. La carátula muestra únicamente 2026.

## Alcance y evidencia

Los resultados de operación y de aceptación se medirán durante la ejecución propuesta. La encuesta conserva los datos y gráficos disponibles del informe original; la revisión de 2026 no representa una nueva aplicación. Las fotografías y los planos originales se conservan sin alterar y se ubican en el desarrollo técnico. Las fichas oficiales y las publicaciones de proveedores se enlazan desde las referencias.

El modelo económico utiliza soles constantes de 2026, un horizonte de cinco años y supuestos explícitos; incorpora además el valor actual de costos con la tasa social de descuento de 8 % y el índice de costo-efectividad para 830 a 870 estudiantes. La matrícula es una referencia del equipo y se confirmará con el registro oficial de 2026-II. Los precios publicados de terminales, energía, red y videovigilancia se consultaron el 30 de octubre de 2026 en proveedores identificados; el 59 % de la base de A2 procede de ellos. Los importes en dólares se convierten con el tipo de cambio SBS del BCRP del 9 de octubre de 2026. El conjunto con FV requiere levantamiento local, medición de carga y cierre de compatibilidad, diseño, ofertas y autorizaciones antes de ejecutar.

## Jira

Los archivos de Jira en `gestion/` documentan el tablero creado para formulación y validación, con dos épicas y dieciséis tareas. No equivalen a la programación de las dieciséis semanas de implementación desarrollada en esta versión integral. Esta ampliación documental no modifica el tablero ni acredita actividades ejecutadas.

## Conservación

Las entregas anteriores de primera parcial se conservan fuera de esta carpeta. Los materiales sincronizados de `sources/` son referencias de solo lectura y no forman parte de las fuentes editables del informe.
