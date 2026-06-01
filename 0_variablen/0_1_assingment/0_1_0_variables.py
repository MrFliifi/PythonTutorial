# 0.1.0: Benennung und Zuweisung von Variablen in Python

# Variablen sind Behälter für Daten. Sie können verschiedene Datentypen 
# speichern, wie z.B. Integer, Strings oder Booleans. Sie sind aber nicht auf
# die primitiven Datentypen beschränkt, sondern können auch komplexe Datenstrukturen
# wie verschiedene collections, custom Datentypen (Klassen) oder sogar Funktionen 
# speichern. 

# Variablen haben einen Namen. Dieser Name muss mit einem Buchstaben oder einem 
# Unterstrich beginnen und kann Buchstaben, Zahlen und Unterstriche enthalten. Es 
# dürfen keine keywords verwendet werden, wie z.B. "if", "else", "for", "while", etc.
# Verwendet man keywords, so wird ein SyntaxError ausgelöst. 

# Beim benennen von Variablen und Funktionen gibt es verschiedene Konventionen, wie 
# z.B. camelCase, snake_case oder PascalCase. In Python wird üblicherweise die
# snake_case Konvention verwendet. Das bedeutet, dass die Wörter klein geschrieben 
# sind und durch Unterstriche getrennt werden, z.B. "my_variable_name".

# Hier sind einige gültige Beispiele für Variablen in Python:
mein_integer = 42
mein_flo4t = 3.14
MEIN_STRING = "Hallo, Welt!"            # All Caps kennzeichet die Variable als constant
mein_string = "Tschüss, Welt!"  
ist_mein_boolean_toll = True            # Booleans benennt man üblicherweise mit einem "is" oder "has" 
meine_liste = [1, 2, 3, 4, 5]           # Hierzu mehr im Kapitel über collections
mein_dictionary = {"name": "Alice", "alter": 30}


# Die Namen der Variablen beachten die Groß- und Kleinschreibung. Das bedeutet, 
# dass "mein_string" und "MEIN_String" als zwei verschiedene Variablen betrachtet werden.
print("mein_string: ", mein_string)     # Ausgabe: "Tschüss, Welt!"
print("MEIN_STRING: ", MEIN_STRING)     # Ausgabe: "Hallo, Welt!"

# Hier sind einige ungültige Beispiele für Variablen in Python:
# 1variable = 10    | Ungültig, da der Name mit einer Zahl beginnt. 
# my-variable = 20  | Ungültig, da der Name ein Bindestrich enthält. Würde aber trotzdem compilen.
# if = 30           | Ungültig, da "if" ein keyword ist. -> SyntaxError
# var!@ble; = 10    | Ungültig, da der Name Sonderzeichen enthält. -> SyntaxError



# TODO: 
# 1. Definiere drei gultige, aber unterschiedliche Variablen 
# 2. Gib ihnen Werte mit unterschiedlichen Datentypen 
# 3. Gib die Werte der Variablen mit print(variablen_name) aus

