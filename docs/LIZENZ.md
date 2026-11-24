# Lizenz, Urheberhinweise und Beiträge Dritter

## Geltungsbereich

Die eigenen Beiträge von Alexander Vidoni werden mit diesem Lizenzstand unter der [PolyForm Noncommercial License 1.0.0](../LICENSE) angeboten. Dazu gehören die selbst entwickelten XML-Experimentdefinitionen, das eigene Releaseprüfskript, die eigene Dokumentation einschließlich Website sowie selbst erzeugte QR-Darstellungen, soweit daran eigene Schutzrechte bestehen. [NOTICE](../NOTICE) enthält den verpflichtend weiterzugebenden Urheberhinweis.

Dies ist **öffentlich verfügbarer Quellcode unter einer nichtkommerziellen Lizenz**, keine OSI-konforme Open-Source-Software. Maßgeblich ist der vollständige, unveränderte [offizielle Lizenztext](https://polyformproject.org/licenses/noncommercial/1.0.0); diese Erläuterung fügt ihm keine Bedingungen hinzu.

Die Lizenz erstreckt sich nur auf Rechte, die der jeweilige Lizenzgeber tatsächlich besitzt. Sie lizenziert weder die phyphox-App noch PocketLab-Software, Firmware, Produktnamen oder fremde Materialien um. Bestehende Tags, Releases, Downloads und Quellstandsarchive bleiben unverändert; diese nachträgliche Lizenzvorbereitung verändert weder deren Inhalt noch die dort enthaltenen Lizenzangaben.

## Nutzung, Bildung und Forschung

Nichtkommerzielle Verwendung, Veränderung und Weitergabe sind für die in der Lizenz erlaubten Zwecke gestattet. Die Abschnitte „Noncommercial Purposes“, „Personal Uses“ und „Noncommercial Organizations“ beschreiben den Umfang.

Schulen und Universitäten als Bildungsinstitutionen sowie öffentliche Forschungsorganisationen dürfen das Projekt nach „Noncommercial Organizations“ unabhängig von ihrer Finanzierung und daraus folgenden Verpflichtungen nutzen. Das schließt die Nutzung durch solche Bildungsinstitutionen im Rahmen kostenpflichtiger Lehre ein. Andere Forschungseinrichtungen können sich insbesondere auf einen nichtkommerziellen Verwendungszweck stützen. Die bloße Bezeichnung eines Unternehmens als Forschungs- oder Bildungsanbieter erlaubt jedoch nicht automatisch jede kommerzielle Tätigkeit; kommerzielle Forschung privater Unternehmen wird nicht pauschal freigegeben.

Bei der Weitergabe auch nur eines Teils müssen Empfänger den Lizenztext oder dessen URL sowie die vom Lizenzgeber bereitgestellten Klartextzeilen mit dem Präfix `Required Notice:` erhalten. Damit ist insbesondere der Copyright-Hinweis aus [NOTICE](../NOTICE) weiterzugeben und zu erhalten. Dies folgt aus „Notices“ im unveränderten Lizenztext. Es besteht keine zusätzliche Pflicht zur öffentlichen Nennung bei jeder Nutzung und keine besondere Pflicht, ein bestimmtes UI-Element beizubehalten.

Für eine kommerzielle Nutzung außerhalb der bereits erlaubten Zwecke ist eine gesonderte Berechtigung der jeweiligen Rechteinhaber erforderlich. Alexander Vidoni behält die kommerziellen Verwertungsrechte an seinen eigenen Beiträgen und kann hierfür eine separate kommerzielle Lizenz anbieten. Eine solche Lizenz erfasst Beiträge Dritter nur, soweit dafür ebenfalls die notwendigen Rechte vorliegen. Die Lizenz enthält darüber hinaus unter anderem Patent-, Haftungs- und Verstoßregelungen; die Kurzbeschreibung ersetzt deren Lektüre nicht.

## Herkunft und Drittmaterialien

Die Projektgeschichte dokumentiert die Entwicklung der Voyager-2-Experimente aus eigenen BLE-Untersuchungen und Funktionstests. Die Prüfung des vorliegenden Bestands ergab keine konkreten Hinweise auf übernommene GPL-Beispiele, fremde Grafiken oder eingebettete externe Codebibliotheken. Die QR-Bilder transportieren die eigenen Experimentdaten beziehungsweise Downloadadressen; die Website bindet keine Herstellerlogos oder externen Skriptbibliotheken ein. Das öffentliche Prüfskript verwendet die Python-Standardbibliothek. Zur QR-Erzeugung oder Prüfung eingesetzte Werkzeuge werden nicht als Bibliothekscode mitgeliefert; ihre eigenen Lizenzen bleiben unberührt.

Die [offizielle phyphox-Beispielsammlung](https://github.com/phyphox/phyphox-experiments) steht unter GPL-3.0. Ihre Nutzung als kopierte oder abgeleitete Vorlage ist von der eigenständigen Verwendung des [dokumentierten XML-Dateiformats](https://phyphox.org/docs/file-format/) zu unterscheiden. Ein technischer Vergleich mit der geprüften Beispielsammlung ist kein lückenloser Nachweis aller denkbaren Ursprungsquellen. Fremde Bestandteile dürfen nur mit geklärter Herkunft, kompatiblen Rechten und den erforderlichen Hinweisen aufgenommen werden. GPL-pflichtige Übernahmen dürfen nicht einfach ausschließlich unter PolyForm gestellt werden.

Bei zukünftigen Beiträgen müssen Herkunft, Lizenz und Verfügungsbefugnis nachvollziehbar sein. Eine Einreichung allein überträgt keine Urheberrechte und begründet keine automatische Berechtigung zur separaten kommerziellen Lizenzierung durch Alexander Vidoni. Dafür sind, soweit erforderlich, gesonderte Rechte der Beitragenden einzuholen. Bestehende fremde Rechte bleiben bei jeder Weitergabe erhalten.

PocketLab, Voyager 2 und phyphox sind Namen der jeweiligen Rechteinhaber. Das Projekt ist unabhängig; es besteht keine offizielle Verbindung oder behauptete Zusammenarbeit mit PocketLab oder phyphox.

## Wissenschaftliche Zitierung

Eine Zitierung wird empfohlen, ist aber keine zusätzliche Lizenzbedingung. [CITATION.cff](../CITATION.cff) enthält Alexander Vidoni, den Projekttitel, die Repository-Adresse und die zuletzt veröffentlichte Version v0.9.7 vom 21.11.2026. Diese bibliografischen Angaben erklären den damaligen Releaseinhalt nicht rückwirkend zu einem geänderten Lizenzstand.

## Vorbereiteter Copyright-Hinweis für die nächste Experimentversion

Die veröffentlichten v0.9.7-Experimente bleiben unverändert. In einer gesondert versionierten Folgefassung soll am unteren Ende der vorhandenen Sensorauswahl lediglich ein zusätzliches `info`-Element erscheinen, ohne neuen Reiter und ohne Änderung der BLE-/Messlogik:

- Deutsch: `© 2026 Alexander Vidoni · Projekt/Lizenz: github.com/vidonialex/pocketlab-voyager2-phyphox`
- Englisch: `© 2026 Alexander Vidoni · Project/license: github.com/vidonialex/pocketlab-voyager2-phyphox`

Dazu sind künftig neue versionierte DE- und DE/EN-Dateien unter `docs/experiments/` anzulegen, ausgehend von `Voyager2_v097_DE.phyphox` und `Voyager2_v097_DE_EN.phyphox`. Der deutsche Text gehört in das zusätzliche sichtbare `info`-Element, der englische in die zugehörige Übersetzungszuordnung der zweisprachigen Datei. Dieser Anzeigehinweis ergänzt die Benutzeroberfläche; die verbindliche Weitergaberegel bleibt die aus LICENSE und NOTICE, ohne besondere UI-Erhaltungspflicht.

Durch jede XML-Änderung ändern sich die Experiment-SHA256-Werte. Für die neue Version müssen Offline-QR-Segmente, deren CRC32 und vollständige Rekonstruktion, das Offline-ZIP einschließlich seiner enthaltenen Dateien sowie alle zugehörigen SHA256-Werte neu erzeugt beziehungsweise geprüft werden. Die Segmentzahl ergibt sich aus den tatsächlichen neuen Daten; 13 Segmente werden nicht vorausgesetzt. Bei neuer versionierter Downloadadresse ist ein eigener Online-QR-Code zu erzeugen und sein Ziel zu prüfen. Manifest, Downloadlinks und Releasechecks sind gezielt auf die Folgeversion anzupassen; neue Quellstandsarchive erhalten eigene Prüfsummen und müssen LICENSE und NOTICE mitführen. Alte Pfade und Pakete werden nicht ersetzt.

Vor Freigabe der Folgeversion sind XML, beide Sprachen, unveränderte Messlogik und CSV-Struktur sowie Direkt- und QR-Import auf Android erneut zu prüfen. Diese Umsetzung und alle Regenerationen sind hier nur beschrieben, nicht durchgeführt.
