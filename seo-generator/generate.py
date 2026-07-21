#!/usr/bin/env python3
"""
NOVA SEO GENERATOR — 1000 articles/jour, 7 langues
GitHub Actions — tourne même PC éteint
"""
import os, sys, random, hashlib
from datetime import datetime

SITE_URL = "https://whatsapp-viewer.netlify.app"
OUTPUT_DIR = "seo-pages"
ARTICLES_PER_RUN = int(sys.argv[1]) if len(sys.argv) > 1 else 334

LANGUAGES = {
    "en": {
        "name": "English",
        "titles": [
            "How to View WhatsApp Messages Online {year}",
            "Read WhatsApp Messages Free — No Verification",
            "WhatsApp Spy Tool — See Anyone's Messages",
            "WhatsApp Viewer Online — {year} Working Method",
            "Free WhatsApp Tracker — Monitor Messages & Location",
            "How to Spy on WhatsApp Without Them Knowing",
            "WhatsApp Message Reader — Instant Access",
            "View WhatsApp Messages Online Free — No Download",
            "WhatsApp Monitoring Tool — Track Conversations",
            "How to Read Deleted WhatsApp Messages",
            "WhatsApp Last Seen Tracker — Online Status",
            "WhatsApp Contact Viewer — See Their Friends",
            "WhatsApp Photo Viewer — See All Media Files",
            "WhatsApp Call History Viewer — Voice & Video",
            "Track Someone's WhatsApp Location in Real Time",
        ],
        "desc": "View WhatsApp messages online free. Read conversations, see photos, track GPS. No verification. Works worldwide.",
        "cta": "Start Viewing Now",
    },
    "fr": {
        "name": "Français",
        "titles": [
            "Voir les Messages WhatsApp en Ligne {year}",
            "Lire Messages WhatsApp Gratuit — Sans Vérification",
            "Application Espion WhatsApp — Voir les Messages",
            "Comment Espionner WhatsApp Sans Se Faire Prendre",
            "Tracker WhatsApp Gratuit — Messages et Localisation",
            "Voir les Messages WhatsApp de Quelqu'un Gratuitement",
            "Lecteur de Messages WhatsApp — Accès Instantané",
            "Pirater un Compte WhatsApp en Ligne",
            "Outil de Surveillance WhatsApp — Conversations",
            "Comment Lire les Messages WhatsApp Supprimés",
            "Voir la Dernière Connexion WhatsApp",
            "Voir les Contacts WhatsApp de Quelqu'un",
            "Voir les Photos WhatsApp — Tous les Médias",
            "Historique d'Appels WhatsApp — Voix et Vidéo",
            "Localiser Quelqu'un sur WhatsApp en Temps Réel",
        ],
        "desc": "Voir messages WhatsApp en ligne gratuit. Lire conversations, voir photos, tracker GPS. Sans vérification. Mondial.",
        "cta": "Commencer Maintenant",
    },
    "es": {
        "name": "Español",
        "titles": [
            "Ver Mensajes de WhatsApp en Línea {year}",
            "Leer Mensajes de WhatsApp Gratis — Sin Verificación",
            "Aplicación Espía de WhatsApp — Ver Mensajes",
            "Cómo Espiar WhatsApp Sin Que Lo Sepan",
            "Rastreador de WhatsApp Gratis — Mensajes y Ubicación",
            "Ver Mensajes de WhatsApp de Alguien Gratis",
            "Lector de Mensajes de WhatsApp — Acceso Instantáneo",
            "Hackear una Cuenta de WhatsApp en Línea",
            "Herramienta de Monitoreo de WhatsApp",
            "Cómo Leer Mensajes Eliminados de WhatsApp",
            "Ver Última Conexión de WhatsApp",
            "Ver Contactos de WhatsApp de Alguien",
            "Ver Fotos de WhatsApp — Todos los Archivos",
            "Historial de Llamadas de WhatsApp",
            "Rastrear Ubicación de WhatsApp en Tiempo Real",
        ],
        "desc": "Ver mensajes WhatsApp online gratis. Leer conversaciones, ver fotos, rastrear GPS. Sin verificación. Mundial.",
        "cta": "Comenzar Ahora",
    },
    "de": {
        "name": "Deutsch",
        "titles": [
            "WhatsApp Nachrichten Online Lesen {year}",
            "WhatsApp Nachrichten Kostenlos Lesen — Keine Verifizierung",
            "WhatsApp Spionage App — Nachrichten Sehen",
            "WhatsApp Überwachungstool — Kostenlos",
            "WhatsApp Tracker — Nachrichten & Standort",
            "Gelöschte WhatsApp Nachrichten Wiederherstellen",
            "WhatsApp Online Status Tracker",
            "WhatsApp Kontakte Einsehen",
            "WhatsApp Fotos & Medien Anzeigen",
            "WhatsApp Anrufliste Einsehen",
        ],
        "desc": "WhatsApp Nachrichten online kostenlos lesen. Konversationen, Fotos, GPS-Tracking. Keine Verifizierung.",
        "cta": "Jetzt Starten",
    },
    "it": {
        "name": "Italiano",
        "titles": [
            "Vedere Messaggi WhatsApp Online {year}",
            "Leggere Messaggi WhatsApp Gratis — Nessuna Verifica",
            "App Spia WhatsApp — Vedi Messaggi",
            "Tracker WhatsApp Gratuito — Messaggi e Posizione",
            "Come Spiare WhatsApp Senza Essere Scoperti",
            "Lettore Messaggi WhatsApp — Accesso Istantaneo",
            "Recuperare Messaggi WhatsApp Cancellati",
            "Vedere Stato Online WhatsApp",
            "Vedere Foto WhatsApp — Tutti i Media",
            "Cronologia Chiamate WhatsApp",
        ],
        "desc": "Vedi messaggi WhatsApp online gratis. Leggi conversazioni, foto, tracciamento GPS. Nessuna verifica.",
        "cta": "Inizia Ora",
    },
    "pt": {
        "name": "Português",
        "titles": [
            "Ver Mensagens WhatsApp Online {year}",
            "Ler Mensagens WhatsApp Grátis — Sem Verificação",
            "Aplicativo Espião WhatsApp — Ver Mensagens",
            "Rastreador WhatsApp Grátis — Mensagens e Localização",
            "Como Espionar WhatsApp Sem Ser Descoberto",
            "Leitor de Mensagens WhatsApp — Acesso Instantâneo",
            "Recuperar Mensagens WhatsApp Apagadas",
            "Ver Status Online WhatsApp",
            "Ver Fotos WhatsApp — Todas as Mídias",
            "Histórico de Chamadas WhatsApp",
        ],
        "desc": "Veja mensagens WhatsApp online grátis. Leia conversas, fotos, rastreamento GPS. Sem verificação.",
        "cta": "Começar Agora",
    },
    "ar": {
        "name": "العربية",
        "titles": [
            "كيفية عرض رسائل واتساب عبر الإنترنت {year}",
            "قراءة رسائل واتساب مجاناً — بدون تحقق",
            "أداة تجسس واتساب — عرض الرسائل",
            "متتبع واتساب مجاني — الرسائل والموقع",
            "كيفية التجسس على واتساب دون معرفتهم",
            "قارئ رسائل واتساب — وصول فوري",
            "استعادة رسائل واتساب المحذوفة",
            "عرض حالة الاتصال في واتساب",
            "عرض صور واتساب — جميع الوسائط",
            "سجل مكالمات واتساب",
        ],
        "desc": "عرض رسائل واتساب عبر الإنترنت مجاناً. قراءة المحادثات والصور وتتبع GPS. بدون تحقق.",
        "cta": "ابدأ الآن",
    },
}

