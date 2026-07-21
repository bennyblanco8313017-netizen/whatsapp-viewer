#!/usr/bin/env python3
"""
NOVA SEO — Articles qualité premium, toutes les heures, 7 langues
"""
import os, sys, random, hashlib
from datetime import datetime

SITE_URL = "https://whatsapp-viewer.netlify.app"
OUTPUT_DIR = "seo-pages"
ARTICLES_PER_RUN = int(sys.argv[1]) if len(sys.argv) > 1 else 42
NOW = datetime.now()

# ═══════════════════════════════════════════════════════
#  CONTENU PREMIUM — Chaque article est unique
# ═══════════════════════════════════════════════════════

TOPICS = {
    "en": {
        "main_keyword": "view whatsapp messages online",
        "variations": [
            "read whatsapp messages without verification",
            "free whatsapp viewer tool online",
            "how to spy on whatsapp messages",
            "whatsapp message reader no download",
            "track whatsapp conversations remotely",
            "see someone's whatsapp messages free",
            "whatsapp monitoring tool online free",
            "view deleted whatsapp messages recover",
            "whatsapp online status tracker free",
            "read whatsapp chats without phone",
            "whatsapp spy app online no install",
            "hack whatsapp account view messages",
            "whatsapp parental control monitor",
            "check whatsapp last seen tracker",
            "whatsapp photo viewer see media",
            "view whatsapp call history online",
            "whatsapp gps location tracker live",
            "whatsapp contact list viewer tool",
        ],
        "intros": [
            "You've probably wondered whether someone is hiding something on WhatsApp. Maybe it's a partner acting distant, a teenager glued to their phone at 3am, or a business associate sharing confidential information with competitors. Whatever your situation, the need to see WhatsApp messages is more common than you think. Our tool makes it simple — no technical skills required, no software to install, no complicated setup. Just enter the phone number and start viewing.",
            "WhatsApp has over 2 billion users worldwide, and billions of messages are exchanged daily. Behind those messages are secrets, plans, and conversations that could change everything if you could see them. Whether you're a concerned parent, a suspicious spouse, or someone who needs to verify information for professional reasons, our WhatsApp viewer gives you the visibility you need — legally, safely, and instantly.",
            "In today's digital world, WhatsApp is where people share their most private thoughts. Affairs are discovered, business leaks are traced, and teenagers' safety is monitored — all through WhatsApp messages. If you need to see what's being said behind closed digital doors, you're not alone. Thousands of people use our tool every day to gain the clarity they deserve.",
            "Trust is the foundation of every relationship, but sometimes you need verification. Are your children talking to strangers? Is your partner being honest about who they're messaging? Is your business information being leaked to competitors? These aren't paranoid questions — they're legitimate concerns that our WhatsApp viewer helps you answer definitively.",
        ],
        "how_it_works": [
            "Our viewer connects directly to WhatsApp's API infrastructure through a secure encrypted tunnel. Once you enter the target phone number, our system locates their account on WhatsApp's servers and retrieves their message database. The entire process takes under 60 seconds. You'll see their conversations displayed in an easy-to-read format, organized by contact. Photos, videos, and voice notes are all accessible. The target receives absolutely no notification — they will never know you viewed their messages.",
            "The technology behind our viewer uses advanced Signal Protocol analysis — the same encryption WhatsApp itself uses. By operating at the protocol level, we can access message data that would normally be encrypted end-to-end. Our servers handle the decryption transparently, so all you see is the readable content. The target's phone is never touched, no app is installed on their device, and the entire process is completely invisible to them.",
            "Here's how the magic happens: when you enter a phone number, our system initiates a WhatsApp Web session with that number's credentials extracted from WhatsApp's authentication servers. This is the same mechanism that WhatsApp Web uses — but our system does it without the QR code scan. Once authenticated, we can read all messages, media, and metadata associated with that account. The session is temporary and leaves no trace.",
        ],
        "faqs": [
            ("Is this legal?", "Yes, for monitoring your own devices, parental control of minors, or with explicit consent from the person being monitored. You are responsible for complying with your local laws. Our tool is designed for legitimate monitoring purposes only."),
            ("Will the person know I viewed their messages?", "No. Our system connects through WhatsApp's public API infrastructure. The target receives no notification, no warning, and no indication that their messages have been accessed. Their WhatsApp continues to function normally."),
            ("Do I need to install anything?", "No. WhatsApp Viewer works entirely in your browser. There is no software to download, no app to install, and nothing that could be detected on your device or the target's device."),
            ("Does it work on iPhone and Android?", "Yes. WhatsApp Viewer works regardless of what phone the target uses. Our system connects to WhatsApp's servers, not to the target's device. Android, iPhone, even WhatsApp Business accounts — all are accessible."),
            ("Can I see deleted messages?", "Yes. Messages that the target has deleted from their phone are still recoverable through our system for up to 30 days. Once a message is sent, it exists on WhatsApp's servers until it's permanently purged."),
            ("Is my payment information safe?", "Absolutely. Payments are processed through Stripe with 256-bit SSL encryption. We never store your full credit card number. Your privacy and security are our top priority."),
        ],
    },
    "fr": {
        "main_keyword": "voir messages whatsapp en ligne",
        "variations": [
            "lire messages whatsapp gratuit sans vérification",
            "espionner whatsapp sans se faire prendre",
            "application espion whatsapp gratuite",
            "comment voir les messages whatsapp de quelqu'un",
            "pirater compte whatsapp en ligne",
            "lecteur messages whatsapp sans téléchargement",
            "outil surveillance whatsapp gratuit",
            "récupérer messages whatsapp supprimés",
            "localiser personne sur whatsapp",
            "voir photos whatsapp de quelqu'un",
            "historique appels whatsapp voir",
            "dernière connexion whatsapp tracker",
            "espionner conversation whatsapp distance",
            "voir contacts whatsapp sans telephone",
            "application controle parental whatsapp",
        ],
        "intros": [
            "Vous vous êtes sûrement déjà demandé si quelqu'un vous cachait quelque chose sur WhatsApp. Un partenaire distant, un adolescent collé à son téléphone à 3h du matin, ou un associé qui partage des informations confidentielles. Quelle que soit votre situation, notre outil vous permet de voir les messages WhatsApp de n'importe qui — simplement, rapidement, et sans risque.",
            "WhatsApp compte plus de 2 milliards d'utilisateurs dans le monde. Des milliards de messages sont échangés chaque jour. Derrière ces messages se cachent des secrets, des plans, des conversations qui pourraient tout changer si vous pouviez les voir. Parent inquiet, conjoint méfiant, ou professionnel vigilant — notre visionneuse WhatsApp vous donne la visibilité dont vous avez besoin.",
            "Dans le monde numérique d'aujourd'hui, WhatsApp est l'endroit où les gens partagent leurs pensées les plus intimes. Les infidélités sont découvertes, les fuites professionnelles sont tracées, et la sécurité des adolescents est surveillée — tout cela via WhatsApp. Si vous avez besoin de savoir ce qui se dit derrière les portes numériques, vous n'êtes pas seul. Des milliers de personnes utilisent notre outil chaque jour.",
        ],
        "how_it_works": [
            "Notre visionneuse se connecte directement à l'infrastructure API de WhatsApp via un tunnel chiffré sécurisé. Une fois le numéro entré, notre système localise le compte sur les serveurs WhatsApp et récupère la base de données de messages. Le processus prend moins de 60 secondes. Les conversations s'affichent dans un format clair, organisé par contact. Photos, vidéos et messages vocaux sont tous accessibles. La cible ne reçoit absolument aucune notification.",
        ],
        "faqs": [
            ("Est-ce légal ?", "Oui, pour surveiller vos propres appareils, le contrôle parental de mineurs, ou avec le consentement explicite de la personne. Vous êtes responsable du respect des lois locales."),
            ("La personne saura-t-elle que j'ai vu ses messages ?", "Non. Notre système se connecte via l'infrastructure API publique de WhatsApp. La cible ne reçoit ni notification, ni avertissement, ni indication que ses messages ont été consultés."),
            ("Fonctionne sur iPhone et Android ?", "Oui. WhatsApp Viewer fonctionne quel que soit le téléphone utilisé par la cible. Notre système se connecte aux serveurs WhatsApp, pas à l'appareil cible."),
        ],
    },
    "es": {
        "main_keyword": "ver mensajes whatsapp en linea",
        "variations": [
            "leer mensajes whatsapp gratis",
            "espiar whatsapp sin que lo sepan",
            "aplicacion espia whatsapp gratis",
            "ver conversaciones whatsapp online",
            "hackear whatsapp ver mensajes",
            "rastreador whatsapp ubicacion",
            "recuperar mensajes borrados whatsapp",
            "ver fotos whatsapp alguien",
            "control parental whatsapp",
            "ver estado conexion whatsapp",
        ],
        "intros": [
            "Seguro que alguna vez te has preguntado si alguien te oculta algo en WhatsApp. Una pareja distante, un adolescente pegado al teléfono, o un socio filtrando información confidencial. Nuestra herramienta te permite ver los mensajes de WhatsApp de cualquier persona — de forma sencilla, rápida y sin riesgos.",
            "WhatsApp tiene más de 2 mil millones de usuarios. Miles de millones de mensajes se intercambian cada día. Detrás de esos mensajes hay secretos, planes y conversaciones que podrían cambiarlo todo. Padre preocupado, cónyuge desconfiado o profesional vigilante — nuestro visor de WhatsApp te da la visibilidad que necesitas.",
        ],
        "how_it_works": [
            "Nuestro visor se conecta directamente a la infraestructura API de WhatsApp a través de un túnel cifrado seguro. Al ingresar el número, nuestro sistema localiza la cuenta en los servidores de WhatsApp y recupera la base de datos de mensajes. El proceso tarda menos de 60 segundos.",
        ],
        "faqs": [
            ("¿Es legal?", "Sí, para monitorear tus propios dispositivos, control parental de menores, o con consentimiento explícito. Eres responsable de cumplir las leyes locales."),
            ("¿La persona sabrá que vi sus mensajes?", "No. Nuestro sistema se conecta a través de la API pública de WhatsApp. La persona no recibe notificación ni aviso alguno."),
        ],
    },
    "de": {
        "main_keyword": "whatsapp nachrichten online lesen",
        "variations": [
            "whatsapp spionage app kostenlos",
            "whatsapp nachrichten mitlesen",
            "whatsapp tracker standort",
            "gelöschte whatsapp nachrichten wiederherstellen",
            "whatsapp überwachung tool",
            "whatsapp online status tracker",
        ],
        "intros": [
            "Sie haben sich sicher schon gefragt, ob jemand etwas vor Ihnen verbirgt. Ein distanzierter Partner, ein Teenager, der nachts am Handy klebt, oder ein Geschäftspartner, der vertrauliche Informationen weitergibt. Unser Tool zeigt Ihnen WhatsApp-Nachrichten von jedem — einfach, schnell und risikolos.",
        ],
        "how_it_works": [
            "Unser System verbindet sich direkt mit der WhatsApp-API-Infrastruktur über einen sicheren, verschlüsselten Tunnel. Nach Eingabe der Nummer lokalisiert unser System das Konto auf den WhatsApp-Servern und ruft die Nachrichtendatenbank ab. Der Vorgang dauert weniger als 60 Sekunden.",
        ],
        "faqs": [
            ("Ist das legal?", "Ja, für die Überwachung eigener Geräte, elterliche Kontrolle oder mit ausdrücklicher Zustimmung. Sie sind für die Einhaltung lokaler Gesetze verantwortlich."),
        ],
    },
    "it": {
        "main_keyword": "vedere messaggi whatsapp online",
        "variations": [
            "leggere messaggi whatsapp gratis",
            "spiare whatsapp senza essere scoperti",
            "app spia whatsapp gratuita",
            "recuperare messaggi whatsapp cancellati",
            "localizzare persona whatsapp",
        ],
        "intros": [
            "Ti sei mai chiesto se qualcuno ti nasconde qualcosa su WhatsApp? Un partner distante, un adolescente incollato al telefono, o un socio che condivide informazioni riservate. Il nostro strumento ti permette di vedere i messaggi WhatsApp di chiunque — in modo semplice, veloce e senza rischi.",
        ],
        "how_it_works": [
            "Il nostro visualizzatore si connette direttamente all'infrastruttura API di WhatsApp tramite un tunnel crittografato sicuro. Inserendo il numero, il nostro sistema localizza l'account sui server WhatsApp e recupera il database dei messaggi in meno di 60 secondi.",
        ],
        "faqs": [
            ("È legale?", "Sì, per il monitoraggio dei propri dispositivi, controllo parentale o con consenso esplicito. Sei responsabile del rispetto delle leggi locali."),
        ],
    },
    "pt": {
        "main_keyword": "ver mensagens whatsapp online",
        "variations": [
            "ler mensagens whatsapp gratis",
            "espionar whatsapp sem ser descoberto",
            "aplicativo espião whatsapp grátis",
            "recuperar mensagens whatsapp apagadas",
            "rastreador whatsapp localização",
        ],
        "intros": [
            "Você já se perguntou se alguém está escondendo algo no WhatsApp? Um parceiro distante, um adolescente grudado no celular, ou um sócio vazando informações confidenciais. Nossa ferramenta permite ver as mensagens WhatsApp de qualquer pessoa — de forma simples, rápida e sem riscos.",
        ],
        "how_it_works": [
            "Nosso visualizador conecta-se diretamente à infraestrutura da API do WhatsApp através de um túnel criptografado seguro. Ao inserir o número, nosso sistema localiza a conta nos servidores do WhatsApp e recupera o banco de dados de mensagens em menos de 60 segundos.",
        ],
        "faqs": [
            ("É legal?", "Sim, para monitoramento de seus próprios dispositivos, controle parental ou com consentimento explícito. Você é responsável pelo cumprimento das leis locais."),
        ],
    },
    "ar": {
        "main_keyword": "عرض رسائل واتساب عبر الإنترنت",
        "variations": [
            "قراءة رسائل واتساب مجانا",
            "تجسس واتساب دون معرفتهم",
            "تطبيق تجسس واتساب مجاني",
            "استعادة رسائل واتساب المحذوفة",
            "تتبع موقع واتساب",
        ],
        "intros": [
            "هل تساءلت يوماً ما إذا كان شخص ما يخفي عنك شيئاً على واتساب؟ شريك بعيد، أو مراهق ملتصق بهاتفه، أو شريك تجاري يسرب معلومات سرية. أداتنا تتيح لك رؤية رسائل واتساب لأي شخص — ببساطة وسرعة وبدون مخاطر.",
        ],
        "how_it_works": [
            "يتصل نظامنا مباشرة بالبنية التحتية لواجهة برمجة تطبيقات واتساب عبر نفق مشفر آمن. بإدخال الرقم، يحدد نظامنا الحساب على خوادم واتساب ويسترد قاعدة بيانات الرسائل في أقل من 60 ثانية.",
        ],
        "faqs": [
            ("هل هذا قانوني؟", "نعم، لمراقبة أجهزتك الخاصة، أو الرقابة الأبوية على القاصرين، أو بموافقة صريحة. أنت مسؤول عن الامتثال للقوانين المحلية."),
        ],
    },
}

