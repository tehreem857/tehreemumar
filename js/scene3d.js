/* ==========================================================
   Tehreem Umar — 3D "Automation Core" scene
   A gold AI core surrounded by a network of nodes, with
   pulses of light (leads / data) flowing along the links.
   The whole system moves through the page as you scroll.
   ========================================================== */
import * as THREE from 'three';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

const canvas = document.getElementById('scene');
const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const isMobile = window.matchMedia('(max-width: 860px)').matches;

const GOLD = new THREE.Color('#E3A857');
const GOLD_HI = new THREE.Color('#F5CF8E');
const RUSSET = new THREE.Color('#80461B');
const BG = new THREE.Color('#0F0908');

function fallback() {
  canvas.style.background = 'radial-gradient(ellipse at 70% 40%, rgba(227,168,87,.18), transparent 55%), radial-gradient(ellipse at 20% 80%, rgba(128,70,27,.25), transparent 50%), #0F0908';
  window.dispatchEvent(new Event('scene-ready'));
}

let renderer;
try {
  renderer = new THREE.WebGLRenderer({ canvas, antialias: !isMobile, powerPreference: 'high-performance' });
} catch (err) {
  fallback();
  throw err;
}

renderer.setPixelRatio(Math.min(window.devicePixelRatio, isMobile ? 1.5 : 2));
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.05;

const scene = new THREE.Scene();
scene.background = BG;
scene.fog = new THREE.FogExp2(BG, 0.055);

const pmrem = new THREE.PMREMGenerator(renderer);
scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;

const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 100);
camera.position.set(0, 0, 11);

/* ---------- Lights ---------- */
scene.add(new THREE.AmbientLight(0xffffff, 0.15));
const key = new THREE.PointLight(GOLD_HI, 60, 30);
key.position.set(4, 4, 6);
scene.add(key);
const rim = new THREE.PointLight(RUSSET, 80, 30);
rim.position.set(-5, -3, -4);
scene.add(rim);

/* ---------- System group (everything that moves together) ---------- */
const system = new THREE.Group();
scene.add(system);
const spin = new THREE.Group(); // inner group for idle rotation
system.add(spin);

/* Core */
const coreMat = new THREE.MeshPhysicalMaterial({
  color: GOLD_HI, metalness: 1, roughness: 0.18, clearcoat: 0.6, clearcoatRoughness: 0.2,
  flatShading: true, emissive: RUSSET, emissiveIntensity: 0.12, envMapIntensity: 2.6,
});
const core = new THREE.Mesh(new THREE.IcosahedronGeometry(1.15, 1), coreMat);
spin.add(core);

/* Inner glow */
const glowTex = (() => {
  const c = document.createElement('canvas');
  c.width = c.height = 128;
  const g = c.getContext('2d');
  const grd = g.createRadialGradient(64, 64, 0, 64, 64, 64);
  grd.addColorStop(0, 'rgba(245,207,142,1)');
  grd.addColorStop(0.25, 'rgba(227,168,87,.55)');
  grd.addColorStop(1, 'rgba(227,168,87,0)');
  g.fillStyle = grd;
  g.fillRect(0, 0, 128, 128);
  const t = new THREE.CanvasTexture(c);
  t.colorSpace = THREE.SRGBColorSpace;
  return t;
})();
const halo = new THREE.Sprite(new THREE.SpriteMaterial({ map: glowTex, transparent: true, opacity: 0.55, depthWrite: false, blending: THREE.AdditiveBlending }));
halo.scale.setScalar(6);
system.add(halo);

/* Wire shell */
const shell = new THREE.LineSegments(
  new THREE.EdgesGeometry(new THREE.IcosahedronGeometry(1.75, 1)),
  new THREE.LineBasicMaterial({ color: GOLD, transparent: true, opacity: 0.35 })
);
spin.add(shell);

