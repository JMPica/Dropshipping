"""Genera las plantillas JSON de la tienda Lume (EE. UU., «spa en casa»).

Uso: python3 plantillas.py  (desde tienda-lume/) → escribe en tema/templates y tema/sections.
"""
import json, os

T = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tema')
CUELLO = 'shopify://products/cordless-neck-shoulder-massager'
IMG = 'shopify://shop_images/'

FAQ = [
    ('How long does shipping take?',
     '<p>We process orders within 1–3 business days and email you a tracking number as soon as your order ships. Delivery within the contiguous US usually takes 7–12 business days.</p>'),
    ('Is shipping really free?',
     '<p>Yes. Standard tracked shipping is free on every order to the United States. No minimum.</p>'),
    ("What if it's not for me?",
     "<p>You're covered by our 30-day money-back guarantee. If you're not happy, contact us within 30 days of delivery and we'll help you return it for a refund. Items that arrive damaged or defective are replaced or refunded at no cost to you.</p>"),
    ('Are the massagers safe to use?',
     '<p>Our massagers are designed for relaxation and everyday comfort. They are not medical devices. If you are pregnant, have a pacemaker, a medical condition or recent injury, please ask your doctor before using them. Start on the lowest setting and never use them on broken or irritated skin.</p>'),
    ('How do I charge them?',
     '<p>Every massager is rechargeable and comes with a USB charging cable. Plug it into any USB wall adapter or laptop. Charge fully before first use.</p>'),
    ('Which payment methods do you accept?',
     '<p>All major credit and debit cards and the express options you see at checkout. Payments are processed securely and we never see or store your card details.</p>'),
]


def faq_bloques():
    blocks, order = {}, []
    for i, (q, a) in enumerate(FAQ, 1):
        k = f'pregunta-{i}'
        blocks[k] = {'type': 'pregunta', 'settings': {'pregunta': q, 'respuesta': a}}
        order.append(k)
    return blocks, order


fb, fo = faq_bloques()

index = {
    'sections': {
        'hero': {'type': 'lu-hero', 'settings': {
            'eyebrow': 'At-home spa rituals',
            'titulo': 'Ten minutes that feel like <em>an hour at the spa</em>.',
            'texto': 'Cordless massagers and self-care tools that turn any evening into a reset. No appointments, no waiting, no cords.',
            'boton_1': 'Shop the massager', 'boton_1_url': CUELLO,
            'boton_2': 'Explore the collection', 'boton_2_url': 'shopify://collections/all',
            'garantia_1': 'Free US shipping', 'garantia_1_icono': 'envio',
            'garantia_2': '30-day guarantee', 'garantia_2_icono': 'devolucion',
            'garantia_3': 'Secure checkout', 'garantia_3_icono': 'seguro',
            'imagen': IMG + '4d80b542f94b7ed0927c57192f48fe90.jpg',
            'sello_grande': '10 min', 'sello_texto': 'a day',
        }},
        'cinta': {'type': 'lu-marquesina', 'blocks': {
            f'frase-{i}': {'type': 'frase', 'settings': {'texto': t}} for i, t in enumerate([
                'Free US shipping', 'Cordless & rechargeable', '30-day money-back guarantee',
                'Your ten-minute reset', 'Secure checkout'], 1)},
            'block_order': [f'frase-{i}' for i in range(1, 6)], 'settings': {'etiqueta': 'Lume perks'}},
        'destacado': {'type': 'lu-destacado', 'settings': {
            'producto': 'cordless-neck-shoulder-massager',
            'eyebrow': 'The Lume favorite', 'oferta': '',
            'texto': 'Two sets of 3D kneading heads grip, knead and release the knots between your neck and shoulders, the way a pair of hands would. Cordless, rechargeable and ready whenever you need ten minutes for yourself.',
            'puntos': 'Hand-like kneading, not just vibration\nCordless: sofa, desk or passenger seat\nWear it hands-free with the clip-on straps\nAuto-off after every 10-minute session',
            'boton_comprar': 'Add to cart', 'boton_ver': 'View details',
        }},
        'beneficios': {'type': 'lu-beneficios', 'blocks': {
            'beneficio-1': {'type': 'beneficio', 'settings': {'icono': 'reloj', 'titulo': 'Ten minutes is enough',
                                                              'texto': 'Short, easy rituals that fit into a busy evening.'}},
            'beneficio-2': {'type': 'beneficio', 'settings': {'icono': 'casa', 'titulo': 'Spa feeling at home',
                                                              'texto': 'No appointments, no commute, no tipping. Just you and your sofa.'}},
            'beneficio-3': {'type': 'beneficio', 'settings': {'icono': 'mano', 'titulo': 'Made to be easy',
                                                              'texto': 'One button, cordless, rechargeable. Nothing to learn.'}},
            'beneficio-4': {'type': 'beneficio', 'settings': {'icono': 'escudo', 'titulo': 'Shop with confidence',
                                                              'texto': 'Free tracked shipping and a 30-day money-back guarantee.'}},
        }, 'block_order': ['beneficio-1', 'beneficio-2', 'beneficio-3', 'beneficio-4'], 'settings': {
            'eyebrow': 'Why Lume', 'titulo': 'Self-care you will <em>actually use</em>.',
            'imagen': IMG + 'cef270bdd35fc0840f5ef04d86ae4731.jpg'}},
        'pasos': {'type': 'lu-pasos', 'blocks': {
            'paso-1': {'type': 'paso', 'settings': {'titulo': 'Charge it', 'texto': 'Plug in the USB cable. One full charge covers about a week of evening sessions.'}},
            'paso-2': {'type': 'paso', 'settings': {'titulo': 'Drape it on', 'texto': 'Rest it on your shoulders and hold the straps, or clip them behind your back to go hands-free.'}},
            'paso-3': {'type': 'paso', 'settings': {'titulo': 'Switch off for 10 minutes', 'texto': 'Pick the mode and intensity, then let it knead. It turns itself off when the session ends.'}},
        }, 'block_order': ['paso-1', 'paso-2', 'paso-3'], 'settings': {
            'eyebrow': 'How it works', 'titulo': 'Three steps. <em>Zero effort.</em>', 'color_fondo': '#F1EBE1'}},
        'esenciales': {'type': 'lu-esenciales', 'settings': {
            'eyebrow': 'The ritual collection', 'titulo': 'Everything for your <em>at-home spa</em>',
            'texto': 'A few tools, carefully chosen. Each one earns its place in your evening routine.',
            'color_fondo': '#FFFFFF'}},
        'manifiesto': {'type': 'lu-manifiesto', 'settings': {
            'eyebrow': 'Our idea',
            'titulo': 'We believe the best self-care is the one you <em>actually do</em>: a few minutes, at home, with tools that work.',
            'firma': '— The Lume team', 'mostrar_imagen': False, 'color_fondo': '#F9F8F4'}},
        'faq': {'type': 'lu-faq', 'blocks': fb, 'block_order': fo, 'settings': {'boton_url': 'shopify://pages/contact'}},
        'cta': {'type': 'lu-cta', 'settings': {}},
    },
    'order': ['hero', 'cinta', 'destacado', 'beneficios', 'pasos', 'esenciales', 'manifiesto', 'faq', 'cta'],
}

