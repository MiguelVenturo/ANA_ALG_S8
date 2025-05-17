print("Que hay de nuevo")
def ite():
    x=1
    while x<=10:
        print(f"hola {x}")
        x+=1

def recursivo(x,n):
    if x==10:
       print(f"hola {x}") 
    else:
       print(f"hola {x}")
       recursivo(x+1,n)

recursivo(1,10)