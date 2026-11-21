# Experiment 057 – IR-Entfernung und Integration

## Ergänzung vom 19.11.2026: erfolgreiche Android-Integration

Der isolierte Debug01-Test war nach Ergänzung des verbrauchenden `keep="false"`-Zugriffs erfolgreich: START/STOPP, Entfernungskurve, CSV und Wiederverbindung funktionierten. Anschließend wurde IR als zehnte Messgröße integriert. Die unveränderten integrierten Testdateien [DE](experiments/tests/Voyager2_Sensorwahl_10_IR_057_Test_DE.phyphox) und [DE/EN](experiments/tests/Voyager2_Sensorwahl_10_IR_057_Test_DE_EN.phyphox) haben Experiment 057.5 am 19.11.2026 bestanden (Rückmeldung der testenden Person).

Erfolgreiche Bereiche: IR allein; IR mit Licht; IR mit externer Temperatursonde; IR mit Beschleunigung; alle zehn Messgrößen gleichzeitig; Wiederverbindung und erneute Messung; deutsch-englische Version. Wandabstand und Beleuchtung wurden unabhängig mit Bewegung beziehungsweise einer Taschenlampe verändert, ohne den Sensor abzudecken. Beide Kanäle reagierten gleichzeitig qualitativ passend. Damit ist die zuvor nur abgeleitete Position von IR vor Licht funktional geprüft; eine quantitative Kalibrierung oder Genauigkeitsbestimmung folgt daraus nicht.

Die Entwicklung verlief von der erfolgreichen offiziellen PocketLab-App über die HCI-Analyse zur ersten isolierten phyphox-Datei, zur Diagnose des fehlenden Pufferverbrauchs, zum erfolgreichen Debug01-Test und schließlich zur getesteten gemeinsamen Auswahl. Der historische Fehlerbefund bleibt unten erhalten. Die damaligen offenen Android-Tests beschreiben den Stand vor diesen erfolgreichen Tests.

## v0.9.7-Releasekandidat

[Deutsch](experiments/Voyager2_v097_DE.phyphox) · [Deutsch/Englisch](experiments/Voyager2_v097_DE_EN.phyphox). Die Messlogik ist mit dem integrierten Teststand identisch; geändert sind Titel, Metadaten und dokumentarische Texte. Zehn auswählbare Messgrößen ergeben 16 numerische Messkanäle und mit zehn eigenen Zeitspalten 26 CSV-Spalten. Der bisherige Kandidat bestand am 21.11.2026 alle fünf Freigabetests: beide Direktimporte, Messung mit START/STOPP/Wiederverbindung/CSV, alle zwölf Offline-Codes und Funktion des darüber importierten Experiments. Nach der Starttextkorrektur sind die aktualisierten Dateien und Codes erneut zu importieren. Der Online-QR-Import wird nach Veröffentlichung geprüft.

IR bleibt in Metern, mit fester Diagrammachse 0–6 m (angegebener Bereich 0,001–6,0 m). Die Achsgrenze begrenzt keine Daten: negative Werte und Werte um 8,191 m bleiben in Wertanzeige, Puffer und CSV. Ihre Bedeutung ist ungeklärt; keine automatische Filterung, Interpolation oder Nullersetzung. NaN ist „Not a Number“, nicht null und nicht automatisch ein Sensordefekt. Bei unterschiedlich langen Reihen kann es Tabellenpositionen auffüllen; jeweils die eigene Zeitspalte verwenden.

Bluetooth verbinden → Sensoren auswählen → ▶ oben rechts → Messdaten STARTEN (empfohlen). STARTEN vor ▶ funktionierte beim erstmaligen Messstart, nach dem Pausieren und Wiederaufnehmen jedoch nicht zuverlässig. Die Ursache ist nicht abschließend geklärt. Deshalb empfehlen wir immer ▶ → „Messdaten STARTEN“. Sensorwechsel: STOPPEN → neue Auswahl → STARTEN. Beenden: STOPPEN → phyphox pausieren. Export: ⋮ → Daten exportieren → CSV → speichern/teilen.

## Paketverarbeitung der Zehnfach-Auswahl

Schreib-/Notification-UUIDs und Initialisierung entsprechen der unten dokumentierten Konfiguration. Sensormasken werden kombiniert; IR allein startet mit `6E 00 00 00 01`, IR mit Licht mit `6E 00 00 00 05`, alle zehn Größen mit `6E F0 1F 9E 05`. STOPP bleibt `6E 00 00 00 00`. Nach sechs Headerbytes folgen drei Abtastsätze mit je einem Float32-LE-Wert pro ausgewähltem Zahlenkanal. Reihenfolge: Beschleunigung, Winkelgeschwindigkeit, Magnetfeld, externe Sonde, interne Temperatur, Druck, Feuchte, Hitzeindex, IR, Licht. Bei allen Größen sind das 48 Float32-Wörter je Notification, insgesamt 198 Bytes.

