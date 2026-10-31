"""Genera 13_cotizaciones.tex, descarga imágenes y actualiza procedencia_imagenes.json."""
import hashlib, json, pathlib, string, struct, subprocess, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from cotizaciones_datos import COMPARATIVOS, UNICAS  # noqa: E402

PROY = pathlib.Path(sys.argv[1])
DIR_IMG = PROY / "imagenes" / "cot"
DIR_IMG.mkdir(parents=True, exist_ok=True)
FECHA = "2026-10-30"


def tam_imagen(datos):
    if datos[:8] == b"\x89PNG\r\n\x1a\n":
        return list(struct.unpack(">II", datos[16:24]))
    if datos[:2] == b"\xff\xd8":
        i = 2
        while i < len(datos):
            if datos[i] != 0xFF:
                i += 1
                continue
            marca = datos[i + 1]
            if marca in (0xC0, 0xC1, 0xC2):
                h, w = struct.unpack(">HH", datos[i + 5:i + 9])
                return [w, h]
            largo = struct.unpack(">H", datos[i + 2:i + 4])[0]
            i += 2 + largo
    return None


procedencia_ruta = PROY / "procedencia_imagenes.json"
procedencia = json.loads(procedencia_ruta.read_text(encoding="utf-8"))
por_archivo = {p["file"]: p for p in procedencia}
fallas = []


def descargar(ident, url, pagina):
    """Devuelve la ruta relativa de la imagen o None."""
    if not url:
        return None
    base = url.split("?")[0]
    ext = pathlib.Path(base).suffix.lower()
    if ext not in (".jpg", ".jpeg", ".png"):
        fallas.append((ident, "formato " + ext))
        return None
    destino = DIR_IMG / f"{ident}{'.jpg' if ext == '.jpeg' else ext}"
    if not destino.exists():
        r = subprocess.run(["curl", "-sL", "-m", "40", "-o", str(destino), "-w", "%{http_code}", url],
                           capture_output=True, text=True)
        datos = destino.read_bytes() if destino.exists() else b""
        if r.stdout.strip() != "200" or tam_imagen(datos) is None:
            fallas.append((ident, f"HTTP {r.stdout.strip()}"))
            destino.unlink(missing_ok=True)
            return None
    datos = destino.read_bytes()
    clave = f"cot/{destino.name}"
    sha = hashlib.sha256(datos).hexdigest()
    por_archivo[clave] = {"file": clave, "source_page": pagina, "source_image_url": url, "retrieved": FECHA,
                          "original_sha256": sha, "original_size": tam_imagen(datos),
                          "processing": "sin modificar", "sha256": sha, "size": tam_imagen(datos)}
    return f"imagenes/cot/{destino.name}"


contador = [0]


def nombre_macro():
    n = contador[0]; contador[0] += 1
    letras = ""
    while True:
        letras = string.ascii_lowercase[n % 26] + letras
        n = n // 26 - 1
        if n < 0:
            break
    return "\\cotu" + letras


def celda_img(ruta, alto="2.3cm"):
    return f"\\imgficha{{{ruta}}}{{{alto}}}" if ruta else "\\emph{Sin imagen publicada}"


salida = []
w = salida.append
w("% Anexo de cotizaciones generado a partir de las consultas del 30 de octubre de 2026.")
w("\\section{Cotizaciones por componente}\\label{sec:cotizaciones}")
w("Este anexo presenta cada componente del presupuesto como una cotización comparada: imagen referencial, características publicadas, proveedor, precio y enlace del producto, con una columna que explica qué significa cada característica. Las opciones se contrastan con la especificación ET que corresponde y se elige con la regla de la sección \\ref{sec:seleccion}: menor costo entre las opciones que cumplen y están documentadas.")
w("")
w("Los terminales, los módulos fotovoltaicos y el alojamiento se comparan en los cuadros \\ref{tab:fichas-totems}, \\ref{tab:modulos_comparados} y \\ref{tab:comp_hosting}. Las imágenes son referenciales, se reproducen con fines académicos y su página de origen, URL y huella SHA-256 se registran en \\texttt{procedencia\\_imagenes.json}. Todas las consultas son del 30 de octubre de 2026.")
w("")
w("\\begin{landscape}")