producto = {
    'sections': {
        'principal': {'type': 'lu-producto', 'blocks': {
            'acordeon-1': {'type': 'acordeon', 'settings': {'titulo': 'Shipping', 'contenido':
                '<p>Free tracked shipping on every US order. We process orders within 1–3 business days; delivery usually takes 7–12 business days. You will get a tracking number by email.</p>'}},
            'acordeon-2': {'type': 'acordeon', 'settings': {'titulo': '30-day money-back guarantee', 'contenido':
                "<p>Not in love with it? Contact us within 30 days of delivery and we'll help you return it for a refund. Damaged or defective items are replaced or refunded at no cost to you.</p>"}},
            'acordeon-3': {'type': 'acordeon', 'settings': {'titulo': 'Safety', 'contenido':
                '<p>Designed for relaxation, not a medical device. If you are pregnant, have a pacemaker, a medical condition or a recent injury, ask your doctor before use. Start on the lowest setting and never use on broken or irritated skin.</p>'}},
            'caracteristica-4': {'type': 'caracteristica', 'settings': {'icono': 'reloj', 'titulo': 'Minutes, not hours',
                                                                        'texto': 'A short ritual that fits into any evening.'}},
            'caracteristica-5': {'type': 'caracteristica', 'settings': {'icono': 'casa', 'titulo': 'Spa feeling at home',
                                                                        'texto': 'No appointments, no waiting, no commute.'}},
            'caracteristica-6': {'type': 'caracteristica', 'settings': {'icono': 'escudo', 'titulo': 'Risk-free',
                                                                        'texto': 'Free US shipping and a 30-day money-back guarantee.'}},
        }, 'block_order': ['acordeon-1', 'acordeon-2', 'acordeon-3', 'caracteristica-4', 'caracteristica-5', 'caracteristica-6'],
            'settings': {'eyebrow': 'Lume · At-home spa', 'texto_impuestos': 'Taxes calculated at checkout.'}},
        'rutina': {'type': 'lu-esenciales', 'settings': {
            'eyebrow': 'Complete your ritual', 'titulo': 'You may also <em>like</em>', 'texto': '',
            'color_fondo': '#FFFFFF', 'padding_top': 88, 'padding_bottom': 88}},
        'faq': {'type': 'lu-faq', 'blocks': fb, 'block_order': fo, 'settings': {'boton_url': 'shopify://pages/contact'}},
    },
    'order': ['principal', 'rutina', 'faq'],
}