Empfangswörter, Header und Empfangszeiten werden gemeinsam verbrauchend in einen Arbeitsstapel übernommen. Bis zu acht passende Notifications werden pro Analysezyklus nacheinander verarbeitet; weitere bleiben für spätere Zyklen vorgemerkt. Jeder der acht Arbeitsschritte verbraucht seinen Rohpuffer. Ungültige Mischstapel werden vollständig verworfen und ihre Notifications gezählt; der Zähler beweist keine Funkverluste. Die Gesamtwortprüfung erkennt keine sich kompensierenden Längenfehler einzelner Notifications mit identischem Header. START verwirft ausstehende Empfangspakete der alten Auswahl, erhält aber Messwerthistorien. Nach STOPP vor Pause gegebenenfalls das Leeren vorgemerkter Pakete abwarten.

Die bisherigen neun Messgrößen behalten Umrechnung, Umwelt-Startfilter, Diagramme und CSV-Spalten. IR erhält das erste passende Paket. Zeitrekonstruktion und Grenzen bleiben wie unten beschrieben: geschätzte, monotonisierte Empfangszeitbasis statt Hardware-Zeitstempel; keine unabhängige Kalibrierung oder systematischen Langzeitstabilitätsprüfungen. Die unbegrenzten Empfangs-/Wartepuffer können unter dauerhafter Überlast wachsen; Rechenlast und Speicher sind nicht systematisch langzeitgeprüft. Messwerthistorien bleiben auf 12.000 Werte je Kanal begrenzt. Gerätenummerierung: zwei erprobte Voyager 2, keine Erprobung aller 14 Unterrichtsgeräte.

---

## Historische Dokumentation: Stand vor erfolgreichem Debug01- und Integrationstest

Die folgenden Abschnitte halten den damaligen Diagnose- und Testplan fest. Aussagen wie „noch prüfen“ beziehen sich ausschließlich auf diesen historischen Stand; der aktuelle Funktionsnachweis steht oben.

### Ursprünglicher isolierter IR-Entfernungstest

**Stand: Experiment 057.3.** Die ursprüngliche deutsche [phyphox-Testdatei](experiments/tests/Voyager2_IR_057_Test_DE.phyphox) läuft nach Rückmeldung auf Android nach ▶ und START weiter, zeigt aber keine IR-Messwerte; sie stoppt nicht automatisch. Die Originaldatei bleibt unverändert. Eine separat benannte [Debug01-Datei](experiments/tests/Voyager2_IR_057_Test_DE_Debug01.phyphox) korrigiert den unten beschriebenen statischen Pufferfehler und muss noch auf Android geprüft werden. Nur der IR-Entfernungssensor wird aktiviert; die gemeinsame Auswahl der bisherigen neun Messgrößen und alle veröffentlichten v0.9.6-Dateien bleiben unverändert.

## Nachgewiesener Pufferfehler und minimaler Debug-Test

Die ursprüngliche IR-Datei liest `packet_words` ausschließlich mit `keep="true"`. Im Gegensatz zu v0.9.6 fehlt am Ende der Analyse ein verbrauchender Lesezugriff. Neue BLE-Notifications werden an den Eingangspuffer angehängt; der Filter verlangt jedoch exakt drei Wörter. Nach dem Ansammeln mehrerer Notifications wird der Inhalt deshalb abgewiesen. Ohne neue Notification kann ein noch vorhandenes Dreierpaket außerdem erneut verarbeitet werden. Dies erklärt eine mögliche Blockade der Auswertung, beweist aber noch nicht, welche Befehle im Android-Versuch tatsächlich gesendet wurden.

Debug01 ergänzt ausschließlich dieses abschließende Modul und einen unterscheidbaren Experimenttitel:

```xml
<count>
  <input as="buffer" keep="false">packet_words</input>
  <output as="count">packet_word_count</output>
</count>
```