def generate_article(lang_code: str, lang: dict, title: str) -> str:
    year = "2026"
    title = title.replace("{year}", year)
    uid = hashlib.md5(f"{lang_code}-{title}-{datetime.now().isoformat()}".encode()).hexdigest()[:8]
    
    body_phrases = [
        f"Looking to view WhatsApp messages? Our tool makes it easy.",
        f"Used by millions worldwide. No download needed.",
        f"Enter any phone number and start reading messages instantly.",
        f"Compatible with all WhatsApp versions including {year}.",
        f"See photos, videos, voice notes, and documents.",
        f"Track real-time GPS location with advanced tracking.",
        f"View contact lists and see who they talk to most.",
        f"Read deleted messages — recovered from WhatsApp servers.",
        f"Monitor online status — know exactly when they're active.",
        f"100% undetectable — target receives no notification.",
        f"Works in all countries — Europe, Americas, Asia, Africa.",
        f"Android and iPhone compatible — no difference.",
        f"Secure connection bypasses end-to-end encryption.",
        f"See call history — voice, video, missed calls.",
        f"Free basic access — no credit card required.",
    ]
    random.shuffle(body_phrases)
    body_text = " ".join(body_phrases[:random.randint(5, 8)])
    
    return f"""<!DOCTYPE html>
<html lang="{lang_code}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{lang['desc']}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{SITE_URL}/">
<meta name="theme-color" content="#075e54">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#0a1014;color:#e9edef;font-family:Inter,system-ui;text-align:center;padding:40px 20px;max-width:800px;margin:0 auto}}
h1{{font-size:clamp(22px,5vw,32px);background:linear-gradient(135deg,#25d366,#128c7e);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:16px}}
p{{color:#8696a0;font-size:15px;line-height:1.8;margin-bottom:24px}}
.btn{{display:inline-block;background:#25d366;color:#000;padding:16px 36px;border-radius:30px;font-weight:700;font-size:16px;text-decoration:none;box-shadow:0 6px 24px rgba(37,211,102,0.3)}}
.features{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin:40px 0;text-align:left}}
.feat{{background:rgba(17,27,33,0.6);border:1px solid rgba(255,255,255,0.04);border-radius:12px;padding:16px}}
.feat h3{{font-size:14px;color:#25d366;margin-bottom:6px}}
.feat p{{font-size:12px;color:#8696a0;line-height:1.5}}
footer{{margin-top:40px;color:#1a2a30;font-size:11px}}
</style>
</head>
<body>
<h1>{title}</h1>
<p>{body_text}</p>
<a href="/app" class="btn">{lang['cta']} →</a>
<div class="features">
<div class="feat"><h3>💬 Read Messages</h3><p>View all conversations including deleted messages.</p></div>
<div class="feat"><h3>📸 See Photos</h3><p>Access all shared media — photos, videos, voice notes.</p></div>
<div class="feat"><h3>📍 Track Location</h3><p>Real-time GPS tracking — see where they are right now.</p></div>
<div class="feat"><h3>🟢 Online Status</h3><p>Know exactly when they come online and go offline.</p></div>
<div class="feat"><h3>📞 Call History</h3><p>View all WhatsApp calls with timestamps.</p></div>
<div class="feat"><h3>🔒 100% Undetectable</h3><p>The target receives no notification.</p></div>
</div>
<a href="/app" class="btn">{lang['cta']} — It's Free</a>
<footer><p>WhatsApp Viewer v3.2 — {year}</p></footer>
</body>
</html>"""

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    articles_per_lang = ARTICLES_PER_RUN // len(LANGUAGES)
    total = 0
    
    for lang_code, lang in LANGUAGES.items():
        lang_dir = os.path.join(OUTPUT_DIR, lang_code)
        os.makedirs(lang_dir, exist_ok=True)
        
        for i in range(articles_per_lang):
            title = random.choice(lang["titles"])
            html = generate_article(lang_code, lang, title)
            slug = title.lower().replace(" ", "-").replace("/", "-")[:60]
            uid = hashlib.md5(html.encode()).hexdigest()[:6]
            filename = f"{slug}-{uid}.html"
            
            with open(os.path.join(lang_dir, filename), "w", encoding="utf-8") as f:
                f.write(html)
            total += 1
    
    print(f"✅ {total} articles ({ARTICLES_PER_RUN} target) — {len(LANGUAGES)} langues × {articles_per_lang}")

if __name__ == "__main__":
    main()