/* Orbit rings */
const rings = [];
[[2.5, 0.006, 1.2, 0.3], [3.0, 0.005, -0.6, 1.1], [3.5, 0.004, 0.4, -0.9]].forEach(([r, t, rx, ry], i) => {
  const ring = new THREE.Mesh(
    new THREE.TorusGeometry(r, t * 2.2, 8, 160),
    new THREE.MeshBasicMaterial({ color: i === 1 ? GOLD_HI : GOLD, transparent: true, opacity: 0.45 - i * 0.08 })
  );
  ring.rotation.set(rx, ry, 0);
  system.add(ring);
  // a small "satellite" on each ring
  const sat = new THREE.Mesh(new THREE.SphereGeometry(0.07, 16, 16), new THREE.MeshBasicMaterial({ color: GOLD_HI }));
  ring.add(sat);
  rings.push({ ring, sat, r, speed: 0.25 + i * 0.12, phase: i * 2 });
});

/* ---------- Network of nodes ---------- */
const NODE_COUNT = isMobile ? 34 : 64;
const nodes = [];
const rand = mulberry32(7);
for (let i = 0; i < NODE_COUNT; i++) {
  const radius = 3.4 + rand() * 2.4;
  const theta = rand() * Math.PI * 2;
  const phi = Math.acos(2 * rand() - 1);
  nodes.push(new THREE.Vector3(
    radius * Math.sin(phi) * Math.cos(theta),
    radius * Math.sin(phi) * Math.sin(theta) * 0.7,
    radius * Math.cos(phi) * 0.6
  ));
}

const nodeMesh = new THREE.InstancedMesh(
  new THREE.IcosahedronGeometry(0.06, 1),
  new THREE.MeshBasicMaterial({ color: GOLD_HI }),
  NODE_COUNT
);
const m4 = new THREE.Matrix4();
nodes.forEach((p, i) => {
  const s = 0.6 + rand() * 1.4;
  m4.makeScale(s, s, s).setPosition(p);
  nodeMesh.setMatrixAt(i, m4);
});
spin.add(nodeMesh);

/* Edges: each node -> its 2 nearest neighbours; some nodes -> core */
const edges = [];
const seen = new Set();
nodes.forEach((a, i) => {
  const near = nodes
    .map((b, j) => ({ j, d: a.distanceToSquared(b) }))
    .filter((o) => o.j !== i)
    .sort((x, y) => x.d - y.d)
    .slice(0, 2);
  near.forEach(({ j }) => {
    const k = i < j ? `${i}-${j}` : `${j}-${i}`;
    if (!seen.has(k)) { seen.add(k); edges.push([a, nodes[j]]); }
  });
  if (i % 4 === 0) edges.push([a, a.clone().setLength(1.75)]);
});

const edgePos = new Float32Array(edges.length * 6);
edges.forEach(([a, b], i) => { a.toArray(edgePos, i * 6); b.toArray(edgePos, i * 6 + 3); });
const edgeGeo = new THREE.BufferGeometry();
edgeGeo.setAttribute('position', new THREE.BufferAttribute(edgePos, 3));
const edgeLines = new THREE.LineSegments(edgeGeo, new THREE.LineBasicMaterial({ color: GOLD, transparent: true, opacity: 0.16 }));
spin.add(edgeLines);

/* Pulses travelling along edges (the "data flow") */
const PULSES = isMobile ? 40 : 90;
const pulseData = [];
const pulsePos = new Float32Array(PULSES * 3);
for (let i = 0; i < PULSES; i++) {
  pulseData.push({ e: Math.floor(rand() * edges.length), t: rand(), v: 0.15 + rand() * 0.35, dir: rand() > 0.5 ? 1 : -1 });
}
const pulseGeo = new THREE.BufferGeometry();
pulseGeo.setAttribute('position', new THREE.BufferAttribute(pulsePos, 3));
const pulses = new THREE.Points(pulseGeo, new THREE.PointsMaterial({
  map: glowTex, size: 0.26, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, color: GOLD_HI,
}));
spin.add(pulses);

