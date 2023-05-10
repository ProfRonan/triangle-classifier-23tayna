a= int(input("lado a= "))
b= int(input("lado b= "))
c= int(input("lado c= "))

if (a < b + c and b < a + c and c < b + c):
    if (a == b and b == c):
       print("nos lados formam um Triângulo Equilátero.")
    else:
        if (a == b or a == c or b == c):
            print("nos lados formam um Triângulo Isósceles.")
        else:
            print("ns lados formam um Triângulo Escaleno.")
else:
    print("nos lados não formam um triângulo!")