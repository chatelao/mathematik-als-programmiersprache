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

**Mathematische Skizze:**

Ein Ampelsystem kann als endlicher Zustandsautomat :math:`A = (S, \delta, s_0)` modelliert werden:

1. **Zustandsmenge** :math:`S`:
   Die Menge der möglichen Signalkombinationen für eine Straße:
   :math:`S_{Straße} = \{ \text{Rot}, \text{Rot-Gelb}, \text{Grün}, \text{Gelb} \}`

   Der Gesamtzustand der Kreuzung ist ein Element des kartesischen Produkts:
   :math:`S = S_A \times S_B`, wobei :math:`S_A = S_B = S_{Straße}`.

2. **Startzustand** :math:`s_0`:
   :math:`s_0 = (\text{Rot}, \text{Rot})` (Initialzustand zur Sicherheit).

3. **Übergangsfunktion** :math:`\delta`:
   Die Funktion :math:`\delta: S \times \text{Ereignis} \to S` definiert den nächsten Zustand.
   Beispiel für einen Übergang:
   :math:`\delta((\text{Rot}, \text{Rot}), \text{Anforderung}_A) = (\text{Rot-Gelb}, \text{Rot})`

4. **Sicherheitsinvariante** :math:`I`:
   Eine Bedingung, die in jedem erreichbaren Zustand :math:`s \in S` gelten muss:
   :math:`I(s) \iff \neg (s_A = \text{Grün} \land s_B = \text{Grün})`

Anwendungsfall 2: Relationales Datenmodell (Bibliotheksverwaltung)
------------------------------------------------------------------

Die Bibliotheksverwaltung wird verwendet, um die Anwendung der Mengenlehre und Relationenalgebra auf Datenstrukturen zu demonstrieren.

**Beschreibung:**
Modellieren Sie ein System zur Verwaltung von Büchern, Autoren und Ausleihen durch Mitglieder.

**Mathematische Relevanz:**
- **Mengen:** Definieren Sie Mengen für :math:`Bücher`, :math:`Autoren` und :math:`Mitglieder`.
- **Relationen:** Bilden Sie die Beziehungen zwischen diesen Mengen ab (z. B. "Autor schreibt Buch", "Mitglied leiht Buch aus").
- **Integrität:** Verwenden Sie mathematische Prädikate, um sicherzustellen, dass beispielsweise ein Buch nur von einem Mitglied gleichzeitig ausgeliehen werden kann.

**Mathematische Skizze:**

Die Bibliotheksverwaltung kann als System von Mengen und Relationen modelliert werden:

1. **Grundmengen:**
   - :math:`B`: Die Menge aller Bücher im Bestand.
   - :math:`A`: Die Menge aller Autoren.
   - :math:`M`: Die Menge aller registrierten Mitglieder.

2. **Relationen und Funktionen:**
   - :math:`schrieb \subseteq A \times B`: Eine Relation, die Autoren ihren Werken zuordnet.
   - :math:`leihtAus: B \mapsto M`: Eine partielle Funktion, die ein Buch seinem aktuellen Entleiher zuordnet. Wenn ein Buch :math:`b \in B` nicht ausgeliehen ist, ist :math:`leihtAus(b)` nicht definiert (geschrieben als :math:`b \notin \text{dom}(leihtAus)`).

3. **Integritätsbedingungen (Invarianten):**
   - Jedes Buch im System muss mindestens einen Autor haben: :math:`\forall b \in B: \exists a \in A: (a, b) \in schrieb`
   - Die Eindeutigkeit der Ausleihe wird durch die funktionale Natur von :math:`leihtAus` sichergestellt (ein Buch kann zu einem Zeitpunkt nur an maximal eine Person ausgeliehen sein).

Anwendungsfall 3: Logikbasierte Geschäftsregeln (Rabattsystem)
--------------------------------------------------------------

Das Rabattsystem illustriert den Einsatz von Aussagen- und Prädikatenlogik zur Spezifikation komplexer Entscheidungsregeln.

**Beschreibung:**
Spezifizieren Sie die Bedingungen, unter denen ein Kunde beim Kauf in einem Online-Shop einen Preisnachlass erhält.

**Mathematische Relevanz:**
- **Prädikate:** Definieren Sie logische Aussagen über Kundenmerkmale (z. B. :math:`istPremium(Kunde)`, :math:`umsatz(Kunde) > 100`).
- **Logische Verknüpfungen:** Kombinieren Sie diese Prädikate mittels Konjunktion (:math:`\land`), Disjunktion (:math:`\lor`) und Implikation (:math:`\implies`), um die finale Rabattentscheidung abzuleiten.
- **Konsistenz:** Überprüfen Sie, ob die Regeln widerspruchsfrei sind und alle möglichen Fälle abdecken.
