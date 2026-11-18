# Bluetooth-Gerätenamen und Nummerierung

**Stand: 18.11.2026.** Umbenennung und Benutzerführung wurden nach Rückmeldung der testenden Person mit **genau zwei PocketLab Voyager 2 erfolgreich erprobt**. Beide Geräte konnten anschließend mit der bestehenden phyphox-Integration verwendet werden. Die Ergebnisse gelten für diese zwei Geräte, nicht für alle 14 Unterrichtsgeräte. Es handelt sich um einen qualitativen Funktionstest, keine Kalibrierung oder quantitative Messunsicherheitsanalyse.

## Namen passend zum Experiment wählen

Die XML-Konfiguration dieses Projekts enthält den Bluetooth-Namensfilter `PL Voyager 2`. Dieser Text muss zusammenhängend, einschließlich Leerzeichen und Schreibweise, im Gerätenamen erhalten bleiben. Die Testexperimente ändern den Filter nicht.

| Gerät | Erfolgreich verwendeter Name | Empfohlene Kennzeichnung am Gehäuse |
| --- | --- | --- |
| Bisheriger Voyager 2 | `PL Voyager 2-01` | `01` |
| Neuer Voyager 2 | `PL Voyager 2-02` | `02` |

Für weitere Geräte wird die fortlaufende Nummerierung `PL Voyager 2-03` usw. empfohlen; ihre Übernahme und Erkennung sind jeweils noch zu prüfen. Keine Namen wie `Voyager-01` verwenden: Der zusammenhängende Filtertext fehlt dann. Die Nummer kennzeichnet das physische Gerät und sagt nichts über Kalibrierung, Qualität oder Messgenauigkeit aus. Ein nur auf dem Smartphone vergebener lokaler Bluetooth-Alias ist kein Nachweis einer Umbenennung des Sensors.

## Beobachtungen vom 18.11.2026

- Beim bisherigen Voyager 2 wurde `PL Voyager 2-01` sofort übernommen.
- Beim neuen Voyager 2 wurde `PL Voyager 2-02` verzögert übernommen. Ein Neustart des Geräts scheint geholfen zu haben. Ohne isolierten Vergleich ist damit weder eine Ursache noch eine allgemein erforderliche Maßnahme nachgewiesen.
- Beide umbenannten Geräte waren anschließend mit der bestehenden phyphox-Integration verwendbar. Das Suchmuster `PL Voyager 2` bleibt unverändert.
- Der Herstellerdialog nennt **3–13 Zeichen und ausschließlich Buchstaben/Ziffern**. Die tatsächlich akzeptierten vollständigen Namen `PL Voyager 2-01` und `PL Voyager 2-02` enthalten dagegen Leerzeichen und einen Bindestrich. Diese Abweichung ist eine konkrete Beobachtung; daraus folgt keine allgemeine Regel über zulässige Zeichen, Namenslängen oder die Zählweise des Dialogs.

Bei verzögerter Anzeige zunächst die Verbindung beenden, das Gerät aus-/einschalten und erneut suchen. Beobachteten Namen und Verlauf notieren; eine verzögerte Anzeige allein belegt keinen fehlgeschlagenen Speichervorgang. Die Herstellerhinweise zum Bluetooth-Cache stehen im folgenden Abschnitt. Eine konkrete Cache-Ursache wurde im Zwei-Geräte-Test nicht nachgewiesen.

## Umbenennen in PocketLab Notebook

