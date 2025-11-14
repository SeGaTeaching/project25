from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape

# Create your views here.
def index(request):
    request.session['super_test'] = "Hallo ich bin in der Session zu finden (hoffentlich)"
    request.session['user_id'] = 12345
    return HttpResponse("<h1>Session-Daten wurden gesetzt!</h1> <a href='/request/'>Jetzt Request-Objekt prüfen</a>")

def req_obj(request):
    
    # Wir bauen jetzt einen HTML-String statt einer Textliste
    html_lines = []

    # --- 1. CSS-Stil (eingebettet im <head>) ---
    html_lines.append("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Django Request Übersicht</title>
        <style>
            body { 
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background-color: #f4f7f6;
                color: #333;
                margin: 0;
                padding: 20px;
            }
            .container {
                max-width: 900px;
                margin: 20px auto;
                background-color: #ffffff;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.05);
                overflow: hidden; /* Für den Header-Farbverlauf */
            }
            h1 {
                background-color: #092E20; /* Django-Grün */
                color: #41D1A1;
                padding: 25px 30px;
                margin: 0;
            }
            h2 {
                border-bottom: 2px solid #f0f0f0;
                padding-bottom: 10px;
                margin-top: 25px;
                color: #092E20;
            }
            .content {
                padding: 10px 30px 30px 30px;
            }
            /* Für Key-Value-Paare */
            .kv-pair {
                display: flex;
                margin-bottom: 8px;
                font-size: 16px;
            }
            .kv-pair strong {
                display: inline-block;
                min-width: 180px;
                color: #555;
            }
            /* Für Code-Blöcke (Header, Parameter) */
            pre {
                background-color: #f9f9f9;
                border: 1px solid #eee;
                padding: 15px;
                border-radius: 5px;
                font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
                font-size: 14px;
                white-space: pre-wrap; /* Zeilenumbruch */
                word-wrap: break-word; /* Lange Werte umbrechen */
            }
            p.empty {
                color: #888;
                font-style: italic;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Django Request-Übersicht</h1>
            <div class="content">
    """)

    # --- 2. Übersicht ---
    html_lines.append("<h2>Übersicht</h2>")
    html_lines.append(f"<div class='kv-pair'><strong>Methode:</strong> {escape(request.method)}</div>")
    html_lines.append(f"<div class='kv-pair'><strong>Pfad:</strong> {escape(request.path)}</div>")
    html_lines.append(f"<div class='kv-pair'><strong>Ist gesichert (HTTPS):</strong> {request.is_secure()}</div>")
    html_lines.append(f"<div class='kv-pair'><strong>Ist AJAX (XHR):</strong> {request.headers.get('x-requested-with') == 'XMLHttpRequest'}</div>")

    # --- 3. GET-Parameter ---
    html_lines.append("<h2>GET-Parameter (Query String)</h2>")
    if request.GET:
        html_lines.append(f"Query Dictionary: {escape(request.GET)}")
        get_params = []
        for key, value in request.GET.items():
            get_params.append(f"{escape(key)}: {escape(value)}")
        html_lines.append(f"<pre>{"\n".join(get_params)}</pre>")
    else:
        html_lines.append("<p class='empty'>Keine GET-Parameter.</p>")

    # --- 4. POST-Parameter ---
    html_lines.append("<h2>POST-Parameter (Formulardaten)</h2>")
    if request.method == 'POST':
        if request.POST:
            post_params = []
            for key, value in request.POST.items():
                post_params.append(f"{escape(key)}: {escape(value)}")
            html_lines.append(f"<pre>{"\n".join(post_params)}</pre>")
        elif request.body and request.headers.get('content-type') == 'application/json':
             html_lines.append(f"<pre><strong>Raw JSON Body:</strong>\n{escape(request.body.decode('utf-8'))}</pre>")
        else:
            html_lines.append("<p class='empty'>Keine POST-Formulardaten.</p>")
    else:
        html_lines.append("<p class='empty'>POST-Parameter nur bei POST-Anfragen relevant.</p>")
    
    # --- 5. Session Daten ---
    html_lines.append("<h2>Session Daten</h2>")
    if request.session.items():
        session_data = []
        for key, val in request.session.items():
            # Wichtig: val in string umwandeln und escapen
            session_data.append(f"{escape(key)}: {escape(str(val))}")
        html_lines.append(f"<pre>{"\n".join(session_data)}</pre>")
    else:
        html_lines.append("<p class='empty'>Keine Daten in der Session.</p>")

    # --- 6. HTTP-Header ---
    html_lines.append("<h2>HTTP-Header (Auswahl aus request.META)</h2>")
    headers = []
    relevant_headers = [
        'HTTP_HOST', 'HTTP_USER_AGENT', 'REMOTE_ADDR', 'CONTENT_TYPE',
        'CONTENT_LENGTH', 'HTTP_ACCEPT', 'HTTP_REFERER', 'HTTP_COOKIE'
    ]
    for key, value in request.META.items():
        if key in relevant_headers or (key.startswith('HTTP_') and not key.startswith('HTTP_X_')):
            headers.append(f"{escape(key)}: {escape(value)}")
    
    if headers:
        html_lines.append(f"<pre>{"\n".join(headers)}</pre>")
    else:
        html_lines.append("<p class='empty'>Keine relevanten HTTP-Header gefunden.</p>")

    # --- 7. Benutzer ---
    html_lines.append("<h2>Angemeldeter Benutzer (request.user)</h2>")
    if hasattr(request, 'user') and request.user.is_authenticated:
        html_lines.append(f"<div class='kv-pair'><strong>Benutzername:</strong> {escape(request.user.username)}</div>")
        html_lines.append(f"<div class='kv-pair'><strong>E-Mail:</strong> {escape(request.user.email)}</div>")
        html_lines.append(f"<div class='kv-pair'><strong>Ist Superuser:</strong> {request.user.is_superuser}</div>")
    else:
        html_lines.append("<p class='empty'>Kein Benutzer angemeldet.</p>")
        
    # --- 8. HTML abschließen ---
    html_lines.append("""
            </div> </div> </body>
    </html>
    """)
    
    return HttpResponse("".join(html_lines))

# Greeting my Comrades - Pfad-Parameter
def greet_taisa(request):
    return HttpResponse("<h2>Hallo Taisa</h2>")

def greet_hoda(request):
    return HttpResponse("<h2>Hallo Hoda</h2>")

def greet(request, name):
    type_name = type(name)
    return HttpResponse(f"<h2>Hallo, {name}!</h2><p>Typ Pfad-Parameter: {escape(type_name)}</p>")

# Integer Pfad-Parameter
def math(request, num1, num2):
    result = f"""
    Addition: {num1 + num2}<br>
    Subratktion: {num1 - num2}<br>
    Multiplikation: {num1 * num2}<br>
    Division: {(num1 / num2):.2f}<br>
    Modulus: {num1 % num2}<br>
    """
    
    return HttpResponse(f"Die Ergebnise von {num1} und {num2}:<br>{result}")