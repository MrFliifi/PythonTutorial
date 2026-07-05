# 4.5: Dictionaries

# Ein Dictionary (kurz: dict) ist ein Container, in dem Informationen in Form von
# Schlüssel-Wert-Paaren gespeichert werden. Jeder Schlüssel (Key) ist einzigartig und
# verweist auf genau einen Wert (Value). Werte können dabei beliebige Datentypen sein,
# zum Beispiel Zahlen, Texte, Listen oder sogar weitere Dictionaries. Seit Python 3.7
# behalten Dictionaries die Reihenfolge, in der Einträge eingefügt wurden. Dictionaries
# sind veränderbar, das heißt: Sie können später Elemente hinzufügen, ändern oder löschen.

# Ein Dictionary wird mit geschweiften Klammern geschrieben. Zwischen Key und Value
# steht ein Doppelpunkt, und einzelne Paare werden durch Kommata getrennt. 

# Beispiel 1: Ein einfaches Dictionary namens `person`.
# In diesem Dictionary gibt es drei Schlüssel: `name`, `age` und `languages`.
# Der Schlüssel `name` zeigt auf einen Text (String), `age` zeigt auf eine Zahl
# und `languages` zeigt auf eine Liste mit zwei Einträgen. So kann man verschiedene
# Informationen zu einer Person unter einem Namen zusammenfassen.
person = {
    "name": "Anna",
    "age": 28,
    "languages": ["Deutsch", "Englisch"],
}

print("Beispiel-Dictionary (person):")
print(person)
print()

# Beispiel 2: Man kann zuerst ein leeres Dictionary erstellen und später Einträge
# hinzufügen. Das ist nützlich, wenn man die Daten erst zur Laufzeit kennt.
empty = {}
empty["new_key"] = 123
print("Leeres Dictionary nach dem Hinzufügen eines Eintrags:")
print(empty)
print()

# Zugriff auf Werte in einem Dictionary
# Um an den Wert zu einem bestimmten Schlüssel zu kommen, gibt es mehrere Möglichkeiten.
# Die erste Möglichkeit ist die eckige Klammer `dict[key]`. Diese Methode liefert den
# Wert zurück, wirft aber einen Fehler, wenn der Schlüssel nicht existiert.
print("Zugriff mit eckigen Klammern (person['name']):")
print(person["name"])  # Gibt den Wert für den Schlüssel 'name' aus

# Eine sichere Alternative ist die Methode `get()`. Sie liefert `None` zurück, wenn
# der Schlüssel nicht existiert, oder einen von Ihnen angegebenen Standardwert.
print("Zugriff mit get(), nicht vorhandener Key => None:")
print(person.get("nickname"))
print("Zugriff mit get() und Default-Wert:")
print(person.get("nickname", "kein Nickname"))
print()

# Werte hinzufügen oder aktualisieren
# Wenn Sie einem Dictionary einen neuen Schlüssel zuweisen, wird dieser angelegt.
# Existiert der Schlüssel bereits, wird sein Wert überschrieben.
person["age"] = 29  # Wir ändern den Wert für 'age'.
person["city"] = "Berlin"  # Wir fügen einen neuen Schlüssel 'city' hinzu.
print("Dictionary nach dem Hinzufügen/Ändern von Einträgen:")
print(person)
print()

# Einträge löschen
# Um einen Eintrag zu entfernen, kann man `del dict[key]` verwenden. Diese Variante
# wirft einen Fehler, wenn der Schlüssel nicht existiert. Deshalb sollte man sicher sein,
# dass der Schlüssel vorhanden ist.
del person["city"]
print("Dictionary nach dem Löschen des Schlüssels 'city' mit del:")
print(person)
print()

# Die Methode `pop()` entfernt einen Schlüssel und liefert den zugehörigen Wert
# zurück. Man kann einen Default-Wert angeben, falls der Schlüssel nicht existiert.
age = person.pop("age", None)
print("Mit pop entfernte 'age' und erhaltenen Wert:")
print(age)
print("Dictionary nach pop('age'):")
print(person)
print()

# `popitem()` entfernt das zuletzt eingefügte Schlüssel-Wert-Paar und gibt es als
# Tupel (key, value) zurück. Das ist nützlich, wenn man schrittweise Einträge
# entnehmen möchte.
last = person.popitem()
print("Mit popitem entnommenes Paar (key, value):")
print(last)
print("Dictionary nach popitem():")
print(person)
print()

