const $ = id => document.getElementById(id);

const navButtons = document.querySelectorAll('nav button');
navButtons.forEach(b => b.onclick = () => {
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
  navButtons.forEach(x => x.classList.remove('active'));
  $(b.dataset.tab).classList.add('active');
  b.classList.add('active');
});

// Tooltips: clic para fijar, clic afuera o ESC para cerrar.
document.addEventListener('click', (e) => {
  const btn = e.target.closest('.tip-btn');
  if (btn) {
    e.preventDefault();
    const host = btn.closest('.tip-host');
    document.querySelectorAll('.tip-host.is-open').forEach(h => {
      if (h !== host) h.classList.remove('is-open');
    });
    host.classList.toggle('is-open');
    return;
  }
  if (!e.target.closest('.tip-host')) {
    document.querySelectorAll('.tip-host.is-open').forEach(h => h.classList.remove('is-open'));
  }
});
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    document.querySelectorAll('.tip-host.is-open').forEach(h => h.classList.remove('is-open'));
  }
});

// Ejemplos cargables — casos que ya convergen, listos para mostrar al profe.
const SINGLE_EXAMPLES = {
  poly:     { fn: 'x^3 - x - 2',      gfn: '(x+2)^(1/3)', a: 1, b: 2,   x0: 1.5, x1: 2,   tol: 1e-6, maxIter: 50 },
  trig:     { fn: 'cos(x) - x',       gfn: 'cos(x)',      a: 0, b: 1,   x0: 0.5, x1: 1,   tol: 1e-6, maxIter: 50 },
  exp:      { fn: 'exp(x) - 3*x',     gfn: 'exp(x)/3',    a: 0, b: 1,   x0: 0.5, x1: 1,   tol: 1e-6, maxIter: 50 },
  multiple: { fn: '(x-2)^3',          gfn: 'x - (x-2)^3', a: 1, b: 3,   x0: 1.5, x1: 2.5, tol: 1e-6, maxIter: 80 },
};

const LINEAR_EXAMPLES = {
  three: { A: '[[4,1,2],[3,5,1],[1,1,3]]',                 b: '[4,7,3]',     x0: '[0,0,0]',     omega: 1.1 },
  two:   { A: '[[4,1],[2,3]]',                             b: '[5,5]',       x0: '[0,0]',       omega: 1.1 },
  four:  { A: '[[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]]', b: '[6,25,-11,15]', x0: '[0,0,0,0]', omega: 1.1 },
};

const INTERP_EXAMPLES = {
  default:      { points: '[{"x":0,"y":1},{"x":1,"y":3},{"x":2,"y":2},{"x":3,"y":5}]', evalX: 1.5 },
  sine:         { points: '[{"x":0,"y":0},{"x":1,"y":0.84},{"x":2,"y":0.91},{"x":3,"y":0.14},{"x":4,"y":-0.76}]', evalX: 2.5 },
  experimental: { points: '[{"x":1,"y":2.1},{"x":2,"y":3.9},{"x":3,"y":6.2},{"x":4,"y":8.1},{"x":5,"y":10.05}]', evalX: 3.5 },
};

function applySingleExample(key) {
  const ex = SINGLE_EXAMPLES[key]; if (!ex) return;
  $('fn').value = ex.fn;
  $('gfn').value = ex.gfn;
  $('a').value = ex.a;
  $('b').value = ex.b;
  $('x0').value = ex.x0;
  $('x1').value = ex.x1;
  $('tol').value = ex.tol;
  $('maxIter').value = ex.maxIter;
  plotFunction();
}

function applyLinearExample(key) {
  const ex = LINEAR_EXAMPLES[key]; if (!ex) return;
  $('A').value = ex.A;
  $('bv').value = ex.b;
  $('xv').value = ex.x0;
  $('omega').value = ex.omega;
}

function applyInterpExample(key) {
  const ex = INTERP_EXAMPLES[key]; if (!ex) return;
  $('points').value = ex.points;
  $('evalX').value = ex.evalX;
  try { plotPoints(parsePoints(ex.points)); } catch {}
}

$('singleExamples').onchange = (e) => { applySingleExample(e.target.value); e.target.value = ''; };
$('linearExamples').onchange = (e) => { applyLinearExample(e.target.value); e.target.value = ''; };
$('interpExamples').onchange = (e) => { applyInterpExample(e.target.value); e.target.value = ''; };

