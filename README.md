# PocketLab Voyager 2 – Integration in phyphox

**Entwicklungsstand:** v0.9.5 (experimenteller Prototyp)  
**Projektkontext:** Bachelorstudium Physik

## Zielsetzung

Dieses Projekt untersucht die Einbindung des **PocketLab Voyager 2** in die Android-App **phyphox**. Eine eigens entwickelte phyphox-Experimentdatei empfängt Messdaten über Bluetooth Low Energy (BLE), ermöglicht die dynamische Auswahl von Sensorgrößen und stellt die Daten in Zeitdiagrammen und als CSV-Export bereit.

Es handelt sich um eine unabhängige Implementierung, nicht um ein offizielles Angebot von PocketLab oder phyphox.

**Projektseite:** https://vidonialex.github.io/pocketlab-voyager2-phyphox/

## Installation

Benötigt werden ein PocketLab Voyager 2, ein Android-Smartphone mit Bluetooth und die installierte [phyphox-App](https://phyphox.org/).

| Verfahren | Sprache | Internet beim Import | Zugang |
| --- | --- | --- | --- |
| Direkter Dateidownload | Deutsch | Ja, zum Herunterladen | [Experimentdatei (.phyphox)](docs/experiments/Voyager2_v095_DE.phyphox) |
| Direkter Dateidownload | Deutsch / Englisch | Ja, zum Herunterladen | [Experimentdatei (.phyphox)](docs/experiments/Voyager2_v095_DE_EN.phyphox) |
| Ein Online-QR-Code | Deutsch / Englisch | Ja | [QR-Code](docs/qr/online.png) |
| Sieben Offline-QR-Codes | Deutsch | Nein, nach vorherigem Herunterladen | [QR-Paket (.zip)](docs/downloads/Voyager2_v095_Offline_QR_DE.zip) |

Bei der zweisprachigen Experimentdatei richtet sich die Sprache nach der Spracheinstellung der App beziehungsweise des Smartphones. Die deutsche Datei bleibt unabhängig davon deutsch.

**Direktdownload:** Die gewünschte `.phyphox`-Datei auf dem Smartphone speichern und mit phyphox öffnen beziehungsweise importieren.

**Online-QR:** Den QR-Scanner im phyphox-Hauptmenü öffnen und den einzelnen Code scannen. Eine Internetverbindung ist erforderlich, da der Code auf die bereitgestellte Experimentdatei verweist.

**Offline-QR:** Das ZIP-Paket vorab herunterladen und entpacken. Anschließend im phyphox-QR-Scanner alle sieben nummerierten Codes nacheinander scannen. Während des Imports ist keine Internetverbindung nötig.

## Messung durchführen

1. Voyager 2 einschalten und Bluetooth am Smartphone aktivieren. Eine gegebenenfalls bestehende Verbindung zur PocketLab-App beenden.
2. Das Experiment in phyphox öffnen und die Verbindung zum Voyager 2 herstellen.
3. Die phyphox-Aufzeichnung über **▶** starten.
4. Im Reiter **Sensorauswahl / Sensor Selection** die gewünschten Messgrößen aktivieren und **DATEN STARTEN / START DATA** antippen.
5. Die Zeitdiagramme unter **Bewegung / Motion** und **Umgebung / Weather** beobachten.
6. Für einen Wechsel der Messgrößen zunächst **DATEN STOPPEN / STOP DATA** auswählen, die Sensorauswahl ändern und den Datenstrom erneut starten.
7. Nach der Messung den Datenstrom stoppen, die phyphox-Aufzeichnung pausieren und über das Exportmenü die Daten als CSV speichern.

Die Reiter enthalten aufklappbare Hilfetexte. Der Reiter **Status** erläutert Verbindungsprobleme und mögliche Datenlücken.

## Verfügbare Messgrößen

| Messgröße | Anzeigeeinheit | Hinweis |
| --- | --- | --- |
| Beschleunigung (X, Y, Z) | m/s² | Drei Raumachsen |
| Winkelgeschwindigkeit (X, Y, Z) | rad/s | Drei Raumachsen |
| Magnetfeld (X, Y, Z) | µT | Drei Raumachsen |
| Interne Temperatur | °C | Temperatur des Sensors |
| Barometrischer Druck | hPa | Im CSV-Export in Pa |
| Relative Luftfeuchtigkeit | % | Dimensionslose relative Feuchte |
| Hitzeindex | °C | Vom Sensor übertragene Messgröße |
| Umgebungslichtintensität | lx | Beleuchtungsstärke |

Die acht Messarten lassen sich auch kombinieren. Die einzelnen Vektorkomponenten werden getrennt dargestellt und exportiert.

## Datenerfassung und Grenzen

- **Zeitbasis:** phyphox erhält BLE-Datenpakete. Die Zeitpunkte innerhalb eines Pakets werden aus dem Empfangszeitpunkt und einer angenommenen Abtastrate von etwa 20 Hz rekonstruiert. Die Zeitachse besteht **nicht** aus Hardware-Zeitstempeln des Voyager 2.
- **Datenlücken:** Bei unterbrochener Bluetooth-Verbindung und während eines gestoppten Datenstroms werden keine Werte nachträglich ergänzt. Nach einer Wiederverbindung muss der Datenstrom gegebenenfalls erneut gestartet werden.
- **Anfangswerte:** Das erste passende Umwelt-Datenpaket wird nach Messbeginn verworfen, um beobachtete extreme Startwerte zu reduzieren. Weitere Einschwingeffekte sind möglich.
- **Messgenauigkeit:** Im Projekt wurde bislang keine unabhängige Kalibrierung oder umfassende metrologische Validierung der Sensoren durchgeführt.
- **Noch nicht integriert:** IR-Distanzmessung, externe Temperatur- und Druckfühler sowie weitere abgeleitete Bewegungsgrößen.
- **Kompatibilität:** Die praktische Erprobung erfolgte mit einem Voyager 2 und einem Android-Smartphone. Eine systematische Prüfung unterschiedlicher Geräte und Betriebssysteme steht aus.

## Verifikation

Die Prüfung der veröffentlichten Dateien erfolgt mit Python (Standardbibliothek):

```bash
python scripts/check_release.py
```

Das Skript kontrolliert SHA-256-Prüfsummen der Experimentdateien und des Offline-Pakets, grundlegende XML- und ZIP-Eigenschaften sowie die wichtigsten Dateiverweise. Es ersetzt keinen Funktionstest auf einem Smartphone.

Die deutsche Offline-QR-Variante wurde auf Android praktisch erprobt. Für den neuen Online-QR-Zugang steht ein abschließender Smartphone-Importtest noch aus.

## Projektstatus

**Version v0.9.5 ist ein experimenteller Entwicklungsstand, keine fertig validierte Messsoftware.** Rückmeldungen zur Bedienbarkeit, zu weiteren Messgrößen und zur Messdatenqualität sind willkommen.

PocketLab, Voyager 2 und phyphox sind Produkt- beziehungsweise Projektnamen der jeweiligen Rechteinhaber. Eine offizielle Zusammenarbeit wird nicht beansprucht.
