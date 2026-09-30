/* Lume — interacciones propias (vanilla, sin librerías) */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Reveals al hacer scroll (un único observer) ---------- */
  var revealObserver = null;
  function initReveals(root) {
    var items = (root || document).querySelectorAll('.lu-reveal:not(.lu-visible)');
    if (!items.length) return;
    if (reduceMotion || !('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('lu-visible'); });
      return;
    }
    if (!revealObserver) {
      revealObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('lu-visible');
            revealObserver.unobserve(entry.target);
          }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    }
    items.forEach(function (el) { revealObserver.observe(el); });
  }

  /* ---------- Parallax suave del hero ---------- */
  function initParallax(root) {
    if (reduceMotion) return;
    var els = (root || document).querySelectorAll('[data-lu-parallax]');
    if (!els.length) return;
    var ticking = false;
    function update() {
      els.forEach(function (el) {
        var intensity = parseFloat(el.getAttribute('data-lu-parallax')) || 0;
        if (!intensity || window.innerWidth < 990) { el.style.transform = ''; return; }
        var rect = el.getBoundingClientRect();
        var offset = (rect.top + rect.height / 2 - window.innerHeight / 2) * (intensity / 100) * -0.25;
        el.style.transform = 'translate3d(0,' + offset.toFixed(1) + 'px,0)';
      });
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }

  /* ---------- Comparador antes / después ---------- */
  function initComparadores(root) {
    (root || document).querySelectorAll('.lu-comparador__marco').forEach(function (marco) {
      if (marco.dataset.luListo) return;
      marco.dataset.luListo = '1';
      var rango = marco.querySelector('.lu-comparador__rango');
      if (!rango) return;
      var set = function (v) { marco.style.setProperty('--lu-pos', v + '%'); };
      set(rango.value);
      rango.addEventListener('input', function () { set(rango.value); });
    });
  }

  /* ---------- Página de producto ---------- */
  function formatMoney(cents, format) {
    if (typeof Shopify !== 'undefined' && Shopify.formatMoney) return Shopify.formatMoney(cents, format);
    var value = (cents / 100).toFixed(2).replace('.', ',');
    return (format || '{{amount_with_comma_separator}} €').replace(/\{\{\s*\w+\s*\}\}/, value);
  }

  function initProducto(root) {
    (root || document).querySelectorAll('[data-lu-producto]').forEach(function (wrap) {
      if (wrap.dataset.luListo) return;
      wrap.dataset.luListo = '1';

      var dataEl = wrap.querySelector('[data-lu-variantes]');
      var variants = dataEl ? JSON.parse(dataEl.textContent) : [];
      var moneyFormat = wrap.getAttribute('data-money-format');
      var principal = wrap.querySelector('[data-lu-principal]');
      var miniaturas = wrap.querySelectorAll('[data-lu-miniatura]');
      var idInput = wrap.querySelector('input[name="id"]');
      var boton = wrap.querySelector('[data-lu-boton]');
      var botonTexto = boton ? boton.querySelector('span') : null;
      var precio = wrap.querySelector('[data-lu-precio]');
      var antes = wrap.querySelector('[data-lu-antes]');
      var ahorro = wrap.querySelector('[data-lu-ahorro]');
      var textos = {
        add: wrap.getAttribute('data-texto-comprar'),
        agotado: wrap.getAttribute('data-texto-agotado'),
        noDisponible: wrap.getAttribute('data-texto-no-disponible'),
        ahorro: wrap.getAttribute('data-texto-ahorro')
      };

      /* Galería */
      function mostrarImagen(src, srcset, alt) {
        if (!principal || !src) return;
        var img = principal.querySelector('img');
        if (!img) return;
        img.classList.add('lu-cambiando');
        setTimeout(function () {
          img.src = src;
          if (srcset) img.srcset = srcset; else img.removeAttribute('srcset');
          img.alt = alt || '';
          img.classList.remove('lu-cambiando');
        }, 180);
      }
      function marcarMiniatura(mediaId) {
        miniaturas.forEach(function (m) {
          m.setAttribute('aria-current', m.getAttribute('data-media-id') === String(mediaId) ? 'true' : 'false');
        });
      }
      miniaturas.forEach(function (m) {
        m.addEventListener('click', function () {
          mostrarImagen(m.getAttribute('data-src'), m.getAttribute('data-srcset'), m.getAttribute('data-alt'));
          marcarMiniatura(m.getAttribute('data-media-id'));
        });
      });

      /* Cantidad */
      var qty = wrap.querySelector('[data-lu-cantidad]');
      if (qty) {
        var input = qty.querySelector('input');
        qty.querySelectorAll('button').forEach(function (b) {
          b.addEventListener('click', function () {
            var v = parseInt(input.value, 10) || 1;
            v = b.getAttribute('data-paso') === '+' ? v + 1 : Math.max(1, v - 1);
            input.value = v;
          });
        });
      }

      /* Variantes */
      var fieldsets = wrap.querySelectorAll('[data-lu-opcion]');
      function opcionesSeleccionadas() {
        var sel = [];
        fieldsets.forEach(function (fs) {
          var checked = fs.querySelector('input:checked');
          sel.push(checked ? checked.value : null);
          var label = fs.querySelector('[data-lu-opcion-valor]');
          if (label && checked) label.textContent = checked.value;
        });
        return sel;
      }
      function actualizar(variant) {
        if (!idInput || !boton) return;
        if (!variant) {
          boton.setAttribute('disabled', 'disabled');
          if (botonTexto) botonTexto.textContent = textos.noDisponible;
          return;
        }
        idInput.value = variant.id;
        idInput.disabled = false;
        if (variant.available) {
          boton.removeAttribute('disabled');
          if (botonTexto) botonTexto.textContent = textos.add;
        } else {
          boton.setAttribute('disabled', 'disabled');
          if (botonTexto) botonTexto.textContent = textos.agotado;
        }
        if (precio) precio.textContent = formatMoney(variant.price, moneyFormat);
        var tieneAntes = variant.compare_at_price && variant.compare_at_price > variant.price;
        if (antes) {
          antes.textContent = tieneAntes ? formatMoney(variant.compare_at_price, moneyFormat) : '';
          antes.hidden = !tieneAntes;
        }
        if (ahorro) {
          ahorro.hidden = !tieneAntes;
          if (tieneAntes) {
            var pct = Math.round((variant.compare_at_price - variant.price) * 100 / variant.compare_at_price);
            ahorro.textContent = (textos.ahorro || '-[pct] %').replace('[pct]', pct);
          }
        }
        if (variant.featured_media && variant.featured_media.preview_image) {
          var src = variant.featured_media.preview_image.src;
          mostrarImagen(src + (src.indexOf('?') > -1 ? '&' : '?') + 'width=1400', null, variant.featured_media.alt);
          marcarMiniatura(variant.featured_media.id);
        }
        document.querySelectorAll('[data-lu-barra-precio]').forEach(function (el) {
          el.textContent = formatMoney(variant.price, moneyFormat);
        });
        if (window.history && window.history.replaceState && wrap.hasAttribute('data-actualizar-url')) {
          var url = new URL(window.location.href);
          url.searchParams.set('variant', variant.id);
          window.history.replaceState({}, '', url.toString());
        }
      }
      if (fieldsets.length) {
        wrap.addEventListener('change', function (e) {
          if (!e.target.closest('[data-lu-opcion]')) return;
          var sel = opcionesSeleccionadas();
          var variant = variants.find(function (v) {
            return v.options.every(function (o, i) { return o === sel[i]; });
          });
          actualizar(variant);
        });
      }

      /* Barra de compra fija: aparece cuando el botón principal sale de pantalla */
      var barra = document.querySelector('[data-lu-barra]');
      if (barra && boton && 'IntersectionObserver' in window) {
        var obs = new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            var pasado = !entry.isIntersecting && entry.boundingClientRect.top < 0;
            barra.classList.toggle('lu-visible', pasado);
          });
        });
        obs.observe(boton);
        var barraBtn = barra.querySelector('button');
        if (barraBtn) {
          barraBtn.addEventListener('click', function () {
            if (boton.hasAttribute('disabled')) {
              boton.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'center' });
              return;
            }
            boton.click();
          });
        }
      }
    });
  }

  function initAll(root) {
    initReveals(root);
    initComparadores(root);
    initProducto(root);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { initAll(); initParallax(); });
  } else {
    initAll();
    initParallax();
  }

  /* Editor de Shopify: re-inicializar al añadir o recargar una sección */
  document.addEventListener('shopify:section:load', function (e) { initAll(e.target); initParallax(e.target); });
})();
