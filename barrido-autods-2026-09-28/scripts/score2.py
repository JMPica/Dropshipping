import json,math,csv,sys
S='/tmp/claude-0/-home-user-Dropshipping/edd3f668-73f0-5b21-9c24-f699ed49a66a/scratchpad'
FX=0.90
base={x['id']:x for x in json.load(open(S+'/s1.json'))}
fb=set(open(S+'/ads_fb.txt').read().split())
over={}
try: over=json.load(open(S+'/override.json'))   # envío/coste reales (CJ) cuando existan
except: pass
def mc(P,L): return P/1.21-L-(0.021*P+0.30)-0.09*P
rows=[]
for r in csv.DictReader(open(S+'/judg.tsv'),delimiter='|'):
    if r['nicho']=='Descartar': continue
    b=base[r['id']]; PV=float(r['PV'])
    c=b['c']; s=b['s']; days=b['days']; srcship='AutoDS (EE. UU.)'
    if r['id'] in over:
        o=over[r['id']]; c=o.get('c',c); s=o.get('s',s); days=o.get('days',days); srcship=o.get('src','CJ')
    L=(c+s)*FX
    offers=[('1+1',PV,2),('2.ª al 50 %',round(PV*1.5,2),2)]
    if r['multi']=='1': offers.append(('3x2',round(PV*2,2),3))
    best=max(offers,key=lambda o:mc(o[1],o[2]*L))
    MC=mc(best[1],best[2]*L)
    mult=PV/L
    # puntuación
    m=max(0,min(1,(MC-15)/35))*25
    orders=b['orders'] or 1
    val=min(12,math.log10(orders)/4*12)+ (b['eng'] or 0)/100*6 + (2 if r['id'] in fb else 0)
    val=min(20,val)
    sat=b['sat'] or 40
    satb=3 if sat<=20 else 2 if sat<=40 else 1 if sat<=60 else 0
    score=m+int(r['prob'])+val+int(r['crea'])+min(10,int(r['satj'])+satb)+int(r['size'])
    rows.append(dict(id=r['id'],es=r['es'],nicho=r['nicho'],score=round(score,1),m=round(m,1),prob=int(r['prob']),val=round(val,1),crea=int(r['crea']),sat=min(10,int(r['satj'])+satb),size=int(r['size']),
        c=c,s=s,L=round(L,2),days=days,srcship=srcship,PV=PV,offer=best[0],AOV=best[1],u=best[2],MC=round(MC,2),mult=round(mult,2),
        ok=(MC>=35 and mult>=3),orders=b['orders'],eng=b['eng'],comp=b['comp'],satA=b['sat'],fb=r['id'] in fb,riesgo=r['riesgo'],gancho=r['gancho'],t=b['t']))
rows.sort(key=lambda x:-x['score'])
json.dump(rows,open(S+'/s2.json','w'),ensure_ascii=False)
for i,x in enumerate(rows,1):
    print(f"{i:2} {x['score']:5} {'OK' if x['ok'] else '--'} MC={x['MC']:6} x{x['mult']:5} {x['offer']:11} AOV={x['AOV']:6} L={x['L']:5} {x['nicho'][:18]:18} {x['es'][:40]}")