// Música de fondo: Milky — Just The Way You Are.
// El mp3 debe estar en frontend/assets/just-the-way-you-are.mp3 (no se incluye por copyright).
(() => {
  const audio = $('bgMusic');
  const toggle = $('musicToggle');
  if (!audio || !toggle) return;
  const iconEl = toggle.querySelector('.music-icon');
  const labelEl = toggle.querySelector('.music-label');
  const IDLE = 'poner musiquita';
  const PLAYING = 'just the way you are';
  const MISSING = 'falta el mp3 ♡';

  audio.volume = 0.6;

  toggle.onclick = async () => {
    if (audio.paused) {
      try {
        await audio.play();
        toggle.classList.remove('is-error');
        toggle.classList.add('is-playing');
        iconEl.textContent = '♫';
        labelEl.textContent = PLAYING;
      } catch {
        toggle.classList.add('is-error');
        labelEl.textContent = MISSING;
        setTimeout(() => {
          toggle.classList.remove('is-error');
          labelEl.textContent = IDLE;
        }, 3500);
      }
    } else {
      audio.pause();
      toggle.classList.remove('is-playing');
      iconEl.textContent = '♪';
      labelEl.textContent = IDLE;
    }
  };

  audio.addEventListener('error', () => {
    toggle.classList.remove('is-playing');
    toggle.classList.add('is-error');
    iconEl.textContent = '♪';
    labelEl.textContent = MISSING;
    setTimeout(() => {
      toggle.classList.remove('is-error');
      labelEl.textContent = IDLE;
    }, 3500);
  });
})();

async function post(url, data) {
  const r = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  const j = await r.json();
  if (!r.ok) throw new Error(j.error || 'Error desconocido');
  return j;
}

function formatNum(v) {
  if (v === null || v === undefined) return '';
  if (Array.isArray(v)) return '[' + v.map(formatNum).join(', ') + ']';
  if (typeof v === 'string') return v;
  if (typeof v === 'object') return JSON.stringify(v);
  const n = Number(v);
  if (Number.isNaN(n)) return String(v);
  if (!Number.isFinite(n)) return n > 0 ? '∞' : '-∞';
  if (n === 0) return '0';
  const abs = Math.abs(n);
  if (abs < 1e-4 || abs >= 1e7) return n.toExponential(6);
  return Number(n.toPrecision(8)).toString();
}

function el(tag, attrs = {}, children = []) {
  const e = document.createElement(tag);
  for (const k in attrs) {
    if (k === 'class') e.className = attrs[k];
    else if (k === 'text') e.textContent = attrs[k];
    else e.setAttribute(k, attrs[k]);
  }
  (Array.isArray(children) ? children : [children]).forEach(c => {
    if (c == null) return;
    e.appendChild(typeof c === 'string' ? document.createTextNode(c) : c);
  });
  return e;
}

function renderTable(rows) {
  if (!Array.isArray(rows) || rows.length === 0) {
    return el('p', { text: '(sin filas)' });
  }
  const cols = Object.keys(rows[0]);
  const thead = el('thead', {}, el('tr', {}, cols.map(c => el('th', { text: c }))));
  const tbody = el('tbody', {}, rows.map(r =>
    el('tr', {}, cols.map(c => el('td', { text: formatNum(r[c]) })))
  ));
  return el('table', {}, [thead, tbody]);
}

function summaryBlock(items) {
  return el('div', { class: 'summary' }, items.map(([k, v]) =>
    el('div', { class: 'summary-row' }, [
      el('span', { class: 'summary-key', text: k }),
      el('span', { class: 'summary-val', text: formatNum(v) })
    ])
  ));
}

function renderError(rootId, message) {
  const root = $(rootId);
  root.innerHTML = '';
  root.appendChild(el('div', { class: 'error-banner' }, [
    el('span', { class: 'error-icon', text: '⚠' }),
    el('span', { text: message })
  ]));
}

