import json,csv,statistics as st
S='/tmp/claude-0/-home-user-Dropshipping/edd3f668-73f0-5b21-9c24-f699ed49a66a/scratchpad'
exec(open(S+'/weights.py').read())
FX=0.90
def ship_usd(g): return 5.0+0.004*max(0,g-500)       # AliExpress→ES estimado: ~1,5 € envío + 3 € arancel por paquete
def mc(P,L): return P/1.21-L-(0.021*P+0.30)-0.09*P
def pvp_min(L): return (35.3+L)/(1/1.21-0.111)       # PVP (1 ud.) con el que MC = 35 €
# --- Brief: validez de los 50 del Radar Salud y Belleza (por rango)
bad={1:'Electrónico con batería',2:'Electrónico con batería',4:'Electrónico con batería',6:'Electrónico',7:'Electrónico',
 9:'Alegación de salud (postura); ya descartado',10:'Producto sanitario / alegación médica',12:'Electrónico',13:'Electrónico + alegaciones de salud',
 14:'Alegación de salud (dolor de coxis)',15:'Electrónico + alegación antiedad',16:'Electrónico con batería',17:'Alegación de salud (fascitis)',
 18:'Producto sanitario (lumbar)',19:'Electrónico',20:'Electrónico + alegación de crecimiento',21:'Electrónico + alegación de crecimiento',
 23:'Eléctrico + cera cosmética',24:'Producto sanitario (bucal)',25:'Electrónico + alegación médica',26:'Producto sanitario (rodilla)',
 28:'Electrónico + alegación médica',29:'Electrónico USB',32:'Alegación de salud (reflexología)',35:'Alegación de salud (artritis)',
 37:'Electrónico con batería',38:'Electrónico + alegación de adelgazamiento',40:'Electrónico USB',41:'Producto sanitario (MDR)',
 42:'Electrónico',43:'Electrónico',45:'Electrónico',46:'Alegación de salud (cervical)',47:'Electrónico',48:'Electrónico',
 49:'Producto sanitario (rodilla)',50:'Alegación de salud (acupresión)'}
riskA={3:'Rosca del cabezal: comprobar compatibilidad UE. Sin prometer efectos en piel o pelo.',22:'Tallas: devoluciones. Higiene: sin devolución si se ha usado.',
 27:'Si incluye delineador magnético es cosmético (CPNP): vender solo pestañas.',31:'No prometer «drenaje linfático».',
 34:'Se vende en tiendas físicas.',39:'Color de pelo: devoluciones.',44:'Venderla como entrenamiento, sin alegaciones de rehabilitación.'}
A=json.load(open(S+'/radar/A.json'))
rows=[]
for a in A:
    w=150 if a['size']=='S' else 600
    c=a['cost']; P=round(a['price'],2)
    L1=(c+ship_usd(w))*FX; L2=(2*c+ship_usd(2*w))*FX
    offers=[('1+1',P,L2),('2.ª al 50 %',round(P*1.5,2),L2)]
    o=max(offers,key=lambda t:mc(t[1],t[2]))
    rows.append(dict(id=a['id'],src='A',name=a['name'],niche=a['niche'],hook=a['problem'],title=a['title'],
      brief=a['rank'] not in bad,why=bad.get(a['rank'],''),risk=riskA.get(a['rank'],a['risk']) if a['rank'] not in bad else a['risk'],
      size=a['size'],w=w,cost=c,land=round(L1,2),pvp=P,pvpnote='Precio objetivo del radar (5× coste o sugerido AutoDS)',
      mc1=round(mc(P,L1),2),offer=o[0],aov=o[1],mco=round(mc(o[1],o[2]),2),pvpmin=round(pvp_min(L1),2),
      orders=a['orders'],sat=a['sat'],comp=a['comp'],score=a['score'],link=a['link']))
# --- Barrido abierto (top 50)
fin=json.load(open(S+'/s3.json')); fin.sort(key=lambda x:-x['score']); fin=fin[:50]
multi={r['id']:r['multi']=='1' for r in csv.DictReader(open(S+'/judg.tsv'),delimiter='|')}
seen={r['id'] for r in rows}
for x in fin:
    c=x['c']; w=x['w']; P=x['PV']
    L1=(c+ship_usd(w))*FX
    def L(u): return (u*c+ship_usd(u*w))*FX
    offers=[('1+1',P,L(2)),('2.ª al 50 %',round(P*1.5,2),L(2))]
    if multi[x['id']]: offers.append(('3x2',round(P*2,2),L(3)))
    o=max(offers,key=lambda t:mc(t[1],t[2]))
    ok=x['id']!='68fbb9bded8668000107ce8d'
    d=dict(id=x['id'],src='B',name=x['es'],niche=x['nicho'],hook=x['gancho'],title=x['t'],brief=ok,
      why='' if ok else 'Voluminoso: envío a España fuera de precio',risk=x['riesgo'],size='S' if w<=300 else 'M',w=w,cost=c,land=round(L1,2),
      pvp=P,pvpnote='PVP creíble en España (competencia y valor percibido)',mc1=round(mc(P,L1),2),offer=o[0],aov=o[1],mco=round(mc(o[1],o[2]),2),
      pvpmin=round(pvp_min(L1),2),orders=x['orders'] or 0,sat=x['satA'] if x['satA'] is not None else 40,comp=x['comp'] or 0,score=x['score'],
      link='https://platform.autods.com/marketplace/hand-picked-products/'+x['id'])
    if x['id'] in seen:
        r=[r for r in rows if r['id']==x['id']][0]; r.update({k:d[k] for k in ('pvp','pvpnote','mc1','offer','aov','mco','risk','hook')}); r['src']='AB'; continue
    rows.append(d)
json.dump(rows,open(S+'/radar/D.json','w'),ensure_ascii=False)
ok=[r for r in rows if r['brief']]
print('total',len(rows),'cumplen',len(ok),'MC>=35',sum(r['mco']>=35 for r in ok),'mejor',max(ok,key=lambda r:r['mco'])['name'],max(r['mco'] for r in ok))
print('pvpmin mediana',st.median(r['pvpmin'] for r in ok))
for r in sorted(ok,key=lambda r:-r['mco'])[:12]: print(r['src'],r['mco'],r['mc1'],r['offer'],r['pvp'],r['pvpmin'],r['name'])
