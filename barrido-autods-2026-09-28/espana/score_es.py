import json,csv,math
S='/tmp/claude-0/-home-user-Dropshipping/edd3f668-73f0-5b21-9c24-f699ed49a66a/scratchpad'
f={x['id']:x for x in json.load(open(S+'/es/f1.json'))}
# Coste de la variante que se venderá (verificado en AutoDS ES, 29 sept)
VER={'66d0bf6b23fb880054730cdf':(6.71,'Cama M 55×20×15 cm'),'7bc87629a1f7585909e7afd3':(7.71,'Talla M'),
     '6792545889c4f6aad28875cf':(3.72,'Talla M'),'69fa0eaa502f2a000168ce27':(5.00,'50×80 cm'),
     '699e079616bc0400018b83fe':(7.10,'Media entre 21 y 24 cm'),'90737817716af80324e7e761':(3.30,'25×60 cm')}
DUTY=3.0
def mc(P,L): return P/1.21-L-(0.021*P+0.30)-0.09*P
def pvp_min(L): return (35.3+L)/(1/1.21-0.111)
REC={'69cd326a6a8f990001e84327','66d0bf6b23fb880054730cdf','6792545889c4f6aad28875cf'}
rows=[]
for j in csv.DictReader(open(S+'/es/judg_es.tsv'),delimiter='|'):
    x=f[j['id']]; c,cn=VER.get(j['id'],(None,None))
    if c is None:
        c = (x['c']+x['cmax'])/2 if x['cmax']<=2.5*x['c'] else x['c']*1.5
        cn='Media de variantes (sin verificar una a una)'
    s=x['s'] or 0; duty=0 if x['wh']=='ES' else DUTY
    P=float(j['PV']); L=lambda u: u*(c+s)+duty
    offers=[('1 unidad',P,L(1)),('1+1',P,L(2)),('2.ª al 50 %',round(P*1.5,2),L(2))]
    if j['multi']=='1': offers.append(('3x2',round(P*2,2),L(3)))
    o=max(offers,key=lambda t:mc(t[1],t[2])); mco=mc(o[1],o[2])
    m1=mc(P,L(1)); x3=P>=3*L(1)
    # Nota 0-100: problema/WOW 20, creativo POV 20, margen 25, competencia 15, demanda 10, plazo 10
    sc=2*int(j['prob'])+2*int(j['crea'])+25*max(0,min(mco,25))/25+15*(100-int(j['satj']))/100 \
       +10*min(1,math.log10(max(x['orders'],1))/4)+(10 if x['days']<=7 else 8 if x['days']<=8 else 6 if x['days']<=9 else 4)
    if not x3: sc-=5
    ok=not j['excl']
    rows.append(dict(id=j['id'],src='ES',name=j['name'],niche=j['niche'],hook=j['gancho'] if j['gancho']!='—' else '',title=x['t'],
      brief=ok,why=j['excl'],risk=j['riesgo'],cost=round(c,2),costnote=cn,ship=s,duty=duty,days=x['days'],land=round(L(1),2),pvp=P,
      mc1=round(m1,2),offer=o[0],aov=o[1],mco=round(mco,2),roas=round(o[1]/mco,2) if mco>0 else None,pvpmin=round(pvp_min(L(1)),2),
      x3=x3,orders=x['orders'] or 0,sat=int(j['satj']),satA=x['sat'],score=round(sc,1),rec=j['id'] in REC,
      link='https://platform.autods.com/marketplace/all-products/'+j['id']))
rows.sort(key=lambda r:(-r['brief'],-r['score']))
json.dump(rows,open(S+'/es/D_es.json','w'),ensure_ascii=False)
ok=[r for r in rows if r['brief']]
print('total',len(rows),'cumplen',len(ok),'MC>=35',sum(r['mco']>=35 for r in ok),'3x',sum(r['x3'] for r in ok))
for i,r in enumerate(ok[:30],1): print(i,r['score'],r['niche'],r['name'],'| L',r['land'],'PVP',r['pvp'],'MC1',r['mc1'],r['offer'],'MCo',r['mco'],'ROAS',r['roas'],'d',r['days'],'3x' if r['x3'] else '')
from collections import defaultdict
g=defaultdict(list)
for r in ok[:50]: g[r['niche']].append(r)
for n,v in sorted(g.items(),key=lambda kv:-sum(r['score'] for r in kv[1][:3])): print(n,len(v),round(sum(r['score'] for r in v[:3])/min(3,len(v)),1),round(sum(r['mco'] for r in v[:3])/min(3,len(v)),1))