function buildResultBody(data) {
  const frag = document.createDocumentFragment();

  const summary = [];
  if (data.method) summary.push(['método', data.method]);
  if (data.root !== undefined) summary.push(['raíz', data.root]);
  if (data.x !== undefined) summary.push(['x', data.x]);
  if (data.value !== undefined && data.value !== null) summary.push(['P(x evaluado)', data.value]);
  if (data.iterations !== undefined) summary.push(['iteraciones', data.iterations]);
  if (data.error !== undefined && typeof data.error === 'number') summary.push(['error final', data.error]);
  if (data.polynomial) summary.push(['polinomio', data.polynomial]);
  if (data.form) summary.push(['forma', data.form]);
  if (summary.length) frag.appendChild(summaryBlock(summary));

  if (Array.isArray(data.table) && data.table.length) {
    if (Array.isArray(data.table[0])) {
      frag.appendChild(el('h5', { text: 'Tabla de diferencias divididas' }));
      const rows = data.table.map((row, i) => {
        const obj = { i };
        row.forEach((v, j) => { obj['Δ' + j] = v; });
        return obj;
      });
      frag.appendChild(renderTable(rows));
    } else {
      frag.appendChild(el('h5', { text: 'Iteraciones' }));
      frag.appendChild(renderTable(data.table));
    }
  }

  if (Array.isArray(data.coefficients)) {
    frag.appendChild(el('h5', { text: 'Coeficientes' }));
    frag.appendChild(renderTable(data.coefficients.map((c, i) => ({ i, coef: c }))));
  }

  if (Array.isArray(data.segments)) {
    frag.appendChild(el('h5', { text: 'Tramos' }));
    frag.appendChild(renderTable(data.segments));
  }

  if (Array.isArray(data.terms)) {
    frag.appendChild(el('h5', { text: 'Términos de Lagrange' }));
    frag.appendChild(renderTable(data.terms));
  }

  if (Array.isArray(data.M)) {
    frag.appendChild(el('h5', { text: 'Vector M (segundas derivadas)' }));
    frag.appendChild(renderTable(data.M.map((m, i) => ({ i, M: m }))));
  }

  return frag;
}

function renderResult(rootId, data) {
  const root = $(rootId);
  root.innerHTML = '';

  if (Array.isArray(data)) {
    data.forEach(item => {
      const card = el('div', { class: 'compare-card' });
      card.appendChild(el('h4', { text: item.method || 'Método' }));
      if (item.success === false) {
        card.appendChild(el('div', { class: 'error-banner' }, [
          el('span', { class: 'error-icon', text: '⚠' }),
          el('span', { text: item.errorMessage || item.error || 'Falló' })
        ]));
      } else {
        card.appendChild(buildResultBody(item));
      }
      root.appendChild(card);
    });
    return;
  }

  if (data && data.success === false) {
    renderError(rootId, data.error || 'Error desconocido');
    return;
  }

  root.appendChild(buildResultBody(data));
}

function parseMatrix(str) {
  let A;
  try { A = JSON.parse(str); }
  catch { throw new Error('La matriz A debe ser un array JSON válido (ej: [[4,1],[2,3]]).'); }
  if (!Array.isArray(A) || !Array.isArray(A[0])) {
    throw new Error('La matriz A debe ser un array de arrays.');
  }
  const n = A.length;
  if (n < 2 || n > 7) throw new Error('La matriz A debe tener tamaño entre 2 y 7.');
  if (!A.every(r => Array.isArray(r) && r.length === n && r.every(v => Number.isFinite(Number(v))))) {
    throw new Error('La matriz A no es cuadrada o tiene valores no numéricos.');
  }
  return A.map(r => r.map(Number));
}

function parseVector(str, name, expectedLen) {
  let v;
  try { v = JSON.parse(str); }
  catch { throw new Error(`El vector ${name} debe ser un array JSON válido (ej: [1,2,3]).`); }
  if (!Array.isArray(v) || !v.every(x => Number.isFinite(Number(x)))) {
    throw new Error(`El vector ${name} debe contener solo números.`);
  }
  if (expectedLen !== undefined && v.length !== expectedLen) {
    throw new Error(`El vector ${name} debe tener tamaño ${expectedLen}.`);
  }
  return v.map(Number);
}

function parsePoints(str) {
  let p;
  try { p = JSON.parse(str); }
  catch { throw new Error('Los puntos deben ser un array JSON válido (ej: [{"x":0,"y":1},{"x":1,"y":3}]).'); }
  if (!Array.isArray(p) || p.length < 2 || p.length > 8) {
    throw new Error('Debes enviar entre 2 y 8 puntos.');
  }
  if (!p.every(o => o && Number.isFinite(Number(o.x)) && Number.isFinite(Number(o.y)))) {
    throw new Error('Cada punto debe tener {x, y} numéricos.');
  }
  const xs = p.map(o => Number(o.x));
  if (new Set(xs).size !== xs.length) throw new Error('Los valores de x no pueden repetirse.');
  return p.map(o => ({ x: Number(o.x), y: Number(o.y) }));
}

function validateExpr(expr, name) {
  if (!expr || !expr.trim()) throw new Error(`La expresión ${name} no puede estar vacía.`);
  return expr.trim();
}

