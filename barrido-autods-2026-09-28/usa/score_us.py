"""Barrido EE. UU. — puntuación de finalistas (juicio manual en judg_us.tsv).

MC (USD) = PVP - coste puesto - (4,5 % PVP + 0,30 $) - 9 % PVP
  - Sin IVA: tienda en España vendiendo a EE. UU. (exportación; sales tax no aplica
    por debajo de los umbrales de nexo económico).
  - 4,5 %: Shopify Payments con tarjeta extranjera + conversión de divisa.
  - 9 %: devoluciones, contracargos y apps (igual que el barrido de España).
Coste puesto = unidades x (coste + envío AutoDS) + arancel (solo si sale de CN/otros; ver f1_us.py).
Objetivo del brief: MC >= 38,9 $ por pedido (= 35 €).
"""
import json, csv, math, os

D = os.path.dirname(os.path.abspath(__file__))
f = {x['id']: x for x in json.load(open(os.path.join(D, 'f1_us.json')))}
# Coste de la variante que se venderá (verificado en AutoDS US, 29 sept); se rellena tras get_product_by_id
VER = json.load(open(os.path.join(D, 'verificados.json'))) if os.path.exists(os.path.join(D, 'verificados.json')) else {}
OBJ = 38.9


def mc(P, L):
    return P - L - (0.045 * P + 0.30) - 0.09 * P


def pvp_min(L):  # PVP para MC = objetivo con 1 unidad
    return (OBJ + 0.30 + L) / (1 - 0.135)


def duty(c, wh):
    if wh == 'US':
        return 0.0
    return round((0.40 if wh == 'CN' else 0.10) * c + 1.0, 2)


rows = []
for j in csv.DictReader(open(os.path.join(D, 'judg_us.tsv')), delimiter='|'):
    x = f[j['id']]
    v = VER.get(j['id'])
    if v:
        c, cn = v['c'], v['nota']
        s = v.get('s', x['s'] or 0)
    else:
        cmax = x['cmax'] or x['c']
        c = (x['c'] + cmax) / 2 if cmax <= 2.5 * x['c'] else x['c'] * 1.5
        cn = 'Media de variantes (sin verificar una a una)'
        s = x['s'] or 0
    P = float(j['PV'])

    def L(u):  # arancel sobre el valor de todas las unidades del paquete; envío por unidad
        return u * (c + s) + (duty(u * c, x['wh']) if x['wh'] != 'US' else 0)

    offers = [('1 unidad', P, L(1)), ('2.ª al 50 %', round(P * 1.5, 2), L(2)), ('1+1 gratis', P, L(2))]
    if j['multi'] == '1':
        offers.append(('3x2', round(P * 2, 2), L(3)))
    o = max(offers, key=lambda t: mc(t[1], t[2]))
    mco = mc(o[1], o[2]); m1 = mc(P, L(1)); x3 = P >= 3 * L(1)
    days = x['days'] or 10
    # Nota 0-100: problema/WOW 20, creativo 20, margen 25 (tope 40 $), competencia 15, demanda 10, plazo 10
    sc = 2 * int(j['prob']) + 2 * int(j['crea']) + 25 * max(0, min(mco, 40)) / 40 + 15 * (100 - int(j['satj'])) / 100 \
        + 10 * min(1, math.log10(max(x['orders'] or 1, 1)) / 4) + (10 if days <= 5 else 8 if days <= 7 else 6 if days <= 9 else 4)
    if not x3:
        sc -= 5
    ok = not j['excl']
    rows.append(dict(id=j['id'], src='US', name=j['name'], niche=j['niche'], hook=j['gancho'] if j['gancho'] != '—' else '',
                     title=x['t'], brief=ok, why=j['excl'], risk=j['riesgo'], cost=round(c, 2), costnote=cn, ship=s,
                     duty=round(L(1) - (c + s), 2), days=days, wh=x['wh'], land=round(L(1), 2), pvp=P, mc1=round(m1, 2),
                     offer=o[0], aov=o[1], mco=round(mco, 2), roas=round(o[1] / mco, 2) if mco > 0 else None,
                     pvpmin=round(pvp_min(L(1)), 2), x3=x3, orders=x['orders'] or 0, sat=int(j['satj']), score=round(sc, 1),
                     link='https://platform.autods.com/marketplace/all-products/' + j['id']))
rows.sort(key=lambda r: (-r['brief'], -r['score']))
json.dump(rows, open(os.path.join(D, 'D_us.json'), 'w'), ensure_ascii=False, indent=0)
ok = [r for r in rows if r['brief']]
print('total', len(rows), 'cumplen', len(ok), f'MC>={OBJ}', sum(r['mco'] >= OBJ for r in ok), '3x', sum(r['x3'] for r in ok))
for i, r in enumerate(ok[:30], 1):
    print(i, r['score'], r['niche'], r['name'], '|', r['wh'], 'L', r['land'], 'PVP', r['pvp'], 'MC1', r['mc1'], r['offer'],
          'AOV', r['aov'], 'MCo', r['mco'], 'ROAS', r['roas'], 'd', r['days'], '3x' if r['x3'] else '', '*' if r['costnote'].startswith('Var') else '')
from collections import defaultdict
g = defaultdict(list)
for r in ok[:40]:
    g[r['niche']].append(r)
print('\nNichos (top 40):')
for n, v in sorted(g.items(), key=lambda kv: -sum(r['score'] for r in kv[1][:3]) / min(3, len(kv[1]))):
    print(n, len(v), round(sum(r['score'] for r in v[:3]) / min(3, len(v)), 1), round(sum(r['mco'] for r in v[:3]) / min(3, len(v)), 1))
