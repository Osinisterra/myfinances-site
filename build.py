#!/usr/bin/env python3
"""Genera las páginas públicas de MyFinances (privacidad y soporte) en español, inglés y portugués.
Uso: python3 build.py  → escribe los .html junto a este archivo (GitHub Pages los sirve tal cual)."""
from pathlib import Path

ROOT = Path(__file__).parent
REPO = "https://github.com/Osinisterra/myfinances-site"
EMAIL = "omarsinisterra00@gmail.com"
CONTACT = "mailto:" + EMAIL + "?subject=MyFinances"
UPDATED = {"es": "21 de noviembre de 2026", "en": "November 21, 2026", "pt": "21 de novembro de 2026"}

# Rutas de cada página por idioma (relativas a la raíz del sitio).
PATHS = {
    "privacy": {"es": "privacidad/", "en": "en/privacy/", "pt": "pt/privacidade/"},
    "support": {"es": "soporte/", "en": "en/support/", "pt": "pt/suporte/"},
    "home": {"es": "", "en": "en/", "pt": "pt/"},
}
LANG_NAMES = {"es": "Español", "en": "English", "pt": "Português"}

UI = {
    "es": {"privacy": "Privacidad", "support": "Soporte", "updated": "Última actualización",
           "tagline": "Tus cuentas, tarjetas e inversiones en un solo lugar, al día con tus correos y extractos.",
           "home_lead": "MyFinances es una app de finanzas personales para iPhone y Android. Tus datos se quedan en tu teléfono: sin servidores y sin cuentas que crear."},
    "en": {"privacy": "Privacy", "support": "Support", "updated": "Last updated",
           "tagline": "Your accounts, cards and investments in one place, kept up to date with your emails and statements.",
           "home_lead": "MyFinances is a personal finance app for iPhone and Android. Your data stays on your phone: no servers and no accounts to create."},
    "pt": {"privacy": "Privacidade", "support": "Suporte", "updated": "Última atualização",
           "tagline": "Suas contas, cartões e investimentos em um só lugar, atualizados com seus e-mails e extratos.",
           "home_lead": "MyFinances é um app de finanças pessoais para iPhone e Android. Seus dados ficam no seu telefone: sem servidores e sem contas para criar."},
}

