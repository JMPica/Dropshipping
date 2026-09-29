# Reset Lume — nicho belleza y top 50 AutoDS (29 sept 2026)

Panel publicado: https://claude.ai/artifact/HMBgBFTuT7uHDULPcuNLdG (copia local: `radar-lume-belleza.html`).

## Decisión

- **Nicho:** salud, belleza y cuidado personal **sin fórmulas** (herramientas y accesorios). Subnicho ganador: **Cabello** (17 de 50 finalistas, nota media top 3: 66,7; margen medio top 3: 17,5 €/pedido).
- **Test propuesto (3 × 150 €):** recortador de puntas abiertas (73,3), cepillo térmico rizador 32 mm (64,7) y rizador sin calor tipo pulpo (62,0).

## Por qué se atascó el proyecto

La regla "MC ≥ 35 € por pedido" era imposible: el propio caso de Adrián (cepillo a 49,99 € con 21 € de coste) deja ≈ 14,50 € por pedido en España con IVA. Nuevo umbral: **MC ≥ 15 € con la oferta**, múltiplo ×3 ideal y ×2 mínimo, envío ≤ 12 días.

## Embudo

2.185 explorados (908 nuevos de Belleza y cuidado personal hoy + 1.277 ganadores del barrido del 28/29 sept) → 1.218 en el nicho → 789 sin fórmulas ni riesgos legales → 438 con coste 5-30 $ y envío ≤ 12 días → 50 finalistas con ventas.

## Archivos

| Archivo | Contenido |
|---|---|
| `datos/explorados.json` | Los 2.185 productos con coste, envío, pedidos y motivo de exclusión. |
| `datos/judg.tsv` | Juicio manual de los 50: PVP, pack, problema, demo, presencia en tiendas, riesgo y gancho; y costes verificados. |
| `datos/D.json` | Los 50 puntuados (nota, margen, ROAS de equilibrio, desglose). |
| `scripts/f1.py`, `scripts/score.py` | Filtro duro y puntuación (rutas del contenedor de la sesión). |
| `scripts/panel_template.html`, `scripts/build.py` | Genera el panel. |

## Fórmula

MC = PVP/1,21 − coste puesto − (2,1 % PVP + 0,30 €) − 9 % PVP. Coste puesto = variante + envío AutoDS a España + 3 € de arancel UE por paquete desde China (supuesto).
