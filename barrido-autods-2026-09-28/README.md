# Barrido AutoDS — Lume (28 sept 2026)

Resultado completo: Google Doc «Lume — resultado barrido AutoDS (28 sept 2026)» en el Drive del proyecto
(copia local: `informe.html`).

## Qué hay aquí

| Archivo | Contenido |
|---|---|
| `datos/candidatos_filtrados.json` | 1.770 candidatos (1.420 ganadores AutoDS + 350 de búsqueda por categoría) con coste, envío AutoDS (a EE. UU.), pedidos, engagement, margen previo y motivo de exclusión del filtro duro. |
| `datos/juicio_manual.tsv` | Puntuación manual de 65 finalistas: nicho, problema/WOW, creativo POV, saturación España, tamaño, PVP creíble, riesgo legal/Meta y gancho. |
| `datos/finalistas_puntuados.json` | Finalistas con nota 0-100, MC por pedido (envío CJ verificado y escenario AliExpress) y oferta. |
| `datos/contraste_cj.tsv` | Contraste de los 20 mejores en CJ Dropshipping. |
| `datos/tarifas_envio_cj.tsv` | Tarifas CJ CN→ES verificadas (`calculate_freight_tip`). |
| `datos/ids_con_anuncios_fb.txt` | IDs de AutoDS que salen con el filtro «anuncios en Facebook». |
| `scripts/` | Scripts usados (rutas absolutas del contenedor de la sesión; ajustar `S=` para reutilizarlos). |

## Fórmula y supuestos

- MC = PVP/1,21 − coste − envío − (2,1 % PVP + 0,30 €) − 9 % PVP. 1 $ = 0,90 €.
- Envío ≤ 10 días a España (CJPacket Fast Ordinary, arancel incluido): 7,03 $ + 0,0122 $/g por paquete.
- Escenario AliExpress (sin verificar): 5 $ por paquete (~1,5 € de envío + 3 € de arancel).

## Conclusión

Ningún producto cumple MC ≥ 35 € con precios creíbles y envío real a España. Nicho recomendado con
reservas: «Regalos» (collar de proyección, rosa 24K sin luz y babero de afeitado), con una media de
17,6 €/pedido con envío CJ. Antes de invertir, el siguiente paso es verificar el envío de AliExpress a
España cambiando la región de AutoDS.

## Actualización 29 sept: región España (AutoDS ES, sin CJ)

Carpeta `espana/`. Se descarta CJ Dropshipping: se trabaja solo con AutoDS en región España con el proveedor AliExpress ES.

- 1.397 ganadores → 276 llegan en ≤ 10 días → 84 pasan el filtro duro (`f1.py`) → 62 cumplen el brief tras juicio manual (`judg_es.tsv`).
- Coste puesto = variante que se venderá + envío AutoDS a España (1,75 €/ud.) + 3 € de arancel UE por paquete desde China.
- Resultado (`D_es.json`, `score_es.py`): **ninguno llega a 35 € por pedido**. Mejor: mochila portaperros, 19,41 € (2.ª al 50 %). Margen mediano: 2,57 €. ROAS de equilibrio mediano: 6,4.
- Nicho recomendado: **Mascotas** (mochila portaperros, cama plátano para gatos y peluca de león como contenido y complemento).
- Dashboard: `radar/radar.html` (versión anterior en el historial de git).

## Actualización 29 sept (tarde): mercado EE. UU.

Carpeta `usa/`. Tienda Lume orientada a EE. UU.: la región de AutoDS ya estaba en US, así que se reutilizan los 1.770
candidatos del 28 sept y se añaden 300 nuevos (ganadores de los últimos 30 días y productos en almacén US).

- Pipeline: `python3 usa/f1_us.py` (filtro duro; genera `f1_us.json` y `f1_quedan.tsv`) → `python3 usa/score_us.py`
  (lee `judg_us.tsv` y `verificados.json`; genera `D_us.json`).
- 2.031 productos → 731 llegan en ≤ 10 días → 490 pasan los vetos de EE. UU. (marca, armas/tabaco, adulto,
  salud/ingeribles FDA, juguete/bebé CPSC, consumible) → 73 finalistas con juicio manual → 10 con coste de variante verificado.
- Fórmula (USD): MC = PVP − coste puesto − (4,5 % PVP + 0,30 $) − 9 % PVP. Sin IVA (exportación). Objetivo: 38,9 $ (= 35 €).
- Arancel CN → EE. UU. sin de minimis: **supuesto** de 40 % del valor + 1 $ por paquete (tras la sentencia del Supremo
  de feb. 2026 sobre IEEPA quedan las tarifas de la Sección 301). Almacén US = 0 $. Verificar en el checkout de AliExpress.
- Resultado: **solo 1 producto llega a 38,9 $ por pedido**: cortapuntas abiertas del pelo (69,99 $, MC 39,36 $ con 1 ud.,
  49,75 $ con la 2.ª al 50 %). Le siguen la mochila portaperros (33,85 $), la bandolera antirrobo (33,80 $) y el
  detector de cámaras ocultas (29,28 $, almacén US).
- Nicho con mejor nota media: **Belleza/cabello** (cortapuntas + flequillo postizo de clip). Alternativa: **Mascotas**
  (mochila, collar LED, alfombrilla de arenero), coherente con el barrido de España.
- El producto de medicube que se planteó (PDRN Pink Collagen Multi Balm) se descarta: es de una marca registrada
  que vende la propia marca en TikTok Shop, Ulta y su web.

### Sector Belleza, Salud y Cuidado Personal (EE. UU.)

- `python3 usa/f1_bel.py` (une `bel_raw.jsonl.gz` con el barrido general → `f1_bel.json`) →
  `python3 usa/score_us.py f1_bel.json judg_bel.tsv D_bel.json`.
- Fuente: los 458 ganadores de AutoDS en «Beauty & Personal Care» (todas las páginas) + 117 de búsqueda en «Health &
  Wellness» y «Tools & Accessories» con envío < 11 días. Sin productos de cabello (a petición) ni ingeribles.
- En esta categoría solo 94 ganadores llegan en ≤ 10 días; se admiten 11 días en 3 finalistas verificados (penalizados
  en la nota) y se descartan los de 12-13 días.
- Cosmética tópica (cremas, sérums, bálsamos) de China: descartada por MoCRA (registro de instalación, listado de
  producto y responsable en EE. UU. en la etiqueta).
- Resultado: **1 producto supera 38,9 $ por pedido**: masajeador de cuello y hombros inalámbrico (almacén US, 29,36 $,
  4,9★ con 1.391 reseñas; PVP 79,99 $, MC 39,53 $ con 1 ud. y 44,76 $ con la 2.ª al 50 %). Le siguen el masajeador de
  rodilla (37,54 $), el masajeador facial de microcorriente (37,06 $, 4,9★ con 2.729 reseñas), los parches de silicona
  antiarrugas (33,95 $) y las ventosas eléctricas (31,25 $).
- Nicho recomendado: **«spa en casa»** (masaje + herramientas faciales sin cosmética), con temporada de regalos Q4.