PRIVACY = {
"es": f"""
<h1>Política de privacidad</h1>
<p class="lead">Resumen: <strong>MyFinances no recopila tus datos.</strong> No hay servidores propios, cuentas de usuario, publicidad, analítica ni rastreo. El desarrollador no puede ver tu información.</p>

<h2>Dónde se guardan tus datos</h2>
<p>Tus cuentas, movimientos, extractos, inversiones y presupuestos se guardan en tu iPhone, protegidos por el cifrado del dispositivo. Si tienes iCloud activo, la app los sincroniza con <strong>tu propio iCloud</strong> (base de datos privada de CloudKit), que solo tú puedes leer. Las claves de los extractos, la clave de la IA y la sesión del correo se guardan en el Llavero del iPhone y no se sincronizan.</p>

<h2>Correo (opcional)</h2>
<p>Si conectas Gmail u Outlook, la app pide permiso <strong>de solo lectura</strong> y busca únicamente los correos de los remitentes de tu banco (avisos de compras, transferencias y extractos). Esos correos se leen y se procesan en tu iPhone; no se envían a ningún servidor del desarrollador. Puedes desconectar el correo cuando quieras desde Ajustes o desde la configuración de seguridad de tu cuenta de Google o Microsoft.</p>
<p>El uso de la información recibida de las API de Google cumple la <a href="https://developers.google.com/terms/api-services-user-data-policy">Política de datos de usuario de los servicios de API de Google</a>, incluidos los requisitos de uso limitado.</p>

<h2>Extractos en PDF</h2>
<p>Los extractos que importas (o que llegan a tu correo, si lo autorizas) se abren y se leen en tu iPhone.</p>

<h2>Inteligencia artificial (opcional, apagada por defecto)</h2>
<p>Solo si la activas y pones tu propia clave de Anthropic, y aceptas el aviso de permiso dentro de la app, MyFinances envía a Anthropic el texto de un extracto o correo que ningún lector entiende y los nombres de comercios que no conoce, para leerlos y categorizarlos. Antes de enviarla, la app <strong>quita los datos personales</strong>: correos, números de documento, números de cuenta y tarjeta, teléfonos y el nombre del titular. El envío va directamente de tu iPhone a Anthropic con tu clave y se rige por las políticas de Anthropic.</p>

<h2>En Android</h2>
<p>Tus cuentas, movimientos, extractos e inversiones se guardan en el almacenamiento privado de la app en tu teléfono. No hay sincronización en la nube; el respaldo es un archivo que tú guardas donde quieras.</p>
<p><strong>Lectura de notificaciones (opcional).</strong> Solo si la activas, después de un aviso que explica qué hace, la app lee las notificaciones de las apps de tus bancos (por ejemplo Bancolombia, Nequi, Nu, Davivienda) y los SMS que vengan de un banco, para registrar compras y transferencias. Las notificaciones de cualquier otra app se ignoran y no se guardan. Todo se procesa en tu teléfono y nada se envía a ningún servidor. Puedes apagarla cuando quieras en los ajustes del teléfono.</p>
<p><strong>Extractos en PDF.</strong> Los abres tú desde el teléfono; si tienen clave, la escribes para abrirlos y no se guarda.</p>
<p><strong>Borrar tus datos en Android:</strong> desinstala la app o ve a Ajustes del teléfono → Apps → MyFinances → Almacenamiento → Borrar datos.</p>

<h2>Tasa de cambio</h2>
<p>Para mostrar los dólares en pesos, la app consulta la TRM oficial en datos.gov.co. Esa consulta no incluye ningún dato tuyo.</p>

<h2>Notificaciones</h2>
<p>Los avisos (pagos de tarjeta, presupuestos, extractos) se generan en tu iPhone.</p>

<h2>Borrar tus datos</h2>
<p>Borra la app del iPhone. Si usaste iCloud, ve a Ajustes del iPhone → tu nombre → iCloud → Administrar almacenamiento → MyFinances → Eliminar datos.</p>

<h2>Menores de edad</h2>
<p>MyFinances no está dirigida a menores de 13 años.</p>

<h2>Cambios y contacto</h2>
<p>Si esta política cambia, se publicará aquí con la nueva fecha. Para preguntas, escribe en <a href="../soporte/">Soporte</a>.</p>
""",
"en": f"""
<h1>Privacy policy</h1>
<p class="lead">In short: <strong>MyFinances does not collect your data.</strong> There are no developer servers, user accounts, ads, analytics or tracking. The developer cannot see your information.</p>

<h2>Where your data is stored</h2>
<p>Your accounts, transactions, statements, investments and budgets are stored on your iPhone, protected by device encryption. If iCloud is on, the app syncs them to <strong>your own iCloud</strong> (CloudKit private database), which only you can read. Statement passwords, the AI key and the email session are kept in the iPhone Keychain and are not synced.</p>

<h2>Email (optional)</h2>
<p>If you connect Gmail or Outlook, the app requests <strong>read-only</strong> access and only looks for emails from your bank's senders (purchase and transfer alerts, statements). Those emails are read and processed on your iPhone; they are never sent to any developer server. You can disconnect email at any time from Settings or from your Google or Microsoft account security settings.</p>
<p>MyFinances' use of information received from Google APIs adheres to the <a href="https://developers.google.com/terms/api-services-user-data-policy">Google API Services User Data Policy</a>, including the Limited Use requirements.</p>

<h2>PDF statements</h2>
<p>Statements you import (or that arrive in your email, if you allow it) are opened and read on your iPhone.</p>

<h2>Artificial intelligence (optional, off by default)</h2>
<p>Only if you turn it on and enter your own Anthropic key, and accept the permission prompt in the app, MyFinances sends Anthropic the text of a statement or email that no reader understands and the names of unknown merchants, to read and categorize them. Before sending, the app <strong>removes personal data</strong>: emails, ID numbers, account and card numbers, phone numbers and the account holder's name. The request goes straight from your iPhone to Anthropic with your key and is governed by Anthropic's policies.</p>

<h2>On Android</h2>
<p>Your accounts, transactions, statements and investments are stored in the app's private storage on your phone. There's no cloud sync; backups are a file you save wherever you choose.</p>
<p><strong>Notification reading (optional).</strong> Only if you turn it on, after a notice that explains what it does, the app reads notifications from your banking apps (for example Bancolombia, Nequi, Nu, Davivienda) and text messages from a bank, to record purchases and transfers. Notifications from any other app are ignored and never stored. Everything is processed on your phone and nothing is sent to any server. You can turn it off anytime in your phone settings.</p>
<p><strong>PDF statements.</strong> You open them from your phone; if they have a password, you type it to open them and it isn't saved.</p>
<p><strong>Delete your data on Android:</strong> uninstall the app, or go to phone Settings → Apps → MyFinances → Storage → Clear data.</p>

<h2>Exchange rate</h2>
<p>To show dollars in pesos, the app fetches the official exchange rate (TRM) from datos.gov.co. That request contains none of your data.</p>

<h2>Notifications</h2>
<p>Alerts (card payments, budgets, statements) are created on your iPhone.</p>

<h2>Deleting your data</h2>
<p>Delete the app from your iPhone. If you used iCloud, go to iPhone Settings → your name → iCloud → Manage Storage → MyFinances → Delete Data.</p>

<h2>Children</h2>
<p>MyFinances is not directed to children under 13.</p>

<h2>Changes and contact</h2>
<p>Any change to this policy will be posted here with a new date. For questions, see <a href="../support/">Support</a>.</p>
""",
"pt": f"""
<h1>Política de privacidade</h1>
<p class="lead">Em resumo: <strong>o MyFinances não coleta seus dados.</strong> Não há servidores do desenvolvedor, contas de usuário, anúncios, análises nem rastreamento. O desenvolvedor não pode ver suas informações.</p>

<h2>Onde seus dados ficam</h2>
<p>Suas contas, movimentações, extratos, investimentos e orçamentos ficam no seu iPhone, protegidos pela criptografia do aparelho. Se o iCloud estiver ativo, o app os sincroniza com <strong>o seu próprio iCloud</strong> (banco de dados privado do CloudKit), que só você pode ler. As senhas dos extratos, a chave da IA e a sessão do e-mail ficam nas Chaves do iPhone e não são sincronizadas.</p>

<h2>E-mail (opcional)</h2>
<p>Se você conectar o Gmail ou o Outlook, o app pede acesso <strong>somente leitura</strong> e procura apenas os e-mails dos remetentes do seu banco (avisos de compras, transferências e extratos). Esses e-mails são lidos e processados no seu iPhone; nunca são enviados a servidores do desenvolvedor. Você pode desconectar o e-mail quando quiser nos Ajustes ou nas configurações de segurança da sua conta Google ou Microsoft.</p>
<p>O uso de informações recebidas das APIs do Google segue a <a href="https://developers.google.com/terms/api-services-user-data-policy">Política de dados do usuário dos serviços de API do Google</a>, incluindo os requisitos de uso limitado.</p>

<h2>Extratos em PDF</h2>
<p>Os extratos que você importa (ou que chegam ao seu e-mail, se você permitir) são abertos e lidos no seu iPhone.</p>

<h2>Inteligência artificial (opcional, desativada por padrão)</h2>
<p>Somente se você ativá-la e informar sua própria chave da Anthropic, e aceitar o aviso de permissão no app, o MyFinances envia à Anthropic o texto de um extrato ou e-mail que nenhum leitor entende e os nomes de estabelecimentos desconhecidos, para lê-los e categorizá-los. Antes do envio, o app <strong>remove os dados pessoais</strong>: e-mails, números de documento, números de conta e cartão, telefones e o nome do titular. O envio vai direto do seu iPhone para a Anthropic com a sua chave e segue as políticas da Anthropic.</p>

<h2>No Android</h2>
<p>Suas contas, movimentações, extratos e investimentos ficam no armazenamento privado do app no seu telefone. Não há sincronização na nuvem; o backup é um arquivo que você salva onde quiser.</p>
<p><strong>Leitura de notificações (opcional).</strong> Somente se você ativar, depois de um aviso que explica o que faz, o app lê as notificações dos apps dos seus bancos (por exemplo Bancolombia, Nequi, Nu, Davivienda) e os SMS que vierem de um banco, para registrar compras e transferências. As notificações de qualquer outro app são ignoradas e não são salvas. Tudo é processado no seu telefone e nada é enviado a nenhum servidor. Você pode desativar quando quiser nas configurações do telefone.</p>
<p><strong>Extratos em PDF.</strong> Você os abre no telefone; se tiverem senha, você a digita para abri-los e ela não é salva.</p>
<p><strong>Apagar seus dados no Android:</strong> desinstale o app ou vá em Configurações do telefone → Apps → MyFinances → Armazenamento → Limpar dados.</p>

<h2>Taxa de câmbio</h2>
<p>Para mostrar dólares em pesos, o app consulta a taxa oficial (TRM) em datos.gov.co. Essa consulta não inclui nenhum dado seu.</p>

<h2>Notificações</h2>
<p>Os avisos (pagamentos de cartão, orçamentos, extratos) são gerados no seu iPhone.</p>

<h2>Apagar seus dados</h2>
<p>Apague o app do iPhone. Se você usou o iCloud, vá em Ajustes do iPhone → seu nome → iCloud → Gerenciar Armazenamento → MyFinances → Apagar Dados.</p>

<h2>Crianças</h2>
<p>O MyFinances não é destinado a menores de 13 anos.</p>

<h2>Alterações e contato</h2>
<p>Qualquer alteração nesta política será publicada aqui com a nova data. Para dúvidas, veja <a href="../suporte/">Suporte</a>.</p>
""",
}

