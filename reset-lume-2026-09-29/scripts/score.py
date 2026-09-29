import json,csv,math
S='/tmp/claude-0/-home-user-Dropshipping/194890f3-5dea-5898-afd6-d3b8aab39306/scratchpad'
pool={}
for fn in ('all.jsonl','prev.jsonl'):
    for l in open(f'{S}/{fn}'):
        p=json.loads(l); pool.setdefault(p['_id'],p)
DUTY=3.0  # arancel/gestión UE por paquete desde China (supuesto)
def mc(P,L): return P/1.21-L-(0.021*P+0.30)-0.09*P
rows=[]
for j in csv.DictReader(open(S+'/judg.tsv'),delimiter='|'):
    p=pool[j['id']]; d=p['product_details']; flags=[]
    ver=j['verif']=='1'
    if j['cost']:
        c=float(j['cost']); s=float(j['ship']); days=int(j['days']); orders=int(j['orders'])
    else:
        c=d['min_price']; cm=d.get('max_price') or c
        if cm>c*1.15: c=round((c+cm)/2,2) if cm<=2.5*d['min_price'] else round(c*1.5,2); flags.append('Coste = media de variantes')
        s=d.get('min_shipping_cost') or 0; days=d.get('min_shipping_time') or 99; orders=p.get('orders_count') or 0
        if s==0 and (d.get('max_shipping_cost') or 0)>3: flags.append('Envío gratis y rápido sin confirmar')
    duty=0 if d.get('min_price_warehouse')=='ES' else DUTY
    L=lambda u:u*(c+s)+duty
    P=float(j['PVP'])
    offers=[('1 unidad',P,L(1))]
    if j['pack']=='1': offers+= [('2.ª al 50 %',round(P*1.5,2),L(2)),('Pack 3x2',round(P*2,2),L(3))]
    else: offers+= [('2.ª al 50 %',round(P*1.5,2),L(2))]
    o=max(offers,key=lambda t:mc(t[1],t[2])); mco=mc(o[1],o[2]); m1=mc(P,L(1))
    mult=P/L(1)
    eng=p.get('engagement') or 0; sat=p.get('saturation'); sat=50 if sat is None else sat
    prob,demo,tienda,riesgo=int(j['prob']),int(j['demo']),int(j['tienda']),int(j['riesgo'])
    elec=any(k in (j['nota_riesgo']+j['name']).lower() for k in ('eléctric','batería','bluetooth','recargable','ems','ce.','ce ','ce y'))
    s_marg=25*max(0,min(1,(mco-5)/20))
    s_mult=10 if mult>=3 else 6 if mult>=2.5 else 2 if mult>=2 else -8
    s_prob=2*prob+2*demo
    s_val=(14*min(1,math.log10(max(orders,1))/4))+6*eng/100
    s_comp=5*(100-sat)/100+tienda
    s_env=10 if days<=8 else 9 if days==9 else 8 if days==10 else 6 if days==11 else 5
    pen=(3 if elec else 0)+(4 if riesgo==1 else 8 if riesgo==2 else 0)
    sc=s_marg+s_mult+s_prob+s_val+s_comp+s_env-pen
    comp_lbl='Baja' if s_comp>=7 else 'Media' if s_comp>=4.5 else 'Alta'
    rows.append(dict(id=j['id'],name=j['name'],sub=j['sub'],title=p['title'],cost=round(c,2),ship=s,duty=duty,land=round(L(1),2),days=days,
        pvp=P,mult=round(mult,2),mc1=round(m1,2),offer=o[0],aov=o[1],mco=round(mco,2),roas=round(o[1]/mco,2) if mco>0 else None,
        orders=orders,eng=eng,sat=sat,comp=p.get('competitors'),complbl=comp_lbl,tienda=tienda,riesgo=riesgo,nota=j['nota_riesgo'],
        gancho='' if j['gancho']=='—' else j['gancho'],elec=elec,ver=ver,flags=flags,
        parts=dict(margen=round(s_marg,1),multiplo=s_mult,problema=s_prob,ventas=round(s_val,1),competencia=round(s_comp,1),envio=s_env,penal=-pen),
        score=round(sc,1),link='https://platform.autods.com/marketplace/all-products/'+j['id'],
        img=(p.get('images') or [None])[0] if isinstance(p.get('images'),list) else None))
rows.sort(key=lambda r:-r['score'])
for i,r in enumerate(rows,1): r['rank']=i
json.dump(rows,open(S+'/D.json','w'),ensure_ascii=False)
for r in rows: print(r['rank'],r['score'],r['sub'],r['name'][:40],'|L',r['land'],'PVP',r['pvp'],'x',r['mult'],'MC1',r['mc1'],r['offer'],'MCo',r['mco'],'ROAS',r['roas'],'d',r['days'],'o',r['orders'],r['complbl'],r['flags'])
from collections import defaultdict
g=defaultdict(list)
for r in rows: g[r['sub']].append(r)
for k,v in sorted(g.items(),key=lambda kv:-sum(x['score'] for x in kv[1][:3])/min(3,len(kv[1]))): print(k,len(v),round(sum(x['score'] for x in v[:3])/min(3,len(v)),1),round(sum(x['mco'] for x in v[:3])/min(3,len(v)),1))