for comp in COMPARATIVOS:
    ops = comp["opciones"]
    n = len(ops)
    rutas = [descargar(o["id"], o["img"], o["pagina"]) for o in ops]
    macros_pag, macros_img = [], []
    for o, ruta in zip(ops, rutas):
        m = nombre_macro(); w(f"\\urldef{{{m}}}\\url{{{o['pagina']}}}"); macros_pag.append(m)
        if o["img"] and ruta:
            mi = nombre_macro(); w(f"\\urldef{{{mi}}}\\url{{{o['img'].split('?')[0]}}}"); macros_img.append(mi)
        else:
            macros_img.append(None)
    cols = "@{}>{\\raggedright\\arraybackslash}p{3.0cm}" + "Y" * n + ">{\\raggedright\\arraybackslash}p{4.4cm}@{}"
    compacta = n >= 4 or len(comp["filas"]) >= 8
    alto = "1.8cm" if compacta else "2.3cm"
    estilo = "\\formatofichas\\scriptsize\\renewcommand{\\arraystretch}{1.0}" if compacta else "\\formatofichas"
    w("\\par\\noindent\\begin{minipage}{\\linewidth}" + estilo)
    w(f"\\captionof{{table}}{{Cotización de {comp['titulo']}}}\\label{{tab:cot-{comp['clave']}}}")
    w(f"\\begin{{tabularx}}{{\\linewidth}}{{{cols}}}")
    w("\\toprule")
    w("\\textbf{Característica} & " + " & ".join(f"\\textbf{{Opción {i + 1}: {o['nombre']}}}" for i, o in enumerate(ops)) + " & \\textbf{Descripción}\\\\\\midrule")
    w("\\textbf{Imagen referencial} & " + " & ".join(celda_img(r, alto) for r in rutas) + " & Fotografía publicada por el proveedor\\\\")
    for etiqueta, valores, desc in comp["filas"]:
        assert len(valores) == n, (comp["clave"], etiqueta)
        w(f"\\textbf{{{etiqueta}}} & " + " & ".join(valores) + f" & {desc}\\\\")
    w("\\textbf{Proveedor e IGV} & " + " & ".join(o["proveedor"] for o in ops) + " & Tienda peruana y tratamiento tributario declarado\\\\")
    w("\\textbf{Precio unitario S/} & " + " & ".join(f"\\textbf{{{o['precio']}}}" for o in ops) + " & Precio publicado en la fecha de consulta\\\\")
    w("\\textbf{Enlace del producto} & " + " & ".join(f"{{\\scriptsize{m}}}" for m in macros_pag) + " & Página consultada\\\\")
    w("\\textbf{Fuente de la imagen} & " + " & ".join(f"{{\\scriptsize{m}}}" if m else "Sin imagen" for m in macros_img) + " & Archivo de imagen descargado\\\\")
    w("\\bottomrule")
    w("\\end{tabularx}")
    w(f"\\fuentefichas{{Páginas de producto consultadas el 30 de octubre de 2026 \\cite{{{comp['cite']}}}. C: cumple y está documentado; P: por acreditar en la oferta; N: no cumple.}}")
    w("\\end{minipage}\\par\\vspace{10pt}")
    w("")

for grupo in UNICAS:
    items = grupo["items"]
    n = len(items)
    rutas = [descargar(it["id"], it["img"], it["pagina"]) for it in items]
    macros_pag, macros_img = [], []
    for it, ruta in zip(items, rutas):
        m = nombre_macro(); w(f"\\urldef{{{m}}}\\url{{{it['pagina']}}}"); macros_pag.append(m)
        if it["img"] and ruta:
            mi = nombre_macro(); w(f"\\urldef{{{mi}}}\\url{{{it['img'].split('?')[0]}}}"); macros_img.append(mi)
        else:
            macros_img.append(None)
    cols = "@{}>{\\raggedright\\arraybackslash}p{3.0cm}" + "Y" * n + "@{}"
    w("\\par\\noindent\\begin{minipage}{\\linewidth}\\formatofichas")
    w(f"\\captionof{{table}}{{Cotización de oferta única: {grupo['titulo']}}}\\label{{tab:cot-{grupo['clave']}}}")
    w(f"\\begin{{tabularx}}{{\\linewidth}}{{{cols}}}")
    w("\\toprule")
    w("\\textbf{Característica} & " + " & ".join(f"\\textbf{{{it['nombre']}}}" for it in items) + "\\\\\\midrule")
    w("\\textbf{Imagen referencial} & " + " & ".join(celda_img(r) for r in rutas) + "\\\\")
    w("\\textbf{Uso en el proyecto} & " + " & ".join(it["uso"] for it in items) + "\\\\")
    w("\\textbf{Características publicadas} & " + " & ".join(it["carac"] for it in items) + "\\\\")
    w("\\textbf{Proveedor e IGV} & " + " & ".join(it["proveedor"] for it in items) + "\\\\")
    w("\\textbf{Cantidad} & " + " & ".join(it["cant"] for it in items) + "\\\\")
    w("\\textbf{Precio unitario S/} & " + " & ".join(f"\\textbf{{{it['precio']}}}" for it in items) + "\\\\")
    w("\\textbf{Parcial S/} & " + " & ".join(it["parcial"] for it in items) + "\\\\")
    w("\\textbf{Enlace del producto} & " + " & ".join(f"{{\\scriptsize{m}}}" for m in macros_pag) + "\\\\")
    w("\\textbf{Fuente de la imagen} & " + " & ".join(f"{{\\scriptsize{m}}}" if m else "Sin imagen" for m in macros_img) + "\\\\")
    w("\\bottomrule")
    w("\\end{tabularx}")
    w(f"\\fuentefichas{{Componentes con una sola oferta identificada en la consulta del 30 de octubre de 2026; se aceptará cualquier equivalente que cumpla la especificación \\cite{{{grupo['cite']}}}.}}")
    w("\\end{minipage}\\par\\vspace{10pt}")
    w("")

w("\\end{landscape}")
w("")
w("\\section{Evidencia de gestión del equipo}\\label{sec:evidencia_gestion}")
w("El tablero de Jira del proyecto organiza las actividades de formulación y validación en dos épicas y dieciséis tareas con responsable asignado. La figura \\ref{fig:jira} muestra la lista de tareas del espacio INFORMA UNSAAC. El cronograma de implementación se presenta en el diagrama de Gantt de la figura \\ref{fig:gantt}.")
w("\\figura{gestion/jira_proyecto_creado.png}{Espacio de trabajo del proyecto en Jira con tareas asignadas}{fig:jira}{11cm}")

(PROY / "13_cotizaciones.tex").write_text("\n".join(salida) + "\n", encoding="utf-8")
procedencia_ruta.write_text(json.dumps(list(por_archivo.values()), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("tablas:", len(COMPARATIVOS) + len(UNICAS), "| imágenes en cot/:", len(list(DIR_IMG.iterdir())), "| fallas:", fallas)