SUPPORT = {
"es": f"""
<h1>Soporte</h1>
<p class="lead">¿Algo no funciona o tienes una idea? <a class="button" href="{CONTACT}">Escríbenos</a></p>
<p class="note">O escribe a {EMAIL}. No incluyas datos personales, números de cuenta ni capturas con tus saldos.</p>

<h2>Preguntas frecuentes</h2>
<details><summary>¿Qué bancos funcionan?</summary><p>Por ahora Bancolombia: correos de compras y transferencias, y extractos de ahorros y tarjetas de crédito. También puedes registrar movimientos a mano, incluido el efectivo.</p></details>
<details><summary>¿Cómo importo un extracto?</summary><p>Comparte el PDF del extracto con MyFinances desde Archivos o Correo, o usa el botón de importar dentro de la app. Si el PDF tiene clave, la app te la pide y puede guardarla en el Llavero.</p></details>
<details><summary>¿La app puede leer mi correo sin permiso?</summary><p>No. Solo después de que conectes tu cuenta, con acceso de solo lectura, y únicamente los correos de tu banco. Puedes desconectarlo desde Ajustes.</p></details>
<details><summary>¿Cómo paso mis datos a otro iPhone?</summary><p>Con iCloud activo se sincronizan solos. También puedes ir a Ajustes → Datos → Respaldo completo, guardar el archivo y restaurarlo en el otro iPhone.</p></details>
<details><summary>¿Necesito la inteligencia artificial?</summary><p>No. Es opcional y está apagada por defecto. Sirve para clasificar los movimientos que la app no reconoce.</p></details>
<details><summary>¿Cómo borro todo?</summary><p>Mira la sección “Borrar tus datos” de la <a href="../privacidad/">política de privacidad</a>.</p></details>
""",
"en": f"""
<h1>Support</h1>
<p class="lead">Something not working, or have an idea? <a class="button" href="{CONTACT}">Contact us</a></p>
<p class="note">Or write to {EMAIL}. Don't include personal data, account numbers or screenshots showing your balances.</p>

<h2>Frequently asked questions</h2>
<details><summary>Which banks are supported?</summary><p>Bancolombia for now: purchase and transfer emails, plus savings and credit card statements. You can also add transactions by hand, including cash.</p></details>
<details><summary>How do I import a statement?</summary><p>Share the statement PDF with MyFinances from Files or Mail, or use the import button inside the app. If the PDF is password-protected, the app asks for it and can save it in the Keychain.</p></details>
<details><summary>Can the app read my email without permission?</summary><p>No. Only after you connect your account, with read-only access, and only your bank's emails. You can disconnect it in Settings.</p></details>
<details><summary>How do I move my data to another iPhone?</summary><p>With iCloud on, it syncs automatically. You can also go to Settings → Data → Full backup, save the file and restore it on the other iPhone.</p></details>
<details><summary>Do I need the AI?</summary><p>No. It's optional and off by default. It helps categorize transactions the app doesn't recognize.</p></details>
<details><summary>How do I delete everything?</summary><p>See “Deleting your data” in the <a href="../privacy/">privacy policy</a>.</p></details>
""",
"pt": f"""
<h1>Suporte</h1>
<p class="lead">Algo não funciona ou tem uma ideia? <a class="button" href="{CONTACT}">Fale conosco</a></p>
<p class="note">Ou escreva para {EMAIL}. Não inclua dados pessoais, números de conta nem capturas com seus saldos.</p>

<h2>Perguntas frequentes</h2>
<details><summary>Quais bancos funcionam?</summary><p>Por enquanto o Bancolombia: e-mails de compras e transferências, e extratos de poupança e cartão de crédito. Você também pode registrar movimentações à mão, inclusive dinheiro em espécie.</p></details>
<details><summary>Como importo um extrato?</summary><p>Compartilhe o PDF do extrato com o MyFinances pelo app Arquivos ou Mail, ou use o botão de importar no app. Se o PDF tiver senha, o app pede e pode guardá-la nas Chaves.</p></details>
<details><summary>O app pode ler meu e-mail sem permissão?</summary><p>Não. Só depois que você conectar sua conta, com acesso somente leitura, e apenas os e-mails do seu banco. Você pode desconectar nos Ajustes.</p></details>
<details><summary>Como passo meus dados para outro iPhone?</summary><p>Com o iCloud ativo, sincronizam sozinhos. Você também pode ir em Ajustes → Dados → Backup completo, salvar o arquivo e restaurá-lo no outro iPhone.</p></details>
<details><summary>Preciso da inteligência artificial?</summary><p>Não. É opcional e vem desativada. Serve para classificar movimentações que o app não reconhece.</p></details>
<details><summary>Como apago tudo?</summary><p>Veja “Apagar seus dados” na <a href="../privacidade/">política de privacidade</a>.</p></details>
""",
}

