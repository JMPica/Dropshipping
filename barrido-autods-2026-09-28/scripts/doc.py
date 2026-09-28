import json,csv,collections,html
S='/tmp/claude-0/-home-user-Dropshipping/edd3f668-73f0-5b21-9c24-f699ed49a66a/scratchpad'
rows=json.load(open(S+'/s3.json'))
rows.sort(key=lambda x:-x['score'])
top=rows[:50]
e=lambda v:(f"{v:,.2f}".replace(',','X').replace('.',',').replace('X','.'))
def ped(x):
    s=f"{x['orders']:,}".replace(',','.')+" ped."
    if x['fb']: s+=" · anuncios FB"
    return s
H=[]
a=H.append
a('<html><head><meta charset="utf-8"></head><body>')
a('<h1>Lume — resultado barrido AutoDS (28 sept 2026)</h1>')
a('<p><i>Encargo: «Lume — brief del barrido AutoDS (28 sept 2026)». Datos leídos el 28/09/2026 de AutoDS (API) y CJ Dropshipping (API). Base, no asesoría legal ni fiscal.</i></p>')
a('<h2>1. Resumen</h2><ul>')
a('<li><b>Recogida:</b> 1.770 candidatos únicos (1.420 «ganadores» de AutoDS con pedidos/engagement + 350 de búsqueda por categorías) y 80 «similares» revisados.</li>')
a('<li><b>Filtro duro:</b> fuera 1.162 (electrónica/batería 466, piel/cosmética 200, salud/alegaciones 184, juguete infantil 144, supermercado 86, frágil 47, marca 21, tabaco/armas 14). Quedan 608; 367 ganadores con par puesto ≤ 21 € revisados uno a uno; 65 puntuados a fondo; 20 contrastados en CJ.</li>')
a('<li><b>Resultado clave:</b> con precios creíbles, IVA descontado y envío real a España en ≤ 10 días, <b>ningún producto cumple MC ≥ 35 €</b> por pedido. Los mejores quedan en unos 13-24 € por pedido según el envío.</li>')
a('<li><b>Por qué:</b> el envío con seguimiento de China a España en ≤ 10 días cuesta ~8,5 € por paquete de 200 g e incluye un arancel fijo de ~3 € por paquete (la tarifa de CJ lo desglosa y DHL lo indica: «€3 customs duty per parcel»). AutoDS mostraba 1,99 $ porque tu cuenta calcula para <b>EE. UU.</b>, no para España.</li>')
a('<li><b>Nicho recomendado (con reservas):</b> «Regalos» para la campaña de Navidad: collar de proyección «te quiero», rosa 24K sin luz y babero de afeitado. Es el único nicho con productos que cumplen PVP ≥ 3× coste puesto y el que mejor margen deja (17,6 €/pedido de media con envío CJ, frente a 9,7 € de «Arreglos»). <b>Tampoco llega a MC ≥ 35 €</b>; ver §4 y la decisión en §5.</li></ul>')
a('<h2>2. Avisos urgentes (no esperan)</h2><ul>')
a('<li><b>La prueba de AutoDS termina el 1 oct 2026 a las 21:34</b> (API: trial_expire_date y next_subscription_payment = 2026-10-01), no el 12 oct. Después: 34,90 €/mes. Decisión antes del 30 sept.</li>')
a('<li><b>Región de AutoDS = EE. UU. (USD).</b> Todos los plazos y costes de envío de AutoDS son a EE. UU. Cambiarla a España (ajustes de AutoDS, 1 minuto) permite leer el envío real de AliExpress a España, que puede ser más barato que CJ.</li>')
a('<li><b>Tienda conectada en AutoDS:</b> «wsyxgf w3» (wsyxgf-w3.myshopify.com, EUR, creada el 28/09 21:50). Comprueba que es lume-es y no una segunda tienda de pago.</li>')
a('<li>Créditos AutoDS disponibles: 400 de búsqueda de productos, 30 de reescritura IA, 5 de pedido automático. No he gastado ninguno ni he subido nada a la tienda.</li></ul>')
a('<h2>3. Método y supuestos</h2><ul>')
a('<li>Llamadas iniciales: get_playbook (product_import), get_user_subscription, list_stores_api. Skill cargada: dropshipping-copiloto (no hay skills de cumplimiento ni marketing disponibles).</li>')
a('<li>MC = PVP/1,21 − coste − envío − (2,1 % PVP + 0,30 €) − 9 % PVP. Tipo de cambio 1 $ = 0,90 €. PVP ≥ 3× (coste + envío) y MC ≥ 35 € con la oferta tipo.</li>')
a('<li><b>Envío verificado (CJ, CN→ES):</b> CJPacket Fast Ordinary 4-9 días: 9,48 $ (200 g) y 13,15 $ (500 g), arancel incluido → modelo 7,03 $ + 0,0122 $/g por paquete. La vía barata (CJPacket Ordinary I, 5,93 $ a 200 g) tarda 8-18 días y no cumple el máximo de 10. Lo voluminoso se dispara: la escalera para mascotas cuesta 86,76 $ (peso volumétrico 6,5 kg).</li>')
a('<li><b>Escenario AliExpress (sin verificar):</b> ~1,5 € de envío + 3 € de arancel por paquete. Solo sirve para ver el techo; hay que confirmarlo con la región de AutoDS en España.</li>')
a('<li>PVP propuesto = valor percibido creíble en España, contrastado con los precios de la competencia que da AutoDS. Oferta elegida entre 1+1, 2.ª unidad al 50 % y 3x2 (3x2 solo si tiene sentido comprar varias). En el caso de Adrián el 41 % eligió pack; el resto compra 1 unidad.</li>')
a('<li>Nota 0-100 con los pesos del brief. Margen (25) calculado con el envío CJ; problema/WOW (20), creativo POV solo manos (15), saturación en España (10) y tamaño/devoluciones (10) puntuados a mano; validación (20) = pedidos (log) + engagement + anuncios de Facebook.</li></ul>')
# Recomendación
fin={x['id']:x for x in rows}
col=fin['65b57921920030bc8881c4a0']; ros=fin['658e6770060eddd0fde72d06']; bab=fin['6913145d00221a0001d3b968']
tel=fin['667be8cc8c04ac166bff0387']; bar=fin['67523ce8dbf199e45c8ce5b2']; par=fin['69cec2b389e77f0001986370']
a('<h2>4. Recomendación: nicho «Regalos» (campaña de Navidad)</h2>')
a('<p><b>Por qué este nicho y no otro:</b> el margen es el requisito que manda y aquí es donde está. Collar y rosa son los <b>únicos</b> productos del barrido que cumplen PVP ≥ 3× coste puesto con el envío real. Media del trío: 17,6 €/pedido con envío CJ y 21,6 € en el escenario AliExpress. El nicho alternativo, «Arreglos: casa y ropa», tiene más candidatos (16 de 50) y mejor nota media, pero su trío (telar, barrera, parche) deja solo 9,7 € y 17,2 €. Además, la ventana es ahora: octubre-diciembre (Navidad y Reyes), y luego San Valentín y el Día de la Madre. El formato POV solo manos (abrir la caja, mirar dentro del colgante) es el natural del regalo, y el riesgo legal y de Meta es bajo.</p>')
a('<p><b>En contra, sin maquillar:</b> no resuelve un «problema» (el problema es «qué le regalo»), hay saturación media (la rosa 24K la importan 228 tiendas en AutoDS y el collar 50), los CPM de Meta suben en Black Friday y Navidad, y sigue sin llegar a MC 35 €.</p>')
a('<table border="1" cellpadding="4" style="border-collapse:collapse"><tr><th>Producto</th><th>Coste</th><th>Envío ES ≤ 10 d</th><th>PVP</th><th>Competencia</th><th>×PVP/puesto</th><th>MC 1 ud. (CJ / Ali)</th><th>MC con oferta (CJ / Ali)</th><th>Validación</th><th>Nota</th></tr>')
for x,comp,var,val in [(col,'25-37 $','2,20 $ (REACH declarado)','3.000 ped. · 4,6★ (841)'),(ros,'21-41 $','1,83-2,60 $ (sin LED)','454 ped. · 4,5★ (232) · anuncio FB'),(bab,'—','2,34 $','10.000 ped.')]:
    a(f"<tr><td>{html.escape(x['es'])}</td><td>{var}</td><td>{e(x['ship1'])} €</td><td>{e(x['PV'])} €</td><td>{comp}</td><td>{e(x['mult'])}</td><td>{e(x['MC1'])} / {e(x['MC1B'])} €</td><td>{e(x['MCo'])} / {e(x['MCoB'])} € ({x['offer']}, {e(x['AOV'])} €)</td><td>{val}</td><td>{e(x['score'])}</td></tr>")
