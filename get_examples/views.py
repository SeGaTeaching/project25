from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def get_query(request):
    # content = f"""
    # <p>Namen: {request.GET["name"]}</p>
    # <p>q: {request.GET["q"]}</p>
    # <p>Page: {request.GET["page"]}</p>
    # <p>Query-Dict: {request.GET.dict().items()}</p>
    # """
    
    url_to_form = reverse('form_example')
    
    # Bessere Methode um Query Daten auszulesen
    content = f"""
    <p>Namen: {request.GET.get("name", "Es sind keine Daten vorhanden")}</p>
    <p>q: {request.GET.get("q", "Kein Suchbegriff vorhanden")}</p>
    <p>Page: {request.GET.get("page", 0)}</p>
    <p>Colors: {request.GET.getlist("color", "Keine Farben ausgewählt - Lieblingsfarbe wohl Schwarz - Berliner Hipster")}</p>
    <p>Query-Dict: {request.GET.dict()}</p>
    <p></p>
    <hr>
    <p><code>request.GET</code> gibt ein Query Dict zurück.<br>
    Mehr Infos hierfür findest in den Django Docs: <a href='https://docs.djangoproject.com/en/5.2/ref/request-response/#django.http.QueryDict' target='_blank'>QueryDict</a></p>
    <p>Ein richtiges Beispiel mit Formular findest Du hier: <a href='{url_to_form}'>Beispiel Query auslesen</a></p>
    """
    
    return HttpResponse(content)

def form_example(request):
    
    """
    # Wichtige Unterscheidung:
    # Der HTTP-GET-Request ist die komplette Anfrage an den Server (das "Fahrzeug").
    # request.GET ist hingegen nur das Django-Objekt, das die Nutzlast dieser Anfrage enthält – 
    # also die URL-Parameter nach dem '?' (die "Fracht").
    """
    
    # Formular Methode GET
    if request.GET:
        
        # NEU: Werte abrufen und auf leere Strings prüfen
        name_raw = request.GET.get("vorname", "")
        stadt_raw = request.GET.get("stadt", "")
        
        # Wenn der Wert leer ist, den Standardwert zuweisen
        name = name_raw if name_raw else "Unbekannt"
        stadt = stadt_raw if stadt_raw else "Buxtehude"
        
        daten_html = f"""
        <div class="daten">
            <h2>Empfangene Daten:</h2>
            <p><strong>Vorname:</strong> {name}</p>
            <p><strong>Stadt:</strong> {stadt}</p>
            <p><strong>Der komplette Query-String in der URL ist:</strong> <code>?{request.GET.urlencode()}</code></p>
        </div>
        """
    else:
        daten_html = f"""
        <div class="daten">
            <h2>No Data yet:</h2>
        </div>
        """
    
    # Response für ein HTTP Get Request    
    html_string = f"""
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <title>Einfaches GET-Formular</title>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; margin: 40px; line-height: 1.6; }}
            .container {{ max-width: 600px; margin: auto; }}
            input, button {{ font-size: 1em; padding: 8px; margin-top: 5px; width: 95%; }}
            button {{ width: auto; cursor: pointer; }}
            .daten {{ margin-top: 30px; padding: 15px; border: 1px solid #ccc; background-color: #f9f9f9; }}
            code {{ background-color: #eee; padding: 2px 5px; border-radius: 3px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Formular mit GET-Methode</h1>
            <p>Die eingegebenen Daten werden an die URL angehängt und die Seite wird neu geladen.</p>
            
            <form method="get" action="">
                <div>
                    <label for="vorname">Vorname:</label><br>
                    <input type="text" id="vorname" name="vorname" value="">
                </div>
                <br>
                <div>
                    <label for="stadt">Stadt:</label><br>
                    <input type="text" id="stadt" name="stadt" value="">
                </div>
                <br>
                <button type="submit">Senden</button>
            </form>
            
            <div>{daten_html}</div>
            
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_string)