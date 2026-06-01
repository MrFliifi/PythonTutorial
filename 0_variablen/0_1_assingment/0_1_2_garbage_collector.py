# 0.1.2: Garbage Collector in Python

# Der Garbage Collector ist ein Mechanismus in Python, der automatisch nicht mehr benötigte 
# Werte im Speicher freigibt. Er verwendet eine Technik namens "Reference Counting", um 
# zu verfolgen, wie viele Referenzen auf einen Wert existieren. Wenn die Anzahl der Referenzen 
# auf einen Wert auf null sinkt, wird der Wert automatisch gelöscht und der Speicher freigegeben.

# Variablen sind Referenzen auf Werte im Speicher. Der Wert liegt also im Speicher (RAM) und 
# die Variable ist eine Möglichkeit auf diesen Wert zuzugreifen. Wenn eine Variable auf einen 
# Wert zeigt, erhöht sich die Anzahl der Referenzen auf diesen Wert um eins. 
# Wenn eine Variable auf einen anderen Wert zeigt oder gelöscht wird, verringert sich die Anzahl
# der Referenzen auf den ursprünglichen Wert um eins. Das bedeutet auch, dass mehr als eine 
# Variable auf denselben Wert zeigen kann. Im Umkehrschluss bedeutet das aber auch, dass auch keine
# Variable auf einen Wert zeigen kann. In diesem Fall wird der Wert als "unreferenced" bezeichnet 
# und vom Garbage Collector gelöscht.

# Hier ist ein Beispiel, um das zu verdeutlichen:
a = 23  
# a zeigt auf den Wert 23. Die Referenzanzahl für 23 ist jetzt 1
b = 23  
# b zeigt jetzt auch auf den Wert 23. Die Referenzanzahl für 23 ist jetzt 2

a = 42          
# a zeigt jetzt auf den Wert 42. Die Referenzanzahl für 23 ist jetzt 1

b = "String"    
# b zeigt jetzt auf den Wert "String". 
# Die Referenzanzahl für 23 ist jetzt 0. 23 wird aus dem Speicher gelöscht.