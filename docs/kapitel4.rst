Kapitel 4: Praktische Anwendungsbeispiele
=========================================

In diesem Kapitel werden drei ausgewählte Anwendungsfälle detailliert beschrieben, die als Grundlage für die mathematischen Spezifikationen in den folgenden Abschnitten dienen. Diese Beispiele wurden so gewählt, dass sie jeweils ein zentrales mathematisches Konzept der Softwareentwicklung illustrieren.

Anwendungsfall 1: Zustandsbasierte Steuerung (Ampelsystem)
----------------------------------------------------------

Das Ampelsystem dient zur Veranschaulichung von endlichen Zustandsautomaten (engl. *Finite State Machines*).

**Beschreibung:**
Betrachten Sie eine einfache Kreuzung zweier Straßen (A und B). Die Steuerung muss sicherstellen, dass zu jedem Zeitpunkt ein sicherer Verkehrsfluss gewährleistet ist.

**Mathematische Relevanz:**
- **Zustände:** Definieren Sie die möglichen Signalkombinationen (z. B. Grün, Gelb, Rot, Rot-Gelb).
- **Übergänge:** Beschreiben Sie die Regeln, nach denen von einem Zustand in den nächsten gewechselt wird, basierend auf Zeitgebern oder Sensordaten.
- **Invarianten:** Stellen Sie sicher, dass niemals beide Straßen gleichzeitig "Grün" signalisiert bekommen.

Anwendungsfall 2: Relationales Datenmodell (Bibliotheksverwaltung)
------------------------------------------------------------------

Die Bibliotheksverwaltung wird verwendet, um die Anwendung der Mengenlehre und Relationenalgebra auf Datenstrukturen zu demonstrieren.

**Beschreibung:**
Modellieren Sie ein System zur Verwaltung von Büchern, Autoren und Ausleihen durch Mitglieder.

**Mathematische Relevanz:**
- **Mengen:** Definieren Sie Mengen für :math:`Bücher`, :math:`Autoren` und :math:`Mitglieder`.
- **Relationen:** Bilden Sie die Beziehungen zwischen diesen Mengen ab (z. B. "Autor schreibt Buch", "Mitglied leiht Buch aus").
- **Integrität:** Verwenden Sie mathematische Prädikate, um sicherzustellen, dass beispielsweise ein Buch nur von einem Mitglied gleichzeitig ausgeliehen werden kann.

Anwendungsfall 3: Logikbasierte Geschäftsregeln (Rabattsystem)
--------------------------------------------------------------

Das Rabattsystem illustriert den Einsatz von Aussagen- und Prädikatenlogik zur Spezifikation komplexer Entscheidungsregeln.

**Beschreibung:**
Spezifizieren Sie die Bedingungen, unter denen ein Kunde beim Kauf in einem Online-Shop einen Preisnachlass erhält.

**Mathematische Relevanz:**
- **Prädikate:** Definieren Sie logische Aussagen über Kundenmerkmale (z. B. :math:`istPremium(Kunde)`, :math:`umsatz(Kunde) > 100`).
- **Logische Verknüpfungen:** Kombinieren Sie diese Prädikate mittels Konjunktion (:math:`\land`), Disjunktion (:math:`\lor`) und Implikation (:math:`\implies`), um die finale Rabattentscheidung abzuleiten.
- **Konsistenz:** Überprüfen Sie, ob die Regeln widerspruchsfrei sind und alle möglichen Fälle abdecken.
