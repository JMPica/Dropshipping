"""Traduce al inglés (EE. UU.) los textos por defecto de las secciones Lume.

Solo cambia los "default" de los ajustes de texto del schema: las etiquetas del
editor siguen en español para que la tienda se pueda editar cómodamente.
Uso: python3 traducir_defaults.py  (desde tienda-lume/). plantillas.py importa EN para
rellenar en las plantillas los textos que no se fijan a mano.
"""
import json, re, os

T = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tema')

EN = {
    'lu-beneficios': {
        'eyebrow': 'Why Lume',
        'titulo': 'Real relief rituals. <em>No appointments.</em>',
        'beneficio.titulo': 'Benefit',
        'beneficio.texto': 'Describe the benefit in one or two sentences.',
    },
    'lu-comparador': {
        'etiqueta_antes': 'Before', 'etiqueta_despues': 'After',
        'etiqueta_control': 'Drag to compare before and after',
        'eyebrow': 'See the difference', 'titulo': 'Slide and <em>see for yourself</em>',
        'texto': 'Move the line to compare.', 'boton': 'I want it',
    },
    'lu-cta': {
        'eyebrow': 'Your moment',
        'titulo': 'Your daily spa is <em>one click away</em>',
        'texto': 'Free tracked shipping across the US and a 30-day money-back guarantee. Zero risk.',
        'boton': 'Shop the collection',
    },
    'lu-destacado': {
        'eyebrow': 'The Lume favorite',
        'oferta': '',
        'texto': 'Deep, hand-like kneading for tight neck and shoulders. Cordless, rechargeable and ready whenever you need ten minutes for yourself.',
        'puntos': 'Kneads like a pair of hands\nCordless and rechargeable\nWear it hands-free at your desk or on the sofa',
        'boton_comprar': 'Add to cart', 'boton_ver': 'View details',
    },
    'lu-esenciales': {
        'eyebrow': 'The ritual collection',
        'titulo': 'Everything for your <em>at-home spa</em>',
        'texto': 'A few tools, carefully chosen. Each one earns its place in your evening routine.',
        'enlace_texto': 'Shop all', 'texto_oferta': 'Sale', 'texto_agotado': 'Sold out',
        'texto_desde': 'From', 'texto_proximamente': 'Coming soon',
    },
    'lu-faq': {
        'eyebrow': 'Questions', 'titulo': 'Frequently asked <em>questions</em>',
        'texto': "Can't find your answer? Email us and we'll reply within one business day.",
        'boton': 'Contact us', 'pregunta.pregunta': 'Question?', 'pregunta.respuesta': '<p>Answer.</p>',
    },
    'lu-hero': {
        'eyebrow': 'At-home spa rituals',
        'titulo': 'Ten minutes that feel like <em>an hour at the spa</em>.',
        'texto': 'Cordless massagers and self-care tools that turn any evening into a reset. No appointments, no waiting.',
        'boton_1': 'Shop now', 'boton_2': 'How it works',
        'garantia_1': 'Free US shipping', 'garantia_2': '30-day guarantee', 'garantia_3': 'Secure checkout',
        'sello_grande': '10 min', 'sello_texto': 'a day',
    },
    'lu-manifiesto': {
        'eyebrow': 'Our idea',
        'titulo': 'We believe the best self-care is the one you <em>actually do</em>: a few minutes, at home, with tools that work.',
        'firma': '— The Lume team',
    },
    'lu-marquesina': {'etiqueta': 'Lume perks', 'frase.texto': 'Free US shipping'},
    'lu-pasos': {
        'eyebrow': 'How it works', 'titulo': 'Three steps. <em>Zero effort.</em>',
        'paso.titulo': 'Step', 'paso.texto': 'Explain this step in one or two sentences.',
    },
    'lu-producto': {
        'texto_ver_foto': 'View photo', 'eyebrow': 'Lume · At-home spa',
        'texto_ahorro': 'You save [pct]%', 'texto_impuestos': 'Taxes calculated at checkout.',
        'boton_texto': 'Add to cart', 'texto_agotado': 'Sold out', 'texto_no_disponible': 'Unavailable',
        'texto_cantidad': 'Quantity', 'texto_menos': 'Remove one', 'texto_mas': 'Add one',
        'confianza_1': 'Free tracked US shipping', 'confianza_2': '30-day money-back guarantee',
        'confianza_3': 'Secure checkout',
        'titulo_descripcion': 'Description', 'caracteristicas_eyebrow': 'Made for your ritual',
        'caracteristicas_titulo': "Why you'll <em>love it</em>",
        'incluye_eyebrow': 'In the box', 'incluye_titulo': "What's <em>included</em>",
        'acordeon.titulo': 'Shipping', 'acordeon.contenido': '<p>Write the content here.</p>',
        'caracteristica.titulo': 'Feature', 'caracteristica.texto': 'Explain the feature in one or two sentences.',
    },
    'footer': {
        'tagline': 'Your daily spa, at home.',
        'col1_titulo': 'Shop', 'col1_enlace_1': 'All products', 'col1_enlace_2': 'FAQ', 'col1_enlace_3': 'About Lume',
        'col2_titulo': 'Help', 'col2_enlace_1': 'Contact', 'col2_enlace_2': 'Shipping', 'col2_enlace_3': 'Returns',
        'col2_enlace_4': 'FAQ',
        'col3_titulo': "Let's talk", 'col3_texto': 'Questions about your order? We reply within one business day.',
        'copyright': 'All rights reserved.', 'texto_privacidad': 'Privacy', 'texto_terminos': 'Terms of service',
        'texto_devoluciones': 'Returns', 'texto_envios': 'Shipping', 'aviso_legal_texto': 'Legal notice',
        'cookies_texto': 'Cookies',
    },
}

if __name__ == '__main__':
    for name, tr in EN.items():
        path = os.path.join(T, 'sections', name + '.liquid')
        s = open(path).read()
        m = re.search(r'(\{%-?\s*schema\s*-?%\})(.*?)(\{%-?\s*endschema\s*-?%\})', s, re.S)
        j = json.loads(m.group(2))
        usados = set()

        def poner(ajustes, pref=''):
            for x in ajustes:
                k = pref + x.get('id', '')
                if k in tr:
                    if tr[k] == '':
                        x.pop('default', None)
                    else:
                        x['default'] = tr[k]
                    usados.add(k)

        poner(j.get('settings', []))
        for b in j.get('blocks', []):
            poner(b.get('settings', []), b['type'] + '.')
        # Los presets también llevan textos de ejemplo en bloques
        for p in j.get('presets', []):
            for b in p.get('blocks', []) if isinstance(p.get('blocks'), list) else []:
                for k, v in list(b.get('settings', {}).items()):
                    clave = b['type'] + '.' + k
                    if clave in tr and tr[clave]:
                        b['settings'][k] = tr[clave]
        faltan = set(tr) - usados
        assert not faltan, (name, faltan)
        nuevo = s[:m.start(2)] + '\n' + json.dumps(j, ensure_ascii=False, indent=2) + '\n' + s[m.end(2):]
        nuevo = nuevo.replace('aria-label="Métodos de pago"', 'aria-label="Payment methods"')
        nuevo = nuevo.replace('Tu producto estrella', 'Our star product')
        open(path, 'w').write(nuevo)
        print('ok', name, len(usados))
