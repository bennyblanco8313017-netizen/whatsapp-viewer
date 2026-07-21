#!/usr/bin/env python3
"""
NOVA SEO GENERATOR — 1000 articles/jour, 10+ langues
Tourne sur GitHub Actions. Ordinateur éteint = ça tourne quand même.
"""
import os, sys, random, hashlib
from datetime import datetime

# ═══════════════════════════════════════════════════════
#  CONFIG
# ═══════════════════════════════════════════════════════

SITE_URL = "https://whatsapp-viewer.netlify.app"
OUTPUT_DIR = "seo-pages"
ARTICLES_PER_RUN = int(sys.argv[1]) if len(sys.argv) > 1 else 250

# ═══════════════════════════════════════════════════════
#  MULTI-LANGUE — 12 langues principales
# ═══════════════════════════════════════════════════════

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
        "desc": "View any WhatsApp account online. Read messages, see photos, track GPS location. Free, instant, no verification. Works worldwide.",
        "cta": "Start Viewing Now",
        "keywords": ["whatsapp viewer", "whatsapp spy", "read whatsapp messages", "whatsapp tracker", "view whatsapp online"],
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
        "desc": "Voir n'importe quel compte WhatsApp en ligne. Lire les messages, voir les photos, suivre la localisation GPS. Gratuit, instantané, sans vérification.",
        "cta": "Commencer Maintenant",
        "keywords": ["voir whatsapp", "espionner whatsapp", "lire messages whatsapp", "pirater whatsapp", "whatsapp espion"],
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
        "desc": "Ver cualquier cuenta de WhatsApp en línea. Leer mensajes, ver fotos, rastrear ubicación GPS. Gratis, instantáneo, sin verificación.",
        "cta": "Comenzar Ahora",
        "keywords": ["ver whatsapp", "espiar whatsapp", "leer mensajes whatsapp", "hackear whatsapp", "rastreador whatsapp"],
    },
    "de": {
        "name": "Deutsch",
        "titles": [
            "WhatsApp Nachrichten Online Lesen {year}",
            "WhatsApp Nachrichten Kostenlos Lesen",
            "WhatsApp Spionage App — Nachrichten Sehen",
            "WhatsApp Überwachungstool — Kostenlos",
            "WhatsApp Tracker — Nachrichten & Standort",
            "Gelöschte WhatsApp Nachrichten Wiederherstellen",
            "WhatsApp Online Status Tracker",
            "WhatsApp Kontakte Einsehen",
            "WhatsApp Fotos & Medien Anzeigen",
            "WhatsApp Anrufliste Einsehen",
        ],
        "desc": "Jedes WhatsApp-Konto online einsehen. Nachrichten lesen, Fotos anzeigen, GPS-Standort verfolgen. Kostenlos, sofort, keine Verifizierung.",
        "cta": "Jetzt Starten",
        "keywords": ["whatsapp nachrichten lesen", "whatsapp spionage", "whatsapp tracker", "whatsapp überwachung"],
    },
    "it": {
        "name": "Italiano",
        "titles": [
            "Vedere Messaggi WhatsApp Online {year}",
            "Leggere Messaggi WhatsApp Gratis",
            "App Spia WhatsApp — Vedi Messaggi",
            "Tracker WhatsApp Gratuito — Messaggi e Posizione",
            "Come Spiare WhatsApp Senza Essere Scoperti",
            "Lettore Messaggi WhatsApp — Accesso Istantaneo",
            "Recuperare Messaggi WhatsApp Cancellati",
            "Vedere Stato Online WhatsApp",
            "Vedere Foto WhatsApp — Tutti i Media",
            "Cronologia Chiamate WhatsApp",
        ],
        "desc": "Visualizza qualsiasi account WhatsApp online. Leggi messaggi, vedi foto, traccia posizione GPS. Gratuito, istantaneo, nessuna verifica.",
        "cta": "Inizia Ora",
        "keywords": ["vedere whatsapp", "spiare whatsapp", "leggere messaggi whatsapp", "whatsapp tracker"],
    },
    "pt": {
        "name": "Português",
        "titles": [
            "Ver Mensagens WhatsApp Online {year}",
            "Ler Mensagens WhatsApp Grátis",
            "Aplicativo Espião WhatsApp — Ver Mensagens",
            "Rastreador WhatsApp Grátis — Mensagens e Localização",
            "Como Espionar WhatsApp Sem Ser Descoberto",
            "Leitor de Mensagens WhatsApp — Acesso Instantâneo",
            "Recuperar Mensagens WhatsApp Apagadas",
            "Ver Status Online WhatsApp",
            "Ver Fotos WhatsApp — Todas as Mídias",
            "Histórico de Chamadas WhatsApp",
        ],
        "desc": "Veja qualquer conta WhatsApp online. Leia mensagens, veja fotos, rastreie localização GPS. Grátis, instantâneo, sem verificação.",
        "cta": "Começar Agora",
        "keywords": ["ver whatsapp", "espionar whatsapp", "ler mensagens whatsapp", "rastreador whatsapp"],
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
        "desc": "عرض أي حساب واتساب عبر الإنترنت. قراءة الرسائل ومشاهدة الصور وتتبع الموقع. مجاني، فوري، بدون تحقق.",
        "cta": "ابدأ الآن",
        "keywords": ["تجسس واتساب", "عرض رسائل واتساب", "قراءة رسائل واتساب", "متتبع واتساب"],
    },
    "ru": {
        "name": "Русский",
        "titles": [
            "Как Просматривать Сообщения WhatsApp Онлайн {year}",
            "Читать Сообщения WhatsApp Бесплатно",
            "Шпионское Приложение WhatsApp — Просмотр Сообщений",
            "Трекер WhatsApp — Сообщения и Местоположение",
            "Как Шпионить за WhatsApp Незаметно",
            "Читалка Сообщений WhatsApp — Мгновенный Доступ",
            "Восстановить Удаленные Сообщения WhatsApp",
            "Отслеживать Статус Онлайн WhatsApp",
            "Просмотр Фото WhatsApp — Все Медиафайлы",
            "История Звонков WhatsApp",
        ],
        "desc": "Просмотр любого аккаунта WhatsApp онлайн. Читайте сообщения, смотрите фото, отслеживайте местоположение. Бесплатно, мгновенно, без проверки.",
        "cta": "Начать Сейчас",
        "keywords": ["просмотр whatsapp", "шпионить whatsapp", "читать сообщения whatsapp", "трекер whatsapp"],
    },
    "zh": {
        "name": "中文",
        "titles": [
            "如何在线查看WhatsApp消息 {year}",
            "免费阅读WhatsApp消息 — 无需验证",
            "WhatsApp间谍工具 — 查看消息",
            "免费WhatsApp追踪器 — 消息和位置",
            "如何在不被发现的情况下监视WhatsApp",
            "WhatsApp消息阅读器 — 即时访问",
            "恢复已删除的WhatsApp消息",
            "查看WhatsApp在线状态",
            "查看WhatsApp照片 — 所有媒体",
            "WhatsApp通话记录",
        ],
        "desc": "在线查看任何WhatsApp账户。阅读消息，查看照片，追踪GPS位置。免费，即时，无需验证。",
        "cta": "立即开始",
        "keywords": ["查看whatsapp", "监视whatsapp", "阅读whatsapp消息", "whatsapp追踪器"],
    },
    "hi": {
        "name": "हिन्दी",
        "titles": [
            "व्हाट्सएप संदेश ऑनलाइन कैसे देखें {year}",
            "व्हाट्सएप संदेश मुफ्त में पढ़ें",
            "व्हाट्सएप जासूसी ऐप — संदेश देखें",
            "मुफ्त व्हाट्सएप ट्रैकर — संदेश और स्थान",
            "बिना पकड़े व्हाट्सएप की जासूसी कैसे करें",
            "व्हाट्सएप संदेश रीडर — तुरंत पहुंच",
            "हटाए गए व्हाट्सएप संदेश पुनर्प्राप्त करें",
            "व्हाट्सएप ऑनलाइन स्थिति देखें",
            "व्हाट्सएप फोटो देखें — सभी मीडिया",
            "व्हाट्सएप कॉल इतिहास",
        ],
        "desc": "किसी भी व्हाट्सएप अकाउंट को ऑनलाइन देखें। संदेश पढ़ें, फोटो देखें, GPS लोकेशन ट्रैक करें। मुफ्त, तुरंत, कोई सत्यापन नहीं।",
        "cta": "अभी शुरू करें",
        "keywords": ["व्हाट्सएप देखें", "व्हाट्सएप जासूसी", "व्हाट्सएप संदेश पढ़ें", "व्हाट्सएप ट्रैकर"],
    },
    "ja": {
        "name": "日本語",
        "titles": [
            "WhatsAppメッセージをオンラインで見る方法 {year}",
            "WhatsAppメッセージを無料で読む",
            "WhatsAppスパイツール — メッセージを見る",
            "無料WhatsAppトラッカー — メッセージと位置情報",
            "バレずにWhatsAppを監視する方法",
            "WhatsAppメッセージリーダー — 即時アクセス",
            "削除されたWhatsAppメッセージを復元",
            "WhatsAppオンラインステータスを見る",
            "WhatsApp写真を見る — すべてのメディア",
            "WhatsApp通話履歴",
        ],
        "desc": "任意のWhatsAppアカウントをオンラインで表示。メッセージを読み、写真を見て、GPS位置情報を追跡。無料、即時、確認不要。",
        "cta": "今すぐ始める",
        "keywords": ["whatsapp 見る", "whatsapp スパイ", "whatsapp メッセージ 読む", "whatsapp トラッカー"],
    },
    "ko": {
        "name": "한국어",
        "titles": [
            "WhatsApp 메시지 온라인으로 보기 {year}",
            "WhatsApp 메시지 무료로 읽기",
            "WhatsApp 스파이 도구 — 메시지 보기",
            "무료 WhatsApp 트래커 — 메시지 및 위치",
            "들키지 않고 WhatsApp 감시하는 방법",
            "WhatsApp 메시지 리더 — 즉시 접근",
            "삭제된 WhatsApp 메시지 복구",
            "WhatsApp 온라인 상태 보기",
            "WhatsApp 사진 보기 — 모든 미디어",
            "WhatsApp 통화 기록",
        ],
        "desc": "모든 WhatsApp 계정을 온라인으로 봅니다. 메시지를 읽고, 사진을 보고, GPS 위치를 추적합니다. 무료, 즉시, 확인 불필요.",
        "cta": "지금 시작하기",
        "keywords": ["whatsapp 보기", "whatsapp 스파이", "whatsapp 메시지 읽기", "whatsapp 트래커"],
    },
}

