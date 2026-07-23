# 4.6: Length

# Container haben eine length. Die length des containers kann mit der len() function heraus- 
# gefunden werden. 

list_name = ["ein Wert", 2, True]
tuple_name = ("ein Wert", 2, True, "hallo Wert", 2.3333)
set_name = {"ein Wert", 2, True, False}
dict_name = {
  "brand": ["Ford", "Toyota"],
  "model": "Mustang",
  "year": 1964
}

print("Das ist die length von list_name: ", len(list_name))
print("Das ist die length von tuple_name: ", len(tuple_name))
print("Das ist die length von set_name: ", len(set_name))
print("Das ist die length von dict_name: ", len(dict_name))

# Die length eines containers kann man beispielsweise verwenden, um die Menge an loops in einem
# loop zu limitieren. Hier ein Beispiel dafür:

isRunning = True
i = 0
list_name = ["ein Wert", 2, True]
print()
print("Hier wird len() in einem loop demonstriert: ")

while isRunning:
    if i < len(list_name):
        print(list_name[i])
    else:
        isRunning = False
    i += 1
    
# Der loop wurde beendet, als wir die länge von list_name erreicht haben.