import sympy as smp
from sympy import *

while True:
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = smp.symbols(
        'a, b, c, d, e, f,g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z')

    func = sympify(input("Enter an expression: "))

    def differentiate():
        wrt = sympify(input("Derivate w.r.t: "))
        D = smp.diff(func, wrt)
        print(D)

    def diffPartially():
        wrt = sympify(input("Derivate w.r.t: "))
        wrt2 = sympify(input("Derivate w.r.t: "))
        pD = smp.diff(func, wrt, wrt2)
        print(pD)

    def nthOrder():
        wrt = sympify(input("Derivate w.r.t: "))
        nth = sympify(input("nth order: "))
        nD = smp.diff(func, wrt, nth)
        print(nD)

    def indIntegral():
        wrt = sympify(input("Derivate w.r.t: "))
        integral = smp.integrate(func, wrt)
        print(integral)

    def defIntegral():
        wrt = sympify(input("Derivate w.r.t: "))
        lowerL = sympify(input("Enter Lower Limit: "))
        upperL = sympify(input("Enter Lower Limit: "))
        dF = smp.integrate(func, (wrt, lowerL, upperL))
        print(dF)

    def Limits():
        vari = sympify(input("Enter variable: "))
        limit1 = sympify(input("Enter Limit: "))
        lim = smp.limit(func, vari, limit1)
        print(lim)

    def summation():
        vari = sympify(input("Enter variable: "))
        n1 = sympify(input("Enter Lower Limit: "))
        n2 = sympify(input("Enter Upper Limit: "))
        sum1 = smp.Sum(func, (vari, n1, n2)).doit()
        sum2 = smp.Sum(func, (vari, n1, n2)).n()
        print(sum1, "OR", sum2)

    def fourierSeries():
        c1 = input("Enter Lower Limit of Interval: ")
        l1 = input("Enter Upper Limit of Interval: ")
        vari = sympify(input("Enter variable: "))
        if "pi" not in c1 or "pi" not in l1:
            cx = sympify(c1)
            lx = sympify(l1)
            L = lx/2
            a_0 = (1/L)*smp.integrate(func, (vari, cx, cx+lx)).simplify()
            a_n = (1/L)*smp.integrate(func * smp.cos((n*smp.pi*vari)/L), (vari, cx, cx+lx))
            b_n = (1/L)*smp.integrate(func * smp.sin((n*smp.pi*vari)/L), (vari, cx, cx+lx))
            print(a_0)
            print(a_n)
            print(b_n)
        else:
            cx = sympify(c1)
            lx = sympify(l1)
            a_0 = (1/pi)*smp.integrate(func, (vari, cx, cx + 2*smp.pi))
            a_n = (1/pi)*smp.integrate(func * smp.cos(n*vari), (vari, cx, cx + 2*smp.pi))
            b_n = (1/pi)*smp.integrate(func * smp.sin(n*vari), (vari, cx, cx + 2*smp.pi))
            print(a_0)
            print(a_n)
            print(b_n)

    print("1. Differentiate")
    print("2. Differentiate Partially")
    print("3. nth Order Derivative")
    print("4. Indefinite Integral")
    print("5. Definite Integrals")
    print("6. Limits")
    print("7. Summation")
    print("8. Fourier Series")
    ask1 = int(input("Choose the operation to be performed: "))

    match ask1:
        case 1:
            differentiate()
        case 2:
            diffPartially()
        case 3:
            nthOrder()
        case 4:
            indIntegral()
        case 5:
            defIntegral()
        case 6:
            Limits()
        case 7:
            summation()
        case 8:
            fourierSeries()
        case _ if ask1 > 8:
            print("Invalid Choice")
        case _ if ask1 < 1:
            print("Invalid Choice")
    ask = input("Do you want to continue?(y/n) ")
    if (ask == "n"):
        break
print("Thank You!!!")