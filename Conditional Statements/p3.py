#ask phy and chem marks. print PASS if student is passed in both subjects
# else print fail

physics = int(input("Enter physics marks = "))
chemistry = int(input("Enter chemistry marks = "))

if physics >=33 and chemistry>=33:
    print("PASS")
else:
    print("FAIL")