"""Datos del anexo de cotizaciones (consultas del 30/10/2026)."""
AS = "https://autosolar.pe/"
CA = "https://cdn.autosolar.pe/images/"
AR = "https://arteus.pe/products/"
AI = "https://arteus.pe/cdn/shop/files/"
PM = "https://www.promelsa.com.pe/"
PI = "https://www.promelsa.com.pe/media/catalog/product/cache/6b4130b32769b1778be6c5b443fe5cb6/"
P_AS = "AutoSolar Perú; IGV incluido"
P_AR = "ARTEUS S.A.C., RUC 20608279637; IGV incluido"
P_PM = "Promelsa; IGV no declarado"

def op(id, nombre, img, pagina, proveedor, precio):
    return dict(id=id, nombre=nombre, img=img, pagina=pagina, proveedor=proveedor, precio=precio)

COMPARATIVOS = [
 dict(clave="inv", titulo="inversor híbrido, ET-05", cite="tensiteinv,suntaicinv,livoltek,growattsph", opciones=[
   op("inv-tensite", "Tensite AH4M-2", CA+"3206103/inversor-hibrido-tensite-4kw-monofasico-ah4m-2-thumb.jpg", AS+"inversores-hibridos/inversor-hibrido-tensite-4kw-monofasico-ah4m-2", P_AS, "6\\,537,03"),
   op("inv-suntaic", "Suntaic STH6M-2/GEN", CA+"3200605/inversor-hibrido-6kw-monofasico-sth6m-2gen-suntaic-684995754ef03-thumb.jpg", AS+"inversores-hibridos-monofasicos/inversor-hibrido-6kw-monofasico-sth6m-2gen-suntaic", P_AS, "4\\,077,77"),
   op("inv-livoltek", "Livoltek Hyper-5000", CA+"3203003/inversor-hibrido-monofasico-5kw-220v-hyper-5000-livoltek-6ad14d44a1e71-thumb.jpg", AS+"inversores-hibridos-monofasicos/inversor-hibrido-monofasico-5kw-220v-hyper-5000-livoltek", P_AS, "2\\,960,94"),
   op("inv-growatt", "Growatt SPH3000", CA+"3205070/inversor-hibrido-3kw-growatt-sph3000-thumb.jpg", AS+"inversores-hibridos/inversor-hibrido-3kw-growatt-sph3000", P_AS, "8\\,368,82")],
  filas=[
   ("Potencia nominal", ["4\\,000 W", "6\\,000 W", "5\\,000 W", "3\\,000 W"], "Potencia AC continua que entrega a las cargas; la carga crítica es de 640 W"),
   ("Corriente por MPPT", ["16 A", "15 A", "14 A", "12 A"], "Corriente máxima que admite cada seguidor; debe igualar o superar la Imp de 15,15 A del módulo"),
   ("Cortocircuito por MPPT", ["20 A", "18 A", "17,5 A", "No publicado"], "Debe superar la Isc de 16,02 A de la cadena"),
   ("Tensión FV máxima y rango MPPT", ["550 V; 40 a 530 V", "550 V; 90 a 500 V", "600 V; 125 a 550 V", "550 V; 150 a 550 V"], "La cadena llega a 318,94 V en frío y trabaja cerca de 243,6 V"),
   ("Batería", ["48 V, 40 a 60 V; 100 A", "48 V, 42 a 59 V; 100 A", "40 a 60 V; 100 A", "42 a 59 V; 66 A"], "Tensión y corriente de carga y descarga del banco de litio"),
   ("Respaldo", ["5\\,000 VA; conmutación de 10 ms", "6\\,000 VA", "5\\,000 W", "3\\,000 W"], "Potencia disponible durante un corte de red"),
   ("Eficiencia y protección", ["97,6\\%; IP66", "98\\%; IP65", "97,8\\%; IP65", "Cerca de 98\\%; IP65"], "Pérdidas de conversión y resistencia al polvo y al agua"),
   ("Altitud de operación", ["4\\,000 m; reducción sobre 3\\,000 m", "3\\,000 m", "No publicada", "Por verificar"], "Cusco se ubica cerca de 3\\,400 m"),
   ("Garantía", ["10 años de producto", "No publicada", "No publicada", "5 años, ampliable a 10"], "Respaldo del fabricante durante el horizonte"),
   ("Cumplimiento de ET-05", ["C", "N: 15 A y 3\\,000 m", "N: 14 A", "N: 12 A"], "C cumple y está documentado; P por acreditar; N no cumple"),
   ("Resultado", ["\\textbf{Elegida}", "Recortaría la producción", "Recortaría la producción", "Más cara y recorta la producción"], "Regla: menor costo entre las opciones sin N"),
  ]),
 dict(clave="bat", titulo="batería de litio, ET-07", cite="tensitebat,suntaicbat,felicity,pylonas", opciones=[
   op("bat-tensite", "Tensite TS-L5000/LV", CA+"1880811/bateria-litio-48kwh-48v-ts-l5000lv-tensite-thumb.jpg", AS+"baterias-de-litio-48v/bateria-litio-48kwh-48v-ts-l5000lv-tensite", P_AS, "4\\,178,47"),
   op("bat-suntaic", "Suntaic ST-L5000/LV", CA+"1882301/bateria-de-litio-solar-suntaic-st-l5000lv-48v-5kwh-thumb.jpg", AS+"baterias-de-litio-48v/bateria-de-litio-solar-48v-5kwh-st-l5000lv-suntaic", P_AS, "3\\,535,17"),
   op("bat-felicity", "Felicity LPBF48100", CA+"1880952/bateria-de-litio-5kwh-48v-100ah-lpbf48100-felicity-solar-68ded8253b4d7-thumb.jpg", AS+"baterias-de-litio-48v/bateria-de-litio-48v-5kwh-100ah-lpbf48100-felicity-solar", P_AS, "3\\,266,66"),
   op("bat-pylontech", "Pylontech US5000", CA+"1880909/bateria-litio-48kwh-pylontech-us5000-48v-thumb.jpg", AS+"baterias-de-litio-48v/bateria-litio-48kwh-pylontech-us5000-48v", "AutoSolar sin precio; Sunperu sin IGV", "7\\,493,00 con IGV en Sunperu")],
  filas=[
   ("Química y tensión", ["LiFePO4; 48 V", "LiFePO4 16S; 51,2 V", "LiFePO4; 51,2 V", "Ión-litio; 48 V"], "Química estable y tensión del bus de baterías"),
   ("Energía total y útil", ["4,8 kWh; 4,3 kWh", "5,22 kWh; 4,7 kWh", "5 kWh útiles", "4,8 kWh; profundidad 95\\%"], "Energía para cuatro horas: se requieren 2,56 kWh AC"),
   ("Ciclos de vida", ["Más de 6\\,000 al 80\\%", "No publicado", "6\\,000 o más", "Más de 6\\,000 al 95\\%"], "Duración esperada antes de la reposición"),
   ("Corriente", ["60 A nominal; 100 A continuos", "50 A nominal; 100 A máx.", "No publicada", "No publicada"], "Debe sostener la descarga del inversor"),
   ("Temperatura de carga", ["0 a 50\\,°C", "No publicada", "No publicada", "0 a 50\\,°C según manual"], "Cusco tiene madrugadas frías en el cuarto técnico"),
   ("Comunicación", ["CAN y RS485", "CAN y RS485", "CAN y RS485", "CAN y RS485"], "Enlace del BMS con el inversor"),
   ("Garantía", ["5 años", "No publicada", "No publicada", "10 años"], "Coincide con la reposición del año 5 del flujo"),
   ("Compatibilidad con el inversor elegido", ["Mismo fabricante", "Por acreditar", "Por acreditar", "Por acreditar"], "Protocolo del BMS reconocido por el inversor"),
   ("Cumplimiento de ET-07", ["C", "P: ciclos y compatibilidad", "P: ficha no enlazada", "P: compatibilidad"], "C cumple y está documentado; P por acreditar"),
   ("Resultado", ["\\textbf{Elegida}", "Equivalente si acredita", "Equivalente si acredita", "S/ 3\\,314,53 más cara"], "Menor costo entre las documentadas"),
  ]),
 dict(clave="est", titulo="estructura de montaje FV, ET-08", cite="autosolarfv", opciones=[
   op("est-incl3", "Falcat inclinada 15°, 3 módulos", CA+"1501662/estructura-3-paneles-144c-15o-inclinada-falcat-thumb.jpg", AS+"soportes-suelo/estructura-3-paneles-144c-15o-inclinada-falcat", P_AS, "459,61"),
   op("est-copl3", "Falcat coplanar, 3 módulos", CA+"1507115/estructura-3-paneles-144c-40mm-coplanar-falcat-thumb.jpg", AS+"soportes-cubierta-metalica/estructura-3-paneles-144c-40mm-coplanar-falcat", P_AS, "346,26"),
   op("est-incl2", "Falcat inclinada 15°, 2 módulos", CA+"1501661/estructura-2-paneles-144c-15o-inclinada-falcat-thumb.jpg", AS+"soportes-suelo/estructura-2-paneles-144c-15o-inclinada-falcat", P_AS, "327,83")],
  filas=[
   ("Tipo de montaje", ["Inclinada 15° para losa", "Coplanar para cubierta metálica", "Inclinada 15°, ajustable 15 a 30°"], "Cusco está a 13,5° S; la inclinación favorece captación y autolimpieza"),
   ("Módulos admitidos", ["144 celdas hasta 1,134 $\\times$ 2,4 m", "Marco de 35 a 45 mm", "144 celdas hasta 1,134 $\\times$ 2,4 m"], "El módulo elegido mide 2,382 $\\times$ 1,134 m y 30 mm"),
   ("Componentes", ["2 rieles de aluminio de 3,70 m; 4 abrazaderas", "2 rieles de 3,70 m; 6 soportes L", "2 rieles de 2,50 m; soporte ajustable"], "Piezas incluidas en el kit"),
   ("Kits para 6 módulos", ["2: S/ 919,22", "2: S/ 692,52", "3: S/ 983,49"], "Costo del conjunto completo"),
   ("Cumplimiento de ET-08", ["C", "N: sin inclinación; para cubierta metálica", "C"], "La especificación pide inclinación de 10 a 20° sobre losa"),
   ("Resultado", ["\\textbf{Elegida}", "No aplica a la losa", "S/ 64,27 más por conjunto"], "Menor costo para seis módulos inclinados"),
  ]),
 dict(clave="sdc", titulo="seccionador DC, ET-09", cite="autosolarfv", opciones=[
   op("sdc-25", "DC Solar Energy 25 A 4P", CA+"7107110/interruptor-termomagnetico-25a-4p-1500vdc-dc-solar-energy-68b2060a19496-thumb.jpg", AS+"termomagneticos-dc/interruptor-termomagnetico-25a-4p-1500vdc-dc-solar-energy", P_AS, "94,21"),
   op("sdc-16", "ZJ Beny 2 $\\times$ 16 A", CA+"7107010/interruptor-termomagnetico-2x16a-600vdc-zj-beny-thumb.jpg", AS+"termomagneticos-dc/interruptor-termomagnetico-2x16a-600vdc-zj-beny", P_AS, "50,03"),
   op("sdc-63", "DC Solar Energy 63 A 2P", CA+"7107086/7107086-thumb.jpg", AS+"termomagneticos-dc/interruptor-termomagnetico-63a-500vdc-2p-dc-solar-energy", P_AS, "74,27")],
  filas=[
   ("Corriente nominal", ["25 A", "16 A", "63 A"], "Debe ser 1,25 $\\times$ Isc, es decir 20,0 A o más"),
   ("Tensión DC", ["1\\,500 V DC", "600 V DC", "120 a 500 V DC"], "La cadena alcanza 318,94 V; ET-09 exige 600 V DC"),
   ("Polos y corte", ["4 polos; 6 kA", "2 polos", "2 polos; 6 kA; curva C"], "Polos en serie elevan la tensión admisible"),
   ("Cumplimiento de ET-09", ["C", "N: 16 A", "N: 500 V"], "Corriente y tensión mínimas"),
   ("Resultado", ["\\textbf{Elegida}", "Dispararía con la corriente de cortocircuito", "Tensión insuficiente"], "Única opción que cumple ambas condiciones"),
  ]),
 dict(clave="spd", titulo="protector de sobretensiones DC, ET-09", cite="autosolarfv", opciones=[
   op("spd-feeo", "FEEO 2P 600 V DC", CA+"7102501/proteccion-sobretensiones-600vdc-2p-20ka-40ka-feeo-thumb.jpg", AS+"protector-de-sobretensiones/proteccion-sobretensiones-600vdc-2p-20ka-40ka-feeo", P_AS, "173,07"),
   op("spd-beny", "ZJ Beny 2P 600 V DC", CA+"7102507/proteccion-sobretensiones-600vdc-2p-40ka-zj-beny-thumb.jpg", AS+"protector-de-sobretensiones/proteccion-sobretensiones-600vdc-2p-40ka-zj-beny", P_AS, "266,82"),
   op("spd-t12", "FEEO tipo 1+2, 600 V DC", CA+"7102529/dps-2p-600vdc-2040kva-t12-feeo-thumb.jpg", AS+"protector-de-sobretensiones/dps-2p-600vdc-2040kva-t12-feeo", P_AS, "571,92")],
  filas=[
   ("Tensión FV máxima", ["600 V", "600 V", "600 V"], "Supera los 318,94 V de la cadena"),
   ("Corriente de descarga", ["20 kA nominal; 40 kA máx.", "20 kA nominal; 40 kA máx.", "20 kA nominal; 40 kA máx."], "Energía que deriva a tierra"),
   ("Tipo y nivel de protección", ["Tipo 2", "Tipo 2; respuesta de 25 ns o menos", "Tipo 1+2; 2,8 kV"], "El tipo 1 sólo se exige con pararrayos o descarga directa"),
   ("Cumplimiento de ET-09", ["C", "C", "C, con capacidad no requerida"], "600 V DC y 20 a 40 kA"),
   ("Resultado", ["\\textbf{Elegida}", "S/ 93,75 más", "S/ 398,85 más"], "Menor costo entre las que cumplen"),
  ]),
 dict(clave="dif", titulo="interruptor diferencial, ET-09", cite="autosolarac", opciones=[
   op("dif-25", "ABB 25 A 30 mA tipo A", CA+"7103040/interruptor-diferencial-monofasico-25a-abb-30ma-tipo-a-2p-thumb.jpg", AS+"interruptores-diferenciales/interruptor-diferencial-monofasico-25a-abb-30ma-tipo-a-2p", P_AS, "179,27"),
   op("dif-40", "ABB 40 A 30 mA tipo A", CA+"7103042/interruptor-diferencial-monofasico-40a-abb-30ma-tipo-a-2p-thumb.jpg", AS+"diferencial-monofasico/interruptor-diferencial-monofasico-40a-abb-30ma-tipo-a-2p", P_AS, "181,51")],
  filas=[
   ("Corriente nominal", ["25 A", "40 A"], "Debe superar el termomagnético de 16 A que protege"),
   ("Sensibilidad y tipo", ["30 mA; tipo A", "30 mA; tipo A"], "Protección de personas; el tipo A detecta fugas con componente pulsante de las fuentes electrónicas"),
   ("Polos y tensión", ["2 polos; 230/400 V", "2 polos"], "Circuito monofásico"),
   ("Cumplimiento de ET-09", ["C", "C"], "30 mA por circuito derivado"),
   ("Resultado", ["\\textbf{Elegida}, 2 unidades", "Capacidad innecesaria"], "Menor costo entre las que cumplen"),
  ]),
 dict(clave="tab", titulo="tablero de distribución, ET-09", cite="autosolarac", opciones=[
   op("tab-18", "Tablero adosable de 18 polos", CA+"5504057/tablero-adosable-18-polos-thumb.jpg", AS+"tableros-adosables/tablero-adosable-18-polos", P_AS, "104,89"),
   op("tab-12", "Tablero adosable de 12 polos", CA+"5504054/tablero-adosable-12-polos-thumb.jpg", AS+"tableros-adosables/tablero-adosable-12-polos", P_AS, "89,07"),
   op("tab-08", "Tablero adosable de 8 polos", CA+"5504052/tablero-adosable-8-polos-thumb.jpg", AS+"tableros-adosables/tablero-adosable-8-polos", P_AS, "74,67")],
  filas=[
   ("Capacidad", ["18 polos", "12 polos", "8 polos"], "Se requieren 14 polos: dos 2P de 32 A, dos 2P de 16 A, dos diferenciales y un protector"),
   ("Material y protección", ["ABS retardante al fuego; IP40 o IP41", "ABS", "ABS retardante al fuego; IP40 o IP41"], "Envolvente aislante para interior"),
   ("Cumplimiento de ET-09", ["C: 4 polos de reserva", "N: faltan 2 polos", "N: faltan 6 polos"], "Capacidad mínima del tablero crítico"),
   ("Resultado", ["\\textbf{Elegida}", "Insuficiente", "Insuficiente"], "Única capacidad suficiente"),
  ]),
 dict(clave="mon", titulo="módulo de monitoreo, ET-10", cite="autosolarmed", opciones=[
   op("mon-tensite", "Tensite T-Dongle", CA+"3206014/monitorizacion-t-dongle-tensite-thumb.jpg", AS+"accesorios-de-inversores/monitorizacion-t-dongle-tensite", P_AS, "147,84"),
   op("mon-suntaic", "Suntaic Stick", CA+"3001030/monitorizacion-stick-suntaic-693c486dca86e-thumb.jpg", AS+"accesorios-de-inversores/monitorizacion-stick-suntaic", P_AS, "126,54"),
   op("mon-growatt", "Growatt Shine WiFi-X", CA+"3202018/monitorizacion-growatt-shine-wifi-x-thumb.jpg", AS+"accesorios-de-inversores/monitorizacion-growatt-shine-wifi-x", P_AS, "209,16")],
  filas=[
   ("Comunicación", ["WiFi; IP66", "Enlace con teléfono; alarmas", "WiFi 802.11 b/g/n"], "Envío de datos de energía y alarmas"),
   ("Compatibilidad", ["Inversores Tensite", "Inversores Suntaic", "Inversores Growatt X y MIN-XE"], "Debe corresponder al inversor elegido"),
   ("Cumplimiento de ET-10", ["C", "N: otra marca de inversor", "N: otra marca de inversor"], "Registro exportable del inversor instalado"),
   ("Resultado", ["\\textbf{Elegida}", "Incompatible", "Incompatible y más cara"], "Única compatible"),
  ]),
 dict(clave="mc4", titulo="conector MC4, ET-09", cite="autosolarfv", opciones=[
   op("mc4-multi", "Multicontact macho-hembra", CA+"5504044/conector-mc4-multicontact-macho-hembra-thumb.jpg", AS+"accesorios-de-paneles-solares/conector-mc4-multicontact-macho-hembra", P_AS, "10,70"),
   op("mc4-weid", "Weidmuller PV Stick", CA+"5504017/conectores-mc4-pvstick-weidmuller-thumb.jpg", AS+"accesorios-de-paneles-solares/conectores-mc4-pvstick-weidmuller", P_AS, "33,81")],
  filas=[
   ("Presentación", ["Par macho y hembra", "Conector sin herramientas, con polaridad marcada"], "Unión de cables de la cadena FV"),
   ("Sección admitida", ["Cable solar de 6 mm²", "Hasta 10 mm²"], "El cable elegido es de 6 mm²"),
   ("Protección", ["Contra humedad y agua", "No publicada"], "Uso a la intemperie en la cubierta"),
   ("Cumplimiento de ET-09", ["C", "C"], "Compatibilidad con el cable de 6 mm²"),
   ("Resultado", ["\\textbf{Elegida}, 4 pares", "S/ 23,11 más por unidad"], "Menor costo entre las que cumplen"),
  ]),
 dict(clave="cam", titulo="cámara IP, ET-04", cite="arteuscctv", opciones=[
   op("cam-hdw1431", "Dahua DH-IPC-HDW1431T1P-S6", AI+"IPC-HDW1431T1-S4.jpg?v=1790332630&width=500", AR+"dahua-dh-ipc-hdw1431t1p-s6-camara-de-seguridad-ip-poe-4mp-2k-2-8mm-wdr-ip67-ir-30m", P_AR, "219,00"),
   op("cam-hdbw1431", "Dahua DH-IPC-HDBW1431EN-S4", AI+"IPC-HDBW1431E-S4.jpg?v=1790332496&width=500", AR+"dahua-dh-ipc-hdbw1431en-s4-camara-de-vigilancia-ip-poe-2k-4mp-2-8mm-wdr-ip67-ir-30m", P_AR, "231,00"),
   op("cam-hdw2449", "Dahua IPC-HDW2449T-S-IL", AI+"IPC-HDW2449T-S-IL.jpg?v=1790332657&width=500", AR+"dahua-ipc-hdw2449t-s-il-camara-ip-poe-4mp-2k-2-8mm-wdr-ip67-microfono-ir-led-30m-wizsense", P_AR, "291,00")],
  filas=[
   ("Resolución", ["4 MP, 2\\,560 $\\times$ 1\\,440", "4 MP, 2K", "Título 4 MP; ficha 1\\,920 $\\times$ 1\\,080"], "Detalle para reconocer personas a 2 a 5 m"),
   ("Lente y visión nocturna", ["2,8 mm; IR de 30 m", "2,8 mm; IR de 30 m", "2,8 mm; IR de 30 m"], "Ángulo amplio sobre el terminal y su entorno"),
   ("Compresión", ["H.265+", "No publicada", "H.265+"], "Menor almacenamiento por día de grabación"),
   ("Alimentación", ["PoE 802.3af; 4,3 W", "PoE; consumo no publicado", "PoE 802.3af; 4,4 W"], "Se alimenta desde el NVR; entra en la cota de 40 W"),
   ("Otros", ["WDR de 120 dB; IP67", "Domo; IP67", "Micrófono; microSD de 256 GB"], "El micrófono no se requiere y aumenta el tratamiento de datos"),
   ("Stock", ["Disponible", "Contactar al vendedor", "Disponible"], "Disponibilidad verificable en la página"),
   ("Cumplimiento de ET-04", ["C", "P: compresión y consumo", "P: resolución"], "4 MP, H.265, PoE y 6 W como máximo"),
   ("Resultado", ["\\textbf{Elegida}, 3 unidades", "Ficha incompleta", "Resolución dudosa y más cara"], "Menor costo entre las documentadas"),
  ]),
 dict(clave="nvr", titulo="grabador NVR, ET-04", cite="arteuscctv", opciones=[
   op("nvr-dahua", "Dahua NVR1104HS-P-S3/H", AI+"NVR1104HS-P-S3-H.jpg?v=1790333288&width=500", AR+"dahua-nvr1104hs-p-s3-h-grabador-nvr-4k-4ch-puertos-poe-hasta-8mp-80mbps-1hdd-hasta-8tb", P_AR, "292,00"),
   op("nvr-vigi", "TP-Link VIGI NVR1004H-4P", AI+"VIGINVR1004H-4P.jpg?v=1792613026&width=500", AR+"tp-link-vigi-nvr1004h-4p-grabador-de-video-nvr-4-canales-poe-4k", P_AR, "280,00"),
   op("nvr-hilook", "Hilook NVR-104H-D/4P", AI+"NVR-104H-D-4P-2.jpg?v=1790400970&width=500", AR+"hilook-nvr-104h-d-4p-mini-grabador-nvr-poe-4-canales-6mp", P_AR, "227,00")],
  filas=[
   ("Canales y PoE", ["4 canales; 4 puertos PoE+", "4 canales; 4 PoE+, 53 W", "4 canales; 4 PoE, 36 W"], "Tres cámaras más una reserva, alimentadas desde el grabador"),
   ("Ancho de banda de entrada", ["80 Mbps", "80 Mbps", "40 Mbps"], "Se requieren 12 Mbps; ET-04 exige 40 Mbps o más"),
   ("Resolución máxima", ["8 MP", "4K", "6 MP"], "Debe admitir las cámaras de 4 MP"),
   ("Disco", ["1 SATA hasta 8 TB", "1 SATA hasta 10 TB; la descripción indica 2 TB preinstalado", "1 SATA hasta 6 TB"], "El cálculo requiere 2 TB"),
   ("Compatibilidad con las cámaras", ["Nativa, misma marca", "ONVIF por demostrar", "ONVIF por demostrar"], "Registro automático, detección y hora"),
   ("Stock", ["Disponible", "Disponible", "No indicado"], "Disponibilidad verificable"),
   ("Cumplimiento de ET-04", ["C", "P: compatibilidad y disco", "P: compatibilidad"], "4 canales, 4 PoE, 40 Mbps"),
   ("Resultado", ["\\textbf{Elegida}", "Si acredita disco y compatibilidad, ahorraría hasta S/ 711", "Al límite de ancho de banda"], "Menor costo entre las documentadas"),
  ]),
 dict(clave="sw", titulo="switch administrable, ET-03", cite="arteuscctv", opciones=[
   op("sw-dlink", "D-Link DGS-1100-08P", AI+"DGS-1100-08PV2.jpg?v=1790373923&width=500", AR+"d-link-dgs-1100-08pv2", P_AR, "327,00"),
   op("sw-dahua", "Dahua S4210-8GT-110", AI+"S4210-8GT-110--2.jpg?v=1790433248&width=500", AR+"dahua-s4210-8gt-110-switch-8-puertos-poe-gigabit-110w-poe-watchdog", P_AR, "517,00"),
   op("sw-hik", "Hikvision DS-3E1510P-SI", AI+"hik82.png?v=1790326700&width=500", AR+"hikvision-ds-3e1510p-si-switch-poe-8-puertos-gigabit-2sfp-110w-smart", P_AR, "543,00")],
  filas=[
   ("Puertos", ["8 Gigabit con PoE", "8 Gigabit con PoE y 2 SFP", "8 Gigabit con PoE y 2 SFP"], "Seis puertos usados y dos de reserva; SFP para un enlace de fibra futuro"),
   ("Potencia PoE", ["64 W", "110 W", "110 W"], "No se requiere PoE: las cámaras se alimentan desde el NVR"),
   ("Gestión", ["Web; VLAN 802.1Q no publicada", "Web y SNMP; 4\\,000 VLAN; STP y RSTP", "Smart; VLAN, QoS y SNMP"], "Separar consulta, cámaras y administración"),
   ("Conmutación", ["16 Gbps; sin ventilador", "20 Gbps; carcasa metálica", "No publicada"], "Capacidad interna del equipo"),
   ("Stock", ["Contactar al vendedor", "No indicado", "Disponible"], "Disponibilidad verificable"),
   ("Cumplimiento de ET-03", ["P: VLAN", "C", "C"], "8 puertos, VLAN, QoS y gestión"),
   ("Resultado", ["Se aceptará si acredita 802.1Q", "\\textbf{Elegida}", "S/ 26 más"], "Menor costo entre las documentadas"),
  ]),
 dict(clave="hdd", titulo="disco de videovigilancia, ET-04", cite="arteuscctv,panacompu", opciones=[
   op("hdd-skyhawk", "Seagate SkyHawk ST2000VX017", AI+"images_a56829c6-7b0b-4940-a14e-945ce5d25e1f.jpg?v=1790465448&width=447", AR+"seagate-st2000vx017-skyhawk-disco-duro-2tb-3-5", P_AR, "699,00"),
   op("hdd-wd22", "WD Purple WD22PURZ", AI+"WD22PURZ-3.jpg?v=1790408981&width=500", AR+"western-digital-wd22purz-disco-duro-interno-purple-2tb", P_AR, "271,00"),
   op("hdd-wd23", "WD Purple WD23PURZ", None, "https://www.panacompu.com/peru/en/product-information/western-digital-purple-wd23purz-internal-hard-drive-2tb-5400rpm-35-64mb-cache", "Panacompu; impuestos incluidos", "313,16")],
  filas=[
   ("Capacidad y uso", ["2 TB; videovigilancia continua", "2 TB; videovigilancia", "2 TB; videovigilancia"], "30 días de grabación requieren 1\\,069 GB"),
   ("Velocidad y caché", ["5\\,400 rpm; 256 MB", "5\\,400 rpm; 256 MB", "5\\,400 rpm; 64 MB"], "Escritura continua de tres cámaras"),
   ("Interfaz", ["SATA de 6 Gb/s", "SATA III", "SATA"], "Bahía del NVR"),
   ("Disponibilidad", ["Disponible", "Agotado", "La tienda no acepta pedidos en Perú"], "Stock verificable en la fecha de consulta"),
   ("Resultado", ["\\textbf{Elegida}", "Equivalente si se repone: S/ 428 menos", "Sin compra posible"], "Única con stock verificable"),
  ]),
 dict(clave="utp", titulo="cable UTP Cat 6, ET-03", cite="arteusred,arteuscctv", opciones=[
   op("utp-dixon", "Dixon 9040/24 LSZH", AI+"9040-24-LSZH.jpg?v=1790359475&width=500", AR+"dixon-9040-24-lszh-cable-utp-cat6-cobre-24awg-gris-305m", P_AR, "666,00"),
   op("utp-satra", "Satra 0212021111 LSZH-1", AI+"0212021111-2_518300e2-bc41-4c82-96be-f5966bbc54f4.jpg?v=1790375625&width=500", AR+"satra-0212021111-cable-de-red-utp-cat6-cobre-24awg-lszh-1-gris-305m", P_AR, "667,00"),
   op("utp-legrand", "Legrand 032754 LSZH", None, AR+"legrand-032754-cable-utp-cat6-lszh-rollo-305m-azul", P_AR, "535,00")],
  filas=[
   ("Categoría", ["Cat 6 según TIA/EIA-568", "Cat 6; 250 MHz", "Cat 6"], "Gigabit con margen hasta 90 m de enlace"),
   ("Conductor", ["Cobre sólido de 24 AWG", "Cobre de 24 AWG", "No declarado"], "ET-03 exige cobre; el aluminio recubierto se calienta con PoE"),
   ("Chaqueta", ["LSZH", "LSZH-1", "LSZH"], "Baja emisión de humo en vías de evacuación"),
   ("Presentación", ["Caja de 305 m", "Caja de 305 m", "Rollo de 305 m"], "El metrado estima 244 m"),
   ("Cumplimiento de ET-03", ["C", "C", "P: conductor"], "Cobre sólido, Cat 6 y LSZH"),
   ("Resultado", ["\\textbf{Elegida}", "S/ 1 más", "Se aceptará si acredita cobre"], "Menor costo entre las documentadas"),
  ]),
 dict(clave="jack", titulo="jack keystone Cat 6, ET-03", cite="arteusred,arteusotros", opciones=[
   op("jack-newlink", "Newlink 3667706", None, AR+"newlink-3667706-keystone-jack-cat6-110-type-azul", P_AR, "13,00"),
   op("jack-nexxt", "Nexxt PCGKJC6TYRJSL", AI+"PCGKJC6TYRJSL-land.png?v=1790447570&width=500", AR+"nexxt-solutions-pcgkjc6tyrjsl-infra-promo-jack-cat-6-stp-keystone-tipo-110", P_AR, "19,00"),
   op("jack-linkbasik", "Linkbasik JKA09-UC6-WH", AI+"JKA09-UC6-WH_a0ea1e8f-2d19-4a71-8b7d-197da9f1510a.jpg?v=1790428184&width=500", AR+"linkbasik-jka09-uc6-wh-jack-rj-45-cat6-color-blanco", P_AR, "5,00")],
  filas=[
   ("Formato", ["Keystone tipo 110, UTP", "Keystone tipo 110, blindado STP", "Jack RJ45 UTP; formato keystone no declarado"], "Debe encajar en el patch panel modular y en el faceplate"),
   ("Categoría", ["Cat 6; la descripción indica 6A", "Cat 6", "Cat 6"], "Igual o superior al cable"),
   ("Conductor admitido", ["24 AWG; contactos con oro de 50 µm", "22 a 26 AWG", "No publicado"], "Compatibilidad con el cable de 24 AWG"),
   ("Cumplimiento de ET-03", ["C", "N: blindado para cable no apantallado", "P: formato"], "Keystone Cat 6 UTP"),
   ("Resultado", ["\\textbf{Elegida}, 16 unidades", "Requeriría cable apantallado", "Se aceptará si acredita keystone"], "Menor costo entre las documentadas"),
  ]),
 dict(clave="pp", titulo="patch panel, ET-03", cite="arteusred,arteusotros", opciones=[
   op("pp-pkj24", "Dixon PKJ24-C6-A/BK", AI+"PKJ24-C6-A-BK.jpg?v=1790475824&width=500", AR+"dixon-pkj24-c6-a-bk-patch-panel-cat-6-modular-24-puertos-vacio", P_AR, "63,00"),
   op("pp-ppkj24", "Dixon PPKJ24", AI+"PPKJ24.jpg?v=1790475774&width=500", AR+"dixon-ppkj24-patch-panel-24-puertos-cat-6-cat-6a-modular-vacio", P_AR, "84,00"),
   op("pp-nexxt", "Nexxt AW191NXT06", AI+"AW191NXT06-1_5dafd035-09c6-4df6-a415-a59d970329d1.jpg?v=1790446655&width=500", AR+"nexxt-solutions-aw191nxt06-patch-panel-rack-24p-1u-cat6-pre-config-tipo-110", P_AR, "169,00")],
  filas=[
   ("Puertos", ["24 vacíos, modulares", "24 vacíos, modulares", "24 cargados, tipo 110"], "Siete enlaces y crecimiento futuro"),
   ("Compatibilidad", ["Jacks Cat 5e, 6 y 6A", "Jacks Cat 6 y 6A", "Cat 6"], "Usa los jacks keystone del mismo enlace"),
   ("Construcción", ["Acero SPCC de 1,5 mm; 1 RU", "Acero SPCC de 1,5 mm; ventanas para etiquetas; 1 RU", "1 RU de 19 pulg."], "Montaje en el gabinete"),
   ("Cumplimiento de ET-03", ["C", "C", "C"], "Terminación en patch panel"),
   ("Resultado", ["\\textbf{Elegida}", "S/ 21 más", "S/ 106 más; jacks incluidos no necesarios"], "Menor costo entre las que cumplen"),
  ]),
 dict(clave="caja", titulo="caja adosable para faceplate, ET-03", cite="arteusred,arteusotros", opciones=[
   op("caja-satra", "Satra 0111048901", AI+"111048901.jpg?v=1790429066&width=500", AR+"satra-0111048901-caja-modular-pvc-adosable-2x4x1-89", P_AR, "7,00"),
   op("caja-dixon", "Dixon JE318/WH", AI+"JE318-WH_5823b47f-378d-413b-a35c-f7e0c56d67a1.jpg?v=1790476387&width=500", AR+"dixon-je318-wh", P_AR, "9,00"),
   op("caja-nexxt", "Nexxt AE180NXT03", AI+"descarga_34.png?v=1790447794&width=500", AR+"nexxt-solutions-ae180nxt03-caja-de-montaje-superficial-rj45", P_AR, "13,00")],
  filas=[
   ("Formato", ["Adosable 2 $\\times$ 4, PVC, 48 mm de fondo", "2 $\\times$ 4; 70 $\\times$ 114 $\\times$ 47 mm", "Caja superficial RJ45"], "Montaje del faceplate sin picar el muro"),
   ("Seguridad", ["UL94V-0, resistente al fuego; IP40", "No publicada", "No publicada"], "Comportamiento ante el fuego"),
   ("Compatibilidad", ["Faceplate 2 $\\times$ 4", "Placa simple o ejecutiva", "No publicada"], "Usa el faceplate de 1 puerto"),
   ("Cumplimiento de ET-03", ["C", "C", "P"], "Caja para faceplate en cada enlace"),
   ("Resultado", ["\\textbf{Elegida}, 7 unidades", "S/ 2 más", "Descripción vacía"], "Menor costo entre las que cumplen"),
  ]),
 dict(clave="pc", titulo="patch cord Cat 6, ET-03", cite="arteusred,arteusotros", opciones=[
   op("pc-legrand", "Legrand 051832, 1 m", AI+"051832_8571b03b-30ab-456d-95b0-3aab68a36c60.jpg?v=1790367451&width=500", AR+"legrand-051832-patch-cord-utp-cat6-lszh-1m-azul", P_AR, "19,00"),
   op("pc-satra", "Satra 0102030104, 1 m", AI+"cat6_1024x.jpg?v=1790375682", AR+"satra-0102030104-cable-patch-cord-utp-cat6-azul-1m", P_AR, "23,00"),
   op("pc-nexxt", "Nexxt AB361NXT24, 3 m", AI+"AB361NXT24-1.jpg?v=1790446541&width=500", AR+"nexxt-solutions-ab361nxt24-cable-de-red-patch-cord-cat6-u-utp-cm-3m-10ft-azul", P_AR, "13,00")],
  filas=[
   ("Longitud y uso", ["1 m; lado del gabinete", "1 m; lado del gabinete", "3 m; lado del terminal o cámara"], "Conexión entre jack y equipo"),
   ("Categoría", ["Cat 6 U/UTP; 24 AWG", "Cat 5e, 6 o 6A según TIA-568C.2; UL y ETL", "Cat 6 U/UTP; CM"], "Igual o superior al enlace"),
   ("Cumplimiento de ET-03", ["C", "C", "C"], "Patch cords Cat 6"),
   ("Resultado", ["\\textbf{Elegida}, 7 unidades", "S/ 4 más", "\\textbf{Elegida}, 7 unidades de 3 m"], "Menor costo por longitud requerida"),
  ]),
 dict(clave="can", titulo="canaleta, ET-03", cite="arteusred,arteusotros", opciones=[
   op("can-dexson", "Dexson DXN10051 20 $\\times$ 12", AI+"dexson-dxn10051-canaleta-blanca-20x12-con-adhesivo-arteus.jpg?v=1790318719&width=500", AR+"dexson-dxn10051-canaleta-blanca-20x12-con-adhesivo", P_AR, "13,00"),
   op("can-efapel40", "Efapel 10060 40 $\\times$ 16", AI+"efapel-10060-cbr-canaleta-40x16-de-2mts-cdivision-arteus-2_1024x.png?v=1790313925", AR+"efapel-10060-cbr-canaleta-40x16-de-2mts-c-division", P_AR, "5,00"),
   op("can-efapel60", "Efapel 10070 60 $\\times$ 16", AI+"efapel-10070-cbr-canaleta-60x16-de-2mts-con-division-arteus-2_1024x.png?v=1790314016", AR+"efapel-10070-cbr-canaleta-60x16-de-2mts-con-division", P_AR, "21,00")],
  filas=[
   ("Sección y longitud", ["20 $\\times$ 12 mm; 2,00 m", "40 $\\times$ 16 mm; 2,10 m", "60 $\\times$ 16 mm; 2,10 m"], "Un cable UTP por canaleta; 106 m de recorrido visible"),
   ("Fijación y protección", ["Adhesiva; PVC; 1 compartimento", "Con división según título; IP44 e IK07", "Con división; IP44 e IK07"], "Instalación sin daño a muros"),
   ("Tramos y costo para 106 m", ["53: S/ 689,00", "51: S/ 255,00", "51: S/ 1\\,071,00"], "Costo total del recorrido"),
   ("Stock", ["Disponible", "Contactar al vendedor", "Disponible"], "Disponibilidad verificable"),
   ("Cumplimiento de ET-03", ["C", "P: stock", "C"], "Canalización con tapa en zonas de tránsito"),
   ("Resultado", ["\\textbf{Elegida}", "Equivalente si confirma stock: S/ 434 menos", "S/ 382 más"], "Menor costo con stock verificable"),
  ]),
 dict(clave="gab", titulo="gabinete de pared, ET-03", cite="arteusred,arteusotros", opciones=[
   op("gab-zkteco", "ZKTECO ZK-R9U-5409A, 9 RU", AI+"gabinetezkteco_80eb8272-b3d2-4714-8d3d-a1583886e07d_1024x.jpg?v=1790339526", AR+"zkteco-zk-r9u-5409a-gabinete-de-pared-9ru-53x40x45cm", P_AR, "172,00"),
   op("gab-g6", "Estándar G6, 6 RU", AI+"GabinetedeParedESTANDAR_G6_-6RU_e2bad193-f580-4701-9daa-5c20e60797a9_1024x.png?v=1790415029", AR+"gabinete-de-pared-estandar-g6-30x60x51cm", P_AR, "225,00"),
   op("gab-finen", "FINEN W1-5406, 6 RU", AI+"W1-5406-2_1024x.jpg?v=1790427812", AR+"finen-w1-5406-gabinete-de-pared-6ru-368-x-540-x-400mm-c-puerta-de-vidrio", P_AR, "117,00")],
  filas=[
   ("Capacidad", ["9 RU de 19 pulg.", "6 RU", "6 RU"], "Switch, NVR, patch panel, organizador y regleta ocupan unos 5 RU"),
   ("Medidas", ["53 $\\times$ 40 $\\times$ 45 cm, ancho, fondo y alto", "30 $\\times$ 60 $\\times$ 51 cm, alto, ancho y fondo", "36,8 $\\times$ 54 $\\times$ 40 cm"], "Espacio en el cuarto técnico"),
   ("Construcción y accesorios", ["Acero; puerta de cristal templado; 1 bandeja", "No publicados", "Puerta de vidrio; se entrega desarmado"], "La bandeja evita una compra adicional"),
   ("Stock", ["Disponible", "Disponible", "Contactar al vendedor"], "Disponibilidad verificable"),
   ("Cumplimiento de ET-03", ["C", "C", "P: stock y accesorios"], "6 RU como mínimo, con puerta y llave"),
   ("Resultado", ["\\textbf{Elegida}", "S/ 53 más y sin bandeja", "Sin stock verificable"], "Menor costo con stock verificable"),
  ]),
 dict(clave="reg", titulo="regleta de gabinete, ET-03", cite="arteusred,arteusotros", opciones=[
   op("reg-pdu", "PDU de 8 tomas GEN-PDU8-10A", AI+"pdu2.jpg?v=1790333749&width=500", AR+"power-rack-8-tomas-planas-y-redonda", P_AR, "100,00"),
   op("reg-nexxt", "Nexxt NPD-21U8U15A", AI+"descarga_27.png?v=1790447281&width=500", AR+"nexxt-solutions-npd-21u8u15a-regleta-horizontal-8-tomacorrientes-15a-monofasica-16awg", P_AR, "117,00")],
  filas=[
   ("Tomas", ["8", "8"], "Switch, NVR, monitoreo y reserva"),
   ("Corriente", ["10 A según el código del modelo", "15 A; 16 AWG"], "La carga del gabinete es menor de 1 A"),
   ("Montaje", ["Rack de 19 pulg.", "Horizontal"], "Fijación dentro del gabinete"),
   ("Cumplimiento de ET-03", ["C", "C"], "Regleta en el gabinete"),
   ("Resultado", ["\\textbf{Elegida}", "S/ 17 más"], "Menor costo entre las que cumplen"),
  ]),
 dict(clave="toma", titulo="tomacorriente 2P+T, ET-03", cite="promelsa", opciones=[
   op("toma-bticino", "Bticino Schuko 2P+T 16 A P50 con placa", PI+"t/o/tomacorriente-schuko-2p-t-16a-p50-placa-blanco-1045958-01.jpg", PM+"tomacorriente-schuko-2p-t-16a-p50-placa-blanco-1045958.html", P_PM, "39,35"),
   op("toma-matix", "Bticino Matix Schuko 2 $\\times$ 16 A+T", PI+"1/0/1017375-01.jpg", PM+"1017375-tomacorriente-p-empotrar-schuko-2x16at-250v-2-modulos-marfil-matix.html", P_PM, "41,96"),
   op("toma-mosaic", "Legrand Mosaic Schuko 2 $\\times$ 16 A+T", PI+"1/0/1016576-01_1.jpg", PM+"1016576-tomacorriente-schuko-2x16at-c-tornillo-2-modulos-blanco-mosaic.html", P_PM, "48,11")],
  filas=[
   ("Tipo", ["Schuko 2P+T de 16 A con placa", "Schuko 2 $\\times$ 16 A+T, 250 V; 2 módulos", "Schuko 2 $\\times$ 16 A+T con tornillo; 2 módulos"], "Conexión con tierra para terminales y gabinete"),
   ("Presentación", ["Placa incluida", "Sistema modular; soporte y placa no indicados", "Sistema modular; soporte y placa no indicados"], "Piezas necesarias para instalar"),
   ("Color", ["Blanco", "Marfil", "Blanco"], "Acabado"),
   ("Cumplimiento de ET-03", ["C", "C", "C"], "2P+T de 16 A y 250 V"),
   ("Resultado", ["\\textbf{Elegida}, 4 unidades", "S/ 2,61 más sin placa", "S/ 8,76 más sin placa"], "Menor costo entre las que cumplen"),
  ]),
 dict(clave="cab", titulo="conductor AC libre de halógenos, ET-09", cite="promelsa", opciones=[
   op("cab-miguelez", "Miguelez H07Z1-K 2,5 mm²", PI+"1/0/1004151-02.jpg", PM+"1004151-cable-h07z1-k-2-5mm2-450-750v-libre-de-halogeno-negro-clase-5-x-rollo.html", P_PM, "213,58"),
   op("cab-indeco", "Indeco NH-90 2,5 mm²", PI+"c/a/cable-nh-90-2-5mm2-450-750v-libre-de-hal-geno-negro-clase-2-x-rollo-practicable-1042538-01.jpg", PM+"cable-nh-90-2-5mm2-450-750v-libre-de-halogeno-negro-clase-2-x-rollo-practicable-1042538.html", P_PM, "240,72")],
  filas=[
   ("Tipo", ["H07Z1-K libre de halógenos", "NH-90 libre de halógenos"], "Menor humo y gases en caso de incendio"),
   ("Tensión y conductor", ["450/750 V; clase 5 flexible", "450/750 V; clase 2"], "Circuitos derivados de 220 V"),
   ("Presentación", ["Rollo; longitud por confirmar", "Rollo; longitud por confirmar"], "Se presupuestan tres rollos para unos 240 m"),
   ("Cumplimiento de ET-09", ["C", "C"], "LSZH de 2,5 mm²; caída de 0,78\\% en 45 m"),
   ("Resultado", ["\\textbf{Elegida}, 3 rollos", "S/ 27,14 más por rollo"], "Menor costo entre las que cumplen"),
  ]),
]

