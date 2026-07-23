# 5.1: For Loops

# For loops sind eine Möglichkeit über jeden Wert eines containers zu iterieren.
# For loops kann man nur auf container anwenden. Man braucht also einen container wie
# lists, tuples, sets oder dictionaries, um einen for loop anwenden zu können.

# For loops verwenden zwei keywords:
# - for x in collection: + body
# - in (Siehe Kapitel 1.4: membership operatoren)

# Man liest das als "Für jeden Wert in der collection mache xy".
# Hier ein Beispiel:

fruits = ["apple", "banana", "pineapple"]

# fruit ist eine Variable, der für diesen loop der Wert eines items in der collection 
# zugewiesen wird. fruits ist der name des Containers, über den wir iterieren.
print()
print("Die Werte, die in fruits enthalten sind: ")
for fruit in fruits:
    print(fruit) 
    
# Man kann den Wert von fruit natürlich auch modifizieren.
print()
print("Die modifizierten Werte von fruits: ")
for fruit in fruits:
    fruit += "abc"   # Hiermit wird an jeden Wert in fruits der string "abc" angehangen.
    print(fruit)
    
# Mit der range function kann man auch von vorneherein festlegen, wie oft der for loop
# durchlaufen soll. Das ist nützlich, wenn man bestimmen möchte, wie oft ein loop läuft.

print()
print("For loop mit range 9:  ")
for i in range(9):
  print(i)
  
  
# TODO: 
# 1. Erstelle eine Liste und fülle sie mit beliebig vielen Werten. Iteriere über jeden 
# Wert der Liste und modifiziere ihn. Gib ihn mit print() aus.
# 2. Erstelle eine Liste und fülle sie mit beliebig vielen Werten, aber mindestens 3. 
# Iteriere über die ersten zwei Werte und lösche sie aus der Liste mit der .remove()
# function. Gib den Rest der Liste mit print() aus. 