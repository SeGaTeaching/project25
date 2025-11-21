from datetime import date
# Falls deine App anders heißt, ersetze 'bia_app' durch den richtigen Namen!
from bia_forms.models import Artifact 

artifacts_list = [
    Artifact(
        name="Kristalliner Datenspeicher",
        discovery_date=date(2024, 1, 15),
        origin_sector="Sektor 7G (Andromeda)",
        threat_level="low",
        is_radioactive=False,
        description="Ein handgroßer Kristall, der bei Berührung leise singt. Enthält vermutlich Sternenkarten einer friedlichen Zivilisation."
    ),
    Artifact(
        name="Verrosteter Ionen-Injektor",
        discovery_date=date(2023, 11, 20),
        origin_sector="Schrottgürtel Omega",
        threat_level="medium",
        is_radioactive=True,
        description="Antriebsteil eines unbekannten Jägers. Leckt immer noch leichte Gammastrahlung. Nicht ohne Handschuhe anfassen."
    ),
    Artifact(
        name="Der Flüsternde Würfel",
        discovery_date=date(2025, 2, 10),
        origin_sector="Unbekannte Dimension",
        threat_level="critical",
        is_radioactive=False,
        description="Ein schwarzer Würfel, der Licht absorbiert. Personal berichtet von Kopfschmerzen und Stimmen in der Nähe des Objekts."
    ),
    Artifact(
        name="Viper-Drohnen-CPU",
        discovery_date=date(2024, 8, 5),
        origin_sector="Kriegszone Alpha",
        threat_level="high",
        is_radioactive=False,
        description="Der zentrale Prozessor einer autonomen Kampfdrohne. Versucht sich ständig mit dem WLAN zu verbinden, um Tötungsbefehle zu empfangen."
    ),
    Artifact(
        name="Versteinerte Xeno-Pflanze",
        discovery_date=date(2022, 5, 12),
        origin_sector="Exoplanet LV-426",
        threat_level="low",
        is_radioactive=False,
        description="Ein harmloses Fossil. Dient aktuell als Briefbeschwerer im Labor, da keine biologische Aktivität messbar ist."
    ),
    Artifact(
        name="Instabiler Plasma-Kern",
        discovery_date=date(2025, 4, 1),
        origin_sector="Wrack der 'Nostromo'",
        threat_level="high",
        is_radioactive=True,
        description="Energiequelle, die extrem instabil ist. Muss konstant gekühlt werden, sonst droht eine Explosion im Kilotonnen-Bereich."
    ),
    Artifact(
        name="Antikes Gold-Tablet",
        discovery_date=date(2020, 10, 30),
        origin_sector="Erde (Ausgrabung)",
        threat_level="medium",
        is_radioactive=False,
        description="Sieht aus wie Gold, besteht aber aus einer unbekannten Legierung. Zeigt Koordinaten, die ins Zentrum der Galaxis zeigen."
    ),
    Artifact(
        name="Symbionten-Probe #84",
        discovery_date=date(2025, 5, 20),
        origin_sector="Labor 3 (Intern)",
        threat_level="critical",
        is_radioactive=True,
        description="Biologische Masse, die Glas durchfressen kann. Hochgradig aggressiv und radioaktiv mutiert."
    ),
    Artifact(
        name="Defekter Universal-Übersetzer",
        discovery_date=date(2021, 3, 14),
        origin_sector="Handelsposten Beta",
        threat_level="low",
        is_radioactive=False,
        description="Übersetzt alles Gesagte nur in Beleidigungen. Witzig, aber diplomatisch nutzlos."
    )
]

# Alles auf einmal in die Datenbank schreiben
Artifact.objects.bulk_create(artifacts_list)

print(f"{len(artifacts_list)} Artefakte wurden erfolgreich katalogisiert und weggesperrt.")