=====================
Das Theme für Zope.de
=====================

Dies ist das Theme für die Website zope.de des DZUG e.V.

Startseite
==========

Nach der Installation des Themes ist der neue View “Frontpage” verfügbar, der im Wurzelverzeichnis von Plone über das Menü “Darstellung” aktiviert wird.

Dieser View bindet die Inhalte auf der Startseite automatisch ein. 

Banner
------

Der View “Frontpage” sucht im Ordner “frontpage-stuff” nach Bildern und Links und bindet sie oben rechts neben der Slideshow als Banner ein. Dafür muss die Frontpage über das ZMI mit dem Interface “IFrontPage” versehen werden. 

Die Bilder und Links im Ordner “frontpage-stuff” müssen folgende Kurznamen haben und veröffentlicht sein:

* image1 (Oberes Bild)
* image2 (Unteres Bild)

* image1-link (Link für das obere Bild)
* image2-link (Link für das untere Bild)

Die Links können dabei sowohl zu Zielen innerhalb der Website, als auch zu anderen Websites führen.

Teaser
------

Die Textblöcke unterhalb der Slideshow werden ebenfalls automatisch eingebunden. Die Inhalte dafür werden aus Links bezogen, die sich im Ordner “frontpage-stuff” befinden. Es werden die Felder “Titel”, “Beschreibung” und “Url” ausgewertet. Die Urls führen in der Regel zu Zielen innerhalb der Website. Die Links müssen folgende Kurznamen haben und veröffentlicht sein:

* teaser-1
* teaser-2

Es können weitere Links im Format “teaser-n” eingefügt werden, wenn dies redaktionell erforderlich wird.

Slideshow
---------

Die Slideshow wird mit collective.easyslider realisiert. Siehe dazu die Dokumentation von Easyslider.

Aktuelles
=========

Für die Übersichtsseite “Aktuelles” gibt es einen neuen View mit dem Namen “pageportlets”. Der View ermöglicht die Einbindung von Portlets im Content-Bereich. Die Portlets werden über “@@manage-page-portlets” eingebunden. 
