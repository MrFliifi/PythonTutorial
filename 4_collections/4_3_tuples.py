# 4.3: Tuples

# tuples sind container. Es ist also eine Variable, die 0 bis n Werte beinhalten kann.
# tuples sind ordered und immutable.
# tuples erkennt man an folgendem Syntax:

tuple_name = ("ein Wert", 2, True)
print("Unser tuple: ", tuple_name)
print()

# Zuerst definiert man einen Namen. Darauf folgt der assignment operator =. Das tuple wird
# dann mit ( geöffnet. Man kann dann beliebig viele Werte, mit beliebigen Datentypen 
# eintragen. Jeder Wert muss durch ein , getrennt sein. Abschließen tut man das tuple mit ).

# Anders als bei lists, kann ein tuple nicht mehr verändert werden. tuples sind also konstant.
# Muss man ein tuple aber dennoch verändern, kann man die Werte des tuples in eine list schreiben,
# die list verändern und ein neues tuple mit den Werten der list erstellen.
# Hier ein Beispiel dafür:

new_list = list(tuple_name)  # Wir typecasten mit der list() function
new_list.append("false")     # Wir fügen einen Wert mit der .append() function hinzu
tuple_name = tuple(new_list) # Wir typecasten mit der tuple() function
print("Hiermit haben wir den Wert von unserem Tuple überschrieben.")
print(tuple_name)

# Da tuples ordered sind, kann man die Werte des tuple mit dem Index abrufen.
print("Das sind die Werte des tuples: ")
print(tuple_name[0])
print(tuple_name[1])
print(tuple_name[2])

# Da man die Werte mit einem Index abrufen kann, sind duplikate Werte möglich.

# TODO:
# 1. Erstelle ein tuple mit mindestens 5 Werten. Füge dem tuple einen neuen Wert hinzu.
# 2. Entferne einen anderen Wert aus dem tuple. 
# Gib nach jedem Schritt das tuple mit print() aus.