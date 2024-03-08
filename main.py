def f(x):
    return x**3-2*x**2-5
def bisection(a,b,n):
    i=1
    condition= True
    while condition:
        x=(a+b)/2
        if f(x)<0:
            a=x
        else:
            b=x
        print("iteration = ",i,"x= ",x,"f(x) =",f(x))
        if i==n:
                condition=False
        else:
                condition=True
                i=i+1
    print("gerekli kök:",x)
a=input("ilk kök : ")
b=input("ikinci kök: ")
n=input("iterasyon numarası :")
a=float(a)
b=float(b)
n=int(n)
if f(a)*f(b)>0:
    print("kök yok ya da birden fazla kök var")
    print("farklı degerlerle tekrar deneyin")
else:
    bisection(a,b,n)
