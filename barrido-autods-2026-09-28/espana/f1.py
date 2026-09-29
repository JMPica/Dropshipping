import json,re
S='/tmp/claude-0/-home-user-Dropshipping/edd3f668-73f0-5b21-9c24-f699ed49a66a/scratchpad'
H=[('piel/cosmética',r'crema|s[eé]rum|loci[oó]n|mascarilla|maquillaje|labial|pintalabios|esmalte|u[ñn]as|tatuaje|perfume|fragancia|aceite esencial|champ[uú]|acondicionador|jab[oó]n|dent[ií]frico|blanquea|pesta[ñn]a|ceja|pegamento|rimel|r[ií]mel|delineador|piel|facial|\bcara\b|colorete|base de maquillaje|protector solar|desodorante|tinte|exfolia|cera|b[aá]lsamo|acn[eé]|arruga|anti ?edad|col[aá]geno|depila|epila|u[nñ]a postiza|slime|cosm[eé]tic'),
 ('salud/sanitario',r'postura|corrector|ortop[eé]dic|rodiller|tobiller|dolor|alivi|terapia|acupresi|acupunt|masaj|m[eé]dic|term[oó]metro|presi[oó]n arterial|audici|plantilla|juanete|hallux|f[eé]rula|compresi[oó]n|adelgaz|quema grasa|detox|dormir|ronqu|nasal|respira|vitamina|suplemento|c[aá]psula|\bt[eé]\b|magn[eé]tic.*terapia|incontinencia|preservativo|lubricante|sexual|vibrador|adulto|er[oó]tic|lencer|o[ií]do|cera de o|lengua|dental|dientes|ortodon|piojo|verruga|callo|varice|celulitis|busto|pecho|gl[uú]teo|faja|moldead|gafas|lentilla|antifaz'),
 ('electrónica/batería',r'usb|recargable|bater[ií]a|inal[aá]mbric|bluetooth|el[eé]ctric|electr[oó]nic|cargador|\bcarga\b|power ?bank|\bled\b|l[aá]mpara|\bluz\b|luces|solar|inteligente|smart|c[aá]mara|altavoz|auricular|remoto|control remoto|dron|aspirador|ventilador|calefact|calentador|humidificador|difusor|proyector|micr[oó]fono|karaoke|reloj|rastreador|gps|l[aá]ser|motor|autom[aá]tic|enchufe|adaptador|cable|linterna|cortapelo|afeitadora|maquinilla|secador|plancha|rizador|batidora|licuadora|b[aá]scula|alarma|sensor|temporizador|digital|pantalla|rat[oó]n|teclado|mando|consola|bombilla|ne[oó]n|mp3|radio|walkie|hervidor|m[aá]quina de coser|vibraci'),
 ('cristal/frágil',r'cristal|vidrio|cer[aá]mica|porcelana|espejo|m[aá]rmol|jarr[oó]n'),
 ('marca/réplica',r'nike|adidas|apple|airpods|iphone|samsung|disney|marvel|pok[eé]mon|hello kitty|sanrio|stanley|lego|barbie|harry potter|star wars|naruto|anime|one piece|dragon ball|spider|batman|minecraft|sonic|mickey|frozen|louis|gucci|chanel|dior|rolex|crocs|dyson|stitch|kuromi|labubu|bluey|tesla|bmw|mercedes|audi|toyota'),
 ('supermercado/consumible',r'esponja|bayeta|bolsa de basura|limpiador de inodoro|ambientador|detergente|papel de horno|papel de aluminio|toallita|pa[ñn]uelo|servilleta|papel de cocina|vela|incienso|comida|snack|caramelo|especia|caf[eé]|salsa|chocolate|chicle|pegatina'),
 ('tabaco/armas',r'cigarr|fumar|tabaco|hierba|picadora|grinder|cachimba|shisha|vape|mechero|encendedor|cuchillo|navaja|daga|espada|cuchilla|pistola|airsoft|ballesta|tirachinas|\bbala\b|funda de pistola|t[aá]ctico|spray de pimienta|pu[ñn]o americano'),
 ('juguete infantil',r'juguete|ni[ñn]os|ni[ñn]as|infantil|beb[eé]|reci[eé]n nacido|montessori|peluche|mu[ñn]eca|puzle|rompecabezas|mordedor|chupete|carrito|cuna|pa[ñn]al')]
H=[(m,re.compile(r,re.I)) for m,r in H]
rows=[json.loads(l) for l in open(S+'/es/es_all.jsonl')]
out=[]
for p in rows:
    d=p['product_details']; t=p['title']
    days=d.get('min_shipping_time') or 99
    ex=[m for m,r in H if r.search(t)]
    duty=0 if d.get('min_price_warehouse')=='ES' else 3.0
    L1=d['min_price']+(d.get('min_shipping_cost') or 0)+duty
    out.append(dict(id=p['_id'],t=t,c=d['min_price'],cmax=d.get('max_price'),s=d.get('min_shipping_cost'),days=days,wh=d.get('min_price_warehouse'),L1=round(L1,2),
       orders=p.get('orders_count'),eng=p.get('engagement'),comp=p.get('competitors'),sat=p.get('saturation'),sell=p.get('sell_price'),excl=ex))
json.dump(out,open(S+'/es/f1.json','w'),ensure_ascii=False)
fast=[o for o in out if o['days']<=10]
ok=[o for o in fast if not o['excl']]
from collections import Counter
print('<=10d',len(fast),'excluidos',len(fast)-len(ok),Counter(o['excl'][0] for o in fast if o['excl']))
print('quedan',len(ok))
ok.sort(key=lambda o:-(o['orders'] or 0))
for o in ok: print(f"{o['id']}|{o['c']}|{o['s']}|{o['days']}|{o['L1']}|{o['sell']}|{o['orders']}|{o['eng']}|{o['sat']}|{o['t'][:100]}")
