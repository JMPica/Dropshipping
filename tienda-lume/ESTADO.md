# Estado del proyecto — Lume (EE. UU., «spa en casa»)

- Tienda: lume-es.myshopify.com (dominio interno wsyxgf-w3.myshopify.com) · plan Basic · moneda base EUR
- Mercado: Estados Unidos (principal, USD) con lista de precios fija «Lume US (USD)»; España desactivada
- Tema de trabajo: **«Lume (Claude)»** (id 202590814472, NO publicado). Tema activo: Horizon.
  Vista previa: https://lume-es.myshopify.com/?preview_theme_id=202590814472
- Carpeta: `tienda-lume/` (tema descargado en `tema/`, textos en `plantillas.py`, fichas en `productos.json`,
  políticas en `politicas/`)
- Última subida: 30 sept 2026 (plantillas, cabecera y pie; las secciones `lu-*` no se han tocado)

## Fases completadas
- [x] 1 Conexión (MCP de Shopify y AutoDS; sin Shopify CLI en la nube)
- [x] 3 Brief: spa en casa, inglés, EE. UU. (a partir de `barrido-autods-2026-09-28/usa/D_bel.json`)
- [x] 4 Construcción (reutiliza las secciones `lu-*` del tema anterior)
- [x] 5 Productos, páginas, menú, pie, políticas (como páginas)
- [ ] 6 Publicar el tema: lo hace el usuario (el conector no permite publicar temas)

## Productos (importados con AutoDS, tienda AutoDS 5803029)

| Producto | Handle | Precio US | Coste AutoDS aprox. | Almacén |
|---|---|---|---|---|
| Cordless Neck & Shoulder Massager (Classic 20W ×3 colores / Pro 26W ×2) | cordless-neck-shoulder-massager | 89,99 $ / 109,99 $ | 39,68–40,97 € / 46,08–48,01 € | US |
| Heated Knee Massager | heated-knee-massager | 89,99 $ | 31,31 € | US |
| Heated Smart Cupping Massager | heated-cupping-massager | 49,99 $ | ≈16,9 € | US |
| Reusable Silicone Smoothing Patches (2 sets) | silicone-smoothing-patches | 29,99 $ | 4,78–4,90 € | CN/ALL |

- Todos con plantilla `product.lu`, vendor Lume, tag `lume-spa`, sin precio «antes» (compare-at).
- El masajeador facial de microcorriente no se pudo importar (AutoDS: «Product unavailable» en 3 fichas).
- Queda un borrador sin publicar en AutoDS: «Lume Cordless Neck & Shoulder Massager (CN)» (se puede borrar).
- Envío: perfil «AutoDS Free Shipping» con zona **United States** gratis (creada el 30 sept).

## Decisiones de diseño
- Paleta crema/cacao/ámbar del tema anterior (encaja con spa). Tipografía Inter.
- Portada: hero (foto del masajeador) → cinta → producto destacado (cuello) → beneficios → 3 pasos →
  colección → manifiesto → FAQ → llamada final.
- Textos sin alegaciones médicas; aviso «not a medical device» en fichas, FAQ y condiciones.
- Garantía de 30 días (devolución a cargo del cliente salvo defecto); envío 7–12 días hábiles.

## Fotos (30 sept, Higgsfield · Nano Banana, 12 créditos)
6 fotos de ambiente generadas a partir de las fotos del proveedor (copias ligeras en `fotos-ia/`), subidas a
Archivos de Shopify y colocadas como primeras fotos de cada producto:
- `lume-neck-massager-still-life.png` y `lume-neck-massager-sofa.png` → masajeador de cuello (la del sofá también en el hero
  de la portada y de «About»)
- `lume-knee-massager-armchair.png` → rodilla (y bloque «Why Lume» de la portada)
- `lume-cupping-massager-spa.png` → ventosas
- `lume-silicone-patches-tray.png` y `lume-silicone-patches-bedtime.png` → parches (la de la bandeja también en «About»)

## Meta (30 sept)
- Página «Lume» pasada a EE. UU.: presentación, 2 publicaciones en inglés, portada caja kraft sin texto,
  campaña de calentamiento de España eliminada. Archivos y textos en `meta/`.
- App «Facebook & Instagram» conectada: portfolio Lume, catálogo nuevo, «Lume's Pixel», datos «Enhanced» (píxel + CAPI).
  Los 4 productos publicados en el canal Facebook & Instagram (30 sept).

## Pendiente
- TikTok: crear la cuenta más adelante (el usuario lo deja para cuando la tienda esté en marcha en EE. UU.);
  luego app «TikTok» de Shopify para el píxel. El orgánico publicado desde España apenas llega a EE. UU.: vender con anuncios.
- Hecho (30 sept): tema «Lume (Claude)» publicado, contraseña quitada, políticas pegadas en Configuración → Políticas,
  devoluciones por defecto a 30 días, correo de atención lume.support.us@gmail.com (tienda, remitente, políticas).
  Páginas antiguas «aviso-legal» y «politica-de-cookies» (España, con NIF y domicilio) ocultadas, no borradas.
- Suscripción de AutoDS: el usuario paga un mes.
- Pedido de prueba para confirmar costes reales, aranceles y plazos.
