"""Modelo de costos INFORMA UNSAAC con partidas desglosadas (30/10/2026)."""
import json, math, sys
from decimal import Decimal as D, ROUND_HALF_UP

def r2(x): return D(x).quantize(D("0.01"), rounding=ROUND_HALF_UP)
def fmt(x, dec=2):
    s = f"{D(x):,.{dec}f}"
    ent, _, fr = s.partition(".")
    ent = ent.replace(",", "\\,")
    return ent + ("," + fr if dec else "")

# (código, descripción, cantidad, unitario, grupo, fv)
pub = [
 ("T1","Tótem interactivo de 55 pulgadas, ET-01",3,"9499.99","term",False),
 ("E1","Módulo FV de 615 Wp, ET-06",6,"405.35","ener",True),
 ("E2","Inversor híbrido de 4 kW, ET-05",1,"6537.03","ener",False),
 ("E3","Batería LFP de 48 V y 4,8 kWh, ET-07",1,"4178.47","ener",False),
 ("E4","Medidor bidireccional Modbus, ET-10",1,"502.41","ener",True),
 ("E5","Módulo de monitoreo del inversor, ET-10",1,"147.84","ener",False),
 ("E6","Estructura inclinada para 3 módulos, ET-08",2,"459.61","ener",True),
 ("E7","Cable solar 6 mm², rollo de 15 m",4,"101.42","ener",True),
 ("E8","Conector MC4 macho-hembra",4,"10.70","ener",True),
 ("E9","Interruptor DC 25 A 1 500 V",1,"94.21","ener",True),
 ("E10","Protector de sobretensiones DC 600 V",1,"173.07","ener",True),
 ("E11","Cable de batería 35 mm²",2,"27.23","ener",False),
 ("E12","Fusible ANL 150 A",1,"39.39","ener",False),
 ("E13","Termomagnético 2P 32 A",2,"53.52","ener",False),
 ("E14","Termomagnético 2P 16 A",2,"40.46","ener",False),
 ("E15","Diferencial 2P 25 A 30 mA tipo A",2,"179.27","ener",False),
 ("E16","Protector de sobretensiones AC 275 V",1,"155.94","ener",False),
 ("E17","Tablero adosable de 18 polos",1,"104.89","ener",False),
 ("E18","Barra de cobre 5/8 pulg. × 2,4 m",1,"298.17","ener",False),
 ("E19","Conector de bronce 5/8 pulg.",2,"6.35","ener",False),
 ("E20","Cemento conductivo, bolsa de 25 kg",2,"170.91","ener",False),
 ("E21","Cable libre de halógenos H07Z1-K de 2,5 mm², rollo",3,"213.58","ener",False),
 ("E22","Tubo PVC SAP de 3/4 pulg. × 3 m",15,"11.17","ener",False),
 ("E23","Tomacorriente 2P+T de 16 A con placa",4,"39.35","ener",False),
 ("R1","Cable Cat 6 de cobre LSZH, caja de 305 m, ET-03",1,"666.00","red",False),
 ("R2","Jack keystone Cat 6",16,"13.00","red",False),
 ("R3","Patch panel modular de 24 puertos",1,"63.00","red",False),
 ("R4","Faceplate de 1 puerto",7,"3.00","red",False),
 ("R5","Caja adosable 2 × 4",7,"7.00","red",False),
 ("R6","Patch cord Cat 6 de 1 m",7,"19.00","red",False),
 ("R7","Patch cord Cat 6 de 3 m",7,"13.00","red",False),
 ("R8","Canaleta 20 × 12 mm adhesiva de 2 m",53,"13.00","red",False),
 ("R9","Gabinete de pared de 9 RU con bandeja",1,"172.00","red",False),
 ("R11","Organizador horizontal de 1 RU",1,"17.00","red",False),
 ("R12","Regleta de 8 tomas para gabinete",1,"100.00","red",False),
 ("R13","Switch Gigabit administrable de 8 puertos, ET-03",1,"517.00","red",False),
 ("R14","Grabador NVR de 4 canales PoE, ET-04",1,"292.00","red",False),
 ("R15","Disco de videovigilancia de 2 TB, ET-04",1,"699.00","red",False),
 ("R16","Cámara IP de 4 MP, ET-04",3,"219.00","red",False),
]
prov = [  # estimaciones propias
 ("P2","Reserva de licencia de sistema","3 × 350 si se requiere adecuación","1050.00",False),
 ("P3","Logística de terminales","3 × 400","1200.00",False),
 ("P4","Flete de equipos de energía y red a Cusco","1 envío consolidado","300.00",False),
 ("P5","Anclajes y fijación de la estructura FV","Pernos, tacos y sellos por metrado","300.00",True),
 ("P6","Soporte y señalización del banco","1 conjunto","250.00",False),
 ("P7","Portafusible ANL y terminales de batería","1 conjunto","80.00",False),
 ("P8","Materiales AC menores por metrado","10 m de 6 mm², 15 m de conductor de protección de 10 mm², cajas, curvas, uniones y rotulación","250.00",False),
 ("P9","Señalética de videovigilancia","3 × 15","45.00",False),
]
hp = [  # (concepto, HP, tarifa, HP FV)
 ("Ingeniería y levantamiento",40,80,16),
 ("Instalación eléctrica, FV, red y videovigilancia",96,65,28),
 ("Configuración y adaptación del CMS",100,60,0),
 ("Interfaz y contenido inicial",60,50,0),
 ("Pruebas y puesta en servicio",48,60,8),
 ("Documentación y formación",24,50,4),
 ("Coordinación y control",40,70,8),
]
res_trib = r2(D("0.18")*3*D("9499.99")) + r2(D("0.18")*(3*D("213.58")+15*D("11.17")+4*D("39.35")))
tot = lambda items: sum((r2(D(i[3])*i[2]) for i in items), D(0))
pub_par = {i[0]: r2(D(i[3])*i[2]) for i in pub}
g = {k: sum(v for c,v in pub_par.items() if [i for i in pub if i[0]==c][0][4]==k) for k in ("term","ener","red")}
publicado = sum(pub_par.values())
provis = sum(D(p[3]) for p in prov)
serv = sum(D(h[1]*h[2]) for h in hp)
HP = sum(h[1] for h in hp)
baseA2 = publicado + res_trib + provis + serv
contA2 = r2(baseA2*D("0.10")); invA2 = baseA2 + contA2
inc_items = [(i[1], pub_par[i[0]]) for i in pub if i[5]] + [(p[1], D(p[3])) for p in prov if p[4]] \
          + [(f"{h[0]}: {h[3]} HP × {h[2]}", D(h[3]*h[2])) for h in hp if h[3]]