function singlePayload() {
  return {
    fn: $('fn').value,
    g: $('gfn').value,
    a: +$('a').value,
    b: +$('b').value,
    x0: +$('x0').value,
    x1: +$('x1').value,
    tol: +$('tol').value,
    maxIter: +$('maxIter').value,
    m: 2
  };
}

$('runSingle').onclick = async () => {
  const method = $('singleMethod').value;
  try {
    if (method === 'fixedPoint') validateExpr($('gfn').value, 'g(x)');
    else validateExpr($('fn').value, 'f(x)');
    const payload = singlePayload();
    const body = method === 'fixedPoint'
      ? { g: payload.g, x0: payload.x0, tol: payload.tol, maxIter: payload.maxIter }
      : payload;
    const data = await post(`/api/single/${method}`, body);
    renderResult('singleOut', data);
    plotFunction();
  } catch (e) {
    renderError('singleOut', e.message);
    plotFunction();
  }
};

const PLOT_LAYOUT = {
  paper_bgcolor: 'transparent',
  plot_bgcolor: 'transparent',
  font: { color: '#9b7b94', family: 'Quicksand, system-ui, sans-serif', size: 11 },
  margin: { t: 16, r: 16, b: 36, l: 44 },
  xaxis: { gridcolor: '#f5d5e3', zerolinecolor: '#ecb8d0', linecolor: '#ecb8d0' },
  yaxis: { gridcolor: '#f5d5e3', zerolinecolor: '#ecb8d0', linecolor: '#ecb8d0' },
  showlegend: false
};

function plotFunction() {
  const expr = $('fn').value;
  if (!expr || !expr.trim()) return;
  let compiled;
  try {
    compiled = math.parse(expr).compile();
  } catch {
    return;
  }
  const xs = [], ys = [];
  for (let x = -10; x <= 10; x += 0.1) {
    xs.push(x);
    try {
      const y = compiled.evaluate({ x });
      const n = Number(y);
      ys.push(Number.isFinite(n) ? n : NaN);
    } catch {
      ys.push(NaN);
    }
  }
  Plotly.newPlot('plotSingle', [
    { x: xs, y: ys, type: 'scatter', mode: 'lines', name: 'f(x)', line: { color: '#ff8fa3', width: 2.4, shape: 'spline' }, connectgaps: false },
    { x: [-10, 10], y: [0, 0], type: 'scatter', mode: 'lines', name: 'eje x', line: { color: '#ecb8d0', width: 1 } }
  ], PLOT_LAYOUT, { displayModeBar: false });
}

let _fnPlotTimer = null;
$('fn').addEventListener('input', () => {
  clearTimeout(_fnPlotTimer);
  _fnPlotTimer = setTimeout(plotFunction, 150);
});

$('runLinear').onclick = async () => {
  try {
    const A = parseMatrix($('A').value);
    const b = parseVector($('bv').value, 'b', A.length);
    const x0 = parseVector($('xv').value, 'x0', A.length);
    const method = $('linearMethod').value;
    const omega = +$('omega').value;
    if (method === 'sor' && (omega <= 0 || omega >= 2)) {
      throw new Error('Para SOR, ω debe estar estrictamente entre 0 y 2.');
    }
    const data = await post(`/api/linear/${method}`, {
      A, b, x0, omega,
      tol: +$('tol').value,
      maxIter: +$('maxIter').value
    });
    renderResult('linearOut', data);
  } catch (e) {
    renderError('linearOut', e.message);
  }
};

$('runInterp').onclick = async () => {
  try {
    const points = parsePoints($('points').value);
    const method = $('interpMethod').value;
    const data = await post(`/api/interpolation/${method}`, {
      points,
      evalX: +$('evalX').value
    });
    renderResult('interpOut', data);
    plotPoints(points);
  } catch (e) {
    renderError('interpOut', e.message);
  }
};

function plotPoints(points) {
  Plotly.newPlot('plotInterp', [
    {
      x: points.map(p => p.x),
      y: points.map(p => p.y),
      mode: 'markers+lines',
      type: 'scatter',
      name: 'puntos',
      line: { color: '#c8a8e9', width: 2, shape: 'spline' },
      marker: { color: '#ff8fa3', size: 10, line: { color: '#ffffff', width: 2 } }
    }
  ], PLOT_LAYOUT, { displayModeBar: false });
}

plotFunction();
try { plotPoints(parsePoints($('points').value)); } catch {}
