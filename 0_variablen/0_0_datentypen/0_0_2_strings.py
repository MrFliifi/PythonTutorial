# 0.0.2: Strings

# Strings sind eine Folge von Zeichen, die in Python durch Anführungszeichen 
# dargestellt werden. Strings können in einfachen (' '), doppelten (" ") 
# oder dreifachen (''' ''' oder """ """) Anführungszeichen geschrieben werden.
# Strings können Buchstaben, Zahlen, Leerzeichen und Sonderzeichen enthalten.

# Strings sind immutable, was bedeutet, dass sie nach ihrer Erstellung nicht 
# mehr geändert werden können. Wenn du einen String ändern möchtest, musst du einen 
# neuen String erstellen. Wie das geht, werden wir später sehen.

"Hallo, Welt!"
'Python ist toll!'
"""Dies ist ein mehrzeiliger String.
Er kann über mehrere Zeilen gehen."""

# Alle diese Werte sind gültige Strings in Python.

# Für später:

# Strings sind eine collection von Zeichen. Dadurch, dass Strings collections sind, 
# können wir mit dem Index auf einzelne Zeichen zugreifen. Das bedeutet, dass wir 
# zum Beispiel den ersten Buchstaben eines Strings mit dem Index 0 erreichen können: 

"H a l l o , _ W e l t  !"[0]  # Gibt 'H' zurück, da der Index bei 0 beginnt
# 0 1 2 3 4 5 6 7 8 9 10 11
"Hallo, Welt!"[7]  # Gibt 'W' zurück, da der Index bei 0 beginnt   

# Wichtig ist, dass die "" nicht gezählt werden. Der String beginnt also bei H 
# und nicht bei "".