# 3.0: if elif else

# Beim Programmieren ist es oft notwendig, Entscheidungen zu treffen. Dafür verwenden wir 
# unterschiedliche Kontrollflüsse. Einer davon ist das if keyword. Es ermöglicht es uns, 
# bestimmte Codeblöcke nur unter bestimmten conditions auszuführen. 

# Ein If-Statement is folgendermaßen aufgebaut:
# Zuerst kommt immer das if keyword. Danach folgt eine condition, die durch einen Doppelpunkt 
# abgeschlossen wird. Anschließend folgt ein eingerückter Codeblock, der nur ausgeführt wird, 
# wenn die condition True ist. Hier ist ein einfaches Beispiel:

condition = True # Die condition muss entwerder True, False, truthy oder falsy sein. 

if condition:
    print("Diese Zeile wird nur ausgeführt, wenn die condition True ist.")
    print("Es können beliebig viele Zeilen in diesem Block sein.")  

# Die condition ist oft komplexer als nur True oder False. Sie kann auch Vergleiche 
# enthalten. Hier ist ein weiteres Beispiel:

x = 5
if x >= 0:
    print("x ist positiv oder null")
    
# Da in der condition immer ein Comparison Operator verwendet wird, wird geprüft, ob das 
# Ergebnis des Vergleichs True oder False ist. In diesem Fall ist x größer oder gleich 0, 
# also ist die condition True und der Codeblock wird ausgeführt.

# In der Praxis müssen wir nur selten eine condition überprüfen. Müssen wir mehr als eine condition
# überprüfen, verwenden wir das elif keyword. elif benötigt immer ein if. Ein if kann aber auch 
# ohne elif auskommen. elif ermöglicht es uns weitere conditions zu überprüfen, wenn die 
# vorherige condition False war. Hier ist ein Beispiel:

# die input() Funktion kommt mit Python. Sie ermöglicht es uns, Benutzereingaben zu erhalten.
x = int(input("Gib eine Zahl ein: ")) 


# In diesem Beispiel überprüfen wir, ob die eingegebene Zahl positiv, negativ oder null ist. 
# Das ist mit einem if nicht getan. Deshalb verwenden wir elif, um die anderen conditions 
# zu überprüfen. Das Programm wird immer von Oben nach Unten ausgeführt. Deshalb gilt, 
# "Wenn die erste condition True ist, werden die anderen conditions nicht mehr überprüft". 
  
if x > 0:
    print("x ist positiv")  
elif x < 0:
    print("x ist negativ")
elif x == 0:
    print("x ist null")
    

# In Python gibt es noch ein keyword, dass verwendet wird, wenn alle Stricke reißen. 
# Es ist das else keyword. Es wird immer am Ende eines if-elif-Blocks verwendet. Es wird 
# nur dann ausgeführt, wenn alle vorherigen conditions False waren. Hier ist ein Beispiel:

x = int(input("Gib eine Zahl ein: "))

if x > 0:
    print("x ist positiv")
elif x < 0:
    print("x ist negativ") 
else:   
    print("x ist null")
    
# else benötigt keine condition, da es immer ausgeführt wird, wenn alle vorherigen conditions 
# False waren. Es ist sozusagen der "Fallback" für alle Fälle, die nicht durch die vorherigen 
# conditions abgedeckt sind. In diesem Fall ist es die Zahl 0, da sie weder positiv noch 
# negativ ist.

# elif und else sind optional. Es ist auch möglich, nur if-Statements zu verwenden. Man würde 
# dann viele if-Statements hintereinander schreiben, um alle conditions zu überprüfen. Das ist 
# aber nicht sehr elegant und führt oft zu Fehlern. Deshalb ist es besser, elif und else zu 
# verwenden, um den Code übersichtlicher und besser lesbar zu machen. Es gibt aber einen großen 
# Vorteil von if-Statements ohne elif und else: Sie können unabhängig voneinander sein. Das 
# bedeutet, dass alle conditions überprüft werden, auch wenn eine vorherige condition True war. 
# Hier ist ein Beispiel:

x = int(input("Gib eine Zahl ein: "))
if x > 0:                       # if-Statement bestehend aus den if-Keyword, der condition und einem :.
    print("x ist positiv")      # Der Codeblock des if-Statements.
if x < 0:
    print("x ist negativ")
if x == 0:
    print("x ist null")
    
# Schreiben wir unser if-Statement so, werden alle conditions überprüft, auch wenn die erste 
# condition True ist. 

# TODO:
# 1. Schreibe ein Programm, dass den Benutzer nach seinem Alter fragt und dann ausgibt, ob 
# er minderjährig, volljährig oder senior ist. (Minderjährig: < 18, Volljährig: >= 18 und < 65, Senior: >= 65)
# 2. Schreibe ein Programm, dass den Benutzer nach einer Zahl fragt und dann ausgibt, ob die Zahl positiv, 
# negativ oder null ist. 
# 3. Schreibe ein Programm, dass den Nutzer nach zwei Strings fragt und dann ausgibt, ob sie gleich sind.