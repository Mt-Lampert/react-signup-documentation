---
title: "Berichte"
date: 2021-12-14T20:21:21+01:00
draft: false
weight: 100
---

Hier finden sich alle Berichte über dieses Projekt in "chronologisch absteigender" Reihenfolge. Das heißt: Die aktuellsten Berichte sind ganz oben, die älteren weiter unten.

## 2021-12-15 &nbsp; 07:51: Einrichten der Doku-Seite

Ja, es ist mir gestern abend tatsächlich gelungen, Hauptprojekt und Doku-Projekt erfolgreich zusammen zu bringen. Nun sollte ich berichten, wie ich das geschafft habe (nach viel Try And Error):

1. Die Sammelwebsite https://mt-lampert.github.io/ einrichten wie in der [offiziellen Dokumentation](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages) beschrieben. Das ist nötig, um der Dokumentation eine "Heimat" im Web zu geben.
2. Im Hauptprojekt den Ordner `docs` einrichten. Dort werden die statischen Webseiten der Dokumentation abgespeichert.
3. Im Hauptprojekt den Git-Branch `DOKU` anlegen. Der wird im weiteren Verlauf noch sehr wichtig werden.
4. Im Hauptprojekt Die Doku-Seite nach Anweisung der [offiziellen Dokumentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#choosing-a-publishing-source) anlegen.
   - benutzter Branch: `DOKU`(deshalb wurde er eingerichtet)
   - benutztes Verzeichnis: `docs` (deshalb wurde auch das eingerichtet)
  
5. Im Doku-Projekt die Dokumentation bis zur "ersten Veröffentlichungsreife" anlegen, committen und pushen.
6. Im Doku-Projekt folgende Änderung in `config.toml` vornehmen, committen und pushen:

    ```toml
    baseURL = 'https://mt-lampert.github.io/react-signup/'
    languageCode = 'de-de'
    title = 'React Signup Documentation'
    ```
    Damit werden beim Kompilieren alle internen Links auf die `baseURL` "geeicht" und kommen da an, wo man sie erwartet.
7. Die Dokumentation mit Hilfe von *Hugo* neu rendern:
   ```sh
   # alle moeglichen Altlasten vermeiden
   $ rm -rf public/*
   # rendern!
   $ hugo
   ```
8. Im Hauptprojekt in den Branch `DOKU` wechseln:
    ```sh
    $ git checkout -b DOKU
    ```
9. Im Hauptprojekt den Inhalt des `public`-Verzeichnisses aus dem Doku-Verzeichnis nach `/docs` kopieren:
   ```sh
   $ rm -rf docs/*
   $ cp -R -f ../react-signup-documentation/public/* docs/
   ```
10. committen und pushen.
11. Das Ergebnis im Browser überprüfen
12. Im Hauptprojekt den `DOKU`-Branch verlassen.

## 2021-12-14 -- 20:23

Es ist mir, glaube ich gelungen, Hauptprojekt und Doku-Projekt erfolgreich zusammen zu bringen. Macht mich sehr stolz und glücklich!