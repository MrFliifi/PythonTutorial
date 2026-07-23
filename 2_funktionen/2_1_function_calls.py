# 2.1: Wie man Funktionen aufruft

# Im vorherigen Kapitel haben wir gelernt, wie man Funktionen definiert. Jetzt wollen wir die Funktionen 
# auch verwenden. Das Aufrufen einer Funktion ist einfach. Dafür schreibt man den Namen der Funktion, gefolgt 
# von Klammern. In den Klammern können die Argumente übergeben werden, die den Parametern der Funktion 
# entsprechen. Das haben wir auch schon einige Male gemacht, als wir die print-Funktion verwendet haben.

print("Hallo, Welt!")  # Hier rufen wir die print-Funktion auf und übergeben ihr den String "Hallo, Welt!" als 
#Argument.
# print() ist eine eingebaute Funktion in Python, die einen oder mehrere Werte als Argumente nimmt und sie 
# auf der Konsole ausgibt. In diesem Fall übergeben wir ihr den String "Hallo, Welt!" als Argument, und die 
# Funktion gibt diesen String auf der Konsole aus.

# Wir können aber auch unsere eigenen Funktionen aufrufen, die wir definiert haben.
# Das ist die Funktion aus dem vorherigen Kapitel
def addition(a, b):  
    c = a + b        
    print("Das Ergebnis ist: ", c)
    

# Die Namen der Parameter ist nicht relevant für den Aufruf der Funktion. Es ist egal, ob die Parameter 
# in der Signatur der Funktion "addition(a, b)" oder "addition(x, y)" heißen. Wichtig sind aber die 
# Anzahl und die Reihenfolge der Parameter, die übergeben werden. 

addition(5, 3) # Hier wird der Wert 5 dem Parameter "a" und der Wert 3 dem Parameter "b" zugewiesen. 
addition(10, 20) # Hier wird der Wert 10 dem Parameter "a" und der Wert 20 dem Parameter "b" zugewiesen.

# Man kann der Funktion auch Variablen übergeben.
y, z = 7, 2
addition(y, z) # Hier wird der Wert 7 dem Parameter "a" und der Wert 2 dem Parameter "b" zugewiesen.
addition(z, y) # Hier wird der Wert 2 dem Parameter "a" und der Wert 7 dem Parameter "b" zugewiesen.

# Wir brauchen bei dem Aufruf der Funktion nicht das Keyword "def" zu verwenden, da wir die Funktion 
# ja schon definiert haben. Das Keyword "def" wird nur verwendet, um eine Funktion zu definieren, nicht 
# um sie aufzurufen.

# TODO:
# 1. Kopiere alle Funktionen, die du im vorherigen Kapitel definiert hast. 
# Definiere Variablen mit den entsprechenden Werten und übergebe ihnen die entsprechenden Argumente, 
# damit sie korrekt ausgeführt werden können. Dann rufe sie auf.