"""Barrido EE. UU. — Belleza, Salud y Cuidado Personal (29 sept 2026).

bel_raw.jsonl.gz: los ~458 ganadores de AutoDS en «Beauty & Personal Care» (todas las páginas, por pedidos)
más productos de búsqueda en esa categoría, «Health & Wellness» y «Tools & Accessories» con envío < 11 días.
Aquí solo se normaliza al esquema de f1_us.py (con arancel) y se añade lo del barrido general que es del sector.
El juicio (vetos, precio, riesgo) va en judg_bel.tsv.
"""
import json, gzip, os
from f1_us import duty  # noqa: E402  (ejecuta f1_us, que regenera f1_us.json)

D = os.path.dirname(os.path.abspath(__file__))
rows = {x['id']: x for x in json.load(open(os.path.join(D, 'f1_us.json')))}
for l in gzip.open(os.path.join(D, 'bel_raw.jsonl.gz'), 'rt'):
    p = json.loads(l); d = p.get('product_details') or {}
    if d.get('min_price') is None:
        continue
    o = dict(id=p['_id'], src=p['src'], t=p['title'], c=d['min_price'], cmax=d.get('max_price'),
             s=d.get('min_shipping_cost') or 0, days=d.get('min_shipping_time') or 99, wh=d.get('min_price_warehouse'),
             orders=p.get('orders_count'), sat=p.get('saturation'), sell=p.get('sell_price'), veto=[], aviso=[])
    o['duty'] = duty(o['c'], o['wh']); o['L1'] = round(o['c'] + o['s'] + o['duty'], 2)
    rows[o['id']] = o
json.dump(list(rows.values()), open(os.path.join(D, 'f1_bel.json'), 'w'), ensure_ascii=False)
print('filas', len(rows))
