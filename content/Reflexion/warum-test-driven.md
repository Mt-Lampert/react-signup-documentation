---
title: "Warum Test-Driven Development?"
date: 2021-12-19T08:24:14+01:00
draft: false
---

Ganz einfach, weil man dadurch Zeit ***spart!*** Bei einem automatisierten Test kann man z.B. Formularfelder automatisch vom Test-Generator ausfüllen lassen, danach den Submit-Button automatisch klicken lassen und daraufhin das neu gerenderte Ergebnis testen. 

Beim nächsten Test kann man das Formular dann mit *anderen* Einträgen automatisch ausfüllen lassen, danach den Submit-Button wieder automatisch klicken lassen und daraufhin ein anderes neu gerendertes Ergebnis testen. Und deshalb will ich Zeit investieren, um diese Sorte Test zu lernen -- damit ich hinterher umso mehr Zeit einsparen kann.

### Was genau sollten wir testen?

Die goldene Regel besagt: Teste nur das, was du selber implementiert hast -- im Fall von React also nur die eigenen Funktionen, die eigenen Hooks, die eigenen Helfer und die eigenen Effekte. **NICHT** testen sollten wir das Rendering von unserem JSX. Dass das sicher und verlässlich gerendert wird, ist Aufgabe von React, also sind auch die Tests dafür dem React-Team zu überlassen. Genau dasselbe gilt für Starndard-Hooks wie `useState()` oder `useEffect()`. 

Unsere Aufgabe ist es aber, zu überprüfen, ob wir Reacts Standard-Werkzeuge richtig eingesetzt haben, und das heißt in der Regel, *ob wir sie richtig kombiniert haben!* Wenn wir mit Hilfe von Hooks z.B. ein Re-Rendering erzwungen haben, sollten wir prüfen, ob das Ergebnis auch tatsächlich unseren Erwartungen enspricht, auch dann, wenn wir wichtige Voraussetzungen ändern oder Spezialfälle checken müssen. 

Hier helfen uns automatisierte Tests immens weiter!