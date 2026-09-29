# Estado del proyecto — Lume (tienda Shopify)

- Tienda: lume-es.myshopify.com (plan Basic, EUR, España)
- Carpeta: `tienda-lume/tema` (este repositorio es la copia de trabajo; Shopify guarda la copia buena)
- Tema base: Dawn 16.0.0 (clonado de GitHub el 29/09/2026)
- Tema de trabajo: **«Lume (Claude)»** — `gid://shopify/OnlineStoreTheme/202590814472` — NO publicado
- Tema viejo (versión cabello, error): «Lume (Claude) – versión cabello, BORRAR» — `202589864200` (el conector no deja borrarlo; borrar desde el panel)
- Tema publicado ahora mismo: «Horizon» (sin tocar)
- Vista previa: https://lume-es.myshopify.com/?preview_theme_id=202590814472
- Editor: https://admin.shopify.com/store/lume-es/themes/202590814472/editor
- Método de subida (sesión en la nube, sin Shopify CLI con login): ZIP → `stagedUploadsCreate` → `themeCreate`;
  cambios sueltos con `themeFilesUpsert` (solo en temas no publicados).
- Última subida: 29/09/2026 (tarde) — v2 corregida: nicho PIES (lima de pies) y logo real de Lume.

## Fases
- [x] 0 Entorno (nube: Node 22, Shopify CLI 4.8.2 solo para `theme check`)
- [x] 1 Conexión (conector de Shopify) — sondeo: 0 productos activos; 1 archivado («Recortador de Puntas Abiertas», handle `recortador-de-puntas-abiertas-lume`, no tocado)
- [x] 2 Proyecto
- [x] 3 Diseño (rama «sin producto»). ⚠️ Error de la v1: se dedujo «cabello» del doc «reset» del Drive; el usuario aclara que el producto que se valora es una **lima de pies**. Corregido en la v2.
- [x] 4 Construcción
- [x] 5 Páginas (faltan datos del titular para el aviso legal)
- [~] 6 Publicación — subido como tema NO publicado; falta revisión visual y OK para publicar

## Brief (v2)
- Producto en valoración: **lima de pies** (sin ficha todavía: modelo, precio y si es eléctrica, pendientes). Textos genéricos válidos para lima manual o eléctrica.
- Nicho de la tienda: cuidado de pies (durezas, talones, piel seca). Marca: «Lume — Pequeñas cosas que mejoran tu día».
- Logo REAL (el publicado por el usuario): punto ámbar `#905714` con anillo arena `#EAD8C0` + «Lume» en sans negrita `#161513` sobre `#F9F8F4`.
  Extraído a `assets/lume-logo.png` (oscuro) y `assets/lume-logo-claro.png` (para el pie oscuro); favicon = el punto.
- Paleta: fondo `#F9F8F4`, alterno `#F1EBE1`, blanco `#FFFFFF`, texto `#161513`, acento `#905714`, arena `#EAD8C0`.
- Tipografía: Inter 700 (títulos, interletraje ajustado, como el logo) + Inter 400 (texto), servidas por Shopify.
- Fotos: sin fotos todavía; huecos con fondo de marca y el punto del logo, editables.

