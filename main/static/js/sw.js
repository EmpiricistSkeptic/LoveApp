const CACHE_NAME = 'v1'; // Меняйте версию при обновлении файлов!

const ASSETS = [
  '/', 
  '/static/css/main.css', 
  '/static/js/app.js',
  '/static/icons/icon-192.png'
];

// Установка
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(ASSETS))
  );
});

// Обработка запросов
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});