Nach der offiziellen Anleitung [How to rename PocketLab sensors?](https://support.thepocketlab.com/knowledge/how-to-rename-pocketlab-sensors), abgerufen am 18.11.2026:

1. [PocketLab Notebook](https://app.thepocketlab.com) in Chrome oder Edge öffnen und als **Teacher** anmelden; diese Anmeldung ist für die Umbenennung erforderlich.
2. Unter **Trials → Connect a PocketLab** das eingeschaltete Zielgerät auswählen und mit **Pair** verbinden.
3. Oben rechts das Einstellungsmenü öffnen, **Rename PocketLab** wählen, beispielsweise `PL Voyager 2-01` eingeben und **Save** wählen.
4. Das Gerät durch längeres Drücken des Einschaltknopfs ausschalten, die Browserseite aktualisieren und erneut verbinden. Der alte Name kann dabei zunächst weiterhin erscheinen. Das Umbenennungsmenü jetzt **nicht erneut öffnen**, da dies laut Hersteller den Vorgang zurücksetzt.
5. Nach dem Verbinden nochmals ausschalten, die Seite aktualisieren und wieder verbinden. Laut Hersteller können bekannte Clients den alten Namen noch für ein bis zwei Verbindungen aus ihrem Bluetooth-Cache anzeigen; ein bisher unverbundener Client soll den neuen Namen direkt sehen.

Die Herstellerseite nennt „Voyager“. Die Anwendung auf unsere beiden Voyager-2-Geräte ist durch die oben dokumentierten Ergebnisse funktional erprobt; eine allgemeine Validierung aller Namensregeln oder langfristiger Persistenz folgt daraus nicht. Andere PocketLab- oder Notebook-Verbindungen vor dem Einsatz in phyphox beenden.

## Verfahren zur Wiederholung mit genau zwei Voyager 2

Vorbereitung: Genau zwei Geräte verwenden, mit abnehmbaren Markierungen **01** und **02** versehen und ihre bisherigen Namen notieren. Datum, Android-/phyphox-Version, Notebook-Browser und gegebenenfalls sichtbare Firmware-Version notieren. Testprotokoll und Messdateien lokal aufbewahren; keine personenbezogenen Daten veröffentlichen. Es werden nacheinander Einzelverbindungen geprüft, keine gleichzeitige Zwei-Geräte-Erfassung in einem Experiment.

1. **Gerät 01:** Gerät 02 bleibt ausgeschaltet. Gerät 01 nach obiger Notebook-Anleitung in `PL Voyager 2-01` umbenennen und alle genannten Ausschalt-/Neuverbindungszyklen durchführen. Jede tatsächlich beobachtete Namensanzeige notieren. Erst nach der Kontrolle die Notebook-Verbindung beenden und Gerät 01 ausschalten.
2. **Gerät 02:** Gerät 01 bleibt ausgeschaltet. Denselben Ablauf für `PL Voyager 2-02` ausführen; Notebook-Verbindung anschließend beenden.
3. **Dauerhaftigkeit und Cache:** Beide Geräte vollständig ausschalten und erneut einschalten. In phyphox eine neue Gerätesuche starten. Falls ein alter Name erscheint, Zeitpunkt und Anzahl der Neuverbindungen notieren. Zunächst erneut suchen, phyphox schließen/neu öffnen und bei Bedarf Bluetooth aus-/einschalten. Falls verfügbar, auf einem bisher unverbundenen Client gegenprüfen. Einen alten Cache-Eintrag nicht mit einem sicher fehlgeschlagenen Speichern gleichsetzen; solange die Anzeige nicht eindeutig ist, ist der Test offen. Keine App-Daten oder Messdateien löschen.
4. **Beide Namen finden:** Bei eingeschalteten Geräten 01 und 02 in der phyphox-Geräteauswahl prüfen, ob **beide vollständigen Namen gleichzeitig** erscheinen und durch den unveränderten Filter gefunden werden. Zur physischen Zuordnung Gerät 02 ausschalten und die Suche neu starten; nur 01 sollte übrig bleiben. Danach umgekehrt verfahren. Bei unklarer Zuordnung nicht auf Verdacht verbinden.
5. **Gerät 01 separat messen:** Nur 01 einschalten. Im Testexperiment `PL Voyager 2-01` verbinden, Beschleunigung auswählen, **▶ oben rechts** starten und erst danach **Messdaten STARTEN** antippen. Nach etwa zehn Sekunden mit einer vorsichtigen Lageänderung fortsetzen. Danach **Messdaten STOPPEN**, phyphox pausieren und **⋮ → Daten exportieren → CSV → speichern/teilen**. Prüfen, ob Beschleunigungswerte mit zugehöriger Zeitspalte vorliegen. Anschließend Verbindung beenden und 01 ausschalten.
6. **Gerät 02 separat messen:** Nur 02 einschalten und dasselbe Verfahren durchführen. Eine neue Aufzeichnung verwenden; die erste vorher sichern. Die Dateien eindeutig als `Voyager2_01_Test.csv` und `Voyager2_02_Test.csv` zuordnen. Werte plausibilisieren, ohne daraus eine Kalibrierung abzuleiten.
7. **Abschluss:** Beide Geräte erneut aus-/einschalten, beide Namen in der Suche nochmals prüfen und Gerätekennzeichnung, Namensanzeige, gewähltes Gerät, Aufnahme und CSV-Zuordnung zusammen bewerten.

Für eine Wiederholung gelten als Prüfkriterien: Beide Namen bleiben nach dem Neustart bestehen, sind gleichzeitig auffindbar und physisch eindeutig zuordenbar, und jedes Gerät liefert einzeln Messwerte samt Zeitspalte. Abweichungen mit erwartetem/beobachtetem Verhalten dokumentieren. Der Funktionstest vom 18.11.2026 wurde für die zwei Geräte als erfolgreich zurückgemeldet; Anzahl und zeitlicher Verlauf aller Neuverbindungen wurden nicht quantitativ ausgewertet. Der Test ist keine Erprobung aller 14 Unterrichtsgeräte und kein Langzeitstabilitätsnachweis.

## Bedienhinweise und weitere Tests

Die vollständige Messreihenfolge und Hinweise zu NaN stehen in der [Projektanleitung](../README.md). Die separat benannten Experimente [Deutsch](experiments/tests/Voyager2_Benutzerfuehrung_Test_DE.phyphox) und [Deutsch/Englisch](experiments/tests/Voyager2_Benutzerfuehrung_Test_DE_EN.phyphox) wurden am 18.11.2026 hinsichtlich Benutzerführung und Funktion erfolgreich erprobt. Der lokale Testbericht dokumentiert positive Rückmeldungen zu Darstellung, Startreihenfolge, Sensorwechsel, Beenden und CSV-/NaN-Hinweisen; ein eigener CSV-Testexport ist dort nicht hinterlegt. Die Testdateien bleiben Entwicklungsstände, keine neue Veröffentlichung. Die veröffentlichten v0.9.6-Dateien bleiben unverändert.

Weitere Prüfungen betreffen die übrigen Unterrichtsgeräte, Langzeitverhalten und gegebenenfalls zusätzliche Namen. Die bereits erfolgreiche Zwei-Geräte-Erprobung wird dadurch nicht als noch offen dargestellt.
