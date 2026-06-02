# 2.2: return values

# Ein Grundprinizip von Funktionen ist, dass sie Input verarbeiten und Werte zurückgeben können. 
# Das bedeutet, dass eine Funktion nicht nur Anweisungen ausführen, sondern auch ein Ergebnis 
# liefern kann, das von anderen Teilen des Programms weiterverwendet werden kann. In Python wird 
# dies mit dem keyword "return" erreicht.

def addition(a, b):
    c = a + b
    return c  # Mit return wird der Wert von c zurückgegeben

# Wenn eine Funktion einen Wert zurückgibt, kann dieser Wert in einer Variable gespeichert oder direkt 
# in anderen Teilen des Programms verwendet werden.

# Beispiel: Wir können die Funktion "addition" aufrufen und das Ergebnis in einer Variable speichern:
ergebnis = addition(5, 3)
print("ergebnis:", ergebnis)  # Ausgabe: 8

# Oder wir können das Ergebnis direkt in einer anderen Funktion verwenden:
print("Das Ergebnis der Addition ist: ", addition(10, 20))  # Ausgabe: Das Ergebnis der Addition ist: 30

# Diese Funktion gibt keinen Wert zurück, sondern druckt das Ergebnis direkt aus
def multiplikation(a, b):
    c = a * b
    print("Das Ergebnis der Multiplikation ist: ", c)  
    
falsches_ergebnis = multiplikation(5, 3)  # Diese Zeile gibt None zurück, da die Funktion keinen Wert zurückgibt
print(falsches_ergebnis)  # Ausgabe: None


# TODO:
# 1. Definiere eine Funktion, die zwei Strings als Parameter nimmt und sie miteinander addiert (konkateniert). 
# Schreibe das Ergebnis in eine Variable und gebe es mit print() aus.
# 2. Definiere eine Funktion, die einen einen Float und einen Integer als Parameter nimmt und sie miteinander 
# multipliziert. Übergebe das Ergebnis an eine andere funktion, die das Ergebnis mit sich selbst potenziert und 
# mit print() ausgibt.