/* ---------- Ambient dust (whole scene depth) ---------- */
const DUST = isMobile ? 700 : 1600;
const dustPos = new Float32Array(DUST * 3);
for (let i = 0; i < DUST; i++) {
  dustPos[i * 3] = (rand() - 0.5) * 40;
  dustPos[i * 3 + 1] = (rand() - 0.5) * 30;
  dustPos[i * 3 + 2] = (rand() - 0.5) * 30 - 4;
}
const dustGeo = new THREE.BufferGeometry();
dustGeo.setAttribute('position', new THREE.BufferAttribute(dustPos, 3));
const dust = new THREE.Points(dustGeo, new THREE.PointsMaterial({
  color: GOLD, size: 0.035, transparent: true, opacity: 0.55, depthWrite: false,
}));
scene.add(dust);

/* ---------- Scroll choreography ----------
   One keyframe per section: where the system sits, how big it is,
   and how far it has turned. Interpolated by scroll position.    */
const sectionIds = ['hero', 'services', 'work', 'process', 'cta'];
const KEYS = isMobile
  ? [
      { x: 0.6, y: 1.9, z: -4, s: 0.75, ry: 0 },
      { x: 0, y: 0, z: -5, s: 0.9, ry: 1.2 },
      { x: 0, y: 0, z: -6, s: 1.0, ry: 2.4 },
      { x: 0, y: 0, z: -5, s: 0.9, ry: 3.6 },
      { x: 0, y: 0, z: -2, s: 0.9, ry: 5.0 },
    ]
  : [
      { x: 3.2, y: 0.1, z: 0, s: 1.0, ry: 0 },
      { x: 4.0, y: 1.6, z: -3, s: 0.9, ry: 1.4 },
      { x: 0, y: 0, z: -9, s: 1.5, ry: 2.6 },
      { x: 4.2, y: 0, z: -2, s: 0.95, ry: 3.8 },
      { x: 0, y: -0.4, z: -11, s: 1.7, ry: 5.2 },
    ];
let sectionTops = [];
function measure() {
  sectionTops = sectionIds.map((id) => {
    const el = document.getElementById(id);
    return el ? el.offsetTop : 0;
  });
}
measure();
window.addEventListener('load', measure);

const smooth = (t) => t * t * (3 - 2 * t);

/* Inner pages: a calmer drift from top-right to bottom-left over the page.
   Articles push the system further back so text stays easy to read.      */
const mode = document.body.dataset.scene || 'home';
const PAGE_PATH = {
  page: isMobile
    ? [{ x: 0.8, y: 2.2, z: -5, s: 0.7, ry: 0 }, { x: -0.6, y: -1.5, z: -8, s: 0.9, ry: 3.5 }]
    : [{ x: 4.4, y: 1.1, z: -3.5, s: 0.85, ry: 0 }, { x: -4.6, y: -0.8, z: -8, s: 1.1, ry: 4 }],
  article: isMobile
    ? [{ x: 0, y: 2.6, z: -9, s: 0.8, ry: 0 }, { x: 0, y: -2, z: -12, s: 1, ry: 3 }]
    : [{ x: 5.2, y: 1.4, z: -6, s: 0.9, ry: 0 }, { x: -5.6, y: -1, z: -12, s: 1.2, ry: 3.5 }],
};
function pagePose(path) {
  const max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
  const t = smooth(Math.min(1, window.scrollY / max));
  const [a, b] = path;
  return {
    x: a.x + (b.x - a.x) * t, y: a.y + (b.y - a.y) * t, z: a.z + (b.z - a.z) * t,
    s: a.s + (b.s - a.s) * t, ry: a.ry + (b.ry - a.ry) * t,
  };
}

