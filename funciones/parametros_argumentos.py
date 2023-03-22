

def suma(n1,n2,n3=None):
    if n3 is not None:
        print(n1+n2+n3)
    else:
        print(n1+n2)

suma(2,3)
suma(2,3,n3=5)