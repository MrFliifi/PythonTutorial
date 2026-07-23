# 3.1: match-case

# If-Statements sind sehr nützlich, um Bedingungen zu überprüfen und den Code entsprechend 
# auszuführen. Sie sind aber nicht die einzige Möglichkeit, Bedingungen zu überprüfen. 
# Es gibt auch das match-case-Statement.

# Hierbei verwenden wir nur zwei keywords:
# - match x: + beliebig viele cases
# - case y: + body

# Der Aufbau vom match keyword ist ähnlich wie bei if-Statements. 
# Erst verwenden wir das match keyword, gefolgt von einer Variable, dessen Wert wir 
# überprüfen wollen. Abgeschlossen wird die Zeile mit einem :. Darauf folgt ein case-Block.
# Jeder case-Block beginnt mit dem case-keyword, gefolgt von dem value, auf den wir prüfen 
# wollen. Abgeschlossen wird die Zeile mit einem :. Jeder case-Block hat auch einen Codeblock.
# Der Codeblock des case-Blocks wird nur ausgeführt, wenn die value mit dem Wert der Variablen 
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
    # die vorherigen case-Blöcke abgedeckt sind. Es erfüllt die gleiche Funktion wie das 
    # else-Keyword bei if-Statements.  
    case _:  
        print("x ist etwas anderes")
        
        
# TODO:
# 1. Schreibe ein Programm, das mit 
# x = str(input("Trage deinen Lieblingswochentag ein: ")).lower() einen Wochentag von 
# der*dem Nutzer*in abruft. Schreibe dann einen match-case, der der*dem Nutzer*in sagt, ob 
# der gewählte Tag der 1., 2., 3., usw. Tag der Woche ist. 
        
