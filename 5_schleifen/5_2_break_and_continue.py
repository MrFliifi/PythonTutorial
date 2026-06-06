# 5.2: Break and Continue

# break und continue sind keywords, die in loops eingesetzt werden können. break beendet
# einen loop ungeachtet ob die condition im Kopf des loops True ist, oder ungeachtet, ob
# es noch Werte in einem container gibt. 


# Hier ein Beispiel für break in while loops:
print("Hier breaken wir einen while loop: ")
x = 0
while True:
    print(x)
    if (x == 10):
        break
    else:
        x += 1
        
# Hier ein Beispiel für break in for loops:
fruits = ["apple", "banana", "pineapple"]

print()
print("Hier breaken wir einen for loop: ")
for fruit in fruits:
    if fruit == "banana":
        print("Banane wollen wir nicht!")
        break
    else:
        fruit += "abc"
    print(fruit)
    
    
# continue ist nicht so extrem wie break. contunie überspring nur die aktuelle iteration 
# des loops, beendet diesen aber nicht komplett. 

# Hier ein Beispiel für continue in while loops:
print()
print("Hier benutzen wir continue in einen while loop: ")
x = 0
while True:
    x += 1
    if x == 10: # Immer noch nötig, damit der loop nicht infite ist.
        break
    elif x == 5:
        print("Skip!")
        continue # Du wirst 5 nicht in der Konsole sehen, weil es übersprungen wurde
    
    print(x)
    
print()
print("Hier benutzen wir continue in einen for loop: ")
for x in range(10):
    if x == 5:
        print("Skip!")
        continue
    print(x)