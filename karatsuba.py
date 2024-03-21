def karatsuba_mul(n1,n2,n):
    if (n == 1):
        return n1*n2
    else:
        m = n//2
        a = n1 // (2**m)
        b = n1 % (2**m)
        c = n2 // (2**m)
        d = n2 % (2**m)
        print(a,b,c,d)
        e = karatsuba_mul(a,c,m)
        f = karatsuba_mul(b,d,m)
        g = karatsuba_mul((a-b),(c-d),m)
        return (2**(2*m))*e + (2**m)*(e+f-g) + f

print(karatsuba_mul(1,43,2))
print(123*43)