Nach Verarbeitung eines Analysezyklus wird so der Rohpuffer geleert. Maßgeblich ist die [offizielle Analyse-Semantik](https://phyphox.org/docs/file-format/analysis/): Ein nicht erhaltender Input verbraucht seinen Puffer. Die übrige BLE-Konfiguration, Headerprüfung, Zeitrekonstruktion, Zahlenwerte, Diagramme und CSV-Spalten sind unverändert. Falls mehrere Notifications zwischen zwei Analysezyklen eintreffen, verwirft der unveränderte Dreiwortfilter weiterhin diesen Zyklus; Debug01 ergänzt keine Paket-Warteschlange. Der nächste Einzelpaket-Zyklus kann sich nun wieder erholen.

Die frühere lokale Simulation ersetzte den Eingangspuffer pro Notification und erfasste dessen Akkumulation nicht. Eine korrigierte Simulation mit getrennten Empfangs- und Analyseereignissen reproduziert den Fehler und prüft die minimale Korrektur; auch sie ist kein Android-Laufzeittest.

**Nächster minimaler Test:** Debug01 importieren und am eigenen Titel erkennen, `PL Voyager 2-02` verbinden, ▶ starten, START drücken und etwa zehn Sekunden messen. Kurve, kumulierten Entfernungszähler und CSV mit beiden Spalten prüfen. Die unmittelbaren Wortzähler können in Analysezyklen ohne neue Notification wieder null anzeigen und beweisen allein keinen fehlenden Empfang. Falls weiterhin keine Werte eintreffen: einen kurzen Android-HCI-Mitschnitt nur dieses Verbindungs-/START-/STOPP-Ablaufs lokal sichern. Prüfen, ob START `6E 00 00 00 01` zur Schreib-UUID gesendet wird, Notifications abonniert sind und 18-Byte-Payloads mit dem erwarteten Header eintreffen. Handles dabei für diese Verbindung den UUIDs zuordnen; die alten Handlewerte sind keine universellen Adressen. Bei Bedarf getrennt mit der originalen PocketLab-App vergleichen, nicht beide Apps gleichzeitig verbinden.

## Ausgangsbefund

Nach der bestätigten Auswertung des HCI-Mitschnitts vom 18.11.2026 wurden 672 Notifications mit insgesamt 2.016 Werten in etwa 100,6 Sekunden beobachtet. Das entspricht einer effektiven Werterate von ungefähr 20 Hz. Die Entfernung in Metern reagierte plausibel und kontinuierlich auf Bewegungen zur Wand und zurück. Das ist ein qualitativer Befund, keine unabhängige Kalibrierung oder Bestimmung der Messunsicherheit.

Zu Beginn traten negative Werte und Werte um 8,191 m auf. Ihre Bedeutung ist ungeklärt. Sie sind keine nachgewiesenen Fehlercodes und werden in diesem Test weder entfernt noch umgerechnet, interpoliert oder durch null ersetzt. Auch das erste passende Paket wird erhalten; der Startfilter der v0.9.6-Umweltmessgrößen wird hier nicht verwendet.

## BLE-Konfiguration

| Funktion | Konfiguration |
| --- | --- |
| Gerätenamensfilter | `PL Voyager 2` (auch in `PL Voyager 2-01` und `PL Voyager 2-02` enthalten) |
| Schreib-Characteristic | `152fdea5-28a1-11ed-a261-0242ac120002` |
| Notification-Characteristic | `152fdea6-28a1-11ed-a261-0242ac120002` |
| Verbindung | BLE-Notifications, MTU-Anforderung 247, `autoConnect=false`, gemeinsame Verbindungs-ID `voyager2` wie in v0.9.6 |
| Initialisierung | `23`, `60 01`, `78 03`, `7C 00`, `70 96 00 03 00`, anschließend `6E 00 00 00 00` (zunächst alle Messgrößen aus) |
| START über Schaltfläche | `6E 00 00 00 01` |
| Sensormaskenbytes | `00 00 00 01` |
| STOPP über Schaltfläche | `6E 00 00 00 00` |
| Erwarteter Header | sechs Bytes `99 00 00 00 01 00` |
| Messwerte | ab Byteoffset 6, drei `float32LittleEndian`-Werte, Wiederholungsschritt 4 Bytes, Einheit m |

Die START- und STOPP-Schaltflächen lösen wie in v0.9.6 getriggerte Ausgaben von fünf UInt8-Bytes aus. Die Initialisierung startet den IR-Datenstrom nicht automatisch. Geprüft werden alle sechs Headerbytes und die Anzahl von genau drei dekodierten Float32-Wörtern. Nicht passende Pakete werden verworfen; die Zahlenwerte passender Pakete werden nicht plausibilitätsgefiltert.

Die Handles `0x0014` (Schreiben) und `0x0016` (Notification) sind Zuordnungen im konkreten Mitschnitt, keine BLE-UUIDs. Die Testkonfiguration verwendet ausschließlich die oben genannten bewährten Characteristic-UUIDs, keine fest codierten Handles.

## Bedienung und CSV

1. Voyager 2 einschalten, andere Sensor-Apps trennen und dieses Testexperiment in phyphox öffnen.
2. Den richtigen Voyager 2 über Bluetooth verbinden.
3. **▶ oben rechts starten.**
4. **Danach „Messdaten STARTEN“ antippen (empfohlen).** Diesen Ablauf auch beim Wiederaufnehmen nach einer Pause verwenden.
5. Entfernungskurve in m beobachten; Anfangswerte nicht verwerfen.
6. Zum Beenden zuerst **„Messdaten STOPPEN“**, anschließend phyphox pausieren.
7. **⋮ → Daten exportieren → CSV → speichern/teilen.** Der Export enthält genau zwei Spalten: geschätzte Zeit in s und IR-Entfernung in m.

## Zeitbasis und Grenzen

Die Zeitrekonstruktion übernimmt das Verfahren von v0.9.6: Der erste der drei Werte erhält näherungsweise die BLE-Empfangszeit minus 0,10 s; die beiden weiteren folgen mit jeweils 0,05 s Abstand. Der erste Zeitpunkt wird bei Bedarf auf den letzten akzeptierten Zeitpunkt plus 0,05 s angehoben. Die Zeitachse ist damit geschätzt und monotonisiert; sie enthält keine Hardware-Zeitstempel. Die angenommene Datenrate ist kein Nachweis exakt konstanter Abtastung. Messwerte werden nicht interpoliert und Verbindungsunterbrechungen nicht mit erfundenen Messwerten aufgefüllt.

Zeit- und Entfernungspuffer enthalten jeweils höchstens 12.000 Werte, bei etwa 20 Hz ungefähr zehn Minuten. Rechtzeitig exportieren. Paketverarbeitung, STOPP-Verhalten, Wiederverbindung, Textdarstellung und tatsächlicher Export müssen noch in phyphox auf Android geprüft werden. Die lokale XML- und Logikprüfung ersetzt diesen Test nicht. Messbereich, Bedeutung der auffälligen Anfangswerte, Messunsicherheit und Langzeitstabilität sind nicht geklärt.

## Noch notwendiger Android-Funktionstest

- Datei importieren; ausschließlich IR-Test, Start-/Stopptasten, Hinweise, Entfernungseinheit m und Diagramm kontrollieren.
- Mit ▶ und anschließend START beginnen. Prüfen, ob Daten erst nach START eintreffen und pro passender Notification drei Werte verarbeitet werden; Statusanzeige und CSV prüfen.
- Mehrfach zur Wand und zurück bewegen und Anfangswerte einschließlich negativer Werte bzw. etwa 8,191 m unverändert dokumentieren. Keine feste Fehlercode-Deutung voraussetzen.
- STOPP, Pause, erneutes ▶/START und eine Wiederverbindung prüfen. Bereits gespeicherte Werte dürfen beim STOPP nicht ersetzt werden; gegebenenfalls nachlaufende Pakete als Befund dokumentieren.
- CSV exportieren: gleiche Anzahl Zeit-/Entfernungswerte, Einheit m, erhaltene Anfangswerte und plausible geschätzte Zeitabstände prüfen. NaN ist „Not a Number“, nicht null und nicht automatisch ein Sensordefekt.

Erst nach bestätigtem Android-Funktionstest wird über eine Integration in die gemeinsame Sensorauswahl entschieden. Private HCI-Dateien und Messdaten gehören nicht in dieses Repository.


## Ergänzung vom 21.11.2026: Startreihenfolge und Freigabetests

Der bisherige v0.9.7-Kandidat bestand beide Direktimporte (DE und DE/EN), Messung mit START/STOPP, Wiederverbindung und CSV, den Import aller zwölf Offline-QR-Segmente und einen Funktionstest des darüber importierten Experiments. STARTEN vor ▶ funktionierte beim erstmaligen Messstart, nach dem Pausieren und Wiederaufnehmen jedoch nicht zuverlässig. Die Ursache ist nicht abschließend geklärt. Deshalb empfehlen wir immer ▶ → „Messdaten STARTEN“. Empfohlen bleibt Bluetooth verbinden → Sensoren auswählen → ▶ → Messdaten STARTEN; diese Bedienempfehlung gilt auch beim Wiederaufnehmen nach einer Pause. Ungetestete weitere Alternativabläufe werden daraus nicht abgeleitet. Sensorwechsel und Beenden bleiben wie beschrieben empfohlen. Archivierte Testdateien behalten aus Nachvollziehbarkeitsgründen ihre historischen Texte; die damalige Behauptung, STARTEN benötige eine bereits laufende phyphox-Aufzeichnung, ist überholt. Die aktualisierten v0.9.7-Dateien und neu erzeugten Offline-Codes benötigen einen erneuten Importtest. Online-QR und Live-Prüfung folgen nach Veröffentlichung.
