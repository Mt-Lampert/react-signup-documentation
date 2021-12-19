---
title: "UseState braucht UseEffect"
date: 2021-12-19T08:18:59+01:00
draft: false
---

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

