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

## Pendiente
- Publicar el tema «Lume (Claude)» y quitar la contraseña cuando se quiera vender.
- Pegar `politicas/*.html` en Configuración → Políticas (el conector no tiene permiso `write_legal_policies`).
- Fotos: las del proveedor llevan textos; sustituir por fotos de ambiente (IA o propias).
- Pedido de prueba para confirmar costes reales, aranceles y plazos.
- Suscripción de AutoDS (la prueba acaba el 1 oct 2026) para los pedidos automáticos.
