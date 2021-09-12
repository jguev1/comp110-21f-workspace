"challenge question #1"

choice: int = int(input("enter number:"))

if choice < 50: 
    if choice < 25:
        print("A")
    else: 
        print("B")    
else:
    if choice > 75:
        print("C")
    else:
        print ("D")