# Author: SMR (AMDG) 09/29/21
x=int(input("How many points did you earn?"))
if (x) >= 15:
    print("You received a gold medal!")
else:
    if (x)>12:
        print("You received a silver medal!")
    else:
        if x<9:
            print("You received zero medal.")
        else:
            print("You received a bronze medal!")
            



