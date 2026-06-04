# 3.1: match-case

# If-Statements sind sehr nützlich, um Bedingungen zu überprüfen und den Code entsprechend 
# auszuführen. Sie sind aber nicht die einzige Möglichkeit, Bedingungen zu überprüfen. 
# Es gibt auch das match-case-Statement.

# Hierbei verwenden wir nur zwei keywords:
# - match x: + beliebig viele cases
# - case y: + body

# Der Aufbau vom match-keyword ist ähnlich wie bei if-Statements. 
# Erst verwenden wir das match-keyword, gefolgt von einer Variable, dessen Wert wir 
# überprüfen wollen. Abgeschlossen wird die Zeile mit einem :. Darauf folg ein case-Block.
# Jeder case-Block beginnt mit dem case-keyword, gefolgt von dem value, auf den wir prüfen 
# wollen. Abgeschlossen wird die Zeile mit einem :. Jeder case-block hat auch einen code-Block.
# Der Codeblock des case-Blocks wird nur ausgeführt, wenn die value mit dem Wert der Variable 
# übereinstimmt. 

# Der große Unterschied zu if-Statements ist, dass wir nicht mehrere Bedingungen überprüfen, 
# sondern nur den Wert einer Variable. Unsere condition ist also nur True, wenn der Wert der 
# Variable genau mit der condition übereinstimmt. 

# Hier ist ein Beispiel:

x = int(input("Gib eine Zahl ein: "))

match x:
    case 0:
        print("x ist null")
    case 1:
        print("x ist eins")
    case 2:
        print("x ist zwei")
    case 15:
        print("x ist 15")
    # Das _ ist ein Platzhalter für alle Werte, die nicht in den vorherigen case-Blöcken 
    # abgefangen wurden. Es ist sozusagen der "Fallback" für alle Fälle, die nicht durch 
    # die vorherigen case-Blöcke abgedeckt sind. Es erfüllt die selbe Funktion wie das 
    # else-Keyword bei if-Statements.  
    case _:  
        print("x ist etwas anderes")
        
        
# TODO:
# 1. Schreibe ein Programm, dass mit 
# x = str(input("Trage deinen Lieblingswochentag ein: ")).lower() eine Wochentag von 
# dem Nutzer abruft. Schreibe dann einen match-case, der dem Nutzer sagt, ob der Wochentag
# der 1., 2., 3., usw. Tag der Woche ist. 
        
