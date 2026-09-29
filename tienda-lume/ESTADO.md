# Estado del proyecto — Lume (tienda Shopify)

- Tienda: lume-es.myshopify.com (plan Basic, EUR, España)
- Carpeta: `tienda-lume/tema` (este repositorio es la copia de trabajo; Shopify guarda la copia buena)
- Tema base: Dawn 16.0.0 (clonado de GitHub el 29/09/2026)
- Tema de trabajo: **«Lume (Claude)»** — `gid://shopify/OnlineStoreTheme/202589864200` — NO publicado
- Tema publicado ahora mismo: «Horizon» (sin tocar)
- Vista previa: https://lume-es.myshopify.com/?preview_theme_id=202589864200
- Editor: https://admin.shopify.com/store/lume-es/themes/202589864200/editor
- Método de subida (sesión en la nube, sin Shopify CLI con login): ZIP → `stagedUploadsCreate` → `themeCreate`;
  cambios sueltos con `themeFilesUpsert` (solo en temas no publicados).
- Última subida: 29/09/2026 — tema completo + `config/settings_data.json` corregido (page_width 1200).

## Fases
- [x] 0 Entorno (nube: Node 22, Shopify CLI 4.8.2 solo para `theme check`)
- [x] 1 Conexión (conector de Shopify) — sondeo: 0 productos activos; 1 archivado («Recortador de Puntas Abiertas», handle `recortador-de-puntas-abiertas-lume`, no tocado)
- [x] 2 Proyecto
- [x] 3 Diseño (rama «sin producto»: brief deducido de los documentos de Lume del Drive)
- [x] 4 Construcción
- [x] 5 Páginas (faltan datos del titular para el aviso legal)
- [~] 6 Publicación — subido como tema NO publicado; falta revisión visual y OK para publicar

## Brief
- Nicho (doc «Lume — reset», 29/09): cuidado del cabello SIN fórmulas (herramientas). Test de 3 productos: recortador de puntas abiertas, cepillo térmico rizador 32 mm, rizador sin calor (2 uds).
- Marca: «Lume — Pequeñas cosas que mejoran tu día». Logo = «L» mayúscula. Tono cálido y cercano, tú, español de España.
- Paleta: crema `#F6EFE7` (fondo), arena `#ECDFCF`, blanco roto `#FFFCF8`, cacao `#2A1F1A` (texto/botones), ámbar `#C4702C` (acento), miel `#E9B87C`.
- Tipografía: Playfair Display (títulos, cursiva ámbar para resaltar) + DM Sans (texto). Servidas por Shopify (sin Google Fonts → sin problema RGPD).
- Forma: botones píldora, esquinas 18-28 px, sombras suaves, reveals al hacer scroll, parallax suave, cinta animada.
- Fotos: no hay fotos todavía (CDN de Shopify bloqueado desde la nube y sin clave de imágenes). Todos los huecos llevan un fondo de marca con la «L» y son `image_picker` editables.

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
| `sections/header.liquid` | Dawn + logo propio por sección (`lu_logo`, `lu_logo_width`) y nombre de marca en Playfair con punto ámbar si no hay logo |
| `snippets/lu-icono.liquid`, `lu-imagen.liquid`, `lu-hueco.liquid` | Iconos SVG, imagen con respaldo y hueco de marca |
| `assets/lu-styles.css`, `assets/lu-scripts.js` | Todo el CSS y JS propios |
| `assets/lu-favicon.png`, `lu-favicon-180.png` | Favicon «L.» (se usa si no hay favicon en la configuración del tema) |

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
- ⬜ Cuando se elijan los 3 productos: subirlos (AutoDS), escribir título/descripción, fotos, etiqueta de oferta, crear el descuento real (2.ª al 50 % / 3x2), colección «Esenciales», fotos del hero, beneficios, antes/después.
- ⬜ Publicar el tema «Lume (Claude)» solo con el OK del usuario (el conector no permite publicar: se hace en Tienda online → Temas → Publicar).
