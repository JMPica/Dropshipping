import json,re
from collections import Counter
S='/tmp/claude-0/-home-user-Dropshipping/194890f3-5dea-5898-afd6-d3b8aab39306/scratchpad'
NICHE=re.compile(r'belleza|cabello|pelo|cuero cabelludo|rizad|alisad|peine|cepillo|facial|\bcara\b|piel|u[ñn]a|manicura|pedicura|pies|pie\b|talón|callo|masaj|gua sha|rodillo|postura|espalda|cuello|dolor|sue[ñn]o|dormir|ronquid|ojos|pesta[ñn]|ceja|maquillaje|brocha|esponja|afeitad|depila|vello|ducha|baño|spa|belleza|dental|dientes|bucal|labio|mascarilla|antifaz|relaj|ejercicio facial|mand[ií]bula|glúteo|celulitis|drenaje|linf',re.I)
H=[('fórmula cosmética (CPNP)',r'crema|s[eé]rum|loci[oó]n|mascarilla (facial|de|para)|\bmascarillas?\b.*(piel|facial|cara)|parches? (de|para) (ojos|acn|granos)|maquillaje(?! brocha)|base de maquillaje|corrector de ojeras|labial|pintalabios|brillo de labios|esmalte|gel (de|para) u|tinte|perfume|fragancia|aceite (esencial|de|para)|champ[uú]|acondicionador|jab[oó]n|dent[ií]frico|pasta de dientes|blanquea|rimel|r[ií]mel|m[aá]scara de pesta|delineador|colorete|sombra de ojos|protector solar|autobronceador|desodorante|exfoliante (facial|corporal)|b[aá]lsamo|pomada|ung[uü]ento|esencia|t[oó]nico|limpiador facial|espuma|polvos|cera (para|de) (pelo|depil)|tratamiento (de|para) u|gotas|spray|col[aá]geno|[aá]cido|retinol|vitamina|kit de tinte|pegamento de pesta|adhesivo'),
 ('complemento/medicamento',r'suplemento|c[aá]psula|comprimido|pastilla|gominola|t[eé] (detox|adelgaz)|minoxidil|probi[oó]tic|melatonina'),
 ('alegación médica/sanitario',r'ortop[eé]dic|corrector de postura|f[eé]rula|juanete|hallux|u[ñn]as? encarnad|hongos|fungic|verruga|terapia de (luz|fot)|l[aá]ser|tens\b|electroestimul|presi[oó]n arterial|term[oó]metro|audífono|adelgaz|quema grasa|reductor|celulitis|varices|ciática|artritis|pérdida de peso|limpiador de o[ií]dos|o[ií]dos? con c[aá]mara|busto|agrandar'),
 ('frágil',r'cristal|vidrio|cer[aá]mica|porcelana|jade|cuarzo|piedra natural'),
 ('marca/réplica',r'dyson|olaplex|nike|disney|marvel|pok[eé]mon|sanrio|hello kitty|chanel|dior|stanley|labubu'),
 ('adulto',r'sexual|vibrador|er[oó]tic|adulto|lencer|masturb|preservativo|lubricante')]
H=[(m,re.compile(r,re.I)) for m,r in H]
ELEC=re.compile(r'el[eé]ctric|recargable|usb|bater[ií]a|inal[aá]mbric|\bled\b|luz roja|ultras[oó]nic|vibraci|calefact|calor|t[eé]rmic|secador|plancha|rizador|cepillo de aire|ion|motor|autom[aá]tic|inteligente|smart|digital|carga',re.I)
fresh=[json.loads(l) for l in open(S+'/all.jsonl')]
prev=[json.loads(l) for l in open(S+'/prev.jsonl')]
ids={p['_id'] for p in fresh}
pool=[]
for p in fresh:
    if p.get('site_name')=='amazon': p['_drop']='Amazon ES (marca de supermercado)'
    pool.append(p)
for p in prev:
    if p['_id'] in ids: continue
    p['_inniche']=bool(NICHE.search(p['title']))
    pool.append(p)
print('explorados',len(pool))
out=[];why=Counter()
for p in pool:
    d=p['product_details'];t=p['title']
    r=dict(id=p['_id'],t=t,src=p['src'],c=d['min_price'],cmax=d.get('max_price'),s=d.get('min_shipping_cost') or 0,days=d.get('min_shipping_time') or 99,wh=d.get('min_price_warehouse'),
           orders=p.get('orders_count'),eng=p.get('engagement'),comp=p.get('competitors'),sat=p.get('saturation'),sell=p.get('sell_price'),
           cat=[c['name'] for c in p.get('categories') or []],win=bool(p.get('is_winning_product')),elec=bool(ELEC.search(t)))
    ex=None
    if p.get('_drop'): ex=p['_drop']
    elif p['src']=='prev_winners_es' and not p['_inniche']: ex='fuera de nicho'
    else:
        for m,rg in H:
            if rg.search(t): ex=m;break
    r['L']=round(r['c']+r['s']+(0 if r['wh']=='ES' else 3),2)
    if not ex and not (r['c']<=27 and r['L']>=5.5): ex='coste fuera de 5-30 $'
    if not ex and r['days']>12: ex='envío > 12 días'
    r['excl']=ex; why[ex or 'PASA']+=1; out.append(r)
json.dump(out,open(S+'/f1.json','w'),ensure_ascii=False)
for k,v in why.most_common(): print(v,k)
ok=[o for o in out if not o['excl']]
ok.sort(key=lambda o:(-(o['orders'] or 0)))
with open(S+'/pass.tsv','w') as f:
    for o in ok: f.write(f"{o['id']}|{o['c']}|{o['s']}|{o['days']}|{o['wh']}|{o['orders']}|{o['eng']}|{o['sat']}|{'E' if o['elec'] else ''}|{o['t'][:95]}\n")
