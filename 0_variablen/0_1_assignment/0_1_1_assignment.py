# 0.1.1: Assignment

# Variablen kann man einen Wert zu ordnen. Das macht man mit den assignment operator "=". 
# Auf der linken Seite des "=" steht der Name der Variable und auf der rechten Seite der Wert.
# Anders herum würde es nicht funktionieren, da der Name der Variable auf der linken Seite 
# stehen muss.
# Zum Beispiel: 
mein_integer = 42
mein_flo4t = 3.14


# Es ist auch möglich, mehrere Variablen gleichzeitig zu definieren und ihnen Werte zuzuweisen.
mein_string, mein_boolean = "Hallo, Welt!", True

# Mit den Namen der Variablen kann man die Werte, die diesen zugeordnet sind, 
# abrufen und manipulieren. Zum Beispiel: 
print("mein_integer: ", mein_integer)   # Ausgabe: 42
mein_integer = mein_integer + 10        # mein_integer hat jetzt den Wert 52
print("mein_integer: ", mein_integer)   # Ausgabe: 52

# Wir haben also mit dem Namen der Variable "mein_integer" den Wert 42 abgerufen, 
# diesen um 10 erhöht und mit dem neuen Wert 52 überschrieben. Außerdem haben wir 
# den Wert der Variable abgerufen und mit print() ausgegeben.

# Variablen können auch durch Werte mit anderen Datentypen überschrieben werden.
print("mein_flo4t: ", mein_flo4t)       # Ausgabe: 3.14
mein_flo4t = "Hallo, Welt!"             # mein_flo4t hat jetzt den Wert "Hallo, Welt!"
print("mein_flo4t: ", mein_flo4t)       # Ausgabe: "Hallo, Welt!"

# Hier hat sich der Wert vom Typ Float zu einem String geändert. Das ist in Python möglich, 
# da Variablen dynamisch typisiert sind. Das bedeutet, dass der Datentyp einer Variable zur 
# Laufzeit geändert werden kann. Sind Variablen veränderbar, nennt man diese mutable. 
# Sind sie unveränderbar, nennt man sie immutable. 


# TODO: 
# 1. Definiere drei gültige, aber unterschiedliche Variablen 
# 2. Gib ihnen Werte mit unterschiedlichen Datentypen 
# 3. Gib die Werte der Variablen mit print(variablen_name) aus
# 4. Ändere die Werte der Variablen und gib sie erneut aus