CSS = """
:root{--bg:#f6f7fb;--card:#fff;--text:#14182b;--muted:#5d6478;--accent:#3b5bdb;--line:#e4e7f0}
@media (prefers-color-scheme:dark){:root{--bg:#0b0e1a;--card:#151a2c;--text:#eef0f7;--muted:#9aa2b8;--accent:#7f9cff;--line:#262c42}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;-webkit-text-size-adjust:100%}
.wrap{max-width:720px;margin:0 auto;padding:24px 16px 64px}
header{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:24px}
header a.brand{display:flex;align-items:center;gap:10px;color:var(--text);text-decoration:none;font-weight:700;font-size:20px;margin-right:auto}
header img{width:40px;height:40px;border-radius:10px}
nav a{color:var(--muted);text-decoration:none;margin-left:14px;font-size:15px}
nav a.on{color:var(--accent);font-weight:600}
main{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:28px 24px}
h1{font-size:30px;line-height:1.2;margin:0 0 12px}
h2{font-size:19px;margin:28px 0 6px}
p{margin:8px 0}
.lead{font-size:18px}
.note,.updated{color:var(--muted);font-size:14px}
a{color:var(--accent)}
.button{display:inline-block;background:var(--accent);color:#fff;text-decoration:none;padding:8px 18px;border-radius:999px;font-weight:600;margin-left:6px}
details{border-top:1px solid var(--line);padding:12px 0}
summary{cursor:pointer;font-weight:600}
.langs{margin-top:20px;text-align:center;font-size:14px;color:var(--muted)}
.langs a{color:var(--muted);margin:0 8px}
.hero{text-align:center}
.hero img{width:96px;height:96px;border-radius:22px;margin:8px 0 12px}
.links{display:flex;gap:12px;justify-content:center;margin-top:20px;flex-wrap:wrap}
"""


