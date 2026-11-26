#!/usr/bin/env python3
"""Genera las páginas públicas de MyFinances (privacidad y soporte) en español, inglés y portugués.
Uso: python3 build.py  → escribe los .html junto a este archivo (GitHub Pages los sirve tal cual)."""
from pathlib import Path

ROOT = Path(__file__).parent
REPO = "https://github.com/Osinisterra/myfinances-site"
EMAIL = "myfinancesapp.co@gmail.com"
CONTACT = "mailto:" + EMAIL + "?subject=MyFinances"
UPDATED = {"es": "26 de noviembre de 2026", "en": "November 26, 2026", "pt": "26 de novembro de 2026"}

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
<p class="lead">Resumen: <strong>MyFinances no recopila tus datos financieros.</strong> No hay servidores propios con tu información, cuentas de usuario, publicidad, analítica ni rastreo. El desarrollador no puede ver tus cuentas ni tus movimientos. Lo único que puede llegarle es el texto sin datos personales que tú decidas enviar con «Compartir formato» (ver abajo).</p>

<h2>Dónde se guardan tus datos (iPhone)</h2>
<p>Tus cuentas, movimientos, extractos, inversiones y presupuestos se guardan en tu iPhone, protegidos por el cifrado del dispositivo. Si tienes iCloud activo, la app los sincroniza con <strong>tu propio iCloud</strong> (base de datos privada de CloudKit), que solo tú puedes leer. <strong>Lo que viene de Gmail nunca va a iCloud</strong>: se queda en el iPhone que lo leyó, y cada dispositivo con Gmail conectado lo lee por su cuenta. Las claves de los extractos y la sesión del correo se guardan en el Llavero del iPhone y no se sincronizan.</p>

<h2>Correo (opcional, iPhone y Android)</h2>
<p>Si conectas Gmail u Outlook, la app pide permiso <strong>de solo lectura</strong> y busca únicamente los correos de los remitentes de los bancos (avisos de compras, transferencias y extractos). Esos correos se leen y se procesan en tu teléfono, y la app guarda solo la frase del movimiento.</p>
<p><strong>Los datos de Gmail nunca salen de tu teléfono:</strong> no se envían a ningún servidor del desarrollador ni de terceros, no se copian a iCloud, no se usan con inteligencia artificial en la nube y no se pueden enviar con «Compartir formato», ni siquiera después de desconectar Gmail. No se usan para publicidad ni se venden.</p>
<p>Puedes desconectar el correo cuando quieras desde Ajustes de la app; al desconectar Gmail, la app le quita su permiso en tu cuenta de Google y te ofrece borrar el texto de los correos guardados. También puedes quitar el permiso desde la configuración de seguridad de tu cuenta de Google o Microsoft.</p>
<p><strong>Gmail:</strong> el uso y la transferencia a cualquier otra app de la información recibida de las API de Google se ajustan a la <a href="https://developers.google.com/terms/api-services-user-data-policy">Política de datos de usuario de los servicios de API de Google</a>, incluidos los requisitos de Uso limitado. En concreto: los datos de Gmail solo se usan para registrar tus movimientos dentro de la app; no se usan para publicidad, para evaluar crédito ni para entrenar modelos de IA; y ninguna persona los lee. La app no guarda tu contraseña de Google.</p>

<h2>Extractos en PDF</h2>
<p>Los extractos que importas (o que llegan a tu correo, si lo autorizas) se abren y se leen en tu teléfono. Si un extracto tiene clave, puedes guardarla para los próximos: queda cifrada solo en tu teléfono (en el Llavero del iPhone) y puedes borrarla en Ajustes.</p>

<h2>Inteligencia artificial</h2>
<p>Cuando un extracto tiene un formato que la app no conoce, el iPhone puede leerlo con la inteligencia artificial de Apple, <strong>dentro del propio iPhone</strong>. MyFinances no usa inteligencia artificial en la nube.</p>

<h2>Compartir formato (opcional)</h2>
<p>Cuando registras a mano un aviso o correo de un banco que la app no reconoce, puede preguntarte si quieres compartir su formato para que la app lo reconozca sola en el futuro. Solo se envía si tocas «Enviar», después de mostrarte el texto exacto. Antes de enviarlo, la app <strong>quita montos, números, nombres de personas y comercios, correos, llaves, documentos, teléfonos, direcciones y tu nombre</strong>; queda solo la forma de la frase (por ejemplo «Compraste [monto] en [nombre]»). Se envía junto con el nombre o dominio del banco, el sistema (iPhone o Android) y la versión de la app, a una hoja de cálculo del desarrollador en Google (Google Apps Script). No lleva ningún dato que te identifique. Nunca se ofrece para lo que vino de Gmail. Puedes elegir «No volver a preguntar».</p>

