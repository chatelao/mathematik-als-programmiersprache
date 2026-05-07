# Roadmap

Dieses Dokument beschreibt die geplanten Schritte zur Erstellung des Buches "Mathematik als ultimatives Werkzeug für Softwarespezifikationen". Bitte halten Sie sich bei der Bearbeitung an die in der `GEMINI.md` definierten Regeln.

## Phase 1: Infrastruktur und Setup
- [x] Dokumentations-Grundgerüst auf readthedocs.org einrichten (2026-05-06, Issue #1)
  - [x] Sphinx-Konfiguration (`docs/conf.py`) erstellen
  - [x] Haupt-Einstiegspunkt (`docs/index.rst`) erstellen
  - [x] ReadTheDocs-Konfiguration (`.readthedocs.yaml`) erstellen
  - [x] Dokumentations-Abhängigkeiten (`requirements-docs.txt`) definieren
- [x] CI/CD-Pipeline mit Github Actions konfigurieren (2026-05-06)
  - [x] `test/install.sh` für Abhängigkeiten erstellen (2026-05-06, Issue #1)
  - [x] GitHub Action Workflow-Datei (`.github/workflows/docs.yml`) erstellen (2026-05-06)
  - [x] Caching für schnellere Builds hinzufügen (2026-05-06)
- [x] Syntax- und Rendering-Prüfung bei jeder Aufgabe automatisieren (2026-05-06)

## Phase 2: Architektur und Design
- [x] Entscheidung über das Buchlayout und die Kapitelstruktur treffen (2026-05-06)
- [x] Mathematische Notation und Symbolik definieren (2026-05-06)
  - [x] Entscheidung über die Art der mathematischen Notation treffen (2026-05-06)
  - [x] Referenzdokument für Symbole und Notationen erstellen (`docs/notation.rst`) (2026-05-06)
- [ ] Anwendungsfälle für Softwarespezifikationen auswählen und entwerfen
  - [x] Auswahlkriterien für Anwendungsfälle festlegen (2026-05-07)
  - [x] Drei verschiedene Anwendungsfälle identifizieren und dokumentieren (2026-05-06, Issue #2)
    - [x] Use Case 1: Zustandsbasierte Steuerung (z. B. Ampelsystem) (2026-05-06)
    - [x] Use Case 2: Relationales Datenmodell (z. B. Bibliotheksverwaltung) (2026-05-06)
    - [x] Use Case 3: Logikbasierte Geschäftsregeln (z. B. Rabattsystem) (2026-05-06)
  - [ ] Mathematische Modellierung der Anwendungsfälle skizzieren
    - [x] Skizze Use Case 1: Ampelsystem (Zustandsautomat) (2026-05-07)
    - [x] Skizze Use Case 2: Bibliotheksverwaltung (Relationen) (2026-05-07)
    - [ ] Skizze Use Case 3: Rabattsystem (Prädikatenlogik)

## Phase 3: Inhaltliche Erstellung
- [ ] Kapitel 1: Einleitung – Mathematik als Fundament
  - [ ] Gliederung erstellen
  - [ ] Ersten Entwurf schreiben
  - [ ] Review und Finalisierung
- [ ] Kapitel 2: Logik und Mengenlehre in der Softwareentwicklung
  - [ ] Gliederung erstellen
  - [ ] Ersten Entwurf schreiben
  - [ ] Review und Finalisierung
- [ ] Kapitel 3: Formale Spezifikationstechniken
  - [ ] Gliederung erstellen
  - [ ] Ersten Entwurf schreiben
  - [ ] Review und Finalisierung
- [ ] Kapitel 4: Praktische Anwendungsbeispiele
  - [ ] Gliederung erstellen
  - [ ] Ersten Entwurf schreiben
  - [ ] Review und Finalisierung
- [ ] Kapitel 5: Fazit und Ausblick
  - [ ] Gliederung erstellen
  - [ ] Ersten Entwurf schreiben
  - [ ] Review und Finalisierung

---

## Anhang: Entscheidungsdokumentation

### Entscheidung: Struktur der Roadmap
Für die Erstellung der Roadmap wurden die folgenden drei Optionen bewertet:

1. **Phasenbasierte Struktur (Infrastruktur, Architektur, Inhalt)**: Diese Option ermöglicht eine klare Trennung zwischen technischen Vorbereitungen, gestalterischen Entscheidungen und der eigentlichen Schreibarbeit. Sie entspricht den Anforderungen der `GEMINI.md` hinsichtlich Zwischenaufgaben für Design und Architektur. (**Ausgewählt**)
2. **Meilensteinbasierte Struktur (Erster Entwurf, Review, Finalisierung)**: Diese Struktur ist sehr ergebnisorientiert, vernachlässigt jedoch die notwendigen technischen Infrastrukturarbeiten zu Beginn des Projekts. (**Verworfen**)
3. **Themenbasierte Struktur (Grundlagen, Methoden, Praxis)**: Hierbei liegt der Fokus auf den Inhalten. Die zeitliche Abfolge der technischen Umsetzung und der Architekturphase wird nicht ausreichend abgebildet. (**Verworfen**)

### Entscheidung: Dokumentations-Framework
Für die Erstellung der Dokumentation wurden die folgenden drei Optionen bewertet:

1. **Sphinx**: Bietet native Unterstützung für reStructuredText, ist der Standard für readthedocs.org und verfügt über umfangreiche Erweiterungen für mathematische Formeln und technische Dokumentation. (**Ausgewählt**)
2. **Docutils**: Ein minimalistisches Werkzeug zur Verarbeitung von reStructuredText. Es ist sehr leichtgewichtig, bietet aber weniger Funktionen für komplexe Buchstrukturen und Cross-Referenzierung als Sphinx. (**Verworfen**)
3. **MkDocs mit RST-Plugin**: Ein modernes Framework, das primär auf Markdown setzt. Die Unterstützung für reStructuredText über Plugins ist möglich, aber weniger ausgereift und integriert als bei Sphinx. (**Verworfen**)

### Entscheidung: CI/CD-Pipeline
Für die Automatisierung der Builds wurden die folgenden drei Optionen bewertet:

1. **GitHub Actions**: Nahtlose Integration in GitHub, einfache Konfiguration über YAML-Dateien und hervorragende Unterstützung für Caching von Abhängigkeiten. (**Ausgewählt**)
2. **GitLab CI/CD**: Bietet umfangreiche Funktionen, würde jedoch einen Wechsel der Hosting-Plattform oder eine komplexe Spiegelung erfordern. (**Verworfen**)
3. **CircleCI**: Ein leistungsstarker externer Dienst, der jedoch eine zusätzliche Kontoverwaltung und Integration außerhalb des GitHub-Ökosystems erfordert. (**Verworfen**)

### Entscheidung: Buchlayout und Kapitelstruktur
Für das Layout und die Struktur des Buches wurden die folgenden drei Optionen bewertet:

1. **Top-Down (Theorie vor Praxis)**: Ein systematischer Aufbau, der mit den mathematischen Grundlagen beginnt und diese schrittweise auf komplexe Softwarespezifikationen anwendet. Dies stellt sicher, dass alle Konzepte präzise eingeführt werden, bevor sie in der Praxis verwendet werden. (**Ausgewählt**)
2. **Bottom-Up (Praxis vor Theorie)**: Ein problemgetriebener Ansatz, der mit realen Softwareproblemen beginnt und die notwendige Mathematik "just-in-time" einführt. Dies könnte motivierender sein, birgt aber das Risiko, dass die mathematische Strenge und die Tiefe der Fundamente zugunsten der schnellen Anwendbarkeit leiden. (**Verworfen**)
3. **Modular (Themenspezifisch)**: Das Buch wird in unabhängige Module unterteilt (z.B. ein Modul für Logik, eines für Mengenlehre, eines für Zustandsmaschinen). Dies ermöglicht ein selektives Lesen, erschwert jedoch die Darstellung des "roten Fadens" und der tiefen Zusammenhänge zwischen den mathematischen Disziplinen. (**Verworfen**)

*Die verworfenen Optionen werden hiermit in komprimierter Form für die Dokumentation archiviert.*