inc = sum(v for _,v in inc_items); inc_c = r2(inc*D("1.10"))
baseA1 = baseA2 - inc; invA1 = r2(baseA1*D("1.10"))
assert invA2 - invA1 == inc_c or abs(invA2-invA1-inc_c) <= D("0.01"), (invA2-invA1, inc_c)
baseA0 = D(8360); invA0 = r2(baseA0*D("1.10"))
E = D(3)*D("0.200")*12*200 + (D("0.040")+D("0.015"))*24*365
tar = D("0.80")
enA1 = r2(E*tar); enA2 = r2(E*tar*D("0.40")); ahorro = r2(E*tar*D("0.60"))
opex0 = {"A0": D(4560), "A1": D(6500), "A2": D(6700)}
op = {"A0": opex0["A0"], "A1": opex0["A1"]+enA1, "A2": opex0["A2"]+enA2}
rep = r2(D("4178.47") + 800)
inv = {"A0": invA0, "A1": invA1, "A2": invA2}
repo = {"A0": D(0), "A1": rep, "A2": rep}
tco = {k: inv[k] + 5*op[k] + repo[k] for k in inv}
fa = sum(D(1)/D("1.08")**k for k in range(1,6)); f5 = D(1)/D("1.08")**5
vac_op = {k: r2(op[k]*fa) for k in op}; vac_rep = {k: r2(repo[k]*f5) for k in op}
vac = {k: inv[k] + vac_op[k] + vac_rep[k] for k in op}
ice = {k: r2(vac[k]/850) for k in vac}
ice_r = {k: (r2(vac[k]/870), r2(vac[k]/830)) for k in vac}
ice_y = {k: r2(vac[k]/850/5) for k in vac}
d10 = vac["A1"]-vac["A0"]; d21 = vac["A2"]-vac["A1"]
neto = ahorro - 200
estim = provis + serv  # estimaciones propias sujetas a sensibilidad
out = {
 "pub_par": {k: str(v) for k,v in pub_par.items()}, "grupos": {k: str(v) for k,v in g.items()},
 "publicado": str(publicado), "res_trib": str(res_trib), "provis": str(provis), "serv": str(serv), "HP": HP,
 "baseA2": str(baseA2), "contA2": str(contA2), "invA2": str(invA2),
 "inc": str(inc), "inc_c": str(inc_c), "inc_items": [(a, str(b)) for a,b in inc_items],
 "baseA1": str(baseA1), "invA1": str(invA1), "invA0": str(invA0),
 "E": str(E), "enA1": str(enA1), "enA2": str(enA2), "ahorro": str(ahorro), "neto": str(neto),
 "op": {k: str(v) for k,v in op.items()}, "rep": str(rep),
 "tco": {k: str(v) for k,v in tco.items()}, "tco_A2_A1": str(tco["A2"]-tco["A1"]),
 "vac_op": {k: str(v) for k,v in vac_op.items()}, "vac_rep": {k: str(v) for k,v in vac_rep.items()},
 "vac": {k: str(v) for k,v in vac.items()}, "vac_A2_A1": str(d21), "vac_A1_A0": str(d10),
 "ice": {k: str(v) for k,v in ice.items()}, "ice_r": {k: [str(a), str(b)] for k,(a,b) in ice_r.items()},
 "ice_y": {k: str(v) for k,v in ice_y.items()},
 "ice_d10": [str(r2(d10/850)), str(r2(d10/870)), str(r2(d10/830)), str(r2(d10/850/5))],
 "ice_d21": [str(r2(d21/850)), str(r2(d21/870)), str(r2(d21/830)), str(r2(d21/850/5))],
 "sens20": [str(r2(estim*D("0.2"))), str(r2(estim*D("0.2")*D("1.1")))], "estim": str(estim),
 "cob": [str(r2(E*tar*D("0.3"))), str(r2(E*tar*D("0.8")))], "tarifa": [str(r2(E*D("0.6")*D("0.6"))), str(r2(E*D("1.0")*D("0.6")))],
 "fa": str(fa.quantize(D("0.0001"))), "f5": str(f5.quantize(D("0.0001"))),
}
json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for k in ("publicado","res_trib","provis","serv","HP","baseA2","contA2","invA2","inc","inc_c","baseA1","invA1","invA0","rep"):
    print(k, out[k])
print("grupos", out["grupos"]); print("op", out["op"]); print("tco", out["tco"], "dif", out["tco_A2_A1"])
print("vac", out["vac"], "A2-A1", out["vac_A2_A1"], "A1-A0", out["vac_A1_A0"])
print("ice", out["ice"], out["ice_r"], out["ice_y"], out["ice_d10"], out["ice_d21"])
print("sens", out["sens20"], "estim", out["estim"], "neto", out["neto"])
