def f(x):
    return x**3+4*x**2-10
def bisection(a,b,n):
    i=1
    x=0
    condition= True
    while condition:
        g=f(x)
        x=(a+b)/2
        if f(x)<0:
            a=x
        else:
            b=x
        print("iteration = ",i,"x= ",x,"f(x) =",f(x))

        condition=abs(f(x)-g)>n
        i=i+1
    print("gerekli kök:",x)
a=input("ilk kök : ")
b=input("ikinci kök: ")
n=input("hata payi :")
a=float(a)
b=float(b)
n=float(n)
if f(a)*f(b)>0:
    print("kök yok ya da birden fazla kök var")
    print("farklı degerlerle tekrar deneyin")
else:
    bisection(a,b,n)
