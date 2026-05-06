Anhang: Entscheidungsdokumentation
==================================

Dieser Anhang enthält die Dokumentation der im Projekt getroffenen Entscheidungen.

.. contents:: Entscheidungen
   :local:

Buchlayout und Kapitelstruktur
------------------------------

Für das Layout und die Struktur des Buches wurden die folgenden drei Optionen bewertet:

1. **Top-Down (Theorie vor Praxis)**: Ein systematischer Aufbau, der mit den mathematischen Grundlagen beginnt und diese schrittweise auf komplexe Softwarespezifikationen anwendet. Dies stellt sicher, dass alle Konzepte präzise eingeführt werden, bevor sie in der Praxis verwendet werden. (**Ausgewählt**)
2. **Bottom-Up (Praxis vor Theorie)**: Ein problemgetriebener Ansatz, der mit realen Softwareproblemen beginnt und die notwendige Mathematik "just-in-time" einführt. Dies könnte motivierender sein, birgt aber das Risiko, dass die mathematische Strenge und die Tiefe der Fundamente zugunsten der schnellen Anwendbarkeit leiden. (**Verworfen**)
3. **Modular (Themenspezifisch)**: Das Buch wird in unabhängige Module unterteilt (z.B. ein Modul für Logik, eines für Mengenlehre, eines für Zustandsmaschinen). Dies ermöglicht ein selektives Lesen, erschwert jedoch die Darstellung des "roten Fadens" und der tiefen Zusammenhänge zwischen den mathematischen Disziplinen. (**Verworfen**)

Mathematische Notation und Symbolik
-----------------------------------

Für die im Buch verwendete mathematische Notation wurden die folgenden drei Optionen bewertet:

1. **Standard-Mathematik (ISO 80000-2)**: Verwendung der international standardisierten mathematischen Symbole und Schreibweisen. Dies bietet die höchste Universalität und Präzision, da sie unabhängig von spezifischen Spezifikationssprachen ist. (**Ausgewählt**)
2. **Z-Notation**: Eine formale Spezifikationssprache basierend auf der Zermelo-Fraenkel-Mengenlehre. Sie ist sehr mächtig für Softwarespezifikationen, erfordert aber eine hohe Einarbeitungszeit für Leser, die nicht mit formalen Methoden vertraut sind. (**Verworfen**)
3. **Programmiersprachen-ähnliche Notation**: Verwendung von Konstrukten, die modernen funktionalen Programmiersprachen ähneln (z.B. Haskell-ähnlich). Dies wäre für Softwareentwickler leichter zugänglich, könnte aber die mathematische Strenge und die universelle Anwendbarkeit einschränken. (**Verworfen**)

Auswahlkriterien für Anwendungsfälle
------------------------------------

Für die Auswahl der im Buch behandelten Anwendungsfälle wurden die folgenden drei Optionen bewertet:

1. **Mathematisch-konzeptionell**: Die Auswahl der Anwendungsfälle orientiert sich an den zu vermittelnden mathematischen Konzepten (z. B. Zustandsmaschinen für Verhaltensspezifikationen, Mengenlehre für Datenmodelle, Prädikatenlogik für Geschäftsregeln). Dies stellt sicher, dass die theoretischen Grundlagen direkt in praktischen, für das jeweilige Konzept typischen Szenarien angewendet werden. (**Ausgewählt**)
2. **Domänen-basiert**: Die Auswahl erfolgt nach verschiedenen Anwendungsdomänen (z. B. Medizintechnik, Finanzwesen, Luft- und Raumfahrt). Dies würde die Vielseitigkeit der Methoden demonstrieren, könnte aber dazu führen, dass mathematische Konzepte redundant oder unvollständig behandelt werden, da sie sich an der Domäne und nicht an der Theorie orientieren. (**Verworfen**)
3. **Komplexitäts-basiert**: Die Anwendungsfälle werden nach steigendem Schwierigkeitsgrad ausgewählt, beginnend bei trivialen Beispielen bis hin zu hochkomplexen Systemen. Dies könnte den Lernfortschritt unterstützen, erschwert aber die systematische Einführung spezifischer mathematischer Werkzeuge, da die Komplexität oft quer zu den konzeptionellen Grundlagen liegt. (**Verworfen**)

Auswahl der Anwendungsfälle
---------------------------

Für die drei Kategorien von Anwendungsfällen wurden jeweils drei Optionen bewertet:

**Kategorie 1: Zustandsbasierte Steuerung**

1. **Ampelsystem**: Ein klassisches Beispiel für endliche Zustandsautomaten. Es ist leicht verständlich und ermöglicht die Demonstration von Zustandsübergängen, Zeitbedingungen und Sicherheitszusagen (z. B. "Nie beide Richtungen gleichzeitig grün"). (**Ausgewählt**)
2. **Getränkeautomat**: Demonstriert ebenfalls Zustände, ist aber in der Modellierung der Interaktionen oft komplexer ohne zusätzlichen mathematischen Mehrwert für die Grundlagen gegenüber dem Ampelsystem. (**Verworfen**)
3. **Mikrowelle**: Beinhaltet Sicherheitsaspekte und Zustände, ist jedoch in der alltäglichen Wahrnehmung der Zustandsübergänge weniger intuitiv als ein Ampelsystem. (**Verworfen**)

**Kategorie 2: Relationales Datenmodell**

1. **Bibliotheksverwaltung**: Bietet eine ideale Struktur zur Anwendung der Mengenlehre und Relationenalgebra. Die Konzepte von Primärschlüsseln, Fremdschlüsseln und Integritätsbedingungen lassen sich hervorragend mathematisch abbilden. (**Ausgewählt**)
2. **Lagerverwaltung**: Ähnlich wie die Bibliotheksverwaltung, aber oft mit komplexeren numerischen Bestandsfortschreibungen verbunden, die vom Fokus auf relationale Strukturen ablenken könnten. (**Verworfen**)
3. **Personalverwaltung**: Bietet relationale Strukturen, bringt aber oft datenschutzrechtliche Komplexitäten in der Diskussion mit sich, die für ein mathematisches Lehrbuch unnötig sind. (**Verworfen**)

**Kategorie 3: Logikbasierte Geschäftsregeln**

1. **Rabattsystem**: Ermöglicht die präzise Anwendung von Prädikatenlogik und Aussagenlogik zur Definition von Bedingungen (z. B. "Wenn Kunde = Premium UND Umsatz > 100, DANN Rabatt = 10%"). (**Ausgewählt**)
2. **Kreditbewilligung**: Sehr gut für Logik geeignet, erfordert aber oft tiefes Domänenwissen über Finanzmathematik, was die mathematische Kernbotschaft überlagern könnte. (**Verworfen**)
3. **Steuerberechnung**: Bietet hochkomplexe Regelsysteme, ist aber aufgrund der ständigen gesetzlichen Änderungen als statisches Buchbeispiel weniger geeignet. (**Verworfen**)
