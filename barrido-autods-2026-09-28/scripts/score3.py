import json,math,csv
S='/tmp/claude-0/-home-user-Dropshipping/edd3f668-73f0-5b21-9c24-f699ed49a66a/scratchpad'
exec(open(S+'/weights.py').read())
FX=0.90
base={x['id']:x for x in json.load(open(S+'/s1.json'))}
fb=set(open(S+'/ads_fb.txt').read().split())
cj={}
for r in csv.DictReader(open(S+'/cj.tsv'),delimiter='|'): cj[r['autods_id']]=r
def ship(g): return 7.03+0.01223*g          # USD, CJPacket Fast Ordinary CN→ES 4-9 días (tasas incl.)
def mc(P,L): return P/1.21-L-(0.021*P+0.30)-0.09*P
rows=[]
for r in csv.DictReader(open(S+'/judg.tsv'),delimiter='|'):
    if r['nicho']=='Descartar': continue
    i=r['id']; b=base[i]; PV=float(r['PV']); w=W[i]; c=C.get(i,b['c'])
    sh1=ship(w) if i!='68fbb9bded8668000107ce8d' else 86.76
    L1=(c+sh1)*FX
    def land(u): return (u*c+(ship(u*w) if i!='68fbb9bded8668000107ce8d' else 86.76*u))*FX
    offers=[('1+1',PV,2),('2.ª ud. al 50 %',round(PV*1.5,2),2)]
    if r['multi']=='1': offers.append(('3x2',round(PV*2,2),3))
    best=max(offers,key=lambda o:mc(o[1],land(o[2])))
    MCo=mc(best[1],land(best[2])); MC1=mc(PV,L1); MCmix=0.6*MC1+0.4*MCo
    mult=PV/L1
    m=max(0,min(1,(MCo-15)/35))*25
    orders=b['orders'] or 1
    val=min(20,min(12,math.log10(orders)/4*12)+(b['eng'] or 0)/100*6+(2 if i in fb else 0))
    sat=b['sat'] or 40; satb=3 if sat<=20 else 2 if sat<=40 else 1 if sat<=60 else 0
    score=m+int(r['prob'])+val+int(r['crea'])+min(10,int(r['satj'])+satb)+int(r['size'])
    ok=MCo>=35 and mult>=3
    rows.append(dict(id=i,es=r['es'],nicho=r['nicho'],score=round(score,1),m=round(m,1),prob=int(r['prob']),val=round(val,1),crea=int(r['crea']),sat=min(10,int(r['satj'])+satb),size=int(r['size']),
      c=c,w=w,ship1=round(sh1*FX,2),L1=round(L1,2),PV=PV,offer=best[0],AOV=best[1],u=best[2],Lo=round(land(best[2]),2),MCo=round(MCo,2),MC1=round(MC1,2),MCmix=round(MCmix,2),mult=round(mult,2),ok=ok,
      orders=b['orders'],eng=b['eng'],comp=b['comp'],satA=b['sat'],fb=i in fb,riesgo=r['riesgo'],gancho=r['gancho'],t=b['t'],cj=cj.get(i)))
rows.sort(key=lambda x:-x['score'])
json.dump(rows,open(S+'/s3.json','w'),ensure_ascii=False)
for k,x in enumerate(rows,1):
    print(f"{k:2} {x['score']:5} {'OK' if x['ok'] else '--'} MCo={x['MCo']:6} MC1={x['MC1']:6} x{x['mult']:4} {x['offer'][:9]:9} AOV={x['AOV']:6} Lo={x['Lo']:5} {x['nicho'][:16]:16} {x['es'][:38]}")
