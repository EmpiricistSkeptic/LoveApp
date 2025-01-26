const CACHE_NAME = 'v4'; // Меняйте версию при обновлении файлов!

const ASSETS = [
  '/', 
  '/static/css/main.css', 
  '/static/js/main.js',
  '/static/manifest.json',
  '/static/icons/android-chrome-192x192.png', // Добавьте сюда иконки
  '/static/icons/android-chrome-512x512.png'
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