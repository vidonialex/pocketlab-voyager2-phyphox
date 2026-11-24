# PocketLab Voyager 2 – Integration in phyphox

**Version:** v0.9.7 (experimenteller Prototyp; finale Android-Funktionstests bestanden). Versionstag und GitHub-Release sind separate Veröffentlichungsschritte.

**Projektkontext:** Bachelorstudium Physik

## Zielsetzung

Dieses Projekt untersucht die Einbindung des **PocketLab Voyager 2** in die Android-App **phyphox**. Eine eigens entwickelte phyphox-Experimentdatei empfängt Messdaten über Bluetooth Low Energy (BLE), ermöglicht die dynamische Auswahl von Sensorgrößen und stellt die Daten in Zeitdiagrammen und als CSV-Export bereit.

Es handelt sich um eine unabhängige Implementierung, nicht um ein offizielles Angebot von PocketLab oder phyphox.

**Projektseite:** https://vidonialex.github.io/pocketlab-voyager2-phyphox/

## Installation

Benötigt werden ein PocketLab Voyager 2, ein Android-Smartphone mit Bluetooth und die installierte [phyphox-App](https://phyphox.org/).

| Verfahren | Sprache | Internet beim Import | Zugang |
| --- | --- | --- | --- |
| Direkter Dateidownload | Deutsch | Ja, zum Herunterladen | [v0.9.7 (.phyphox)](docs/experiments/Voyager2_v097_DE.phyphox) |
| Direkter Dateidownload | Deutsch / Englisch | Ja, zum Herunterladen | [v0.9.7 (.phyphox)](docs/experiments/Voyager2_v097_DE_EN.phyphox) |
| Ein Online-QR-Code | Deutsch / Englisch | Ja | [v0.9.7-QR-Code](docs/qr/online_v097.png) |
| Offline-QR-Codes (13) | Deutsch | Nein, nach vorherigem Herunterladen | [v0.9.7-QR-Paket (.zip)](docs/downloads/Voyager2_v097_Offline_QR_DE.zip) |

**Android-Freigabetests abgeschlossen (21.11.2026):** Die aktuellen deutschen und zweisprachigen v0.9.7-Dateien wurden erfolgreich importiert, Bedienhinweise beziehungsweise Übersetzungen geprüft und Messungen durchgeführt. Die Wiederaufnahme STOPP → Pause → ▶ → STARTEN sowie der Import aller **13 aktuellen Offline-QR-Segmente** mit anschließender IR-Messung waren erfolgreich. Noch offen sind die Online-QR-Live-Prüfung, HTTP-/Pages-Prüfung und die weiteren Veröffentlichungsschritte.

Bei der zweisprachigen Experimentdatei richtet sich die Sprache nach der Spracheinstellung der App beziehungsweise des Smartphones. Die deutsche Datei bleibt unabhängig davon deutsch.

**Vorversion v0.9.5:** [Deutsch](docs/experiments/Voyager2_v095_DE.phyphox) · [Deutsch/Englisch](docs/experiments/Voyager2_v095_DE_EN.phyphox) · [Offline-QR-Paket](docs/downloads/Voyager2_v095_Offline_QR_DE.zip).

**Veröffentlichte v0.9.6, unverändert:** [Deutsch](docs/experiments/Voyager2_v096_DE.phyphox) · [Deutsch/Englisch](docs/experiments/Voyager2_v096_DE_EN.phyphox) · [Online-QR](docs/qr/online_v096.png) · [Offline-QR-Paket mit acht Codes](docs/downloads/Voyager2_v096_Offline_QR_DE.zip).

**Direktdownload:** Die gewünschte `.phyphox`-Datei auf dem Smartphone speichern und mit phyphox öffnen beziehungsweise importieren.

**Online-QR:** Den QR-Scanner im phyphox-Hauptmenü öffnen und den einzelnen Code scannen. Eine Internetverbindung ist erforderlich, da der Code auf die bereitgestellte Experimentdatei verweist.

**Offline-QR:** Das ZIP-Paket vorab herunterladen und entpacken. Anschließend im phyphox-QR-Scanner alle 13 nummerierten v0.9.7-Codes nacheinander scannen. Während des Imports ist keine Internetverbindung nötig. Codes verschiedener Versionen nicht mischen.

## Messung durchführen

Vorbereitung: Voyager 2 einschalten, Bluetooth am Smartphone aktivieren und eine bestehende Verbindung zur PocketLab-App oder anderen Sensor-Apps beenden. Das Experiment in phyphox öffnen.

1. Den Voyager 2 in phyphox über Bluetooth verbinden.
2. Unter **Sensorauswahl / Sensor Selection** die gewünschten Sensoren auswählen.
3. Die phyphox-Aufzeichnung mit **▶ oben rechts** starten.
4. **Danach „Messdaten STARTEN / START DATA“ antippen (empfohlen).** Diesen Ablauf auch beim Wiederaufnehmen nach einer Pause verwenden. Jetzt die Messwerte und Zeitdiagramme unter **Bewegung / Motion** und **Umgebung / Weather** beobachten.
5. **Sensorwechsel:** „Messdaten STOPPEN / STOP DATA“, neue Sensoren auswählen, wieder „Messdaten STARTEN / START DATA“. Die phyphox-Aufzeichnung bleibt dabei aktiv; falls sie pausiert wurde, auch wieder ▶ starten.
6. **Beenden:** erst „Messdaten STOPPEN / STOP DATA“, danach phyphox pausieren.
7. **Export:** **⋮ → Daten exportieren → CSV → speichern/teilen**.

**Beobachtung zur Startreihenfolge:** STARTEN vor ▶ funktionierte beim erstmaligen Messstart, nach dem Pausieren und Wiederaufnehmen jedoch nicht zuverlässig. Die Ursache ist nicht abschließend geklärt. Deshalb empfehlen wir immer ▶ → „Messdaten STARTEN“. Dies ist eine Beobachtung dieses Tests, kein Nachweis eines allgemeinen phyphox-Verhaltens.

Die Reiter enthalten aufklappbare Hilfetexte. Der Reiter **Status** erläutert Verbindungsprobleme und mögliche Datenlücken.

**NaN im CSV:** NaN bedeutet „Not a Number“. Insbesondere werden in der gemeinsamen CSV-Tabelle unterschiedlich lange Datenreihen mit NaN aufgefüllt. NaN ist nicht gleich null und nicht automatisch ein Sensordefekt; es kann auch einen fehlenden oder ungültigen Zahlenwert kennzeichnen. Verwende zur zeitlichen Zuordnung die **separate Zeitspalte jeder Messgröße**. Die gleiche Tabellenzeile bedeutet bei unterschiedlich langen Datenreihen nicht automatisch den gleichen Messzeitpunkt. NaN nicht ungeprüft durch null ersetzen.

Bei mehreren Geräten hilft die Anleitung [Bluetooth-Gerätenamen und Nummerierung](docs/BLUETOOTH_GERAETENAMEN.md). Am **18.11.2026** wurden genau zwei Voyager 2 erfolgreich in `PL Voyager 2-01` und `PL Voyager 2-02` umbenannt und anschließend mit der bestehenden Integration verwendet. Beim ersten Gerät wurde der Name sofort, beim zweiten verzögert übernommen; ein Neustart scheint geholfen zu haben. Das Suchmuster `PL Voyager 2` bleibt unverändert. Die Erprobung umfasst nicht alle 14 Unterrichtsgeräte. Die Anleitung dokumentiert auch die Abweichung zwischen den angezeigten Namensregeln des Herstellerdialogs und den tatsächlich akzeptierten Namen, ohne allgemeine Namensregeln daraus abzuleiten.

## Entwicklungstest der Bedienhinweise

Separat benannte Testdateien auf Basis von v0.9.6 ergänzen die neue Reihenfolge und einen direkt sichtbaren START-Hinweis in phyphox: [Test Deutsch](docs/experiments/tests/Voyager2_Benutzerfuehrung_Test_DE.phyphox) · [Test Deutsch/Englisch](docs/experiments/tests/Voyager2_Benutzerfuehrung_Test_DE_EN.phyphox). **Die Benutzerführung wurde am 18.11.2026 mit zwei Voyager 2 erfolgreich erprobt.** Der qualitative Funktionstest wurde durch die testende Person bestätigt; er ist keine Kalibrierung oder Messunsicherheitsanalyse. Die Messlogik stammt unverändert aus v0.9.6; die veröffentlichten v0.9.6-Dateien und ihre QR-Pakete bleiben unverändert. Die Tests verwenden eigene Experimenttitel zur Unterscheidung von der veröffentlichten Version und sind weiterhin Entwicklungsstände.

## Verfügbare Messgrößen

**IR integriert:** [Experiment 057 – Entwicklung und Fehlerdiagnose](docs/IR_RANGEFINDER_057.md) dokumentiert den fehlenden Pufferverbrauch der isolierten Originaldatei, die erfolgreiche Debug01-Korrektur und die am 19.11.2026 erfolgreich getestete Zehnfach-Integration. Die getrennten [integrierten Testdateien DE](docs/experiments/tests/Voyager2_Sensorwahl_10_IR_057_Test_DE.phyphox) und [DE/EN](docs/experiments/tests/Voyager2_Sensorwahl_10_IR_057_Test_DE_EN.phyphox) bleiben unverändert; v0.9.7 übernimmt deren Messlogik.

| Messgröße | Anzeigeeinheit | Hinweis |
| --- | --- | --- |
| Beschleunigung (X, Y, Z) | m/s² | Drei Raumachsen |
| Winkelgeschwindigkeit (X, Y, Z) | rad/s | Drei Raumachsen |
| Magnetfeld (X, Y, Z) | µT | Drei Raumachsen |
| Interne Temperatur | °C | Temperatur des Sensors |
| Externe Temperatursonde | °C | Temperatur des angeschlossenen Fühlers; separat auswählbar |
| Barometrischer Druck | hPa | Im CSV-Export in Pa |
| Relative Luftfeuchtigkeit | % | Dimensionslose relative Feuchte |
| Hitzeindex | °C | Vom Sensor übertragene Messgröße |
| Umgebungslichtintensität | lx | Beleuchtungsstärke |
| IR-Entfernung | m | Angegebener Bereich 0,001–6,0 m; feste Diagrammachse 0–6 m, keine Begrenzung der exportierten Rohwerte |

Die zehn Messgrößen sind einzeln oder gleichzeitig auswählbar und ergeben zusammen **16 numerische Messkanäle**. Die einzelnen Vektorkomponenten werden getrennt dargestellt und exportiert. Zusammen mit zehn zugehörigen, geschätzten Zeitspalten enthält der CSV-Export **26 Spalten**. Die feste IR-Achse 0–6 m betrifft nur die Darstellung; außerhalb liegende Rohwerte bleiben in Wertanzeige und CSV erhalten.

## Datenerfassung und Grenzen

- **Zeitbasis:** phyphox erhält BLE-Datenpakete. Die Zeitpunkte innerhalb eines Pakets werden aus dem Empfangszeitpunkt und einer angenommenen Abtastrate von etwa 20 Hz rekonstruiert. Die Zeitachse besteht **nicht** aus Hardware-Zeitstempeln des Voyager 2.
- **Datenlücken:** Bei unterbrochener Bluetooth-Verbindung und während eines gestoppten Datenstroms werden keine Werte nachträglich ergänzt. Nach einer Wiederverbindung muss der Datenstrom gegebenenfalls erneut gestartet werden.
- **Anfangswerte:** Für die bisherigen Umweltkanäle wird wie in v0.9.6 das erste passende Paket nach START verworfen. IR und Bewegungskanäle behalten es. Negative IR-Werte und Werte um 8,191 m wurden beobachtet; ihre Bedeutung ist ungeklärt. Sie werden nicht als Fehlercodes interpretiert, gefiltert, interpoliert oder durch null ersetzt.
- **Messgenauigkeit:** Im Projekt wurde bislang keine unabhängige Kalibrierung oder umfassende metrologische Validierung der Sensoren durchgeführt.
- **Paketverarbeitung:** Bis zu acht Notifications werden je Analysezyklus verarbeitet; weitere bleiben vorgemerkt. Ungültige Mischstapel werden vollständig verworfen und gezählt. Nach STOPP vor dem Pausieren gegebenenfalls auf das Leeren des vorgemerkten Puffers warten. Dauerhafte Überlast kann die unbegrenzt angelegten Empfangs-/Wartepuffer wachsen lassen; eine systematische Prüfung von Rechenlast und Speicherverhalten steht aus. Messwertpuffer halten höchstens 12.000 Werte je Kanal (bei ungefähr 20 Hz etwa zehn Minuten); rechtzeitig exportieren.
- **Weitere Entwicklung:** Weitere externe Fühler (z. B. Drucksonde), Orientierung und andere abgeleitete Bewegungsgrößen sind nicht integriert. Systematische Langzeitstabilitätstests stehen aus.
- **Kompatibilität:** Die ursprüngliche v0.9.6-Erprobung erfolgte mit einem Voyager 2 und einem Android-Smartphone. Am 18.11.2026 wurden Benutzerführung und Umbenennung mit genau zwei Voyager 2 erfolgreich erprobt. Eine Prüfung aller 14 Unterrichtsgeräte sowie eine systematische Prüfung unterschiedlicher Geräte und Betriebssysteme stehen aus.

## Verifikation

Die Prüfung der veröffentlichten Dateien erfolgt mit Python (Standardbibliothek):

```bash
python scripts/check_release.py
```

Das Skript kontrolliert SHA-256-Prüfsummen der Experimentdateien und des Offline-Pakets, grundlegende XML- und ZIP-Eigenschaften sowie die wichtigsten Dateiverweise. Es ersetzt keinen Funktionstest auf einem Smartphone.

Die externe Temperatursonde wurde auf Android funktional getestet: einzeln, gemeinsam mit interner Temperatur, gemeinsam mit Beschleunigung und mit allen neun Messgrößen gleichzeitig. Diese Tests sind keine Kalibrierung oder metrologische Validierung. Ein Langzeittest steht noch aus.

**Bestätigte Android-Abschlussprüfungen vom 15.11.2026:** Die endgültige deutsche und die zweisprachige v0.9.6-Experimentdatei wurden erfolgreich importiert und visuell geprüft. Alle acht korrigierten Offline-QR-Codes wurden erfolgreich in phyphox importiert. Die externe Temperatursonde ist in der Sensorauswahl und den Info-/Hilfetexten vorhanden; eine Temperaturmessung mit der externen Sonde war erfolgreich. Die gleichzeitige Erfassung aller neun Messgrößen war bereits zuvor erfolgreich getestet.

Die HTTP-Erreichbarkeit der veröffentlichten v0.9.6-Projektwebsite und ihrer Downloads wurde am 15.11.2026 geprüft. Der Online-QR-Import auf einem Android-Smartphone bleibt ein offener manueller Test. Die funktionalen Tests bestätigen keine unabhängige Kalibrierung oder metrologische Validierung.

**Bestätigte Android-Tests vom 19.11.2026 (Experiment 057.5):** IR allein; IR mit Licht, externer Temperatursonde oder Beschleunigung; alle zehn Messgrößen gleichzeitig; Wiederverbindung und erneute Messung; deutsch-englische Version. Wandabstand und Beleuchtung wurden unabhängig mit Bewegung beziehungsweise einer Taschenlampe verändert, ohne den Sensor abzudecken. Beide Kanäle reagierten gleichzeitig qualitativ passend. Dies bestätigt Funktion und Kanalzuordnung, keine quantitative Genauigkeit. Die abschließenden Android-Nachtests der aktuellen v0.9.7-Dateien folgten am 21.11.2026 und sind ebenfalls bestanden.

**Bestätigte finale Android-Nachtests vom 21.11.2026:** Die aktuellen DE- und DE/EN-Experimentdateien sowie alle 13 Offline-QR-Segmente aus Commit `88396e544828249942015b697ca2dbde89c628b1` wurden erfolgreich importiert und funktional geprüft. Bedienhinweise, Übersetzungen, Messung und Wiederaufnahme STOPP → phyphox pausieren → ▶ → STARTEN bestanden; nach dem Offline-QR-Import war eine IR-Messung erfolgreich. Frühere Tests mit zwölf Codes betrafen einen vorherigen Kandidatenstand. Online-QR-Live-Prüfung und HTTP-/Pages-Prüfung bleiben für den Veröffentlichungsablauf offen. Auch diese Funktionstests sind keine Kalibrierung oder metrologische Genauigkeitsprüfung.

Neue Funktionen, Messergebnisse, technische Erkenntnisse und Bedienhinweise werden zeitnah in der jeweils betroffenen Projektdokumentation ergänzt. Eine vollständige sprachliche, stilistische und gestalterische Überarbeitung folgt separat und verzögert diese fachlichen Aktualisierungen nicht.

## Projektstatus

**v0.9.7 ist ein experimenteller Prototyp mit bestandenen finalen Android-Funktionstests.** Eine unabhängige Kalibrierung und systematische Langzeitprüfungen fehlen. Versionstag und GitHub-Release erfolgen im gesonderten Veröffentlichungsablauf. Rückmeldungen zur Bedienbarkeit, zu weiteren Messgrößen und zur Messdatenqualität sind willkommen.

## Lizenz und Zitierung

Die eigenen Beiträge von Alexander Vidoni werden unter der **[PolyForm Noncommercial License 1.0.0](LICENSE)** angeboten: öffentlich verfügbarer Quellcode unter einer nichtkommerziellen Lizenz, keine OSI-konforme Open-Source-Software. Nichtkommerzielle Verwendung, Veränderung und Weitergabe sind nach den Lizenzbedingungen erlaubt. Schulen und Universitäten als Bildungsinstitutionen sowie öffentliche Forschungsorganisationen dürfen das Projekt unabhängig von der Finanzierung nutzen, einschließlich kostenpflichtiger Lehre durch solche Bildungsinstitutionen. Für andere Forschungseinrichtungen kommt insbesondere ein nichtkommerzieller Verwendungszweck in Betracht; kommerzielle Forschung ist nicht pauschal freigegeben.

Bei Weitergabe müssen der Lizenztext oder seine URL sowie der verpflichtende Copyright-Hinweis aus **[NOTICE](NOTICE)** mitgegeben und erhalten bleiben. Eine öffentliche Nennung bei jeder Nutzung oder eine besondere UI-Erhaltungspflicht wird nicht zusätzlich verlangt. Für kommerzielle Nutzungen außerhalb der erlaubten Zwecke ist eine gesonderte Berechtigung der jeweiligen Rechteinhaber erforderlich; Alexander Vidoni kann seine eigenen Beiträge separat kommerziell lizenzieren. Rechte an Beiträgen Dritter werden dadurch nicht eingeräumt.

Weitere Erläuterungen zu [Lizenzumfang, Herkunft und künftigen Beiträgen](docs/LIZENZ.md) sowie die [Zitiermetadaten](CITATION.cff) sind im Repository enthalten. Wissenschaftliche Zitierung wird empfohlen, ist keine zusätzliche Lizenzbedingung. Die Metadaten beziehen sich auf die zuletzt veröffentlichte Version v0.9.7 vom 21.11.2026; bestehende Releases, Experimente und QR-Pakete werden durch diese Lizenzvorbereitung nicht verändert.

PocketLab, Voyager 2 und phyphox sind Produkt- beziehungsweise Projektnamen der jeweiligen Rechteinhaber. Das Projekt ist unabhängig; es besteht keine offizielle Verbindung oder behauptete Zusammenarbeit mit PocketLab oder phyphox.