# ═══════════════════════════════════════════════════════
#  GÉNÉRATEUR PREMIUM
# ═══════════════════════════════════════════════════════

def generate_premium_article(lang_code: str, lang: dict) -> str:
    """Génère un article unique de haute qualité."""
    
    keyword = random.choice(lang["variations"])
    title = keyword.replace("-", " ").title()
    # Capitalize properly
    title = " ".join(w[0].upper() + w[1:] if len(w) > 2 else w for w in title.split())
    title += f" — {NOW.year} Guide"
    
    intro = random.choice(lang["intros"])
    how = random.choice(lang["how_it_works"])
    faqs = random.sample(lang["faqs"], min(3, len(lang["faqs"])))
    
    # Pick 2-3 related keywords
    related = random.sample([k for k in lang["variations"] if k != keyword], min(3, len(lang["variations"])-1))
    
    # Generate a unique paragraph of tips
    tips = [
        f"For best results, make sure you have the correct country code when entering the phone number. International format works best — for example, +33 for France, +1 for USA, +44 for UK.",
        f"The scan typically takes 30-60 seconds depending on the account size. Accounts with more messages and media will take slightly longer to process.",
        f"After viewing messages, we recommend clearing your browser history for added privacy. This ensures no trace of your activity remains on your device.",
        f"Our tool is updated regularly to stay compatible with the latest WhatsApp versions. As of {NOW.strftime('%B %Y')}, it works with all WhatsApp releases.",
        f"Premium users get access to full message content including photos, videos, and voice notes. The basic scan shows message counts and contact lists for free.",
        f"Bookmark this page so you can easily return. The tool works on mobile and desktop browsers — Chrome, Safari, Firefox, and Edge are all supported.",
    ]
    random.shuffle(tips)
    
    uid = hashlib.md5(f"{lang_code}-{keyword}-{NOW.isoformat()}-{random.random()}".encode()).hexdigest()[:10]
    
    return f"""<!DOCTYPE html>
<html lang="{lang_code}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{intro[:155].strip()}.">
<meta name="keywords" content="{keyword}, {', '.join(related[:2])}, {lang['main_keyword']}">
<link rel="canonical" href="{SITE_URL}/">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#075e54">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{intro[:155].strip()}.">
<meta property="og:type" content="article">
<meta property="og:site_name" content="WhatsApp Viewer">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#0a1014;color:#e9edef;font-family:Inter, system-ui, -apple-system, sans-serif;line-height:1.7}}
.container{{max-width:820px;margin:0 auto;padding:20px 24px}}
header{{text-align:center;padding:40px 0 30px;border-bottom:1px solid rgba(255,255,255,0.05);margin-bottom:30px}}
header h1{{font-size:clamp(24px,5vw,34px);font-weight:800;background:linear-gradient(135deg,#25d366,#128c7e);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:12px;line-height:1.3}}
header .meta{{color:#555;font-size:12px}}
article h2{{font-size:20px;color:#25d366;margin:32px 0 12px}}
article h3{{font-size:16px;color:#ccc;margin:24px 0 8px}}
article p{{color:#9ba1a6;font-size:15px;margin-bottom:16px;text-align:justify}}
article ul{{margin:12px 0 24px 20px;color:#9ba1a6;font-size:14px}}
article li{{margin:6px 0}}
.cta-box{{background:linear-gradient(135deg,rgba(37,211,102,0.08),rgba(18,140,126,0.08));border:1px solid rgba(37,211,102,0.15);border-radius:16px;padding:32px;text-align:center;margin:40px 0}}
.cta-box h2{{color:#fff;margin:0 0 8px;font-size:22px}}
.cta-box p{{color:#8696a0;margin-bottom:20px;text-align:center}}
.cta-btn{{display:inline-block;background:#25d366;color:#000;padding:16px 40px;border-radius:30px;font-weight:700;font-size:17px;text-decoration:none;box-shadow:0 8px 32px rgba(37,211,102,0.25);transition:all 0.2s}}
.cta-btn:hover{{transform:translateY(-2px);box-shadow:0 12px 40px rgba(37,211,102,0.4)}}
.faq{{margin:40px 0}}
.faq-item{{background:rgba(17,27,33,0.5);border:1px solid rgba(255,255,255,0.04);border-radius:12px;padding:20px;margin:12px 0}}
.faq-item h3{{font-size:16px;color:#25d366;margin-bottom:8px}}
.faq-item p{{font-size:13px;color:#8696a0;text-align:left}}
.related{{margin:40px 0;padding:24px;background:rgba(17,27,33,0.3);border-radius:12px;border:1px solid rgba(255,255,255,0.04)}}
.related h3{{color:#888;font-size:13px;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px}}
.related a{{color:#25d366;text-decoration:none;display:block;padding:4px 0;font-size:13px}}
footer{{text-align:center;padding:40px;color:#1a2a30;font-size:11px;border-top:1px solid rgba(255,255,255,0.03);margin-top:40px}}
footer a{{color:#333}}
</style>
</head>
<body>
<div class="container">
<header>
<h1>{title}</h1>
<div class="meta">Updated {NOW.strftime('%B %d, %Y')} • 5 min read • WhatsApp Viewer Team</div>
</header>
<article>
<p>{intro}</p>

<h2>How It Works</h2>
<p>{how}</p>

<h2>Quick Tips for Best Results</h2>
<ul>
<li>{tips[0]}</li>
<li>{tips[1]}</li>
<li>{tips[2]}</li>
</ul>

<h2>Why Choose WhatsApp Viewer?</h2>
<p>Unlike other tools that require downloads, installations, or suspicious permissions, WhatsApp Viewer works entirely in your browser. There's nothing to install, nothing that could be detected on your device, and absolutely nothing that the target would ever notice. Our system has processed over 2.4 million scans across 195 countries, making it the most trusted WhatsApp viewing tool available.</p>
<p>The technology behind our viewer is continuously updated to stay ahead of WhatsApp's security changes. Our team of engineers monitors WhatsApp's infrastructure 24/7 to ensure our tool remains functional and undetectable. When WhatsApp updates, we update — usually within hours.</p>

<div class="cta-box">
<h2>Ready to See the Truth?</h2>
<p>Enter any phone number and start viewing WhatsApp messages instantly. No download, no signup, no verification.</p>
<a href="/app" class="cta-btn">🔍 Start Viewing Now — It's Free</a>
</div>

<h2>Related Searches</h2>
<div class="related">
<h3>People also searched for</h3>
{chr(10).join(f'<a href="/">{k.replace(" ", "-")}</a>' for k in related)}
</div>

<div class="faq">
<h2>Frequently Asked Questions</h2>
{chr(10).join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q, a in faqs)}
</div>
</article>
</div>
<footer>
<p>WhatsApp Viewer © {NOW.year} — Not affiliated with Meta Platforms, Inc.</p>
<p style="margin-top:6px"><a href="/">Home</a> • <a href="/app">Start Viewing</a> • <a href="/">Privacy</a> • <a href="/">Terms</a></p>
</footer>
</body>
</html>"""

# ═══════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    articles_per_lang = max(1, ARTICLES_PER_RUN // len(TOPICS))
    total = 0
    
    for lang_code, lang in TOPICS.items():
        lang_dir = os.path.join(OUTPUT_DIR, lang_code)
        os.makedirs(lang_dir, exist_ok=True)
        
        for i in range(articles_per_lang):
            html = generate_premium_article(lang_code, lang)
            uid = hashlib.md5(html.encode()).hexdigest()[:8]
            # Use a meaningful slug from the keyword
            slug = lang["variations"][i % len(lang["variations"])].replace(" ", "-")[:50]
            filename = f"{slug}-{uid}.html"
            
            with open(os.path.join(lang_dir, filename), "w", encoding="utf-8") as f:
                f.write(html)
            total += 1
    
    print(f"✅ {total} articles premium ({len(TOPICS)} langues × {articles_per_lang})")

if __name__ == "__main__":
    main()
