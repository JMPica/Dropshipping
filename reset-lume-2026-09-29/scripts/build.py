import json,os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=json.load(open(R+'/datos/D.json'))
for r in D: r.pop('img',None)
F=[["Productos explorados",2185],["En belleza y cuidado personal",1218],["Sin fórmulas ni riesgos legales",789],["Coste 5-30 $ y envío ≤ 12 días",438],["Top 50 con ventas",50]]
t=open(R+'/scripts/panel_template.html').read()
t=t.replace('__DATA__',json.dumps(D,ensure_ascii=False)).replace('__FUNNEL__',json.dumps(F,ensure_ascii=False))
open(R+'/radar-lume-belleza.html','w').write(t)
print(len(t))