function scrollPose() {
  if (PAGE_PATH[mode]) return pagePose(PAGE_PATH[mode]);
  const y = window.scrollY + window.innerHeight * 0.35;
  let i = 0;
  while (i < sectionTops.length - 1 && y >= sectionTops[i + 1]) i++;
  const a = KEYS[i];
  const b = KEYS[Math.min(i + 1, KEYS.length - 1)];
  const start = sectionTops[i];
  const end = sectionTops[i + 1] ?? start + 1;
  const t = i === KEYS.length - 1 ? 0 : smooth(Math.min(1, Math.max(0, (y - start) / (end - start))));
  return {
    x: a.x + (b.x - a.x) * t, y: a.y + (b.y - a.y) * t, z: a.z + (b.z - a.z) * t,
    s: a.s + (b.s - a.s) * t, ry: a.ry + (b.ry - a.ry) * t,
  };
}

/* ---------- Pointer parallax ---------- */
const pointer = { x: 0, y: 0, tx: 0, ty: 0 };
window.addEventListener('pointermove', (e) => {
  pointer.tx = (e.clientX / window.innerWidth) * 2 - 1;
  pointer.ty = (e.clientY / window.innerHeight) * 2 - 1;
}, { passive: true });

/* ---------- Resize ---------- */
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
  measure();
});

/* ---------- Loop ---------- */
const clock = new THREE.Clock();
const cur = { ...scrollPose() };
const tmpA = new THREE.Vector3();
let first = true;

function tick() {
  const dt = Math.min(clock.getDelta(), 0.05);
  const time = clock.elapsedTime;
  const speed = reduce ? 0.15 : 1;

  // ease toward scroll pose
  const target = scrollPose();
  const k = first ? 1 : 1 - Math.pow(0.0015, dt);
  for (const key of ['x', 'y', 'z', 's', 'ry']) cur[key] += (target[key] - cur[key]) * k;
  system.position.set(cur.x, cur.y + Math.sin(time * 0.6) * 0.12 * speed, cur.z);
  system.scale.setScalar(cur.s);

  // pointer parallax
  pointer.x += (pointer.tx - pointer.x) * 0.05;
  pointer.y += (pointer.ty - pointer.y) * 0.05;
  system.rotation.y = cur.ry + pointer.x * 0.35;
  system.rotation.x = pointer.y * 0.25;

  // idle motion
  spin.rotation.y += dt * 0.08 * speed;
  core.rotation.x += dt * 0.25 * speed;
  core.rotation.y += dt * 0.35 * speed;
  shell.rotation.y -= dt * 0.15 * speed;
  shell.rotation.z += dt * 0.05 * speed;
  coreMat.emissiveIntensity = 0.12 + Math.sin(time * 1.8) * 0.06;
  halo.material.opacity = 0.45 + Math.sin(time * 1.8) * 0.1;

  rings.forEach((o) => {
    const a = time * o.speed * speed + o.phase;
    o.sat.position.set(Math.cos(a) * o.r, Math.sin(a) * o.r, 0);
  });

  // data pulses
  for (let i = 0; i < PULSES; i++) {
    const p = pulseData[i];
    p.t += dt * p.v * speed;
    if (p.t > 1) { p.t = 0; p.e = Math.floor(Math.random() * edges.length); p.dir = Math.random() > 0.5 ? 1 : -1; }
    const [a, b] = edges[p.e];
    const t = p.dir > 0 ? p.t : 1 - p.t;
    tmpA.lerpVectors(a, b, t).toArray(pulsePos, i * 3);
  }
  pulseGeo.attributes.position.needsUpdate = true;

  // dust drift + camera sway
  dust.rotation.y = time * 0.01 * speed;
  camera.position.x = pointer.x * 0.4;
  camera.position.y = -pointer.y * 0.3;
  camera.lookAt(0, 0, 0);

  renderer.render(scene, camera);
  if (first) { first = false; window.dispatchEvent(new Event('scene-ready')); }
  requestAnimationFrame(tick);
}
requestAnimationFrame(tick);

/* deterministic random so the network looks the same every visit */
function mulberry32(a) {
  return function () {
    a |= 0; a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
