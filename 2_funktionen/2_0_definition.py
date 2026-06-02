# 2.0: Definition von Funktionen in Python

# Funktionen sind benannte Blöcke von Code, die eine bestimmte Aufgabe erfüllen. Genau wie Variablen auch,
# haben Funktionen einen Namen, der ihnen zugewiesen wird. Für den Namen der Funktion gelten die gleichen 
# Regeln wie für Variablennamen. Der Name muss mit einem Buchstaben oder einem Unterstrich beginnen und kann 
# Buchstaben, Zahlen und Unterstriche enthalten. Es dürfen keine keywords verwendet werden, wie z.B. "if", 
# "else", "for", "while", etc.

# In Python werden Funktionen mit dem Schlüsselwort "def" definiert, gefolgt von dem Namen der Funktion und
# einer Klammer, die die Parameter der Funktion enthält. Diese drei Teile nennt man die Signatur der Funktion.
# Nach der Signatur folgt ein Doppelpunkt und der Codeblock, der die Anweisungen enthält, die ausgeführt werden, 
# wenn die Funktion aufgerufen wird.

# Parameter sind Variablen, die in der Signatur der Funktion definiert werden. Sie dienen als Platzhalter für 
# die Werte, die, von außen, an die Funktion übergeben werden, wenn sie aufgerufen wird. In unserem Beispiel 
# sind "a" und "b" die Parameter der Funktion "addition". Sie können beliebige, legale, Namen haben. Einer Funktion
# können zwischen 0 und beliebig viele Parameter übergeben werden. 

# Außerdem haben Funktionen einen Body. Der Body ist der Codeblock, der die Anweisungen enthält, die ausgeführt 
# werden, wenn die Funktion aufgerufen wird. In unserem Beispiel werden in dem Body der Funktion die Parameter 
# "a" und "b" addiert und das Ergebnis wird in der Variable "c" gespeichert. Anschließend wird das Ergebnis mit 
# der print-Funktion ausgegeben.

# Hier ist ein einfaches Beispiel für eine Funktion, die zwei Zahlen addiert und das Ergebnis ausgibt:

def addition(a, b):  # Diese Zeile ist die Signatur der Funktion
    c = a + b        # Ab hier beginnt der Body der Funktion
    print("Das Ergebnis ist: ", c)
    
# In Python werden Bodies von Funktionen durch Einrückung definiert. Alle Zeilen, die zum Body der Funktion 
# gehören, müssen gleichmäßig eingerückt sein. Alle Zeilen, die nicht korrekt eingerückt sind, werden nicht 
# als Teil des Body der Funktion betrachtet und werden nicht mit dieser ausgeführt.

def hallo_welt():  # Diese Funktion hat keine Parameter
    print("Ich bin Teil der Funktion")  # Diese Zeile gehört zum Body der Funktion
print("Ich bin kein Teil der Funktion")  # Diese Zeile gehört nicht zum Body der Funktion
    
# TODO:
# 1. Definiere eine Funktion, die zwei Strings als Parameter nimmt und sie miteinander addiert (konkateniert) 
# und das Ergebnis mit print() ausgibt.
# 2. Definiere eine Funktion, die einen einen Float und einen Integer als Parameter nimmt und sie miteinander 
# multipliziert und das Ergebnis mit print() ausgibt.
# 3. Definiere eine Funktion, die keinen Parameter nimmt und einfach "Hallo, Welt!" mit print() ausgibt.
# 4. Definiere eine Funktion, die drei Parameter nimmt. Der erste Parameter soll mit dem zweiten addiert werden. 
# Das Ergebnis soll in eine Variable gespeichert und mit dem Dritten multipliziert werden. Das Endergebnis soll 
# mit print() ausgegeben werden.