<h2>Catálogo de bancos</h2>
<p>Una vez al día, la app descarga de este sitio la lista pública de formatos de los bancos, firmada por el desarrollador, para reconocer correos nuevos sin actualizar la app. Esa descarga no lleva ningún dato tuyo.</p>

<h2>Tasa de cambio</h2>
<p>Para mostrar los dólares en pesos, la app consulta la TRM oficial en datos.gov.co. Esa consulta no incluye ningún dato tuyo.</p>

<h2>En Android</h2>
<p>Tus cuentas, movimientos, extractos e inversiones se guardan en el almacenamiento privado de la app en tu teléfono. No hay sincronización en la nube ni copia automática en Google; el respaldo es un archivo que tú guardas donde quieras.</p>
<p><strong>Lectura de notificaciones (opcional).</strong> Solo si la activas, después de un aviso que explica qué hace, la app lee las notificaciones de las apps de tus bancos (por ejemplo Bancolombia, Nequi, Nu, Davivienda) y los SMS que vengan de un banco, para registrar compras y transferencias. Las notificaciones de cualquier otra app se ignoran y no se guardan. Todo se procesa en tu teléfono. Puedes apagarla cuando quieras en los ajustes del teléfono.</p>
<p><strong>Traducción de categorías.</strong> Los nombres de las categorías que creas se traducen a los otros idiomas dentro del teléfono con ML Kit de Google. Esa biblioteca descarga el modelo del idioma y envía a Google datos técnicos de diagnóstico (modelo del teléfono, versión del sistema y de la app, rendimiento y errores), cifrados; no envía tus textos ni tus datos financieros.</p>

<h2>Notificaciones</h2>
<p>Los avisos (pagos de tarjeta, presupuestos, extractos) se generan en tu teléfono.</p>

<h2>Borrar tus datos</h2>
<p><strong>iPhone:</strong> borra la app. Si usaste iCloud, ve a Ajustes del iPhone → tu nombre → iCloud → Administrar almacenamiento → MyFinances → Eliminar datos.</p>
<p><strong>Android:</strong> desinstala la app o ve a Ajustes del teléfono → Apps → MyFinances → Almacenamiento → Borrar datos.</p>

<h2>Menores de edad</h2>
<p>MyFinances no está dirigida a menores de 13 años.</p>

<h2>Cambios y contacto</h2>
<p>Si esta política cambia, se publicará aquí con la nueva fecha. Para preguntas, escribe en <a href="../soporte/">Soporte</a>.</p>
""",
"en": f"""
<h1>Privacy policy</h1>
<p class="lead">In short: <strong>MyFinances does not collect your financial data.</strong> There are no developer servers with your information, user accounts, ads, analytics or tracking. The developer cannot see your accounts or transactions. The only thing that can reach the developer is text without personal data that you choose to send with "Share format" (see below).</p>

<h2>Where your data is stored (iPhone)</h2>
<p>Your accounts, transactions, statements, investments and budgets are stored on your iPhone, protected by the device's encryption. If iCloud is on, the app syncs them with <strong>your own iCloud</strong> (CloudKit private database), which only you can read. <strong>Anything that comes from Gmail never goes to iCloud</strong>: it stays on the iPhone that read it, and each device with Gmail connected reads it on its own. Statement passwords and the email session are stored in the iPhone Keychain and are not synced.</p>

<h2>Email (optional, iPhone and Android)</h2>
<p>If you connect Gmail or Outlook, the app asks for <strong>read-only</strong> access and only looks for emails from bank senders (purchase, transfer and statement notices). Those emails are read and processed on your phone, and the app keeps only the transaction sentence.</p>
<p><strong>Gmail data never leaves your phone:</strong> it is not sent to any developer or third-party server, not copied to iCloud, not used with cloud AI, and it cannot be sent with "Share format", not even after you disconnect Gmail. It is not used for ads or sold.</p>
<p>You can disconnect email at any time in the app's Settings; when you disconnect Gmail, the app revokes its access in your Google account and offers to delete the stored email text. You can also remove access from your Google or Microsoft account security settings.</p>
<p><strong>Gmail:</strong> MyFinances' use and transfer to any other app of information received from Google APIs will adhere to the <a href="https://developers.google.com/terms/api-services-user-data-policy">Google API Services User Data Policy</a>, including the Limited Use requirements. Specifically: Gmail data is only used to record your transactions inside the app; it is not used for advertising, credit decisions or training AI models; and no person reads it. The app never stores your Google password.</p>

<h2>PDF statements</h2>
<p>Statements you import (or that arrive in your email, if you allow it) are opened and read on your phone. If a statement has a password, you can save it for the next ones: it stays encrypted on your phone only (in the iPhone Keychain) and you can delete it in Settings.</p>