UNICAS = [
 dict(clave="u1", titulo="subsistema FV, batería y medición", cite="autosolarfv,autosolarmed,autosolarac", items=[
   dict(id="u-cablesolar", nombre="Cable solar H1Z2Z2-K de 6 mm², rollo de 15 m", img=CA+"5204032/rollo-cable-solar-unipolar-6mm2-h1z2z2-k-15kv-15m-rojo-687eabd165d08-thumb.jpg", pagina=AS+"cable-unipolar/rollo-cable-solar-unipolar-6mm2-h1z2z2-k-15kv-15m-rojo", proveedor=P_AS, uso="Cadena FV hasta el inversor; 30 m por polaridad", carac="1,5 kV; cobre estañado; aislamiento XLPO libre de halógenos", cant="4", precio="101,42", parcial="405,68"),
   dict(id="u-cablebat", nombre="Cable para baterías de 35 mm²", img=CA+"5504036/cable-para-baterias-interconexion-en-serie-35mm2-thumb.jpg", pagina=AS+"cables-de-baterias/cable-para-baterias-interconexion-en-serie-35mm2", proveedor=P_AS, uso="Batería al inversor; caída de 0,39\\%", carac="35 mm²; longitud no indicada", cant="2", precio="27,23", parcial="54,46"),
   dict(id="u-anl", nombre="Fusible ANL de 150 A", img=CA+"5504203/fusible-anl-150a-698a04b8dbdf5-thumb.jpg", pagina=AS+"fusibles/fusible-anl-150a", proveedor=P_AS, uso="Protección del cable de batería", carac="Tipo ANL; 150 A; alta capacidad de ruptura", cant="1", precio="39,39", parcial="39,39"),
   dict(id="u-sdm230", nombre="Vatímetro SDM230 Modbus monofásico", img=CA+"3206050/vatimetro-sdm230-modbus-pro-monofasico-tensite-thumb.jpg", pagina=AS+"accesorios-de-inversores/vatimetro-sdm230-modbus-pro-monofasico-tensite", proveedor=P_AS, uso="Exportación cero y medición de red, ET-10", carac="Monofásico; Modbus; compatible con inversores Tensite", cant="1", precio="502,41", parcial="502,41"),
   dict(id="u-barra", nombre="Barra de cobre de 5/8 pulg. $\\times$ 2,4 m", img=CA+"5509040/barra-de-cobre-58-x-240m-cpunta-6909207fa33d0-thumb.jpg", pagina=AS+"materiales-para-pozo-a-tierra/barra-de-cobre-58-x-24m-con-punta", proveedor=P_AS, uso="Electrodo del pozo a tierra", carac="Cobre puro; 2,40 m; con punta", cant="1", precio="298,17", parcial="298,17"),
  ]),
 dict(clave="u2", titulo="tablero, puesta a tierra e instalación", cite="autosolarac,promelsa,arteusred", items=[
   dict(id="u-tm16", nombre="Termomagnético 2P de 16 A, 6 kA", img=CA+"7102070/termomagnetico-nxb-63-2p-16a-6ka-monofasico-chint-thumb.jpg", pagina=AS+"termomagneticos-monofasicos/termomagnetico-nxb-63-2p-16a-6ka-monofasico-chint", proveedor=P_AS, uso="Circuitos de terminales y de red", carac="230/400 V; poder de corte de 6 kA", cant="2", precio="40,46", parcial="80,92"),
   dict(id="u-tm32", nombre="Termomagnético 2P de 32 A, 6 kA", img=CA+"7102071/termomagnetico-2p-32a-6ka-monofasico-chint-thumb.jpg", pagina=AS+"termomagneticos/termomagnetico-2p-32a-6ka-monofasico-chint", proveedor=P_AS, uso="Entrada de red y salida de respaldo", carac="230/400 V; 6 kA; Ui 500 V", cant="2", precio="53,52", parcial="107,04"),
   dict(id="u-spdac", nombre="Protector de sobretensiones AC 2P 275 V", img=CA+"7102517/proteccion-sobretensiones-2p-275v-40ka-chint-thumb.jpg", pagina=AS+"protector-de-sobretensiones/proteccion-sobretensiones-2p-275v-40ka-chint", proveedor=P_AS, uso="Tablero crítico", carac="Uc 275 V; 40 kA; Up 1,5 kV; tipo II", cant="1", precio="155,94", parcial="155,94"),
   dict(id="u-cemento", nombre="Cemento conductivo, bolsa de 25 kg", img=CA+"3201080/cemento-conductivo-para-pozo-a-tierra-25kg-thor-cem-690df404b6e66-thumb.jpg", pagina=AS+"materiales-para-pozo-a-tierra/cemento-conductivo-para-pozo-a-tierra-25kg-thor-cem", proveedor=P_AS, uso="Relleno del pozo a tierra", carac="Menos de 5 $\\Omega$·m; IEC 62561-7", cant="2", precio="170,91", parcial="341,82"),
   dict(id="u-tubo", nombre="Tubo PVC SAP de 3/4 pulg. $\\times$ 3 m", img=PI+"1/0/1026759-01_1.jpg", pagina=PM+"1026759-tubo-pvc-sap-3-4-x-3mts.html", proveedor=P_PM, uso="Tramos verticales y protegidos de conductores", carac="PVC SAP; 3/4 pulg.; 3 m", cant="15", precio="11,17", parcial="167,55"),
  ]),
 dict(clave="u3", titulo="red local", cite="arteusred", items=[
   dict(id="u-faceplate", nombre="Faceplate Dixon JE3001WH de 1 puerto", img=AI+"JE3001WH.jpg?v=1790475842&width=500", pagina=AR+"dixon-je3001wh-faceplate-placa-frontal-simple-1-puerto-blanco", proveedor=P_AR, uso="Salida de cada enlace en terminal y cámara", carac="Compatible con keystone; 70 $\\times$ 114 mm", cant="7", precio="3,00", parcial="21,00"),
   dict(id="u-organizador", nombre="Organizador horizontal GLC de 1 RU", img=None, pagina=AR+"glc-tec-glc-orgab-001-organizador-horizontal-de-cable-de-1ru-19-metal", proveedor=P_AR, uso="Orden de patch cords en el gabinete", carac="Metal; 19 pulg.; 1 RU", cant="1", precio="17,00", parcial="17,00"),
   dict(id="u-conector", nombre="Conector de bronce de 5/8 pulg.", img=None, pagina=AS+"materiales-para-pozo-a-tierra/conector-de-bronce-58-para-pozo-a-tierra", proveedor=P_AS, uso="Unión del conductor con la barra del pozo", carac="Bronce; para barra de 5/8 pulg.", cant="2", precio="6,35", parcial="12,70"),
  ]),
]
