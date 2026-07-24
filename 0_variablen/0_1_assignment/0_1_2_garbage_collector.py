# 0.1.2: Garbage Collector

# Der Garbage Collector ist ein Mechanismus in Python, der automatisch nicht mehr
# benötigte Werte im Speicher freigibt. Er verwendet eine Technik namens "reference counting", um 
# zu verfolgen, wie viele Referenzen auf einen Wert existieren. Wenn die Anzahl der Referenzen 
# auf den Wert null sinkt, wird der Wert automatisch gelöscht und der Speicher freigegeben.

# Variablen sind Referenzen auf Werte im Speicher. Der Wert liegt also im Speicher (RAM) und 
# die Variable ist eine Möglichkeit auf diesen Wert zuzugreifen. Die Werte der Variablen bleiben 
# solange erhalten, wie das Programm läuft. Das nennt sich Laufzeit. Endet das Programm, werden 
# alle Werte im Speicher gelöscht. Es ist also nicht möglich, dass Werte im Speicher bleiben, 
# nachdem das Programm beendet wurde. Möchte man Daten dauerhaft speichern, braucht man eine 
# Datenbank oder eine andere Datei, in der die Daten gespeichert werden können.

# Wenn eine Variable auf einen Wert zeigt, erhöht sich die Anzahl der Referenzen auf diesen Wert 
# um eins. Wenn eine Variable auf einen anderen Wert zeigt oder gelöscht wird, verringert sich die 
# Anzahl der Referenzen auf den ursprünglichen Wert um eins. Das bedeutet auch, dass mehr als eine 
# Variable auf denselben Wert zeigen kann. Im Umkehrschluss bedeutet das aber auch, dass auch keine
# Variable auf einen Wert zeigen kann. In diesem Fall wird der Wert als "unreferenced" bezeichnet 
# und vom Garbage Collector gelöscht.

# Hier ist ein Beispiel, um das zu verdeutlichen:
a = 23  
# a zeigt auf den Wert 23. Die Referenzanzahl für 23 ist jetzt 1.
b = 23  
# b zeigt jetzt auch auf den Wert 23. Die Referenzanzahl für 23 ist jetzt 2.

a = 42          
# a zeigt jetzt auf den Wert 42. Die Referenzanzahl für 23 ist jetzt 1.

b = "String"    
# b zeigt jetzt auf den Wert "String". 
# Die Referenzanzahl für 23 ist jetzt 0. 23 wird aus dem Speicher gelöscht.

# TODO:
# 1. Definiere eine Variable und weise ihr einen Wert zu.
# 2. Definiere eine weitere Variable und weise ihr denselben Wert zu.
# 3. Ändere den Wert aller Variablen so, dass keine Referenz mehr auf den ursprünglichen Wert zeigt.