# Über ein Dictionary iterieren
# Standardmäßig iteriert `for key in dict:` über die Schlüssel. Wenn Sie die Werte
# benötigen, verwenden Sie `dict.values()`. Wenn Sie beides brauchen, verwenden Sie
# `dict.items()`, das Tupel aus (key, value) liefert.
data = {"a": 1, "b": 2, "c": 3}
print("Iteration: Ausgabe der Schlüssel:")
for k in data:
    print(k)
print("Iteration: Ausgabe der Werte:")
for v in data.values():
    print(v)
print("Iteration: Ausgabe von Schlüssel und Wert zusammen:")
for k, v in data.items():
    print(k, v)
print()

# Verschachtelte Dictionaries und komplexe Werte
# Ein Dictionary kann als Wert ein weiteres Dictionary oder eine Liste enthalten.
# Damit lassen sich komplexe Strukturen wie ein Lagerbestand darstellen.
inventory = {
    "fruits": {"apple": 10, "banana": 5},
    "vegetables": ["carrot", "spinach"],
}
print("Beispiel für ein verschachteltes Dictionary (inventory):")
print(inventory)
print("Anzahl der Äpfel im inventory (inventory['fruits']['apple']):")
print(inventory["fruits"]["apple"])
print()

# Dictionary Comprehension
# Mit einer sogenannten Comprehension können Sie ein Dictionary kompakt aus einer
# Iteration erzeugen. Im folgenden Beispiel wird für jede Zahl n ihr Quadrat als
# Wert im Dictionary gespeichert.
squares = {n: n * n for n in range(6)}
print("Dictionary mit Quadraten von 0 bis 5:")
print(squares)
print()

# Nützliche Methoden (kurze Übersicht)
# Einige häufig verwendete Methoden sind: `keys()`, `values()`, `items()`, `get()`,
# `pop()`, `popitem()`, `clear()`, `update()` und `copy()`.

# Beispiel: `update()` fügt mehrere Schlüssel-Wert-Paare auf einmal hinzu oder
# aktualisiert vorhandene Schlüssel.
stats = {"wins": 5}
stats.update({"losses": 2, "draws": 1})
print("Beispiel für update() - Statistik-Dictionary:")
print(stats)
print()

# Beispiel: `copy()` erzeugt eine flache Kopie des Dictionaries. Das ist praktisch,
# wenn Sie die Originaldaten behalten möchten, aber die Kopie verändern wollen.
copy_stats = stats.copy()
print("Flache Kopie von stats:")
print(copy_stats)
print()

# Hinweise und Fallstricke
# Schlüssel eines Dictionaries müssen sogenannte hashbare Typen sein. Mutable Typen
# wie Listen können deshalb nicht als Schlüssel verwendet werden. Außerdem sollte man
# ein Dictionary nicht während einer Iteration verändern; das kann zu unerwartetem
# Verhalten oder Fehlern führen. Wenn Sie während des Iterierens löschen wollen,
# erzeugen Sie zuerst eine Liste der Schlüssel mit `list(d.keys())` und iterieren
# über diese Liste.

# --- Beispiele mit Ausgabe ---
people = {
  "alice": {"age": 30, "city": "München"},
  "bob": {"age": 25, "city": "Hamburg"},
}
for name, info in people.items():
  print(f"{name.title()} ist {info['age']} Jahre alt und lebt in {info['city']}")
print()

# TODO:
# 1) Erstelle ein dict "student" mit den Keys: "name", "matrikel", "fächer" (Liste) und trage beliebig viele Werte ein.
#    Gib den Namen und das erste Fach aus.
# 2) Schreibe eine Funktion, die ein dict mit Noten (z.B. {"Math": 1.3, "Bio": 2.0})
#    entgegennimmt und den Durchschnitt (Mittelwert) der Noten zurückgibt.
# 3) Gegeben ist ein Textstring. Erstelle ein dict, das die Häufigkeit jedes Buchstabens
#    im Text zählt (ignoriere Leerzeichen, verwende Kleinbuchstaben. Verwende dafür
#    die function lower()).
# 4) Verwende Dictionary Comprehension, um ein dict zu erstellen, das Zahlen von 1 bis 10
#    auf ihre Kubikwerte abbildet.
