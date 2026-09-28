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