<h2>Artificial intelligence</h2>
<p>When a statement has a format the app doesn't know, the iPhone can read it with Apple's artificial intelligence, <strong>on the iPhone itself</strong>. MyFinances does not use cloud AI.</p>

<h2>Share format (optional)</h2>
<p>When you manually add a bank notice or email the app doesn't recognize, it may ask whether you want to share its format so the app recognizes it on its own in the future. It is only sent if you tap "Send", after showing you the exact text. Before sending, the app <strong>removes amounts, numbers, names of people and merchants, emails, keys, ID numbers, phone numbers, addresses and your name</strong>; only the shape of the sentence remains (for example "You bought [amount] at [name]"). It is sent with the bank's name or domain, the system (iPhone or Android) and the app version, to a developer spreadsheet on Google (Google Apps Script). It carries no data that identifies you. It is never offered for anything that came from Gmail. You can choose "Don't ask again".</p>

<h2>Bank catalog</h2>
<p>Once a day, the app downloads from this site the public list of bank formats, signed by the developer, to recognize new emails without updating the app. That download carries none of your data.</p>

<h2>Exchange rate</h2>
<p>To show dollars in pesos, the app checks the official exchange rate (TRM) at datos.gov.co. That request includes none of your data.</p>

<h2>On Android</h2>
<p>Your accounts, transactions, statements and investments are stored in the app's private storage on your phone. There is no cloud sync and no automatic Google backup; the backup is a file you save wherever you want.</p>
<p><strong>Reading notifications (optional).</strong> Only if you turn it on, after a notice that explains what it does, the app reads notifications from your banks' apps (for example Bancolombia, Nequi, Nu, Davivienda) and SMS that come from a bank, to record purchases and transfers. Notifications from any other app are ignored and not stored. Everything is processed on your phone. You can turn it off at any time in your phone's settings.</p>
<p><strong>Category translation.</strong> The names of categories you create are translated into the other languages on the phone with Google's ML Kit. That library downloads the language model and sends Google technical diagnostic data (phone model, system and app version, performance and errors), encrypted; it does not send your texts or your financial data.</p>

<h2>Notifications</h2>
<p>Alerts (card payments, budgets, statements) are generated on your phone.</p>

<h2>Deleting your data</h2>
<p><strong>iPhone:</strong> delete the app. If you used iCloud, go to iPhone Settings → your name → iCloud → Manage Storage → MyFinances → Delete Data.</p>
<p><strong>Android:</strong> uninstall the app or go to phone Settings → Apps → MyFinances → Storage → Clear data.</p>

<h2>Children</h2>
<p>MyFinances is not directed to children under 13.</p>

<h2>Changes and contact</h2>
<p>If this policy changes, it will be posted here with the new date. For questions, write via <a href="../support/">Support</a>.</p>
""",
"pt": f"""
<h1>Política de privacidade</h1>
<p class="lead">Resumo: <strong>o MyFinances não coleta seus dados financeiros.</strong> Não há servidores próprios com suas informações, contas de usuário, publicidade, análise nem rastreamento. O desenvolvedor não pode ver suas contas nem suas movimentações. A única coisa que pode chegar a ele é o texto sem dados pessoais que você decidir enviar com «Compartilhar formato» (veja abaixo).</p>

<h2>Onde seus dados ficam (iPhone)</h2>
<p>Suas contas, movimentações, extratos, investimentos e orçamentos ficam no seu iPhone, protegidos pela criptografia do aparelho. Se o iCloud estiver ativo, o app os sincroniza com <strong>o seu próprio iCloud</strong> (banco de dados privado do CloudKit), que só você pode ler. <strong>O que vem do Gmail nunca vai para o iCloud</strong>: fica no iPhone que o leu, e cada dispositivo com o Gmail conectado o lê por conta própria. As senhas dos extratos e a sessão do e-mail ficam nas Chaves do iPhone e não são sincronizadas.</p>

<h2>E-mail (opcional, iPhone e Android)</h2>
<p>Se você conectar o Gmail ou o Outlook, o app pede acesso <strong>somente leitura</strong> e busca apenas os e-mails dos remetentes dos bancos (avisos de compras, transferências e extratos). Esses e-mails são lidos e processados no seu telefone, e o app guarda só a frase da movimentação.</p>
<p><strong>Os dados do Gmail nunca saem do seu telefone:</strong> não são enviados a nenhum servidor do desenvolvedor nem de terceiros, não são copiados para o iCloud, não são usados com inteligência artificial na nuvem e não podem ser enviados com «Compartilhar formato», nem depois de desconectar o Gmail. Não são usados para publicidade nem vendidos.</p>
<p>Você pode desconectar o e-mail quando quiser nos Ajustes do app; ao desconectar o Gmail, o app remove o próprio acesso na sua conta do Google e oferece apagar o texto dos e-mails guardados. Você também pode remover o acesso nas configurações de segurança da sua conta do Google ou da Microsoft.</p>
<p><strong>Gmail:</strong> o uso e a transferência para qualquer outro app de informações recebidas das APIs do Google seguem a <a href="https://developers.google.com/terms/api-services-user-data-policy">Política de dados do usuário dos serviços de API do Google</a>, incluindo os requisitos de Uso limitado. Ou seja: os dados do Gmail só são usados para registrar suas movimentações no app; não são usados para publicidade, análise de crédito ou treinamento de modelos de IA; e nenhuma pessoa os lê. O app nunca guarda sua senha do Google.</p>

