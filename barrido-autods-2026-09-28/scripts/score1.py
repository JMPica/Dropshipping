import json,re,math,sys
S='/tmp/claude-0/-home-user-Dropshipping/edd3f668-73f0-5b21-9c24-f699ed49a66a/scratchpad'
FX=0.90  # USD->EUR (supuesto conservador de la skill)
rows=[json.loads(l) for l in open(S+'/all.jsonl')]
H=[ # (motivo, regex)  -> filtro duro
 ('piel/cosmética (CPNP)', r'\b(cream|serum|lotion|mask|makeup|make-up|lipstick|lip ?gloss|lip|nail polish|gel polish|uv gel|polygel|tattoo|perfume|fragrance oil|essential oil|shampoo|conditioner|soap|toothpaste|whitening|eyelash|lash|glue|foundation|concealer|mascara|eyeliner|eyebrow|blush|skin ?care|facial|face wash|cleanser|moisturi|sunscreen|deodorant|hair dye|hair color|wax|scrub|body oil|bath bomb|balm|toner|acne|pimple|wrinkle|anti[- ]?aging|collagen|hair removal|epilat|depilat|false nails|press on nails|nail tips|nail art|kiss|temporary tattoo|slime)\b'),
 ('salud/sanitario/alegaciones', r'\b(posture|corrector|brace|orthopedic|orthotic|pain|relief|therapy|therapeutic|acupressure|acupuncture|massag\w*|medical|thermometer|blood|pressure|hearing|insoles?|bunion|hallux|knee|splint|compression|slimming|weight loss|fat|detox|sleep(ing)? aid|snor\w*|anti[- ]?snore|mouth tape|nasal|breath|inhaler|pill|vitamin|supplement|capsule|tea|herbal|magnetic therapy|tens|ems|scoliosis|hemorrhoid|incontinence|condom|lubricant|sex|vibrator|dildo|adult|erotic|lingerie|ear ?wax|earwax|ear cleaner|tongue|teeth|dental|orthodont|lice|wart|mole|callus|foot peel|varicose|cellulite|bust|breast|butt lift|waist trainer|shapewear|glasses|eyeglass|contact lens|eye mask)\b'),
 ('electrónica/batería/radio (CE/RED, RAEE)', r'\b(usb|rechargeable|battery|batteries|wireless|bluetooth|electric|electronic|cordless|charger|charging|power ?bank|led|lamp|light|lights|solar|smart|camera|speaker|headphone|earphone|earbuds?|remote|rc|drone|vacuum|fan|heater|heated|humidifier|diffuser|projector|mic|microphone|karaoke|watch|smartwatch|tracker|gps|laser|motor|automatic|electrical|plug|adapter|cable|flashlight|torch|trimmer|shaver|clipper|dryer|straightener|curler|curling iron|hair straightening|blender|juicer|scale|alarm|sensor|timer|digital|lcd|display|mouse|keyboard|gamepad|controller|console|dash ?cam|inverter|bulb|neon|string lights|night light|glow|luminous|sound|music|mp3|radio|walkie|kettle|iron|sewing machine)\b'),
 ('cristal/frágil', r'\b(glass|glasses|ceramic|porcelain|crystal|mirror|marble|terrarium|vase)\b'),
 ('marca/réplica', r'\b(nike|adidas|apple|airpods?|samsung|disney|marvel|pokemon|pok[eé]mon|hello kitty|sanrio|stanley|lego|barbie|harry potter|star wars|naruto|anime|one piece|dragon ball|spiderman|spider-man|batman|minecraft|sonic|mickey|frozen|louis|gucci|chanel|dior|rolex|yeti|owala|crocs|dyson|burt|dawn|blenderbottle|fifa|nba|nfl|ferrari|bmw|mercedes|audi|toyota|tesla|jeep|ford|honda|mitsubishi|volkswagen|vw|lexus|kia|hyundai|nissan|mazda|porsche|harley|kawasaki|yamaha|suzuki|ktm|ducati|stitch|kuromi|squishmallow|labubu|jellycat|bluey|sesame)\b'),
 ('supermercado/consumible', r'\b(sponge|dish ?cloth|dishcloth|trash bag|garbage bag|toilet cleaner|cleaning gel|air freshener|detergent|laundry pod|parchment|aluminum foil|cling|wipes|tissue|napkin|paper towel|candle|incense|food|snack|candy|seasoning|spice|coffee|sauce|chocolate|gum|stickers?|washi)\b'),
 ('tabaco/armas/otros vetados Meta', r'\b(cigarette|smoking|tobacco|weed|herb grinder|grinder|hookah|shisha|vape|rolling|pipe|lighter|knife|knives|dagger|sword|blade|gun|pistol|airsoft|crossbow|slingshot|bullet|ammo|holster|tactical|pepper spray|stun|brass knuckle|bong)\b'),
 ('juguete infantil (CE juguetes EN71)', r'\b(toy|toys|kids|children|child|baby|infant|toddler|newborn|montessori|plush|doll|puzzle|teether|pacifier|stroller|crib|diaper)\b'),
]
H=[(m,re.compile(r,re.I)) for m,r in H]
out=[]
for p in rows:
    d=p.get('product_details') or {}
    t=p.get('title','')
    c=d.get('min_price'); s=d.get('min_shipping_cost') or 0
    if c is None: continue
    reasons=[m for m,r in H if r.search(t)]
    landed=(c+s)*FX          # 1 ud puesta, EUR
    pair=2*landed
    sell=(p.get('sell_price') or 0)*FX
    tiers=[29.95,34.95,39.95,44.95,49.95,54.95,59.95,64.95,69.95,74.95,79.95]
    P=max([x for x in tiers if x<=max(sell,29.95)] or [29.95]); P=min(P,79.95)
    mc=lambda P,L: P/1.21-L-(0.021*P+0.30)-0.09*P
    mc_pair=mc(P,pair)
    mult=P/landed if landed else 0
    out.append(dict(id=p['_id'],src=p['src'][:3],t=t,c=c,cmax=d.get('max_price'),s=s,days=d.get('min_shipping_time'),wh=d.get('min_price_warehouse'),
        orders=p.get('orders_count'),eng=p.get('engagement'),comp=p.get('competitors'),sat=p.get('saturation'),sell=round(sell,2),
        landed=round(landed,2),pair=round(pair,2),P=P,mc=round(mc_pair,2),mult=round(mult,2),excl=reasons,
        cat=(p.get('categories') or [{}])[0].get('name','') if p.get('categories') else '', created=(p.get('created_at') or '')[:7]))
json.dump(out,open(S+'/s1.json','w'))
n=len(out); ex=[o for o in out if o['excl']]; keep=[o for o in out if not o['excl']]
print('total',n,'excluidos',len(ex),'quedan',len(keep))
from collections import Counter
print(Counter(r for o in ex for r in o['excl'][:1]))
ok=[o for o in keep if o['mc']>=35 and o['mult']>=3]
print('quedan con MC>=35 y x3:',len(ok), ' de ellos ganadores:',sum(o['src']=='get' for o in ok))
