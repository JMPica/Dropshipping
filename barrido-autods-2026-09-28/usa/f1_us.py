"""Barrido EE. UU. (29 sept 2026) — filtro duro.

Une los 1.770 candidatos del 28 sept (ya en región US) con los ganadores de los
últimos 30 días y los productos de almacén US (nuevos.jsonl), y aplica:
  - envío a EE. UU. <= 10 días
  - vetos para EE. UU. (marca/réplica, armas/tabaco, adulto, ingeribles y
    alegaciones de salud (FDA), juguete infantil/bebé (CPSC/CPC), consumible)
  - avisos (no vetan): electrónica/batería (FCC, envío de litio),
    cosmética (FDA/MoCRA, alegaciones), frágil.
Todo en USD.
"""
import json, re, os, gzip
from collections import Counter

D = os.path.dirname(os.path.abspath(__file__))
DUTY_RATE, DUTY_FIX = 0.40, 1.00  # CN -> US sin de minimis: ~40 % del valor + ~1 $ de gestión (supuesto)


def duty(c, wh):
    if wh == 'US':
        return 0.0
    if wh == 'CN':
        return round(DUTY_RATE * c + DUTY_FIX, 2)
    return round(0.10 * c + DUTY_FIX, 2)  # otros orígenes (UE, UK...): MFN aprox.


VETO = [
    ('marca/réplica', r'\b(nike|adidas|apple|airpods?|iphone|samsung|disney|marvel|pokemon|pok[eé]mon|hello kitty|sanrio|stanley|lego|barbie|harry potter|star wars|naruto|anime|one piece|dragon ball|spiderman|spider-man|batman|minecraft|sonic|mickey|frozen|louis|gucci|chanel|dior|rolex|yeti|owala|crocs|dyson|fifa|nba|nfl|ferrari|bmw|mercedes|audi|toyota|tesla|jeep|ford|honda|stitch|kuromi|squishmallow|labubu|jellycat|bluey|sesame|medicube|kahi)\b'),
    ('tabaco/armas', r'\b(cigarette|smoking|tobacco|weed|grinder|hookah|shisha|vape|rolling|pipe|lighter|knife|knives|dagger|sword|gun|pistol|airsoft|crossbow|slingshot|bullet|ammo|holster|tactical|pepper spray|stun|brass knuckle|bong)\b'),
    ('adulto', r'\b(sex|sexy|vibrator|dildo|adult|erotic|lingerie|condom|lubricant)\b'),
    ('salud/ingerible (FDA)', r'\b(posture|corrector|orthopedic|orthotic|pain|relief|therapy|therapeutic|acupressure|acupuncture|medical|thermometer|blood|hearing|bunion|hallux|splint|slimming|weight loss|fat burn|detox|sleep aid|snor\w*|mouth tape|nasal|inhaler|pill|vitamin|supplement|capsule|herbal|tens|ems|scoliosis|hemorrhoid|incontinence|ear ?wax|earwax|lice|wart|varicose|cellulite|butt lift|contact lens|teeth whitening|whitening strips?)\b'),
    ('juguete/bebé (CPSC)', r'\b(toy|toys|kids|children|child|baby|infant|toddler|newborn|montessori|plush|doll|teether|pacifier|stroller|crib|diaper)\b'),
    ('consumible', r'\b(sponge|dish ?cloth|trash bag|garbage bag|toilet cleaner|cleaning gel|air freshener|detergent|laundry pod|parchment|aluminum foil|wipes|tissue|napkin|paper towel|incense|food|snack|candy|seasoning|spice|coffee|sauce|chocolate|gum|stickers?|washi)\b'),
]
AVISO = [
    ('electrónica/batería', r'\b(usb|rechargeable|battery|batteries|wireless|bluetooth|electric|cordless|charger|charging|power ?bank|solar|smart|camera|speaker|headphone|earbuds?|remote|drone|vacuum|heater|heated|humidifier|projector|laser|motor|plug|trimmer|shaver|straightener|curler|blender|juicer)\b'),
    ('cosmética', r'\b(cream|serum|lotion|mask|makeup|lipstick|lip|nail|perfume|shampoo|soap|eyelash|lash|foundation|mascara|skin ?care|facial|moisturi|balm|wrinkle|anti[- ]?aging|collagen|hair removal)\b'),
    ('frágil', r'\b(glass|ceramic|porcelain|crystal|mirror|marble|vase)\b'),
]
VETO = [(m, re.compile(r, re.I)) for m, r in VETO]
AVISO = [(m, re.compile(r, re.I)) for m, r in AVISO]

rows = {}
for x in json.load(open(os.path.join(D, '..', 'datos', 'candidatos_filtrados.json'))):
    rows[x['id']] = dict(id=x['id'], src='28sep-' + x['src'], t=x['t'], c=x['c'], cmax=x['cmax'], s=x['s'],
                         days=x['days'], wh=x['wh'], orders=x['orders'], sat=x['sat'], sell=x['sell'])
for l in gzip.open(os.path.join(D, 'nuevos.jsonl.gz'), 'rt'):
    p = json.loads(l); d = p.get('product_details') or {}
    if d.get('min_price') is None:
        continue
    rows[p['_id']] = dict(id=p['_id'], src='29sep-' + p['src'][:3], t=p['title'], c=d['min_price'], cmax=d.get('max_price'),
                          s=d.get('min_shipping_cost') or 0, days=d.get('min_shipping_time') or 99, wh=d.get('min_price_warehouse'),
                          orders=p.get('orders_count'), sat=p.get('saturation'), sell=p.get('sell_price'))

out = []
for o in rows.values():
    o['veto'] = [m for m, r in VETO if r.search(o['t'])]
    o['aviso'] = [m for m, r in AVISO if r.search(o['t'])]
    o['duty'] = duty(o['c'], o['wh'])
    o['L1'] = round(o['c'] + (o['s'] or 0) + o['duty'], 2)
    out.append(o)
json.dump(out, open(os.path.join(D, 'f1_us.json'), 'w'), ensure_ascii=False)

fast = [o for o in out if (o['days'] or 99) <= 10]
ok = [o for o in fast if not o['veto']]
print('total', len(out), '| <=10 d', len(fast), Counter(o['wh'] for o in fast))
print('vetados', len(fast) - len(ok), Counter(o['veto'][0] for o in fast if o['veto']))
print('quedan', len(ok), Counter(o['wh'] for o in ok), '| con aviso', Counter(a for o in ok for a in o['aviso']))
ok.sort(key=lambda o: -(o['orders'] or 0))
with open(os.path.join(D, 'f1_quedan.tsv'), 'w') as f:
    f.write('id|src|c|cmax|s|duty|L1|days|wh|sell|orders|sat|aviso|titulo\n')
    for o in ok:
        f.write(f"{o['id']}|{o['src']}|{o['c']}|{o['cmax']}|{o['s']}|{o['duty']}|{o['L1']}|{o['days']}|{o['wh']}|{o['sell']}|{o['orders']}|{o['sat']}|{','.join(o['aviso'])}|{o['t'][:110]}\n")
