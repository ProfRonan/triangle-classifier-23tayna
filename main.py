a= int(input("lado a="))
b= int(input("lado b="))
c= int(input("lado c="))

if (a+b> c and a+c> b and b+c > a):
    if (a==b and a==c):
        print("nos lados formam um triângulo Equilátero.")
    
    else: 
        if(a == b or a == c or b == c): 
            print("nos lados formam um triângulo Isósceles.")
        else:
            print("nos lados formam um triângulo Escaleno.")
            
else: 
    print("Não é um triângulo.")