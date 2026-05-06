# Roadmap

Dieses Dokument beschreibt die geplanten Schritte zur Erstellung des Buches "Mathematik als ultimatives Werkzeug für Softwarespezifikationen". Bitte halten Sie sich bei der Bearbeitung an die in der `GEMINI.md` definierten Regeln.

## Phase 1: Infrastruktur und Setup
- [x] Dokumentations-Grundgerüst auf readthedocs.org einrichten (2026-05-06, Issue #1)
  - [x] Sphinx-Konfiguration (`docs/conf.py`) erstellen
  - [x] Haupt-Einstiegspunkt (`docs/index.rst`) erstellen
  - [x] ReadTheDocs-Konfiguration (`.readthedocs.yaml`) erstellen
  - [x] Dokumentations-Abhängigkeiten (`requirements-docs.txt`) definieren
- [ ] CI/CD-Pipeline mit Github Actions konfigurieren
  - [x] `test/install.sh` für Abhängigkeiten erstellen (2026-05-06, Issue #1)
  - [ ] Caching für schnellere Builds hinzufügen
- [ ] Syntax- und Rendering-Prüfung bei jeder Aufgabe automatisieren

## Phase 2: Architektur und Design
- [ ] Entscheidung über das Buchlayout und die Kapitelstruktur treffen (Bewerten Sie hierzu drei Optionen)
- [ ] Mathematische Notation und Symbolik definieren
- [ ] Anwendungsfälle für Softwarespezifikationen auswählen und entwerfen

## Phase 3: Inhaltliche Erstellung
- [ ] Kapitel 1: Einleitung – Mathematik als Fundament
- [ ] Kapitel 2: Logik und Mengenlehre in der Softwareentwicklung
- [ ] Kapitel 3: Formale Spezifikationstechniken
- [ ] Kapitel 4: Praktische Anwendungsbeispiele
- [ ] Kapitel 5: Fazit und Ausblick

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

*Die verworfenen Optionen werden hiermit in komprimierter Form für die Dokumentation archiviert.*
