# 0.0.3: Booleans

# Beim programmieren mit den meisten Sprachen gibt es einen Datentyp,
# der nur zwei Werte annehmen kann: True (wahr) und False (falsch). 
# Dieser Datentyp nennt sich Boolean. 

# In Python schreiben wir die Werte True und False mit einem großen Anfangsbuchstaben.
# Booleans werden oft in Bedingungen verwendet, um Entscheidungen zu treffen (if) oder 
# Schleifen zu steuern (while).

# Booleans entweder sind:
True
False

# Es gibt aber auch Werte, die "truthy" oder "falsy" sind. 
# Das heißt, sie werden in einem booleschen Kontext als True oder False interpretiert.
# Das ist nicht in jeder Programmiersprache so. Java kennt diese Art von Werten nicht.

# Beispiele für truthy Werte:
1           # True
"Hallo"     # True
[1, 2, 3]   # True    

# Werte, die nicht ohne Wert sind, werde als truthy interpretiert. 
# Alle Werte, die nicht falsy sind, sind automatisch truthy.

# Beispiele für falsy Werte:
0           # False
""          # False
[]          # False
None        # False

# Werte, die leer sind, wie der leere String "", die leere Liste [] 
# oder der Wert None, werden als falsy interpretiert. Auch die Zahl 0 wird 
# als falsy betrachtet.