<h2>Extratos em PDF</h2>
<p>Os extratos que você importa (ou que chegam ao seu e-mail, se você autorizar) são abertos e lidos no seu telefone. Se um extrato tiver senha, você pode guardá-la para os próximos: ela fica criptografada só no seu telefone (nas Chaves do iPhone) e você pode apagá-la nos Ajustes.</p>

<h2>Inteligência artificial</h2>
<p>Quando um extrato tem um formato que o app não conhece, o iPhone pode lê-lo com a inteligência artificial da Apple, <strong>dentro do próprio iPhone</strong>. O MyFinances não usa inteligência artificial na nuvem.</p>

<h2>Compartilhar formato (opcional)</h2>
<p>Quando você registra à mão um aviso ou e-mail de um banco que o app não reconhece, ele pode perguntar se você quer compartilhar o formato para reconhecê-lo sozinho no futuro. Só é enviado se você tocar em «Enviar», depois de ver o texto exato. Antes do envio, o app <strong>remove valores, números, nomes de pessoas e estabelecimentos, e-mails, chaves, documentos, telefones, endereços e o seu nome</strong>; fica só a forma da frase (por exemplo «Você comprou [valor] em [nome]»). É enviado com o nome ou domínio do banco, o sistema (iPhone ou Android) e a versão do app, para uma planilha do desenvolvedor no Google (Google Apps Script). Não leva nenhum dado que identifique você. Nunca é oferecido para o que veio do Gmail. Você pode escolher «Não perguntar de novo».</p>

<h2>Catálogo de bancos</h2>
<p>Uma vez por dia, o app baixa deste site a lista pública de formatos dos bancos, assinada pelo desenvolvedor, para reconhecer e-mails novos sem atualizar o app. Esse download não leva nenhum dado seu.</p>

<h2>Câmbio</h2>
<p>Para mostrar os dólares em pesos, o app consulta a taxa oficial (TRM) em datos.gov.co. Essa consulta não inclui nenhum dado seu.</p>

<h2>No Android</h2>
<p>Suas contas, movimentações, extratos e investimentos ficam no armazenamento privado do app no seu telefone. Não há sincronização na nuvem nem backup automático no Google; o backup é um arquivo que você guarda onde quiser.</p>
<p><strong>Leitura de notificações (opcional).</strong> Só se você ativar, depois de um aviso que explica o que faz, o app lê as notificações dos apps dos seus bancos (por exemplo Bancolombia, Nequi, Nu, Davivienda) e os SMS que vierem de um banco, para registrar compras e transferências. Notificações de qualquer outro app são ignoradas e não são guardadas. Tudo é processado no seu telefone. Você pode desativá-la quando quiser nas configurações do telefone.</p>
<p><strong>Tradução de categorias.</strong> Os nomes das categorias que você cria são traduzidos para os outros idiomas no próprio telefone com o ML Kit do Google. Essa biblioteca baixa o modelo do idioma e envia ao Google dados técnicos de diagnóstico (modelo do telefone, versão do sistema e do app, desempenho e erros), criptografados; não envia seus textos nem seus dados financeiros.</p>

<h2>Notificações</h2>
<p>Os avisos (pagamentos de cartão, orçamentos, extratos) são gerados no seu telefone.</p>

<h2>Apagar seus dados</h2>
<p><strong>iPhone:</strong> apague o app. Se você usou o iCloud, vá em Ajustes do iPhone → seu nome → iCloud → Gerenciar armazenamento → MyFinances → Apagar dados.</p>
<p><strong>Android:</strong> desinstale o app ou vá em Configurações do telefone → Apps → MyFinances → Armazenamento → Limpar dados.</p>

<h2>Menores de idade</h2>
<p>O MyFinances não é direcionado a menores de 13 anos.</p>

<h2>Alterações e contato</h2>
<p>Se esta política mudar, será publicada aqui com a nova data. Para dúvidas, escreva em <a href="../suporte/">Suporte</a>.</p>
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