a('</table>')
a('<p><b>Lente Hormozi (oferta):</b> subir el valor en vez de bajar el precio. «Regalo listo para entregar» (caja y tarjeta incluidas), devolución hasta el 15 de enero para que el regalo se pueda cambiar después de Reyes (idea del vídeo 3 de Adrián) y 2.ª unidad al 50 % con el ángulo «una para ella y otra para tu madre». Es la oferta que más sube el ticket sin otro paquete: el mismo envío y el mismo arancel se reparten entre dos unidades.</p>')
a('<p><b>Lente Sutherland (percepción):</b> quien regala no compra el objeto, compra la reacción. El gancho es «su cara al mirar dentro del colgante», no el metal. Hay que darle nombre propio al producto (p. ej., «Colgante Cien Idiomas»), cuidar la caja porque es lo primero que se ve y anclar contra un ramo de flores («40 € que duran una semana; esta rosa no se marchita»). Es un ancla legal; nada de precios tachados inventados ni «últimas unidades».</p>')
a('<p><b>Riesgos legales y de Meta:</b> collar: bisutería con níquel/plomo bajo REACH, así que hay que pedir o conservar la declaración (la ficha de AliExpress la indica). Rosa: comprar la variante sin luz (sin pila, fuera del RAEE) y venderla sin la marca del proveedor «YO CHO». Babero: sin alegaciones. Meta: sin problema; en el copy nada de «49 % OFF» ni «edición limitada» (sí lo hacen los competidores).</p>')
a('<p><b>Alternativa (si prefieres nota a margen):</b> «Arreglos: casa y ropa» con telar de zurcir, barrera de agua para ducha y parche de polipiel. Tiene la nota media más alta entre los nichos con varios productos y cero riesgo legal, pero MC de 17,3 / 6,5 / 5,3 € con envío CJ. Solo el telar es defendible.</p>')
a('<h2>5. La decisión que necesito de ti</h2>')
a('<p>Con los datos, el listón MC ≥ 35 € y este catálogo no casan en ninguno de los dos escenarios de envío. Con un MC de 13-24 € por pedido, el CPA máximo sostenible es de 13-24 €; el caso de Adrián tuvo un CPA de 24,36 €, así que el test apenas tendría colchón o perdería dinero.</p><ol>')
a('<li><b>Mi recomendación: antes de gastar un euro en anuncios, cambia la región de AutoDS a España (1 minuto) y releo el envío real de AliExpress de collar, rosa y babero.</b> Si sale ≤ 2 € + arancel y ≤ 10 días, el trío queda en 17-24 €/pedido con la 2.ª unidad al 50 %; solo entonces tendría sentido un test pequeño con regla de corte dura (matar si el CPA supera el MC tras ~100 clics o tras gastar 15-20 €).</li>')
a('<li>Si el envío real no mejora: no testear y cancelar AutoDS antes del 1 oct (solo habrás gastado 0,99 €).</li>')
a('<li>Alternativa estructural (otra sesión): productos de ticket alto y ligeros, o stock en almacenes UE (sin arancel de 3 €, 2-5 días).</li></ol>')
# Tabla top 50
a('<h2>6. Top 50 (ordenado por nota)</h2>')
a('<p>Plazo: 4-9 días (CJPacket Fast Ordinary) para todos los que tienen envío CJ. «MC CJ» = envío verificado; «MC Ali» = escenario optimista sin verificar. Coste = variante mínima de AutoDS salvo en los verificados.</p>')
a('<table border="1" cellpadding="3" style="border-collapse:collapse;font-size:9pt"><tr><th>#</th><th>Producto</th><th>Nicho</th><th>Nota</th><th>Coste €</th><th>Envío ES €</th><th>PVP €</th><th>Oferta (escenario Ali)</th><th>MC oferta CJ €</th><th>MC oferta Ali €</th><th>×PVP/puesto</th><th>Validación</th><th>Riesgo legal / Meta</th><th>Gancho</th></tr>')
for k,x in enumerate(top,1):
    a(f"<tr><td>{k}</td><td>{html.escape(x['es'])}</td><td>{html.escape(x['nicho'])}</td><td>{e(x['score'])}</td><td>{e(x['c']*0.9)}</td><td>{e(x['ship1'])}</td><td>{e(x['PV'])}</td><td>{x['offerB']} ({e(x['AOVB'])})</td><td>{e(x['MCo'])}</td><td>{e(x['MCoB'])}</td><td>{e(x['mult'])}</td><td>{ped(x)}</td><td>{html.escape(x['riesgo'])}</td><td>{html.escape(x['gancho'])}</td></tr>")
