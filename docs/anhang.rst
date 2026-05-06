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
