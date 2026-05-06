# Ziel
Schreibe ein Buch über Mathematik als ultimatives Werkzeug für Softwarespezifikationen.

# ANLEITUNG
- Verwenden Sie readthedocs.org, um die Dokumentation zu erstellen.
- Verwenden Sie reStructuredText für alles, was nicht in Markdown verfasst ist.
- Bewerten Sie für jede Entscheidung drei Optionen und archivieren Sie die verworfenen in komprimierter Form in einem Anhang der Dokumentation.

# Lokales Testen & mit Github Action Workflow
- Behalten Sie eine CI/CD-Pipeline bei, die bei jedem Commit und jedem Push ausgeführt wird.
- Verwenden Sie `test/install.sh`, um testspezifische Abhängigkeiten zu installieren.
- Überprüfen Sie die Syntax und das Rendering bei jeder Aufgabe und jedem Schritt.
- Fügen Sie Caching zu den Github-Action-Workflows hinzu, um Builds zu beschleunigen.

# ROADMAP-Regeln
- Teilen Sie große Aufgaben in mehrere Teilaufgaben auf, wenn sie nicht in einem Durchgang bescheiden, machbar und angemessen sind.
- Fügen Sie Zwischenaufgaben für Anwendungsfälle, Architektur oder Design hinzu, wenn eine direkte Implementierung riskant ist.
- Markieren Sie Aufgaben als abgeschlossen mit einem Zeitstempel und der entsprechenden Issue-ID, wenn sie geschlossen werden.
