// UCIVET Service Worker
// Provides offline caching for static assets

const CACHE_NAME = 'ucivet-v1';
const STATIC_ASSETS = [
  '/',
  '/index',
  '/contacto-y-ubicacion',
  '/preguntas-frecuentes',
  '/aviso-legal',
  '/politica-de-privacidad',
  '/politica-de-cookies',
  '/servicios/cardiologia-veterinaria',
  '/servicios/citopatologia-veterinaria',
  '/servicios/dermatologia-veterinaria',
  '/servicios/gastroenterologia-veterinaria',
  '/servicios/medicina-interna-veterinaria',
  '/servicios/nefrologia-veterinaria',
  '/servicios/neurologia-veterinaria',
  '/servicios/nutricion-veterinaria',
  '/servicios/oncologia-veterinaria',
  '/servicios/ortopedia-veterinaria',
  '/servicios/radiologia-veterinaria',
  '/js/ui-components.js',
  '/js/tailwind-config.js',
  '/css/custom.css',
  '/img/logo-sin-fondo-uci.webp',
  '/img/fondo-del-hero.webp',
  '/manifest.json'
];

// Install event - cache static assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('[SW] Caching static assets');
        return cache.addAll(STATIC_ASSETS.map(url => new Request(url, { credentials: 'same-origin' })));
      })
      .then(() => self.skipWaiting())
  );
});

// Activate event - clean old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((cacheNames) => {
        return Promise.all(
          cacheNames
            .filter((name) => name !== CACHE_NAME)
            .map((name) => caches.delete(name))
        );
      })
      .then(() => self.clients.claim())
  );
});

// Fetch event - serve from cache, fallback to network
self.addEventListener('fetch', (event) => {
  // Skip non-GET requests
  if (event.request.method !== 'GET') return;

  // Skip external requests (CDN, Google Fonts, etc.)
  const url = new URL(event.request.url);
  if (url.origin !== location.origin) {
    // For external resources, try network first, fallback to cache
    event.respondWith(
      fetch(event.request)
        .then((response) => {
          // Cache successful responses
          if (response.ok) {
            const responseClone = response.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, responseClone);
            });
          }
          return response;
        })
        .catch(() => caches.match(event.request))
    );
    return;
  }

  // For same-origin requests: cache first, then network
  event.respondWith(
    caches.match(event.request)
      .then((cachedResponse) => {
        if (cachedResponse) {
          // Serve from cache, update in background
          event.waitUntil(
            fetch(event.request)
              .then((networkResponse) => {
                if (networkResponse.ok) {
                  caches.open(CACHE_NAME).then((cache) => {
                    cache.put(event.request, networkResponse.clone());
                  });
                }
              })
              .catch(() => {})
          );
          return cachedResponse;
        }

        // Not in cache, fetch from network
        return fetch(event.request)
          .then((networkResponse) => {
            if (networkResponse.ok) {
              const responseClone = networkResponse.clone();
              caches.open(CACHE_NAME).then((cache) => {
                cache.put(event.request, responseClone);
              });
            }
            return networkResponse;
          })
          .catch(() => {
            // Offline fallback for HTML pages
            if (event.request.headers.get('accept')?.includes('text/html')) {
              return caches.match('/index');
            }
            return new Response('Offline', { status: 503 });
          });
      })
  );
});

// Handle messages from clients
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});