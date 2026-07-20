# 6.0: Import

# Python bietet dir die Möglichkeit Code, den andere schon geschriben haben in dein eigenes Projekt zu 
# importieren und zu verwenden. Diesen Code nennt man auch eine "library". libraries sind generell sehr 
# nützlich, da man sich damit spart Probleme zu lösen, die sich gelöst wurden. Um libraries zu verwenden,
# nutzen wir folgende keywords:

# - import  -> immer nötig
# - as      -> optional. Wird genutzt, um aliases zu machen

# Sagen wir, ich will eine Zahl quadrieren. Die math library bietet dafür die .exp2() function. Diese rufe ich wie folgt auf:
x = math.exp2(3.14)
print("3,14 im quadrat ist:", x)

# Dir wird aufgefallen sein, dass das nicht funktiniert hat. Damit wir eine library benutzen können, muss über der Zeile Code,
# die die library verwenden will, die library erst importiert worden sein. Das liegt daran, dass Code immer von oben nach unten
# gelesen wird. Kommentiere die Zeilen 12 und 13 aus und Probiere es ereneut. Hat das geklappt?

# Will ich beispielsweise die Math library verwenden, brauche ich folgenden Syntax:
import math

# Im Anschluss kann ich die math library verwenden, indem ich ihnen Namen mit angebe und die entsprechende function auswähle:
print("PI im Quadrat:")
x = math.exp2(3.14)     # math ist der Name der library und .exp2() ist die funktion aus der math library
print(x)
print()

# Man kann die library aber auch mit einem alias innerhalb von dem Script umbenennen. Hier ein Beispiel:
import time as ticktock

# Dadurch, dass wir time das alias ticktock gegeben haben, können wir die "time" library unter dem neuen Namen aufrufen.
print("Aktuelle Zeit und Datum:")
y = ticktock.asctime()  # gibt die aktuelle Zeit aus
print(y)
print()


# TODO:
# 1. Importiere die random library und lasse dir einen zufälligen Integer mit print() ausgeben.
# 2. Importiere die math library und gib ihr einen alias.