def rel(from_path: str, to_path: str) -> str:
    depth = from_path.count("/")
    return "../" * depth + to_path


def page(lang: str, key: str, body: str, title: str) -> str:
    here = PATHS[key][lang]
    ui = UI[lang]
    nav = "".join(
        f'<a class="{"on" if k == key else ""}" href="{rel(here, PATHS[k][lang])}">{ui[k]}</a>'
        for k in ("privacy", "support"))
    langs = "".join(
        f'<a href="{rel(here, PATHS[key][l])}" hreflang="{l}">{LANG_NAMES[l]}</a>' for l in ("es", "en", "pt"))
    updated = f'<p class="updated">{ui["updated"]}: {UPDATED[lang]}</p>' if key == "privacy" else ""
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{ui['tagline']}">
<link rel="icon" href="{rel(here, 'icon.png')}">
<link rel="stylesheet" href="{rel(here, 'style.css')}">
</head>
<body><div class="wrap">
<header><a class="brand" href="{rel(here, PATHS['home'][lang])}"><img src="{rel(here, 'icon.png')}" alt="">MyFinances</a><nav>{nav}</nav></header>
<main>{body}{updated}</main>
<p class="langs">{langs}</p>
</div></body>
</html>
"""


def home(lang: str) -> str:
    ui = UI[lang]
    here = PATHS["home"][lang]
    body = f"""<div class="hero"><img src="{rel(here, 'icon.png')}" alt=""><h1>MyFinances</h1>
<p class="lead">{ui['home_lead']}</p>
<div class="links"><a class="button" href="{rel(here, PATHS['privacy'][lang])}">{ui['privacy']}</a><a class="button" href="{rel(here, PATHS['support'][lang])}">{ui['support']}</a></div></div>"""
    return page(lang, "home", body, "MyFinances")


def write(path: str, html: str) -> None:
    target = ROOT / path / "index.html" if path else ROOT / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")


(ROOT / "style.css").write_text(CSS.strip() + "\n", encoding="utf-8")
for lang in ("es", "en", "pt"):
    write(PATHS["home"][lang], home(lang))
    write(PATHS["privacy"][lang], page(lang, "privacy", PRIVACY[lang], f"MyFinances · {UI[lang]['privacy']}"))
    write(PATHS["support"][lang], page(lang, "support", SUPPORT[lang], f"MyFinances · {UI[lang]['support']}"))
print("ok")