## Secciones creadas (prefijo `lu-`)
| Archivo | Qué hace |
|---|---|
| `sections/lu-hero.liquid` | Apertura: titular grande, texto, 2 botones, 3 garantías, imagen con parallax y sello redondo |
| `sections/lu-marquesina.liquid` | Cinta de frases en movimiento infinito (velocidad editable) |
| `sections/lu-destacado.liquid` | Producto destacado con precio real, oferta, ventajas y «Añadir al carrito» (si vacío, usa el 1.er producto) |
| `sections/lu-beneficios.liquid` | Escena con imagen fija + beneficios con iconos |
| `sections/lu-pasos.liquid` | «Cómo funciona» en pasos numerados (ancla `#como-funciona`) |
| `sections/lu-comparador.liquid` | Antes/después con deslizador |
| `sections/lu-esenciales.liquid` | Rejilla de productos (colección o todos), 2.ª foto al pasar el ratón |
| `sections/lu-manifiesto.liquid` | Frase de marca + imagen panorámica opcional |
| `sections/lu-faq.liquid` | Preguntas frecuentes desplegables + datos estructurados para Google |
| `sections/lu-cta.liquid` | Llamada final oscura con luz animada |
| `sections/lu-producto.liquid` | Página de producto: galería con miniaturas, precio/tachado/% ahorro, variantes en píldoras, cantidad, carrito lateral de Dawn, pago rápido, garantías, descripción del catálogo, desplegables, características, «qué incluye», barra de compra fija |
| `sections/footer.liquid` | Pie propio (reescrito): marca, 2 columnas de enlaces, contacto, legales, iconos de pago |
| `sections/header.liquid` | Dawn + logo propio por sección (`lu_logo`, `lu_logo_width`); si no hay, usa `assets/lume-logo.png` |
| `snippets/lu-icono.liquid`, `lu-imagen.liquid`, `lu-hueco.liquid` | Iconos SVG, imagen con respaldo y hueco de marca |
| `assets/lu-styles.css`, `assets/lu-scripts.js` | Todo el CSS y JS propios |
| `assets/lume-logo.png`, `lume-logo-claro.png` | Logo real de Lume (header y pie) |
| `assets/lu-favicon.png`, `lu-favicon-180.png` | Favicon: el punto del logo (se usa si no hay favicon en la configuración del tema) |

## Plantillas
- `templates/index.json`: hero → cinta → destacado → beneficios → pasos → antes/después → productos → nuestra idea → FAQ → llamada final.
- `templates/product.json` (por defecto, para que los productos que suba AutoDS salgan ya con el diseño) y `templates/product.lu.json` (idéntica, sufijo `lu`).
- `templates/page.sobre.json` (página «Sobre Lume»), `templates/page.faq.json` (página «Preguntas frecuentes»).
- Truco de oferta por producto: etiqueta del producto `oferta: 2.ª unidad al 50 %` → sale en el recuadro de oferta de ese producto.

## Cambios en datos de la tienda (Admin API)
- Páginas creadas: `sobre-lume` (plantilla sobre), `preguntas-frecuentes` (plantilla faq), `politica-de-cookies` (publicada), `aviso-legal` (**oculta** hasta rellenar titular, NIF y email).
- Página `contact` renombrada a «Contacto».
- Menú principal en español: Inicio · Tienda · Sobre Lume · Preguntas frecuentes · Contacto.
- Textos de la tienda (carrito, botones…) en español de España dentro de `locales/en.default.json`, porque el idioma principal de la tienda es inglés.

## Pendiente
- ⬜ Revisión visual de la vista previa (desde la nube no se puede abrir la tienda: el dominio está bloqueado por la red).
- ⬜ Usuario: cambiar el idioma principal a español (Configuración → Idiomas) para que el pago y los emails salgan en español.
- ⬜ Usuario: rellenar titular, NIF y email en «Aviso legal» y publicarla.
- ⬜ Políticas de envío, devoluciones y términos (Configuración → Políticas; la de privacidad existe en inglés).
- ⬜ Ficha de la lima de pies (enlace AutoDS): título, descripción, fotos, precio, oferta; ajustar textos si es eléctrica.
- ⬜ Borrar el tema viejo «versión cabello, BORRAR» desde el panel.
- ⬜ Cuando se elijan los productos: subirlos (AutoDS), escribir título/descripción, fotos, etiqueta de oferta, crear el descuento real (2.ª al 50 % / 3x2), colección «Esenciales», fotos del hero, beneficios, antes/después.
- ⬜ Publicar el tema «Lume (Claude)» solo con el OK del usuario (el conector no permite publicar: se hace en Tienda online → Temas → Publicar).
