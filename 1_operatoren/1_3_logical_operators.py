# 1.3: Logical Operators

# Überspring dieses Kapitel zuerst. Komm wieder, wenn du das Kapitel über Kontrollflüsse 
# abgeschlossen hast.

# Logical operators bestehen aus drei keywords:
# - and
# - or
# - not

# Logical operators werden dann verwendet, wenn es darum geht conditions zu prüfen. Brauchen
# tun wir sie dann, wenn mehr als eine condition geprüft werden muss. Deshalb brauchen wir diese
# Art von Operator vor allem in den Kapiteln "Kontrollflüsse" und "Schleifen".

# Hier ein paar Beispiele dafür, wie man logical operators verwendet:
x = 55
y = 100

#    v True         v False
if y - x >= 5 and y - x <= 100:
    print("Mich siehst du nur, wenn beide conditions True sind.")
    
#    v False       v True
if y - x <= 5 or y - x <= 90:
    print("Mich siehst du sobald eine von beiden conditions True ist.")
    
#    v True
if not False:
    print("not invertiert den Wert der condition. not Ture ist gleich bedeutend mit False.")
    
# Man kann logical operators in beliebiger Menge und Reihenfolge kombinieren. 
# Beispiel:
a = 1
b = 2
c = 3

if a - b < 0 or c - b == 0 and a + c == 5 or not c * b == 5:
    print("TODO: Erkläre, warum ich ausgegeben werde!")
    
# Wie du sehen kannst, wird das ganz schnell ganz schön unübersichtlich. Deshalb ist es am besten
# die conditions so simpel wie möglich zu schreiben.