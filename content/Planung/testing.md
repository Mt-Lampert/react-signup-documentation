---
title: "Testing"
date: 2021-12-21T07:09:54+01:00
draft: true
---

Die wichtigste Regel:

> Testen muss geplant sein!

Einfach drauf los und alles testen, was Beine hat -- so funktioniert es nicht! Was funktioniert, ist dort testen, wo wir uns unsicher fühlen: Neue Features, State-Updates, DOM-Updates usw.

Unit-Tests, wo wir nur einzelne Components testen, werden wir aller Wahrscheinlichkeit nach nicht brauchen. Was wir ganz sicher brauchen, sind Integrations-Tests. Dort pruefen wir, wie gut ein Parent-Component mit seinen Child-Components zusammenarbeitet und harmoniert: Ob props in den Child-Components richtig umgesetzt werden, ob Binding richtig funktioniert, ob State-Updates auch auf dem Bildschirm die gewünschten Resultate liefern.

Wie müssen wir uns einen Integrations-Test vorstellen? In der Regel läuft er nach folgendem Schema ab:

1. Das Parent-Component wird gerendert. Dabei wird ein virtuelles `window.document`, d.h. ein DOM im Speicher aufgebaut -- so wie im Browser; nur bleibt dieses `window.document` vollständig im Speicher und wird nicht im Browser angezeigt.
2. Mit Hilfe von `screen` werden Node-Elemente aus `window.document` ausgewählt.
3. Die ausgewählten Node-Elemente werden mit Hilfe von Events verändert. Dadurch ändert sich auch der Inhalt von `window.document`.
4. Jetzt werden erneut Node-Elemente aus `window.document` mit Hilfe von `screen` ausgewählt -- nämlich die, bei denen wir erwarten, dass die Events von gerade eben sie in eine bestimmte Richtung verändert haben (Neue Werte, neue Formatierung, vielleicht sogar Auftauchen oder Verschwinden)
5. Mit Hilfe von `expect()` überprüfen wir nun, ob sich die Änderungen tatsächlich wie erwünscht eingestellt haben oder nicht.

Grafisch sieht das etwa so aus:

{{< mermaid >}}
graph TD
A[render] -->|init| L{window.document}
L --> B(screen)
B -->|gets| D(el-1)
B -->|gets| E(el-2)
B -->|gets| F(el-3)
D -->|fireEvent| G{update document}
E -->|fireEvent| G
F -->|fireEvent| G
G -->H(screen)
H -->|gets Elements| I(expect)
I -->|checks elements| J{show Result}
{{< /mermaid >}}

## Vollständiges Beispiel

Das folgende Beispiel nimmt neue Einträge in einer To-Do-App vor und überprüft, ob sie wie erwartet in der To-Do-Liste angezeigt werden:

```jsx
// Datei: Todo.spec.js
import { render, screen, fireEvent } from "@testing-library/react";
import Todo from "../Todo";
import { BrowserRouter } from "react-router-dom";

// Wir brauchen dieses Component, weil in einem Child-Component von
// <Todo /> Routing stattfindet. Dem muessen wir Rechnung tragen.
const MockTodo = () => {
  return (
    <BrowserRouter>
      <Todo />
    </BrowserRouter>
  );
};

/**
 * @func  addTask Helfer-Funktion, mit der man neue Eintraege in die To-Do-Liste simulieren kann.
 * @arg   tasks   Array mit neuen Eintraegen fuer die ToDo-Liste
 */
const addTask = (tasks) => {
  // `screen` waehlt Elemente immer aus dem jetzt aktuellen window.document aus.
  // nach einem Rendering werden sich dort hoffentlich entsprechende Elemente finden.
  const inputElement = screen.getByPlaceholderText(/Add a new task here.../i);
  const buttonElement = screen.getByRole("button", { name: /Add/i });

  tasks.forEach((task) => {
    // Change-Event fuer inputElement ausloesen
    // und task in target.value eintragen
    fireEvent.change(inputElement, { target: { value: task } });
    // Click-Event fuer buttonElement ausloesen
    fireEvent.click(buttonElement);
  });
};

it("creates new todo list item after adding one in the add component", () => {
  // <MockTodo /> wird gerendert und window.document initialisiert
  render(<MockTodo />);
  // Neuer Eintrag in die Todo-Liste => update von window.document
  addTask(["Go Grocery Shopping"]);
  // Auswahl des Node-Elements, das sich durch addTask geaendert hat
  const divElement = screen.getByText(/Go Grocery Shopping/i);
  // Test: Ist es im DOM vorhanden oder nicht?
  expect(divElement).toBeInTheDocument();
});

it("adds multiple items of same kind if added in a likewise way", () => {
  // <MockTodo /> wird gerendert und window.document initialisiert
  render(<MockTodo />);
  // Drei identische neue Eintraege in die Todo-Liste => update von window.document
  addTask([
    "Go Grocery Shopping",
    "Go Grocery Shopping",
    "Go Grocery Shopping",
  ]);
  // Auswahl des Node-Elements, das sich durch addTask geaendert hat
  const divElements = screen.queryAllByText(/Go Grocery Shopping/i);
  // Test: Haben die drei identischen Eintraege tatsaechlich zu drei identischen
  // Eintraegen in der ToDo-Liste gefuehrt?
  expect(divElements.length).toBe(3);
});

it("creates a new todo list entry without 'todo-item-done' class", () => {
  // <MockTodo /> wird gerendert und window.document initialisiert
  render(<MockTodo />);
  // Neuer Eintrag in die Todo-Liste => update von window.document
  addTask(["Go Grocery Shopping"]);
  // Auswahl des Node-Elements, das sich durch addTask geaendert hat
  const divElement = screen.getByText(/Go Grocery Shopping/i);
  // Test: FEHLT divElement tatsaechlich die CSS-Klasse "todo-item-active"?
  expect(divElement).not.toHaveClass("todo-item-done");
});

it("adds the 'todo-item-done' class to a todo list item when clicked", () => {
  // <MockTodo /> wird gerendert und window.document initialisiert
  render(<MockTodo />);
  // Neuer Eintrag in die Todo-Liste => update von window.document
  addTask(["Go Grocery Shopping"]);
  // Auswahl des Node-Elements, das sich durch addTask geaendert hat
  const divElement = screen.getByText(/Go Grocery Shopping/i);
  // Click auf `divElement` simulieren
  fireEvent.click(divElement);
  // Test: wurde die CSS-Klasse "todo-item-active" 
  // fuer `divElement` tatsaechlich hinzugefuegt?
  expect(divElement).toHaveClass("todo-item-done");
});
```
