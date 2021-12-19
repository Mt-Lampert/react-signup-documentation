---
title: "Berichte"
date: 2021-12-14T20:21:21+01:00
draft: false
weight: 100
---

Hier finden sich alle Berichte über dieses Projekt in "chronologisch absteigender" Reihenfolge. Das heißt: Die aktuellsten Berichte sind ganz oben, die älteren weiter unten.

## `useState()` braucht manchmal `useEffect()`
#### 2021-12-19

Beim Rumprobieren mit Ronas Version des Projektes kam es zu überraschenden Effekten: State-Variablen, die wir mit `setX()` upgedatet haben, hatten direkt nach dem Update immer noch ihren alten Wert:

```javascript
function changeHandler(event) {
   // alter Wert: "hi"
   // target.value hat "his"
   setFoo(event.target.value)

   // wird NICHT ausgefuehrt!
   // OBWOHL foo jetzt eigentlich 
   // den Wert "his" haben muesste!
   if (foo.length > 2) {
      changeButton()
   }
}
```

Das Problem ist, dass `setFoo()` *asynchron* ausgefuehrt wird. D.h. die If-Abfrage findet statt, während sich `setFoo()` in der "Warteschleife" befindet *und das State-Update noch aussteht!* Deshalb "passiert nix".

Die Lösung heißt `useEffect()`. Dieser Hook wird von React bekanntlich immer direkt nach einem Re-Rendering ausgeführt, und *genau dort* muessen wir die if-Abfrage platzieren:

```js
function MyComponent(props) {
   const [foo, setFoo] = useState('');
   
   // Siehe Erklaerung unten!
   useEffect(() => {
     if (foo.length > 2) {
       changeButton()
     } 
   }[foo]);

   function changeHandler(event) {
      setFoo(event.target.value)
   }

  // ...
}
```

Jetzt wird die If-Abfrage *DIREKT* nach dem Re-Rendering ausgeführt, aber nur dann, wenn `foo` mit Hilfe von `setFoo()` einen neuen Wert bekommen hat. Das ist genau das, was wir wollen!


## Doku-Seite automatisieren
#### 2021-12-16 06:50:

Ich habe mit Hilfe von Python `invoke` den Prozess automatisiert, neue Doku mit Hugo zu generieren und dann im Hauptprojekt hochzuladen. Das `shutils` package war dabei ausgesprochen nützlich und hilfreich.

##  Einrichten der Doku-Seite
#### 2021-12-15 07:51:

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

## Erste Erfolgsmeldung

#### 2021-12-14 -- 20:23

Es ist mir, glaube ich gelungen, Hauptprojekt und Doku-Projekt erfolgreich zusammen zu bringen. Macht mich sehr stolz und glücklich!