sobre = {
    'sections': {
        'hero': {'type': 'lu-hero', 'settings': {
            'eyebrow': 'About Lume', 'titulo': 'Small rituals that <em>change your evenings</em>',
            'texto': 'Lume started with a simple idea: the spa feeling should not require an appointment. We test at-home massage and self-care tools and only keep the ones that are easy, effective and a pleasure to use.',
            'boton_1': 'Shop the collection', 'boton_1_url': 'shopify://collections/all', 'boton_2': '',
            'imagen': IMG + '4d80b542f94b7ed0927c57192f48fe90.jpg',
            'sello_grande': '', 'sello_texto': '', 'heading_size': 64}},
        'manifiesto': {'type': 'lu-manifiesto', 'settings': {
            'eyebrow': 'What we care about',
            'titulo': 'Fewer things, <em>better chosen</em>. Every Lume product has to earn a place in your evening routine.',
            'firma': '— The Lume team', 'mostrar_imagen': False, 'color_fondo': '#FFFFFF'}},
        'beneficios': {'type': 'lu-beneficios', 'blocks': index['sections']['beneficios']['blocks'],
                       'block_order': index['sections']['beneficios']['block_order'], 'settings': {
            'eyebrow': 'Our promise', 'titulo': 'How we <em>work</em>', 'imagen_derecha': True,
            'imagen': IMG + 'cef270bdd35fc0840f5ef04d86ae4731.jpg'}},
        'cta': {'type': 'lu-cta', 'settings': {'padding_top': 0}},
    },
    'order': ['hero', 'manifiesto', 'beneficios', 'cta'],
}

faq_page = {
    'sections': {
        'faq': {'type': 'lu-faq', 'blocks': fb, 'block_order': fo,
                'settings': {'boton_url': 'shopify://pages/contact', 'padding_top': 72}},
        'cta': {'type': 'lu-cta', 'settings': {'padding_top': 0}},
    },
    'order': ['faq', 'cta'],
}

from traducir_defaults import EN


def rellenar(plantilla):
    """Pone en inglés todo texto de sección que la plantilla no fije (los defaults del schema están en español)."""
    for sec in plantilla['sections'].values():
        tr = EN.get(sec['type'], {})
        st = sec.setdefault('settings', {})
        for k, v in tr.items():
            if '.' not in k and k not in st:
                st[k] = v
        for b in sec.get('blocks', {}).values():
            for k, v in tr.items():
                if k.startswith(b['type'] + '.') and k.split('.', 1)[1] not in b.setdefault('settings', {}):
                    b['settings'][k.split('.', 1)[1]] = v
    return plantilla


def escribir(ruta, datos):
    with open(os.path.join(T, ruta), 'w') as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    print('escrito', ruta)


escribir('templates/index.json', rellenar(index))
escribir('templates/product.lu.json', rellenar(producto))
escribir('templates/product.json', rellenar(producto))
escribir('templates/page.sobre.json', rellenar(sobre))
escribir('templates/page.faq.json', rellenar(faq_page))

# Cabecera y pie (grupos de secciones)
import re


def cargar(ruta):
    s = open(os.path.join(T, ruta)).read()
    return json.loads(re.sub(r'^/\*.*?\*/', '', s, flags=re.S))


h = cargar('sections/header-group.json')
h['sections']['announcement-bar']['blocks']['announcement-bar-0']['settings']['text'] = \
    'Free tracked shipping across the US · 30-day money-back guarantee'
escribir('sections/header-group.json', h)

f = cargar('sections/footer-group.json')
f['sections']['footer']['settings'] = {
    'col1_url_1': 'shopify://collections/all',
    'col1_enlace_2': 'FAQ', 'col1_url_2': 'shopify://pages/faq',
    'col1_enlace_3': 'About Lume', 'col1_url_3': 'shopify://pages/about-lume',
    'col2_url_1': 'shopify://pages/contact',
    'col2_url_2': 'shopify://policies/shipping-policy',
    'col2_url_3': 'shopify://policies/refund-policy',
    'col2_enlace_4': '',
    'email': '',
    'aviso_legal_texto': '',
    'cookies_texto': '',
}
escribir('sections/footer-group.json', rellenar(f))