a('</table>')
# Nichos
g=collections.defaultdict(list)
for x in top:
    n='Mascotas' if x['nicho'].startswith('Mascotas') else ('Arreglos: casa y ropa' if x['nicho'] in ('Arreglos del hogar','Costura y arreglos de ropa') else x['nicho'])
    g[n].append(x)
a('<h2>7. Agrupación por nicho (top 50)</h2><table border="1" cellpadding="4" style="border-collapse:collapse"><tr><th>Nicho</th><th>Nº en top 50</th><th>Nota media</th><th>Mejor MC oferta CJ €</th><th>Mejor MC oferta Ali €</th><th>Productos</th></tr>')
for n,v in sorted(g.items(),key=lambda kv:(-len(kv[1]),-sum(x['score'] for x in kv[1])/len(kv[1]))):
    a(f"<tr><td>{n}</td><td>{len(v)}</td><td>{e(sum(x['score'] for x in v)/len(v))}</td><td>{e(max(x['MCo'] for x in v))}</td><td>{e(max(x['MCoB'] for x in v))}</td><td>{html.escape(', '.join(x['es'] for x in v))}</td></tr>")
a('</table>')
# CJ
a('<h2>8. Contraste en CJ (20 mejores)</h2><table border="1" cellpadding="3" style="border-collapse:collapse;font-size:9pt"><tr><th>Producto</th><th>En CJ</th><th>Precio CJ $</th><th>Peso</th><th>Nota</th></tr>')
for r in csv.DictReader(open(S+'/cj.tsv'),delimiter='|'):
    a(f"<tr><td>{html.escape(r['producto'])}</td><td>{html.escape(r['cj_nombre'])}</td><td>{r['cj_precio_usd']}</td><td>{r['peso_g']}</td><td>{html.escape(r['nota'])}</td></tr>")
a('</table><p>Solo 9 de 20 están en CJ; el resto solo se puede servir desde AliExpress vía AutoDS. Donde existen, CJ es más caro salvo la funda antihielo (0,57-1,19 $) y el saco para gato (3,25-4,20 $).</p>')
a('<h2>9. Límites de este barrido</h2><ul><li>AutoDS no da pedidos ni engagement en la búsqueda por categorías (solo en «ganadores»), y «similares» devolvió sobre todo marcas de Amazon EE. UU.: no aportó candidatos.</li><li>Pesos estimados salvo la escalera; los datos de envío de AliExpress a España no están verificados (región EE. UU.).</li><li>La puntuación cualitativa (problema, creativo, saturación, tamaño) es criterio mío: revisable.</li></ul>')
a('</body></html>')
open(S+'/informe.html','w').write(''.join(H))
print(len(''.join(H)))