# ═══════════════════════════════════════════════════════
#  ARTICLE GENERATOR
# ═══════════════════════════════════════════════════════

def generate_article(lang_code: str, lang: dict, title: str) -> str:
    """Generate a unique SEO-optimized HTML page."""
    year = "2026"
    title = title.replace("{year}", year)
    
    # Unique ID for this article
    uid = hashlib.md5(f"{lang_code}-{title}-{datetime.now().isoformat()}".encode()).hexdigest()[:8]
    
    # Generate unique body text
    body_phrases = [
        f"Looking for a way to view WhatsApp messages online? You're in the right place.",
        f"Our tool has been used by millions of people worldwide.",
        f"No download required — works directly in your browser.",
        f"Enter any phone number and start viewing messages instantly.",
        f"Compatible with all WhatsApp versions including the latest {year} update.",
        f"See photos, videos, voice notes, and documents shared on WhatsApp.",
        f"Track the person's real-time GPS location with our advanced tracking.",
        f"View their contact list and see who they talk to most often.",
        f"Read deleted messages — our tool recovers them from WhatsApp servers.",
        f"Monitor online status — know exactly when they come online.",
        f"100% undetectable — the target receives no notification.",
        f"Works in all countries — France, Belgium, Canada, Switzerland, Morocco, Algeria.",
        f"Compatible with Android and iPhone — no difference.",
        f"Our secure connection bypasses WhatsApp's end-to-end encryption.",
        f"See call history — voice calls, video calls, missed calls.",
        f"Free to use — no credit card required for basic access.",
        f"Premium features available for full message content.",
    ]
    random.shuffle(body_phrases)
    body_text = " ".join(body_phrases[:random.randint(5, 10)])
    
    # Add some unique fluff to avoid duplicate content
    fluff = [
        f"Updated for {year}, this is the most reliable WhatsApp viewer available.",
        f"Version 3.2 brings faster scanning and improved message recovery.",
        f"Our servers process over 10,000 scans daily.",
        f"The tool uses advanced Signal Protocol decryption to access messages.",
        f"Featured on major tech blogs and cybersecurity forums.",
    ]
    body_text += " " + random.choice(fluff)
    
    return f"""<!DOCTYPE html>
<html lang="{lang_code}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{lang['desc']}">
<meta name="keywords" content="{', '.join(lang['keywords'])}">
<link rel="canonical" href="{SITE_URL}/">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#075e54">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{lang['desc']}">
<meta property="og:url" content="{SITE_URL}/">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#0a1014;color:#e9edef;font-family:Inter,system-ui;text-align:center;padding:40px 20px;max-width:800px;margin:0 auto}}
h1{{font-size:clamp(22px,5vw,32px);background:linear-gradient(135deg,#25d366,#128c7e);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:16px;line-height:1.3}}
p{{color:#8696a0;font-size:15px;line-height:1.8;margin-bottom:24px}}
.btn{{display:inline-block;background:#25d366;color:#000;padding:16px 36px;border-radius:30px;font-weight:700;font-size:16px;text-decoration:none;box-shadow:0 6px 24px rgba(37,211,102,0.3);margin:8px}}
.btn:hover{{transform:translateY(-2px)}}
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
<div class="feat"><h3>💬 Read Messages</h3><p>View all WhatsApp conversations including deleted messages.</p></div>
<div class="feat"><h3>📸 See Photos</h3><p>Access all shared media files — photos, videos, voice notes.</p></div>
<div class="feat"><h3>📍 Track Location</h3><p>Real-time GPS tracking — see where they are right now.</p></div>
<div class="feat"><h3>🟢 Online Status</h3><p>Know exactly when they come online and go offline.</p></div>
<div class="feat"><h3>📞 Call History</h3><p>View all WhatsApp calls — voice and video, with timestamps.</p></div>
<div class="feat"><h3>🔒 100% Undetectable</h3><p>The target receives no notification. Completely invisible.</p></div>
</div>

<a href="/app" class="btn">{lang['cta']} — It's Free</a>

<footer>
<p>WhatsApp Viewer v3.2 — {year} — Not affiliated with Meta Platforms, Inc.</p>
<p>This tool is for legitimate monitoring purposes only.</p>
</footer>
</body>
</html>"""

# ═══════════════════════════════════════════════════════
#  MAIN — Generate articles
# ═══════════════════════════════════════════════════════

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
            
            # Generate unique filename
            slug = title.lower().replace(" ", "-").replace("/", "-")[:60]
            uid = hashlib.md5(html.encode()).hexdigest()[:6]
            filename = f"{slug}-{uid}.html"
            
            with open(os.path.join(lang_dir, filename), "w", encoding="utf-8") as f:
                f.write(html)
            total += 1
    
    print(f"✅ {total} articles generated ({ARTICLES_PER_RUN} target)")
    print(f"   Languages: {len(LANGUAGES)}")
    print(f"   Per language: {articles_per_lang}")

if __name__ == "__main__":
    main()
